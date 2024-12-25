from setuptools import setup, find_packages

setup(
    name="pymongo-schema",
    version="0.1.0",
    description="A Python SDK for exporting MongoDB schema metadata",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your_email@example.com",
    url="https://github.com/yourusername/pymongo-schema",
    packages=find_packages(),
    install_requires=["pymongo", "bson"],
    entry_points={
        "console_scripts": [
            "pymongo-schema=pymongo_schema.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)