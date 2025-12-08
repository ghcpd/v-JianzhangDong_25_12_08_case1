"""Minimal lxml.etree shim backed by xml.etree.ElementTree
This implements only the pieces needed by the tests (fromstring and Element indexing)
"""
import xml.etree.ElementTree as _et

fromstring = _et.fromstring

# Provide a simple Element wrapper to mirror small lxml features if needed
Element = _et.Element
