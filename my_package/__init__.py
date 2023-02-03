
if __name__ == '__main__' :
    from os import path
    import sys
    #절대 경로
    print(print(path.dirname( path.dirname( path.abspath(__file__) ) )))
    sys.path.append(path.dirname( path.dirname( path.abspath(__file__) ) ))

    from map_function import map
    
    from checksum import checksum
  
else :
    #상대 경로
    from .map_function import map
    
    from .checksum import checksum