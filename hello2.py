import argparse

parser = argparse.ArgumentParser(description='Say Hello')
parser.add_argument('name') 
parser.add_argument('--repeats', type=int, default=1, help='Repeats')
args = parser.parse_args()

for _ in range(args.repeats):
  print('Hello ' + args.name + '!')
