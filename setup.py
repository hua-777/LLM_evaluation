from setuptools import setup, find_packages

setup(
    name="CS162_Winter_2024_project",
    description="FoF: Fact or Flawed? Understanding the factuality and fairness of LLMs",
    version="1.0",
    license='MIT',
    author='Rohan Wadhawan',
    author_email='rohanwadhawan7@gmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)