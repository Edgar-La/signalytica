from setuptools import setup, find_packages

def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    with open(filename, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines if line and not line.startswith('#')]

setup(
    name="signalytica",
    version="0.1.11",
    author="Edgar Lara",
    author_email="elara480@gmil.com",
    description="Feature extraction for time series and EEG signals",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Edgar-La/signalytica",
    #packages=find_packages(),
    package_dir={"": "src"},  # Tells setuptools that packages are inside the src/ directory
    packages=find_packages(where="src"),  # Automatically find all packages inside src/
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',	
)