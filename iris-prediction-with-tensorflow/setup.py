from setuptools import find_packages, setup

setup(
    name="iris_prediction_with_tensorflow",
    packages=find_packages(exclude=["iris_prediction_with_tensorflow_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
