from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="educational-packet-analyzer",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="An educational network packet analyzer for learning networking protocols",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DhitalPrakriti/packet-analyzer",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: System :: Networking :: Monitoring",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "packet-analyzer=cli:main",
        ],
    },
    keywords="networking, packet-analysis, education, cybersecurity, protocol-analysis",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/packet-analyzer/issues",
        "Source": "https://github.com/yourusername/packet-analyzer",
    },
)