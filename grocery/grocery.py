def main():
    dict = {}
    while True:

        try:
            x = input().upper()
            if x not in dict:
                dict.update({x:1})
            else:
                dict[x]=dict[x]+1



        except EOFError:
            break

    for item in sorted(dict):
        print(dict[item],item)
main()