import os
import unittest
from unittest.mock import patch

import agent


class AgentConfigTests(unittest.TestCase):
    @patch.dict(os.environ, {}, clear=True)
    def test_get_api_key_requires_environment_variable(self):
        with self.assertRaisesRegex(RuntimeError, "GEMINI_API_KEY is required"):
            agent.get_api_key()

    @patch.dict(os.environ, {"GEMINI_API_KEY": "test-key"}, clear=True)
    def test_get_api_key_reads_environment_variable(self):
        self.assertEqual(agent.get_api_key(), "test-key")


if __name__ == "__main__":
    unittest.main()
