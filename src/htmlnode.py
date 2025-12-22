class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None or self.props == {}:
            return ""
        result = ""
        for key, item in self.props.items():
            result += f' {key}="{item}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    VOID_ELEMENTS = {"img", "br", "hr", "input", "meta", "link", "area", "base", "col", "embed", "source", "track", "wbr"}

    def __init__(self, tag, value, props=None):
        if value is None and tag not in self.VOID_ELEMENTS:
            raise ValueError("Invalid HTML: LeafNode must have a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        if self.tag in self.VOID_ELEMENTS:
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: ParentNode must have a tag")
        if self.children is None:
            raise ValueError("Invalid HTML: ParentNode must have children")

        html_str = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_str += child.to_html()
            
        return html_str + f"</{self.tag}>"