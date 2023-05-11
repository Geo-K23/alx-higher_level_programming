#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for st in dir(hidden_4):
        if st[:2] != "__":
            print("{:s}".format(st))
