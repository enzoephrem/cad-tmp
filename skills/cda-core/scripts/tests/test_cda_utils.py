import os
import json
import unittest
import shutil
import re
from pathlib import Path
from cda_utils import write_artifact, read_artifact, rebuild_index, extract_standards

class TestCDAUtils(unittest.TestCase):
    def setUp(self):
        self.test_root = Path("test_project").absolute()
        self.test_root.mkdir(exist_ok=True)
        self.docs_cda = self.test_root / "docs/cda"
        self.docs_cda.mkdir(parents=True, exist_ok=True)
        
    def tearDown(self):
        if self.test_root.exists():
            shutil.rmtree(self.test_root)
            
    def test_write_read_artifact(self):
        path = self.docs_cda / "PRD.md"
        metadata = {"id": "PRD-001", "type": "PRD", "status": "draft"}
        content = "# My PRD\nThis is a test."
        
        result = write_artifact(path, content, metadata)
        self.assertEqual(result["status"], "success")
        
        read_metadata, read_content = read_artifact(path)
        self.assertEqual(read_metadata["id"], "PRD-001")
        self.assertEqual(read_metadata["status"], "draft")
        self.assertIn("# My PRD", read_content)

    def test_rebuild_index(self):
        # Create a few artifacts
        write_artifact(self.docs_cda / "PRD.md", "Content", {"id": "PRD", "type": "PRD"})
        write_artifact(self.docs_cda / "FTR-001/feature.md", "Content", {"id": "FTR-001", "type": "FEATURE"})
        
        result = rebuild_index(self.test_root)
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["artifact_count"], 2)
        
        ledger_json = self.docs_cda / "ledger.json"
        self.assertTrue(ledger_json.exists())
        
        with open(ledger_json, 'r') as f:
            data = json.load(f)
            self.assertEqual(len(data["artifacts"]), 2)

    def test_extract_standards(self):
        std_dir = self.test_root / "standards"
        std_dir.mkdir(exist_ok=True)
        with open(std_dir / "sec.md", "w") as f:
            f.write("# Security Rules\nMust use SSL.\n# Data Rules\nMust encrypt.")
            
        rules = extract_standards(std_dir, ["security"])
        self.assertEqual(len(rules), 1)
        self.assertIn("Must use SSL", rules[0])

if __name__ == "__main__":
    unittest.main()
