import enum


class ElementTag(enum.Enum):
    DIV = 'div'
    HEADING_1 = 'h1'
    HEADING_2 = 'h2'
    ARTICLE = 'article'
    IMG = 'img'
    A = 'a'


class ElementTagProperty(enum.Enum):
    HREF = 'href'
    SRC = 'src'
    ALT = 'alt'
