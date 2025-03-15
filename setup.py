from setuptools import setup, find_packages

setup(
    name="ai_experiments",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=22.0",
            "isort>=5.0",
            "flake8>=4.0",
            "mypy>=0.9",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="AI experiments and utilities",
    keywords="ai, machine learning, experiments",
    url="https://github.com/yourusername/ai-experiments",
)
