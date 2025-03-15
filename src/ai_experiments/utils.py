"""Utility functions for AI experiments."""

import logging
from typing import Any, Dict, List, Optional, Union

# Configure logging
logger = logging.getLogger(__name__)


def setup_logger(level: int = logging.INFO) -> logging.Logger:
    """
    Configure and return a logger for the application.

    Args:
        level: The logging level to use

    Returns:
        A configured logger instance
    """
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logger
