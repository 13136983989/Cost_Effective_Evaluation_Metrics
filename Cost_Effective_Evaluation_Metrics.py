import math
#Example baseline ResNet 18
time_1 = 1.22
time_4 = 2.19
time_8 = 3.63
FLOPs_G = 1.83
Params_M = 11.70
ACC = 0.7098





def main():
    avg_time = (time_1 + time_4 + time_8)/3.0
    p = math.sqrt(math.pow(FLOPs_G,2)+math.pow(Params_M,2)+math.pow(avg_time,2))
    print("The complexity index ρ is",p)
    y = -14.6*math.pow(ACC,2)+2.5*ACC+2.9
    _lambda = 1/(1+math.pow(math.exp( 1 ) ,-y))
    TALES = (ACC*100)/(_lambda*p)
    print('TALES (Cost Effective Evaluation Metrics):',TALES)


if __name__ =="__main__":
    main()





