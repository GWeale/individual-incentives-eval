import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


class DefaultEvalTests(unittest.TestCase):
    def test_repository_default_runs_only_individual(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "run"
            result = subprocess.run([sys.executable, "-m", "individual_incentives_eval", "run",
                "--plan", "examples/baselines.json", "--out", str(out),
                "--seeds", "1", "--rotations", "1"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            summary = json.loads((out / "summary.json").read_text())
            self.assertEqual(summary["manifest"]["evals"], ["individual"])
            self.assertEqual({r["eval"] for r in summary["rows"]}, {"individual"})
            self.assertEqual(sum(r["completed"] for r in summary["rows"]), 5)
