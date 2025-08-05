from setuptools import setup, find_packages

setup(
    name="common-cli-tool",
    version="0.1.0",
    description="A CLI tool to help study for CompTIA A+ exams",
    author="Omar Zebibo",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "colorama",
        "tabulate",
    ],
    entry_points={
        "console_scripts": [
            "common=common.cli:main",
        ],
    },
)
