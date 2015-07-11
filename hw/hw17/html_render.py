#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):

    IND_LEVEL = "    "

    def __init__(self, content="", **kwargs):
        self.children = [content] if content else []
        self.attributes = kwargs

    def append(self, new_child):
        self.children.append(new_child)

    def render(self, file_out, indent="    ", ):

        if len(self.attributes) < 1:
            file_out.write("\n%s<%s>" % (indent, self.name))
        else:
            for k, v in self.attributes.items():
                file_out.write('\n%s<%s %s="%s">' % (indent, self.name, k, v))

        for child in self.children:
            if (type(child) == str):
                # Add new content string without rendering
                file_out.write("\n" + indent + Element.IND_LEVEL + child)
            else:
                # Add new child node, by recursively rendering
                child.render(file_out, indent + Element.IND_LEVEL)
        file_out.write("\n%s</%s>" % (indent, self.name))


class Html(Element):
    name = 'html'

    def __init__(self, content=""):
        Element.__init__(self, content="")

    def render(self, file_out, indent=""):
        file_out.write("<!DOCTYPE html>")
        Element.render(self, file_out, "")


class Head(Element):
    name = 'head'


class OneLineTag(Element):

    def __init__(self, content=""):
        Element.__init__(self, content=content)

    def render(self, file_out, indent=""):

        if len(self.attributes) < 1:
            file_out.write("\n%s<%s>" % (indent, self.name))
        else:
            for k, v in self.attributes.items():
                file_out.write("\n%s<%s %s='%s'>" % (indent, self.name, k, v))

        for child in self.children:
            try:
                child.render(file_out, self.content)
            except AttributeError:
                file_out.write(child)
        file_out.write("</%s>" % (self.name))


class Title(OneLineTag):
    name = 'title'


class Body(Element):
    name = 'body'


class P(Element):
    name = 'p'


class SelfClosingTag(Element):

    def __init__(self):
        Element.__init__(self)

    def render(self, file_out, indent=""):
        file_out.write("\n%s<%s/>" % (indent, self.name))


class Hr(SelfClosingTag):
    name = 'hr'


class Br(SelfClosingTag):
    name = 'br'


class A(OneLineTag):
    name = 'a'

    def __init__(self, link="", content=""):
        Element.__init__(self, content=content, href=link)
