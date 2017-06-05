def growingPlant(upSpeed, downSpeed, desiredHeight):
    
    
    if ( desiredHeight < upSpeed):
        return 1;
    
    num_of_days = int(desiredHeight/(upSpeed-downSpeed))
    if(((num_of_days * (upSpeed-downSpeed)) + downSpeed >= desiredHeight)):
        return num_of_days;
    else :
        return num_of_days+1;
