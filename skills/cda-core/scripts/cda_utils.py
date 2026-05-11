# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
import os
import json
import argparse
import sys
import re
from pathlib import Path

def write_artifact(path, content, metadata):
    """
    Writes a markdown file with YAML-like frontmatter.
    metadata: dict of keys and values.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    frontmatter = "---\n"
    for k, v in metadata.items():
        if isinstance(v, list):
            frontmatter += f"{k}: {json.dumps(v)}\n"
        else:
            frontmatter += f"{k}: '{v}'\n"
    frontmatter += "---\n\n"
    
    with open(path, 'w') as f:
        f.write(frontmatter + content)
    
    return {"status": "success", "path": str(path)}

def read_artifact(path):
    """
    Reads a markdown file and returns (metadata, content).
    """
    path = Path(path)
    if not path.exists():
        return None, None
        
    with open(path, 'r') as f:
        full_content = f.read()
        
    match = re.match(r"^---\n(.*?)\n---\n\n?(.*)", full_content, re.DOTALL)
    if not match:
        return {}, full_content
        
    fm_raw = match.group(1)
    content = match.group(2)
    
    metadata = {}
    for line in fm_raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip().strip("'").strip('"')
            # Handle list-like strings
            if v.startswith("[") and v.endswith("]"):
                try:
                    v = json.loads(v)
                except:
                    pass
            metadata[k] = v
            
    return metadata, content

def rebuild_index(project_root):
    """
    Scans docs/cda/ for all .md files and rebuilds ledger.json and ledger.md.
    """
    cda_root = Path(project_root) / "docs/cda"
    artifacts = []
    
    if not cda_root.exists():
        return {"status": "error", "message": "CDA root not found"}
        
    for md_file in cda_root.rglob("*.md"):
        # Skip the ledger itself
        if md_file.name in ["ledger.md", "ledger.json"]:
            continue
            
        metadata, _ = read_artifact(md_file)
        if metadata and "id" in metadata:
            entry = {
                "id": metadata["id"],
                "type": metadata.get("type", "unknown"),
                "name": metadata.get("name", md_file.stem),
                "path": str(md_file.relative_to(cda_root)),
                "status": metadata.get("status", "draft"),
                "parent_id": metadata.get("parent_id")
            }
            artifacts.append(entry)
            
    # Sort for consistency
    artifacts.sort(key=lambda x: x["id"])
    
    ledger = {"project_name": "Citizen Dev Project", "artifacts": artifacts}
    
    # Write JSON
    ledger_json_path = cda_root / "ledger.json"
    with open(ledger_json_path, 'w') as f:
        json.dump(ledger, f, indent=4)
        
    # Write Markdown
    ledger_md_path = cda_root / "ledger.md"
    with open(ledger_md_path, 'w') as f:
        f.write("# CDA Project Ledger\n\n")
        f.write("| ID | Type | Name | Status | Path |\n")
        f.write("| --- | --- | --- | --- | --- |\n")
        for entry in artifacts:
            f.write(f"| {entry['id']} | {entry['type']} | {entry['name']} | {entry['status']} | {entry['path']} |\n")
            
    return {"status": "success", "artifact_count": len(artifacts)}

def extract_standards(standards_dir, keywords):
    """
    Extracts relevant lines/sections from standards files based on keywords.
    """
    standards_dir = Path(standards_dir)
    relevant_rules = []
    
    if not standards_dir.exists():
        return []
        
    for std_file in standards_dir.glob("*.md"):
        with open(std_file, 'r') as f:
            lines = f.readlines()
            
        current_section = ""
        capture = False
        for line in lines:
            if line.startswith("#"):
                if capture and current_section:
                    relevant_rules.append(current_section.strip())
                current_section = line
                capture = any(kw.lower() in line.lower() for kw in keywords)
            elif capture:
                current_section += line
        
        if capture and current_section:
            relevant_rules.append(current_section.strip())
            
    return relevant_rules

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    
    # Write artifact
    write_parser = subparsers.add_parser("write-artifact")
    write_parser.add_argument("--path", required=True)
    write_parser.add_argument("--content", required=True)
    write_parser.add_argument("--metadata", required=True) # JSON string
    
    # Rebuild index
    rebuild_parser = subparsers.add_parser("rebuild-index")
    rebuild_parser.add_argument("--root", required=True)
    
    # Extract standards
    extract_parser = subparsers.add_parser("extract-standards")
    extract_parser.add_argument("--dir", required=True)
    extract_parser.add_argument("--keywords", required=True) # Comma-separated
    
    args = parser.parse_args()
    
    try:
        if args.command == "write-artifact":
            metadata = json.loads(args.metadata)
            result = write_artifact(args.path, args.content, metadata)
            print(json.dumps(result))
        elif args.command == "rebuild-index":
            result = rebuild_index(args.root)
            print(json.dumps(result))
        elif args.command == "extract-standards":
            keywords = [kw.strip() for kw in args.keywords.split(",")]
            rules = extract_standards(args.dir, keywords)
            print(json.dumps({"status": "success", "rules": rules}))
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))
        sys.exit(1)
