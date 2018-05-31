from broker import Broker
from rotation import Rotation
def main():
    b = Broker('test')
    print(b)
if __name__ == '__main__':
    Rotation().cmdloop()