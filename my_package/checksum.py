
def checksum(x: any, y: any) ->bytes :
    chk = 0
    chk = chk^int(x)
    chk = chk^int(y)
    return chk


if __name__ =="__main__":
    chk = checksum(400,600)
    print(chk)