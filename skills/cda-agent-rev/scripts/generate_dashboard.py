# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
import os
import json
import argparse
import sys
from pathlib import Path

def generate_html(project_root):
    ledger_path = Path(project_root) / "docs/cda/ledger.json"
    output_path = Path(project_root) / "docs/cda/cda-dashboard.html"
    
    if not ledger_path.exists():
        print(json.dumps({"status": "error", "message": "ledger.json not found"}))
        sys.exit(1)
        
    with open(ledger_path, 'r') as f:
        data = json.load(f)
        
    artifacts = data.get("artifacts", [])
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CDA Project Dashboard</title>
        <style>
            body {{ font-family: sans-serif; margin: 20px; background: #f4f4f9; }}
            h1 {{ color: #333; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; background: white; }}
            th, td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
            th {{ background-color: #4CAF50; color: white; }}
            tr:hover {{ background-color: #f5f5f5; }}
            .status-complete {{ color: green; font-weight: bold; }}
            .status-draft {{ color: orange; }}
            .status-reviewed {{ color: blue; font-weight: bold; }}
            .status-needs-revision {{ color: red; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>CDA Project Dashboard: {data.get('project_name', 'Citizen Dev Project')}</h1>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Type</th>
                    <th>Name</th>
                    <th>Status</th>
                    <th>Path</th>
                </tr>
            </thead>
            <tbody>
    """
    
    for art in artifacts:
        status_class = f"status-{art['status'].replace(' ', '-')}"
        html_content += f"""
                <tr>
                    <td>{art['id']}</td>
                    <td>{art['type']}</td>
                    <td>{art['name']}</td>
                    <td class="{status_class}">{art['status']}</td>
                    <td><a href="{art['path']}">{art['path']}</a></td>
                </tr>
        """
        
    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """
    
    with open(output_path, 'w') as f:
        f.write(html_content)
        
    print(json.dumps({"status": "success", "path": str(output_path)}))
    sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    args = parser.parse_args()
    generate_html(args.root)
