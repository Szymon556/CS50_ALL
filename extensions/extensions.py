def extension(name):
    name2=name.strip().lower()
    ext = name2.split(".")#dzielimy nazwe pliku na to co za kropka i przed bo nazwa pliku moze miec tylko jedna kropke
    match ext[-1]:#to za kropka to rozszerzenie i teraz dopasujemy jakie rozszerzenie do jakiego typu mediow

        case "jpeg"|"jpg":
            print("image/jpeg")
        case "gif":
            print("image/gif")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")



resource = input("File name: ")
extension(resource)