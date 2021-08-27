import setuptools

with open("README.md", "r", encoding="utf8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="porcodio",
    version="1.0.0",
    author="BranchScope",
    author_email="rocco4064@gmail.com",
    description="A random \"porcodio\" ascii art generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BranchScope/porcodio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)