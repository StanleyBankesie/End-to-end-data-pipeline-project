from dagster_fivetran import FivetranResource, load_assets_from_fivetran_instance
from dagster import (
    ScheduleDefinition,
    define_asset_job,
    AssetSelection,
    EnvVar,
    Definitions,
)

fivetran_instance = FivetranResource(
    api_key=EnvVar("FIVETRAN_API_KEY"),
    api_secret=EnvVar("FIVETRAN_API_SECRET"),
)
fivetran_assets = load_assets_from_fivetran_instance(fivetran_instance)

# materialize all assets
run_everything_job = define_asset_job("run_everything", selection="*")

# only run my_fivetran_connection and downstream assets
my_etl_job = define_asset_job(
    "my_etl_job", AssetSelection.groups("my_fivetran_connection").downstream()
)

defs = Definitions(
    assets=[fivetran_assets],
    schedules=[
        ScheduleDefinition(
            job=my_etl_job,
            cron_schedule="@daily",
        ),
        ScheduleDefinition(
            job=run_everything_job,
            cron_schedule="@weekly",
        ),
    ],
)
