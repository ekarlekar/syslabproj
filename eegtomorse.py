path = "C:\\Users\\atinr\\OneDrive\\Documents\\GitHub\\syslabproj\\OSC-server\\output.txt"
f = open(path)
blink_counter = 0
for line in f:
    if line == "blink\n":
        blink_counter += 1
        if blink_counter == 5:
            print("blink detected")
    elif line == "neutral\n":
        blink_counter = 0
