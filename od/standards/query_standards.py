import os
import yaml
from pathlib import Path

STANDARDS_DIR = Path(__file__).parent.parent / "standards"

def query_standards(tags_to_match):
    """
    Scans the local standards/ directory, reads the YAML frontmatter, 
    and returns all markdown contents that match the requested tags.
    """
    matched_standards = []
    
    for md_file in STANDARDS_DIR.rglob("*.md"):
        if md_file.name == "README.md":
            continue
            
        content = md_file.read_text(encoding="utf-8")
        
        # Parse YAML frontmatter
        if content.startswith("---"):
            try:
                parts = content.split("---", 2)
                frontmatter = yaml.safe_load(parts[1])
                markdown_body = parts[2].strip()
                
                file_tags = set(frontmatter.get("tags", []))
                
                # Check for tag intersection
                if file_tags.intersection(set(tags_to_match)):
                    matched_standards.append({
                        "id": frontmatter.get("id"),
                        "title": frontmatter.get("title"),
                        "content": markdown_body
                    })
            except Exception as e:
                print(f"Error parsing {md_file}: {e}")
                
    return matched_standards

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Query local company standards.")
    parser.add_argument("--tags", nargs="+", required=True, help="Tags to filter by (e.g., fastapi azure)")
    
    args = parser.parse_args()
    results = query_standards(args.tags)
    
    print(f"Found {len(results)} matching standard(s) for tags: {args.tags}\n")
    for res in results:
        print(f"--- {res['title']} ({res['id']}) ---")
        print(f"{res['content'][:200]}...\n")
