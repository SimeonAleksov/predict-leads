import enum


class Scraper(enum.IntEnum):
    DEEL = 0
    SCALE = 1
    WEBFLOW = 2

    def get_filename(self):
        _mapping = {
            self.DEEL: 'deel.json',
            self.SCALE: 'scale.json',
            self.WEBFLOW: 'webflow.json',
        }
        return _mapping[self]
