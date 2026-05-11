import os
import json
import unittest
import shutil
from pathlib import Path
from generate_dashboard import generate_html

class TestDashboard(unittest.TestCase):
    def setUp(self):
        self.test_root = Path("test_dashboard_project").absolute()
        self.test_root.mkdir(exist_ok=True)
        self.docs_cda = self.test_root / "docs/cda"
        self.docs_cda.mkdir(parents=True, exist_ok=True)
        
        self.ledger_path = self.docs_cda / "ledger.json"
        with open(self.ledger_path, 'w') as f:
            json.dump({
                "project_name": "Test Project",
                "artifacts": [
                    {"id": "PRD", "type": "PRD", "name": "PRD", "status": "complete", "path": "PRD.md"}
                ]
            }, f)
            
    def tearDown(self):
        if self.test_root.exists():
            shutil.rmtree(self.test_root)
            
    def test_generate_html(self):
        with self.assertRaises(SystemExit) as cm:
            generate_html(self.test_root)
        self.assertEqual(cm.exception.code, 0)
        
        dashboard_html = self.docs_cda / "cda-dashboard.html"
        self.assertTrue(dashboard_html.exists())
        
        with open(dashboard_html, 'r') as f:
            content = f.read()
            self.assertIn("CDA Project Dashboard: Test Project", content)
            self.assertIn("PRD.md", content)

if __name__ == "__main__":
    unittest.main()
