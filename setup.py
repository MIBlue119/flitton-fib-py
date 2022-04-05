from setuptools import find_packages, setup
# We are going to use setup tp define parameters, and use find_packages to exclude tests.

setup(
    name="flitton_fib_py",
    version="0.0.1",
    author="Weiren",
    author_email="miblue119@gmail.com",
    description="Calculates a Fibonacci number",
    long_description="A basic practice for calculating fibonacci numbers",
    url="https://github.com/MIBlue119/flitton-fib-py",
    install_requires=[],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python ::3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    test_require=['pytest'],
)