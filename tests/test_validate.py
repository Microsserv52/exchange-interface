"""Regression checks for example format validation."""

import importlib.util
import json
import shutil
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ValidationTests(unittest.TestCase):
    def test_published_contract(self):
        with redirect_stdout(StringIO()):
            self.assertEqual(validator.main(), 0)

    def test_invalid_uuid_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("examples", "schemas", "openapi"):
                shutil.copytree(ROOT / name, root / name)
            example = root / "examples/usd-eur.json"
            payload = json.loads(example.read_text())
            payload["id-account"] = "invalid-uuid"
            example.write_text(json.dumps(payload))
            errors = StringIO()
            with (
                patch.multiple(
                    validator,
                    ROOT=root,
                    OPENAPI=root / "openapi/exchange.yaml",
                    SCHEMA_DIR=root / "schemas",
                ),
                redirect_stderr(errors),
            ):
                self.assertEqual(validator.main(), 1)
            self.assertIn("is not a 'uuid'", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
