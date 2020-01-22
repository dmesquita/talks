import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text_similarity_model",
    version="1.0.0",
    entry_points={
        'console_scripts': ["text_similarity_model=text_similarity_model.cmd:main"]
    },
    author="Déborah Mesquita",
    description="Computa similaridade entre documentos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmesquita/similaridades-palestras",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
)
