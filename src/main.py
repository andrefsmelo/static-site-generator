from textnode import TextType, TextNode

def main():
    dummy_node  = TextNode(
        text="This is some anchor text", 
        text_type=TextType.LINK, 
        url="https://www.boot.dev"
    )
    print(dummy_node)

if __name__ == "__main__":
    main()
