#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    IND_LEVEL = "    "

    def __init__(self, name="", content=""):
            self.name = name
            self.children = [content] if content else []

    def append(self, new_child):
            self.children.append(new_child)

    def render(self, file_out, indent="    ", ):

            file_out.write("%s<%s>\n" % (indent, self.name))
            for child in self.children:
                if (type(child) == str):
                    # Add new content string without rendering
                    file_out.write(indent + Element.IND_LEVEL + child)
                else:
                    # Add new child node, by recursively rendering
                    child.render(file_out, indent + Element.IND_LEVEL)
            file_out.write("%s</%s>\n" % (indent, self.name))


class Html(Element):

    def __init__(self, name="", content=""):
        Element.__init__(self, name='html', content="")

    def render(self, file_out, indent=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, "")


class Head(Element):

    def __init__(self, content=""):
        Element.__init__(self, name='head', content="")


class OneLineTag(Element):

    def __init__(self, content="", name=""):
        Element.__init__(self, content=content)

    def render(self, file_out, indent=""):

        file_out.write("%s<%s>" % (indent, self.name))
        for child in self.children:
            try:
                child.render(file_out, self.content)
            except AttributeError:
                file_out.write(child)
        file_out.write("</%s>\n" % (self.name))


class Title(OneLineTag):

    def __init__(self, content=""):
        Element.__init__(self, name='title', content=content)


class Body(Element):

    def __init__(self, content=""):
        Element.__init__(self, name='body', content=content)


class P(Element):

    def __init__(self, content=""):
        Element.__init__(self, name='p', content=content)
