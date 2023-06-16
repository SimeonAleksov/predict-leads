import json
import os

from attrs import asdict

from observer import base
from models import dtos


class Storage(base.ObserverBase):
    def execute(self, data: dtos.ObserverDTO):
        print(f'Storing data: {asdict(data.dto)}')
        self.append_data_to_json(file_path=data.scraper.get_filename(), data=[asdict(data.dto)])

    @staticmethod
    def append_data_to_json(file_path, data):
        file_path = f'data/{file_path}'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    existing_data = json.load(file)
                    if isinstance(existing_data, list):
                        existing_data.extend(data)
                    else:
                        raise TypeError(f"Invalid JSON data: {existing_data}")
                except json.JSONDecodeError:
                    raise ValueError("Invalid JSON file")

            with open(file_path, 'w') as file:
                json.dump(existing_data, file, indent=4)
        else:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
