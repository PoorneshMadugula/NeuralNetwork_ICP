
with open('input.txt', 'r') as file:
    Input_Line = file.readlines()

w_counts = []
for line in Input_Line:
    ws = line.strip().split()
    w_count = {w: ws.count(w) for w in set(ws)}
    w_counts.append(w_count)

with open('output.txt', 'w') as output_file:
    for i, counts in enumerate(w_counts, start=1):
        print(f"Line {i}:")
        output_file.write(f"Line {i}:\n")

        for w, count in counts.items():
            print(f"{w}: {count}")
            output_file.write(f"{w}: {count}\n")

        print()  
        output_file.write('\n')
