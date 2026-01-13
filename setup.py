from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="colab-env-switcher",
    version="0.1.2.post1",
    author="911218sky",
    author_email="sky@sky1218.com",
    description="A Python environment switcher for Google Colab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/911218sky/colab-env-switcher",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[],
)
