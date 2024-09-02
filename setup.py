from setuptools import setup, find_packages

setup(
    name="signalytica",
    version="0.1.0",
    author="Edgar Lara",
    author_email="elara480@gmil.com",
    description="Feature extraction for time series and EEG signals",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Edgar-La/signalytica",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "antropy>=0.1.5",
        "numpy>=1.21.6",
	"scipy>=1.7.3",
    ],	
)