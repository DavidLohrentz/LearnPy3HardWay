from sys import argv; from os.path import exists
script, from_file, to_file = argv
in_file = open(from_file); indata = in_file.read()
print(">>>>>>>>>> indata", repr(indata))

print(f"The input file is {len(indata)} bytes long\nDoes Goldy's dick exist? {exists(to_file)}\nReady, hit RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close(); in_file.close()
