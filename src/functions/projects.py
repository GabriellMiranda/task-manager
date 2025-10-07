def hello():
    print("Hello, World!")

def handler(event, context):
    hello()

if __name__ == "__main__":
    handler()