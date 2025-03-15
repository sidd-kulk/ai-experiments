"""Base model definitions for AI experiments."""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

import numpy as np


class BaseModel(ABC):
    """Abstract base class for all models."""

    def __init__(self, name: str):
        """
        Initialize the model.

        Args:
            name: Name of the model
        """
        self.name = name

    @abstractmethod
    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        """
        Train the model on data.

        Args:
            X: Training features
            y: Training labels
        """
        pass

    @abstractmethod
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions on new data.

        Args:
            X: Features to predict on

        Returns:
            Predictions for the input features
        """
        pass

    def __repr__(self) -> str:
        """Return string representation of the model."""
        return f"{self.__class__.__name__}(name={self.name})"
