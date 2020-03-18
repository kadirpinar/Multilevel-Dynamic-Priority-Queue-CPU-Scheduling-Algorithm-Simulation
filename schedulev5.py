import numpy as np
import random
import matplotlib.pyplot as plt
class process():
    def __init__(self,burst_time="None",arrival_time="None"):
        self.burst_time=burst_time
        self.arrival_time=arrival_time

n = np.random.poisson(5, 5)
rnd=np.random.exponential(5,5)

p1=process()
p2=process()
p3=process()
p4=process()
p5=process()

p1.arrival_time=n[0]
p2.arrival_time=n[1]
p3.arrival_time=n[2]
p4.arrival_time=n[3]
p5.arrival_time=n[4]

p1.burst_time = rnd[0]
p2.burst_time = rnd[1]
p3.burst_time = rnd[2]
p4.burst_time = rnd[3]
p5.burst_time = rnd[4]


fcfs=[]
fcfs_burst_time=[]
fcfs_arrival_time=[]


sjf=[]
sjf_burst_time=[]
sjf_arrival_time=[]
p=[]


for i in range(0,5):
    x=random.randint(1, 2)
    if (x==1):
        fcfs.append("p{}".format(i))
        fcfs_arrival_time.append(n[i])
        fcfs_burst_time.append(int(rnd[i]))



    else:
        sjf.append("p{}".format(i))
        sjf_arrival_time.append(n[i])
        sjf_burst_time.append(int(rnd[i]))

print(fcfs)
print(fcfs_burst_time)
print(fcfs_arrival_time)

print(sjf)
print(sjf_burst_time)
print(sjf_arrival_time)

f=[]
s=[]
array=[]
array1=[]

process=[]
process1=[]

r1=[]
r2=[]


queu=[]
for  i in range (0,len(fcfs)):
    f.append(0)

for  i in range (0,len(sjf)):
    s.append(1)



for i in range(0,len(sjf)):
    process.append(sjf[i])
    process.append(s[i])
    process.append(sjf_burst_time[i])
    process.append(sjf_arrival_time[i])

for i in range(0,len(fcfs)):
    process.append(fcfs[i])
    process.append(f[i])
    process.append(fcfs_burst_time[i])
    process.append(fcfs_arrival_time[i])




queu=np.reshape(process,(-1,4))


idle=0
idle_count=0
print(queu)
count = 0
rand=random.random()
fcfs_length=[]
queu_time=[]
sjf_length=[]

fcfs_pri=[]
sjf_pri=[]
count_pri=[]
arv=[]


lim=0.6
while(1):
    if((int(queu[0][1])==-1  and int(queu[1][1])==-1 and int(queu[2][1])==-1 and int(queu[3][1])==-1) and int(queu[4][1])==-1 and array==[] and array1==[]):
        fcfs_length.append(0)
        sjf_length.append(0)
        queu_time.append(count)

        fcfs_pri.append(lim)
        sjf_pri.append((1 - lim))
        count_pri.append(count)
        break

    else:
        rand = random.random()
        print(rand)

        fcfs_length.append(0)
        sjf_length.append(0)
        queu_time.append(count)

        fcfs_pri.append(lim)
        sjf_pri.append((1 - lim))
        count_pri.append(count)

        for j in range(0,len(queu)):
            print("count:{}".format(count))
            print(queu[j][3])
            a=int(queu[j][3])
            b=int (queu[j][1])





            if rand<lim:

                if (count >= a ):




                    for i in range(0,len(queu)):

                        if (count >= int(queu[i][3]) and int(queu[i][1]) == 1):
                            r1.append(queu[i][0])
                            array.append(int(queu[i][2]))
                            queu[i][1]=int(-1)


                    print("sjf queu len :{}".format(len(array)))

                    if len(array)==0:
                        for i in range(0, len(queu)):
                            if (count >= int(queu[i][3]) and int(queu[i][1]) == 0):
                                r1.append(queu[i][0])
                                array1.append(int(queu[i][2]))
                                arv.append(int(queu[i][3]))
                                queu[i][1] = int(-1)
                        print(arv)
                        if len(arv) == 0:
                            break
                        else:
                            min_arrival = np.argmin(arv)

                        arv.pop(min_arrival)
                        print("fcfs queu len :{}".format(len(array1)))
                        if len(array1) == 0:
                            break
                        fcfs_length.pop()
                        fcfs_length.append(len(array1))

                        r2.append(count)
                        count += array1[min_arrival]
                        print("fcfs")
                        if (len(array1) == 1 and array1[0] == 1):
                            arv.clear()
                            array1.clear()
                            count -= 1

                            break
                        array1.pop(min_arrival)
                        count -= 1
                        break

                    sjf_length.pop()
                    sjf_length.append(len(array))
                    array.sort()
                    r2.append(count)
                    count+=array[0]
                    print("sjf")

                    if (len(array) == 1 and array[0] == 1):
                        array.clear()
                        count -= 1
                        break
                    array.pop(0)
                    count -= 1

                    break
                else:

                    idle += 1
                    if idle / 5 == 1:
                        idle = 0
                        idle_count += 1
                    if idle_count == 3:
                        idle_count = 0
                        lim-=0.1
                        print("idle")



            if rand>=lim:
                if ((count>=a ) ):



                    for i in range(0,len(queu)):
                        if (count >= int(queu[i][3]) and int(queu[i][1]) == 0):
                            r1.append(queu[i][0])
                            array1.append(int(queu[i][2]))
                            arv.append(int(queu[i][3]))
                            queu[i][1] = int(-1)
                    print(arv)
                    if len(arv)==0:
                        for i in range(0, len(queu)):

                            if (count >= int(queu[i][3]) and int(queu[i][1]) == 1):
                                r1.append(queu[i][0])
                                array.append(int(queu[i][2]))
                                queu[i][1] = int(-1)

                        print("sjf queu len :{}".format(len(array)))
                        sjf_length.pop()
                        sjf_length.append(len(array))
                        array.sort()
                        r2.append(count)
                        count += array[0]
                        print("sjf")

                        if (len(array) == 1 and array[0] == 1):
                            array.clear()
                            count -= 1
                            break
                        count -= 1
                        array.pop(0)
                        break

                    else:
                        min_arrival=np.argmin(arv)

                    arv.pop(min_arrival)
                    print("fcfs queu len :{}".format(len(array1)))
                    if len(array1)==0:
                        break
                    fcfs_length.pop()
                    fcfs_length.append(len(array1))

                    r2.append(count)
                    count += array1[min_arrival]
                    print("fcfs")
                    if(len(array1)==1 and array1[0]==1):
                        arv.clear()
                        array1.clear()
                        count -= 1
                        break
                    array1.pop(min_arrival)
                    count -= 1
                    break
                else:

                    idle += 1
                    if idle / 5 == 1:
                        idle=0
                        idle_count += 1

                    if idle_count == 3:
                        idle_count=0
                        lim-=0.1
                        print("idle")



        count+=1

