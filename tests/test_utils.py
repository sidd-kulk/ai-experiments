"""Tests for the utils module."""

import logging

import pytest

from ai_experiments.utils import setup_logger


def test_setup_logger():
    """Test that the logger is properly configured."""
    logger = setup_logger(level=logging.DEBUG)

    assert logger.level == logging.DEBUG
    assert logger.name == "root"

    # Test with default level
    logger = setup_logger()
    assert logger.level == logging.INFO
