"""This module contains the main process of the robot."""

import shutil
import json
from pathlib import Path

from OpenOrchestrator.orchestrator_connection.connection import OrchestratorConnection
from OpenOrchestrator.database.queues import QueueElement


# pylint: disable-next=unused-argument
def process(orchestrator_connection: OrchestratorConnection, queue_element: QueueElement | None = None) -> None:
    """Do the primary process of the robot."""
    orchestrator_connection.log_trace("Running process.")

    args = json.loads(orchestrator_connection.process_arguments)
    source_folder = Path(args["source_folder"])
    target_folder = Path(args["target_folder"])

    for file in source_folder.iterdir():
        new_file = target_folder / file.name
        if not new_file.exists():
            orchestrator_connection.log_info(f"Moving file '{file}' to '{new_file}'")
            shutil.copyfile(file, new_file)
