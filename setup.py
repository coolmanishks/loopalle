from setuptools import setup, find_packages

setup(
    name="loopalle",
    version="1.0.0",
    author="Manish Singh",
    author_email="manishks.bitsindri@gmail.com",
    description="A package for simplified parallel processing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/coolmanishks/loopalle",
    packages=find_packages(),
    install_requires=["pandas", "tqdm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
