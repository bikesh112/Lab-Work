distance=4
speed1=25
stopingtime=10*2
time=1/speed1
time_1=time*60
total_time=time_1 + stopingtime
print(f"the total time to reach university by bus is {total_time}")

speed2=7
time1=1/speed2
Time_1=time1*60

speed3=15
time2=2/speed3
time_2=time2*60

speed4=7
time3=1/speed4
time_3=time3*60
total_time2=Time_1+time_2+time_3
print(f"total time of walking upto university is {total_time2}")

if total_time2>total_time:
    print(f"walking is faster then bus to reach university")
    s