import base64
from curses import raw
import json
import os
from PIL import Image


class PandoraBoxService:
    def __init__(self, raw_event: None = None) -> None:

        if raw_event:
            self.event_data_b64 = raw_event.get("message", None).get("data", None)
            self.event_json = json.loads(base64.b64decode(self.event_data_b64))
            self.file_name = self.event_json["file_name"]
            self.file_base64 = self.event_json["file_base64"]
            self.file_path = self.file_name.split(".")[0]

    def make_tree(self, path):
        tree = dict(name=os.path.basename(path), children=[])
        try:
            lst = os.listdir(path)
        except OSError:
            pass  # ignore errors
        else:
            for name in lst:
                fn = os.path.join(path, name)
                if os.path.isdir(fn):
                    tree["children"].append(self.make_tree(fn))
                else:
                    tree["children"].append(dict(name=name))
        return tree

    def save_original_file(self) -> None:
        try:
            os.system(f"cd pandora_box/images && mkdir {self.file_path}")
        except:
            pass
        self.file = f"pandora_box/images/{self.file_path}/{self.file_name}"
        with open(self.file, "wb") as fh:
            fh.write(base64.decodebytes(self.file_base64.encode()))

        #  resize image

    def save_resized_file(self) -> None:
        base_size = 384
        img = Image.open(self.file)
        img = img.resize((base_size, base_size), Image.ANTIALIAS)

        img.save(f"pandora_box/images/{self.file_path}/resized_{self.file_name}")
