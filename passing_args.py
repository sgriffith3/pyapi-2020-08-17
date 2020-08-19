import argparse

parser = argparse.ArgumentParser(description="Learning How to Use Argparse")

# Required Positional Arguments
parser.add_argument("addit", type=int, help="An int we want to pass to mathy()")
parser.add_argument("subit", type=int, help="An int we want to pass to mathy02()")

# Optional Arguments
parser.add_argument("--multit", type=int, default=0, help="An int we want to pass to mathy03()")
parser.add_argument("-p", "--port", type=int, default=9999, help="The port we want to serve the API on")
parser.add_argument("-d", "--dev", default=False, action="store_true", help="If this flag is thrown, this will serve in development mode")
parser.add_argument("-n", "--name", required=True, help="Your name")
parser.add_argument("--nums", type=int, nargs='+', help="Numbers to sum")

args = parser.parse_args()

print(args)
print(type(args))
print(args.addit)
print(args.subit)
print(args.multit)
print(args.port)
print(args.dev)
print(args.name)
print(args.nums)


def mathy(x):
    print(x + 111)

def mathy02(x):
    print(x - 111)

def mathy03(x=0):
    print(x * 111)

def mathy04(x):
    y = 0
    for num in x:
        print(num)
        y += num
        print(f"Sum is now: {y}")

mathy(args.addit)
mathy02(args.subit)
if args.multit:
    mathy03(args.multit)
if not args.dev:
    print(f"We are serving on port: {args.port}")
else:
    print(f"We are in DEV mode. We would be serving on {args.port}")
print(f"Your name is: {args.name}")
print("Yay our args are working")

mathy04(args.nums)
