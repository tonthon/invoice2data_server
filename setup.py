import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

entry_points = {
    "console_scripts": [
        "aio-server = invoice2data_server:serve"
    ]
}

setuptools.setup(
    name="invoice2data_server", # Replace with your own username
    version="0.0.1",
    author="Tjebbes Gaston",
    author_email="g.t@majerti.fr",
    description="A aiohttp server providing an interface to invoice2data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tonthon/invoice2data_server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points=entry_points,
)
