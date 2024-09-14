from pathlib import Path


class FileDALSingleton:
    instance_exists = False
    _data_file_path = None

    @classmethod
    def initialize_class(cls, data_file: Path, *, default_file_content="[]"):
        if cls.instance_exists:
            raise TypeError("Cannot create more than one instance of this class")

        cls._data_file_path = data_file
        if not cls._data_file_path.is_file():
            cls._data_file_path.write_text(default_file_content)

        cls.instance_exists = True
