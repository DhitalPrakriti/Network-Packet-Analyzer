from setuptools import setup, find_packages

setup(
    name="packetanalyzer",
    version="1.0.0",
    description="A professional network packet analyzer for educational purposes",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "scapy>=2.4.5",
    ],
    entry_points={
        'console_scripts': [
            'packetanalyzer=cli:main',
        ],
    },
    python_requires=">=3.8",
     classifiers=[  # Add classifiers for better metadata
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
     ], 
)