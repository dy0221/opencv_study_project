def map(x, in_min, in_max, out_min, out_max):

    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

if __name__ == "__main__" :
    frame = map(0.1, 0,1,0,640)
    print(int(frame))
