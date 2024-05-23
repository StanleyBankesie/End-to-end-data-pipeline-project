import os

from dagster import Definitions
from dagster_dbt import DbtCliResource

from .assets import transformation_dbt_assets
from .constants import dbt_project_dir
from .schedules import schedules
from .fivetran import fivetran_assets

defs = Definitions(
    assets=[transformation_dbt_assets,fivetran_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=os.fspath(dbt_project_dir)),
    },
)