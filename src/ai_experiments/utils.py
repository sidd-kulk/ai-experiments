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
    # Create logger with the module name
    logger = logging.getLogger("ai_experiments.utils")
    
    # Set the passed-in level
    logger.setLevel(level)  # This line is likely missing or incorrect
    
    # Create console handler with appropriate formatting if needed
    handler = logging.StreamHandler()
    handler.setLevel(level)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(handler)
    
    return logger
