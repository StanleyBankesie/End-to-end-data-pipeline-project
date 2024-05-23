from setuptools import find_packages, setup

setup(
    name="orchestration",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-bigquery",
        "dbt-postgres",
        "dbt-postgres",
        "dbt-bigquery",
        "dbt-bigquery",
        "dbt-postgres",
        "dbt-snowflake",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)