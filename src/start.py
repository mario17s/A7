from src.repo.repository import Repository, TextFileRepository, BinaryRepository, JSONFileRepository
from src.services.service import ExpenseService
from src.ui.console import Console
from jproperties import Properties

if __name__ == "__main__":
    configurations = Properties()
    configurations_file = open("settings.properties", "rb")
    configurations.load(configurations_file)
    repository_format = configurations.get("repository").data

    try:
        if repository_format not in ["memory", "text-file", "binary-file", "json-file"]:
            raise ValueError("ERROR: invalid setting!!!")

        if repository_format == "memory":
            repo = Repository()
        elif repository_format == "text-file":
            repo = TextFileRepository()
        elif repository_format == "binary-file":
            repo = BinaryRepository()
        elif repository_format == "json-file":
            repo = JSONFileRepository()

        service = ExpenseService(repo)
        console = Console(service)
        console.run_console()

    except ValueError as ve:
        print(ve)

