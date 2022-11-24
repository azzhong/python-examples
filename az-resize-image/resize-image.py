from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='Description of your program')
parser.add_argument('-i','--input', help='input file', required=True)
parser.add_argument('-f','--factor', help='size factor, for example, 0.5 means half of the original size', required=True, type=float)
parser.add_argument('-o','--output', help='output file', required=True)
args = vars(parser.parse_args())

inputFile = args['input']
factor = args['factor']
outputFile = args['output']

print(f'={inputFile}')

foo = Image.open(inputFile)  
(h, w) = foo.size  
factor = 0.5
h = int(h*factor)
w = int(w*factor)

foo = foo.resize((h, w),Image.ANTIALIAS)
foo.save(outputFile, optimize=True, quality=95)  