#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
#of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
#run to university. You jog the first mile at 7mph; then run the next two at 15mph; before
#jogging the last at 7mph again. Will this be quicker or slower than the bus?

distance=4
x=25
#bus stops at 10 stops and spends 2 mintues at each stop
stop_time=10*2
e=1/x
t=e*60
total_time=t+stop_time
print(f"The total time to reach university by bus {total_time}")
#he runs with the speed of 7mph
y=7
f=1/y
time_1=f*60
z=15
g=2/z
time_2=g*60
a=7
h=1/a
time_3=h*60
total_time2=time_1+time_2+time_3
print(f"The total time taken running is {total_time2}")
if total_time2>total_time:
    print(f"Running is slower than bus.")
