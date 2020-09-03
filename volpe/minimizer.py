import re

def minimize(source):
    with open(source, "r") as input_file:
        out = input_file.read()

    # remove comments
    out = re.sub("(#!.*?!#)|(#.*?\n)", "", out)
    
    # remove spaces outside of strings and chars
    for match in re.findall("\".*?\"|' '", out):
        # replace spaces inside strings and chars with woozy face
        woozied_match = match.replace(" ", "🥴")
        out = out.replace(match, woozied_match)
    out = out.replace(" ", "")
    # restore spaces inside strings and chars
    out = out.replace("🥴", " ")

    # put everything into a single line
    out = out.replace("\n", ";")
    while ";;" in out:
        out = out.replace(";;", ";")
    out = out.replace("{;", "{")
    out = out.replace(";}", "}")
    out = out.replace(",;", ",")

    # get rid of leading and trailing semi-colon
    if out[-1] == ";":
        out = out[:-1]
    if out[0] == ";":
        out = out[1:]

    # shorten variable names
    names = set()
    for match in re.findall("\".*?\"|'.*?'|([a-zA-Z_]*)", out):
        if len(match) > 1:
            names.add(match)
    names = sorted(names, key=lambda name: len(name), reverse=True)
    for i, name in enumerate(names):
        out = out.replace(name, f"_{i}")

    return out
    

if __name__ == "__main__":
    
    with open("mini.vlp", "w") as output_file:
        output_file.write(minimize("examples/mandelbrot.vlp"))