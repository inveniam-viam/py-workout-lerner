# Solution to exercise 24

# kwargs can be used to pass an arbitrary number of keyword args
# they can be accessed in the same way a dictionary is accessed

def myxml(tag, content = '', **kwargs):

    attrs = ' '.join(f"{key} = {value}" for key, value in kwargs.items())

    out_str: str = f"<{tag} {attrs}>{content}</{tag}>"

    return out_str

