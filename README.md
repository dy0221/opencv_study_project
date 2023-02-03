    RIGHT_EYE = 0
    LEFT_EYE = 1
    NOSE_TIP = 2
    MOUTH_CENTER = 3
    RIGHT_EAR_TRAGION = 4
    LEFT_EAR_TRAGION = 5
    
    w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("원본 동영상 너비(가로) : {}, 높이(세로) : {}".format(w, h))