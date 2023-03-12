#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = dir(hidden_4)
    no_names = len(dir(hidden_4))
    for i in range(no_names):
        current = names[i]
        if current[0] == '_':
            continue
        print("{name}".format(name=current), end='')
