"""cronlish — translate cron expressions into plain human language.

>>> from cronlish import describe
>>> describe("*/5 * * * *")
'Every 5 minutes'
"""
from cronlish.describe import DescribeError, describe

__version__ = "0.2.0"

__all__ = ["describe", "DescribeError", "__version__"]
