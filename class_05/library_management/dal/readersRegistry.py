import json
from pathlib import Path

from models.readers import Reader
from consts import PERSISTENT_DATA_DIR
from dal.dal_utils import parse_models_from_file
from dal.FileDALSingleton import FileDALSingleton
from dal.DAL import Dal

PERSISTENT_READERS_DATA = PERSISTENT_DATA_DIR / "readers_data.json"


class ReadersRegistry(FileDALSingleton, Dal):

    def __init__(self, data_file: Path = PERSISTENT_READERS_DATA):
        ReadersRegistry.initialize_class(data_file, default_file_content="[]")
        # self.get_all()

    def get_all(self) -> list[Reader]:
        return parse_models_from_file(self._data_file_path, Reader)

    # TODO: this is not clean. Copy pasted from bookInventory.py
    def add(self, new_reader: Reader):
        all_readers = self.get_all()

        existing_identifiers = [reader.identifier for reader in all_readers]
        if new_reader.identifier in existing_identifiers:
            raise ValueError(f"Identifier {new_reader.identifier} already exists")

        all_readers.append(new_reader)
        readers_dicts = [reader.model_dump() for reader in all_readers]
        self._data_file_path.write_text(json.dumps(readers_dicts, indent=2))
