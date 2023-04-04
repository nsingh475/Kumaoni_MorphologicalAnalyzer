import sys

print('digraph G { rankdir="LR"')
print('node [fontname="Lohit Devanagari",shape=circle,fontsize=14,fixedsize=true,fillcolor="grey",style=filled]')
print('edge [fontname="Lohit Devanagari",fontsize=14]')

# Read input as bytes and decode using UTF-8 encoding
input_bytes = sys.stdin.buffer.read()
input_text = input_bytes.decode('utf-8')

# Split the input into lines and process each line
for line in input_text.split('\n'):
    line = line.strip()
    row = line.split('\t')
    if len(row) >= 4:
        print('%s [label="%s"];' % (row[0], row[0]))
        print('%s -> %s [label="%s:%s"];' % (row[0], row[1], row[2], row[3]))
    elif len(row) == 2: # Final state
        print('%s [label="%s",shape=doublecircle];' % (row[0], row[0]))
        print('}')

