#!/usr/bin/python3

from elem import Elem, Text


# Éléments structurels
class Html(Elem):
    def __init__(self, content=None):
        super().__init__('html', {}, content, 'double')


class Head(Elem):
    def __init__(self, content=None):
        super().__init__('head', {}, content, 'double')


class Body(Elem):
    def __init__(self, content=None):
        super().__init__('body', {}, content, 'double')


# Titre et métadonnées
class Title(Elem):
    def __init__(self, content=None):
        super().__init__('title', {}, content, 'double')


class Meta(Elem):
    def __init__(self, attr=None):
        super().__init__('meta', attr or {}, None, 'simple')


# Images
class Img(Elem):
    def __init__(self, attr=None):
        super().__init__('img', attr or {}, None, 'simple')


# Tableau
class Table(Elem):
    def __init__(self, content=None):
        super().__init__('table', {}, content, 'double')


class Tr(Elem):
    def __init__(self, content=None):
        super().__init__('tr', {}, content, 'double')


class Th(Elem):
    def __init__(self, content=None):
        super().__init__('th', {}, content, 'double')


class Td(Elem):
    def __init__(self, content=None):
        super().__init__('td', {}, content, 'double')


# Listes
class Ul(Elem):
    def __init__(self, content=None):
        super().__init__('ul', {}, content, 'double')


class Ol(Elem):
    def __init__(self, content=None):
        super().__init__('ol', {}, content, 'double')


class Li(Elem):
    def __init__(self, content=None):
        super().__init__('li', {}, content, 'double')


# En-têtes
class H1(Elem):
    def __init__(self, content=None):
        super().__init__('h1', {}, content, 'double')


class H2(Elem):
    def __init__(self, content=None):
        super().__init__('h2', {}, content, 'double')


# Paragraphes et divisions
class P(Elem):
    def __init__(self, content=None):
        super().__init__('p', {}, content, 'double')


class Div(Elem):
    def __init__(self, content=None):
        super().__init__('div', {}, content, 'double')


class Span(Elem):
    def __init__(self, content=None):
        super().__init__('span', {}, content, 'double')


# Lignes de séparation et sauts de ligne
class Hr(Elem):
    def __init__(self):
        super().__init__('hr', {}, None, 'simple')


class Br(Elem):
    def __init__(self):
        super().__init__('br', {}, None, 'simple')