print(count)

print(queu[0][1])
print(queu[1][1])
print(queu[2][1])
print(queu[3][1])
print(queu[4][1])

print(r1)
print(r2)
x=r1
y=r2

r=count-min(r2)
utilization=float(r/count)
turnaroundtime=0
throughput=5/count


for i in range(len(queu)):
    turnaroundtime+=int(queu[i][3])

y_post = np.arange(len(r2))
a=[]
b=[]
for i in range (0,len(queu)):
   a.append(queu[i][3])
   b.append(queu[i][2])


plt.bar(x,y,align="center",alpha=0.5)
plt.ylabel('Time')
plt.xlabel('Process')
plt.title('Response & Waiting Time')
plt.show()

a.sort()
plt.bar(x,a,align="center",alpha=0.5)
plt.ylabel('Arrival Time')
plt.xlabel('Process')
plt.show()
b.sort()
plt.bar(x,b,align="center",alpha=0.5)
plt.ylabel('Burst Time')
plt.xlabel('Process')
plt.show()


plt.bar('Utilization',utilization,align="center",alpha=0.5)
plt.title('Utilization')
plt.show()

plt.bar('Turnaround Time',turnaroundtime,align="center",alpha=0.5)
plt.title('Turnaround Time')
plt.show()


plt.bar('Throughput',throughput,align="center",alpha=0.5)
plt.title('Throughput')
plt.show()
avg_fcfs=0
avg_sjf=0

for i in range(len(fcfs_length)):
    avg_fcfs+=fcfs_length[i]
avg_fcfs=avg_fcfs/len(fcfs_length)

for i in range(len(sjf_length)):
    avg_sjf+=sjf_length[i]
avg_sjf=avg_sjf/len(sjf_length)

plt.plot(queu_time,fcfs_length)
plt.xlabel(' Time')
plt.ylabel('FCFS Length')
plt.show()

plt.plot(queu_time,sjf_length)
plt.xlabel(' Time')
plt.ylabel('SJF Length')
plt.show()


plt.bar('AVG FCFS LENGTH',avg_fcfs,align="center",alpha=0.5)
plt.title('AVG FCFS LENGTH')
plt.show()
plt.bar('AVG SJF LENGTH',avg_sjf,align="center",alpha=0.5)
plt.title('AVG SJF LENGTH')
plt.show()

plt.plot(sjf_pri,fcfs_pri)


plt.show()




print(fcfs_length)
print(sjf_length)
print(queu_time)

print(avg_fcfs)
print(avg_sjf)

print(fcfs_pri)
print(sjf_pri)
print(count_pri)


