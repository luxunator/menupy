import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="menupy",
    version="1.0.2",
    author="luxunator",
    author_email="luxunator@pm.me",
    url="https://github.com/luxunator/menupy",
    description="Interactive Python Menu",
    packages=['menupy'],
    keywords='menu menupy curses',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
    )
