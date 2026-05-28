class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        f_string = ""
        for key, value in self.props.items():
            f_string += f' {key}="{value}"'
        return f_string

    def __repr__(self):
        return f"Tag: {self.tag};\nValue: {self.value};\nChildren: {self.children};\nProps: {self.props};"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError()
        if not self.tag:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"Tag: {self.tag};\nValue: {self.value};\nProps: {self.props};"

    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is missing")
        if not self.children:
           raise ValueError("Children is missing")

        childrenResult = ''
        for child in self.children:
            childrenResult += child.to_html()

        return f'<{self.tag}>{childrenResult}</{self.tag}>'
