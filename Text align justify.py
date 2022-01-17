def split_to_lines(text, width):
    text = text.split()
    line_tmp = str(text.pop(0))
    all_lines = []
    while len(text) != 0:
        if len(line_tmp) + len(text[0]) < width:
            line_tmp += f" {text.pop(0)}"  
        else:
            all_lines.append(line_tmp)
            line_tmp = text.pop(0)
    all_lines.append(line_tmp)
    return all_lines

def stretch(line, width):
    if " " in line:
        diff = width - len(line)
        gap = " "
        while diff > 0:
            line = line.replace(gap, gap+" ", diff)
            diff = width - len(line)
            gap += " "
    return line

def justify(text, width):
    text_split_to_lines = split_to_lines(text, width)
    text_with_stretched_lines = [stretch(line, width) for line in text_split_to_lines[:-1]] + [text_split_to_lines[-1]]
    justified_text = "\n".join(text_with_stretched_lines)
    return justified_text
    


        
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor."

print()
print(justify(lorem, 30))
print()