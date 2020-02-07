from setuptools import setup


setup(
    name="list_adder",
    description="Demo for compy journal club",
    version="1.0",
    author="Henrik Finsberg",
    license="MIT",
    author_email="henriknf@simula.no",
    url="https://github.com/ComputationalPhysiology/journal_club",
    packages=["list_adder"],
    install_requires=[
        "pytest",
        "numpy",
        "mypy",
        "flake8",
        "isort",
        "pre-commit",
        "black",
    ],
)
