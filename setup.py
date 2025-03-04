from setuptools import setup, find_packages

setup(
    name="CL_Chess_Nishnath",
    version="1.3.2",
    packages=find_packages(),
    install_requires=[], 
    long_description=open('ReadMe.md').read(),
    long_description_content_type='text/markdown',
    author="Nishnath Rai",
    author_email="nishnathnishu1122@gmail.com",
    description="Play Chess",
    url="https://github.com/NishnathRai/CL-Chess",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
