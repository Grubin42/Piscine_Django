#!/usr/bin/python3

from elem import Elem, Text
from elements import Html, Head, Body, Title, Meta, Img, Table, Tr, Th, Td, Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br


class Page:
    """Classe pour valider et générer des pages HTML"""
    
    # Types valides dans le document
    VALID_TYPES = {
        'html', 'head', 'body', 'title', 'meta', 'img', 
        'table', 'tr', 'th', 'td', 'ul', 'ol', 'li', 
        'h1', 'h2', 'p', 'div', 'span', 'hr', 'br', 'Text'
    }
    
    # Règles de contenu pour chaque élément
    ALLOWED_CONTENT = {
        'html': ['head', 'body'],
        'head': ['title', 'meta'],
        'body': ['h1', 'h2', 'div', 'table', 'ul', 'ol', 'span', 'img', 'Text'],
        'title': ['Text'],
        'h1': ['Text'],
        'h2': ['Text'],
        'p': ['Text'],
        'li': ['Text'],
        'th': ['Text'],
        'td': ['Text'],
        'div': ['h1', 'h2', 'div', 'table', 'ul', 'ol', 'span', 'img', 'Text'],
        'span': ['Text', 'p'],
        'table': ['tr'],
        'tr': ['th', 'td'],
        'ul': ['li'],
        'ol': ['li'],
    }
    
    def __init__(self, elem):
        """Constructeur de la classe Page"""
        if not isinstance(elem, Elem):
            raise TypeError("Page must be initialized with an Elem instance")
        self.root = elem
    
    def __str__(self):
        """Retourne le code HTML avec doctype si c'est une balise html"""
        html = str(self.root)
        if self.root.tag == 'html':
            return '<!DOCTYPE html>\n' + html
        return html
    
    def write_to_file(self, filename):
        """Écrit le HTML dans un fichier"""
        with open(filename, 'w') as f:
            f.write(str(self))
    
    def is_valid(self):
        """Vérifie si la page est valide selon les règles"""
        return self._validate_elem(self.root)
    
    def _get_elem_type(self, elem):
        """Retourne le type de l'élément"""
        if isinstance(elem, Text):
            return 'Text'
        elif isinstance(elem, Elem):
            return elem.tag
        return None
    
    def _validate_elem(self, elem):
        """Valide un élément et son contenu"""
        elem_type = self._get_elem_type(elem)
        
        # Vérifier que le type est valide
        if elem_type not in self.VALID_TYPES:
            return False
        
        # Si c'est du texte, c'est valide
        if elem_type == 'Text':
            return True
        
        # Cas spécial : html doit contenir exactement un head puis un body
        if elem_type == 'html':
            if len(elem.content) != 2:
                return False
            if self._get_elem_type(elem.content[0]) != 'head':
                return False
            if self._get_elem_type(elem.content[1]) != 'body':
                return False
            return self._validate_elem(elem.content[0]) and self._validate_elem(elem.content[1])
        
        # Cas spécial : head doit contenir exactement un unique title
        if elem_type == 'head':
            if len(elem.content) != 1:
                return False
            if self._get_elem_type(elem.content[0]) != 'title':
                return False
            return self._validate_elem(elem.content[0])
        
        # Cas spécial : title, h1, h2, li, th, td ne doivent contenir qu'un unique Text
        if elem_type in ['title', 'h1', 'h2', 'li', 'th', 'td']:
            if len(elem.content) != 1:
                return False
            if self._get_elem_type(elem.content[0]) != 'Text':
                return False
            return True
        
        # Cas spécial : ul et ol doivent contenir au moins un li et uniquement des li
        if elem_type in ['ul', 'ol']:
            if len(elem.content) == 0:
                return False
            for child in elem.content:
                if self._get_elem_type(child) != 'li':
                    return False
                if not self._validate_elem(child):
                    return False
            return True
        
        # Cas spécial : tr doit contenir au moins un th ou td et uniquement des th/td
        if elem_type == 'tr':
            if len(elem.content) == 0:
                return False
            has_th = False
            has_td = False
            for child in elem.content:
                child_type = self._get_elem_type(child)
                if child_type == 'th':
                    has_th = True
                    if not self._validate_elem(child):
                        return False
                elif child_type == 'td':
                    has_td = True
                    if not self._validate_elem(child):
                        return False
                else:
                    return False
            # th et td doivent être mutuellement exclusifs
            if has_th and has_td:
                return False
            return True
        
        # Cas spécial : table ne doit contenir que des tr
        if elem_type == 'table':
            for child in elem.content:
                if self._get_elem_type(child) != 'tr':
                    return False
                if not self._validate_elem(child):
                    return False
            return True
        
        # Pour les autres éléments, valider le contenu selon les règles
        if elem_type in self.ALLOWED_CONTENT:
            allowed = self.ALLOWED_CONTENT[elem_type]
            for child in elem.content:
                child_type = self._get_elem_type(child)
                if child_type not in allowed:
                    return False
                if not self._validate_elem(child):
                    return False
            return True
        
        # Si pas de règle spécifiée, c'est valide
        return True

