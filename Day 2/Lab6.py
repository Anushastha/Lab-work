#You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each
#of the 10 stops on the way. How long will the bus journey take? Alternatively, you could
#run to university. You jog the first mile at 7mph; then run the next two at 15mph; before
#jogging the last at 7mph again. Will this be quicker or slower than the bus?

distance=4
velocity=25
t1=((distance/velocity)*60)
#bus stops at 10 stops and spends 2 mintues at each stop
t2=10*2
total1=t1+t2
print(f"The total time to reach university by bus {total1}")
#he runs with the speed of 7mph
j1=((1/7)*60)
j2=((2/15)*60)
j3=((1/7)*60)
total2=j1+j2+j3
print(f"The total time taken running is {total2}")
if total1>total2:
    print(f"Going by bus is slower.")
else:
    print(f"Going on foot is quicker.")

