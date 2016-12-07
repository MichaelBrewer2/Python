#!/usr/bin/python

import random
import math

def main():
	avg_arr = 0
	avg_max = 0
	total_arr = 0
	total_max = 0
	iterations = 100

	for i in range(0, iterations):
		r_a = 4
		r_d = 1
		#k IS USED FOR WEIBULL
		#k = 5
		time_close = 10000
		
		t = 0
		n_a = 0
		n_d = 0
		state = 0
		
			#FIRST ARRIVAL
		u = random.random()
		t_a = (-r_a)*math.log(1 - u)
			#DEPARTURE TIME SET TO INFINITY
		t_d = math.inf
			#LISTS FOR EVENT TIMES
		arrivals = []
		departures = []
			#MAX LINE LENGTH
		max_line = 0
	
		while(1):
			#NEXT EVENT IS AN ARRIVAL
			if((t_a <= t_d) and (t_a <= time_close)):
				t = t_a
				state = state + 1
				if(state > max_line):
					max_line = state
				u = random.random()
				t_a = t + (-r_a)*math.log(1 - u)
				if(state == 1):
					y = random.random()
					t_d = t + (-r_d)*math.log(1 - y)
					#WEIBULL DEPARTURE BELOW
					#t_d = t + ((r_d)*((-math.log(1 - y))**(1/k)))
				arrivals.append(t)

			#NEXT EVENT IS A DEPARTURE	
			elif((t_d <= t_a) and (t_d <= time_close)):
				t = t_d
				state = state - 1
				n_d = n_d + 1
				if(state == 0):
					t_d = math.inf
				else:
					y = random.random()
					t_d = t + (-r_d)*math.log(1 - y)
					#WEIBULL DEPARTURE BELOW
					#t_d = t + ((r_d)*((-math.log(1 - y))**(1/k)))
				departures.append(t)
	
			#AFTER TIME_CLOSE
			elif((min(t_a, t_d) > time_close) and (state > 0)):
				t = t_d
				state = state - 1
				n_d = n_d + 1
				if(state > 0):
					y = random.random()
					t_d = t + (-r_d)*math.log(1 - y)
					#WEIBULL DEPARTURE BELOW
					#t_d = t + ((r_d)*((-math.log(1 - y))**(1/k)))
				departures.append(t)
	
			elif((min(t_a, t_d) > time_close) and (state == 0)):
				t_p = max(t - time_close, 0)
				break
	
		total_arr = total_arr + len(arrivals)
		total_max = total_max + max_line
	print("Iterations: " + str(iterations))
	print("Parameters:")
	print("     E[x].arrival: " + str(r_a))
	#E[x].DEPARTURES ALSO SERVES AS LAMBDA FOR WEIBULL
	print("     E[x].departures: " + str(r_d))
	#K VALUE FOR WEIBULL BELOW
	#print("     k.weibull: " + str(k))
	print("     Time: " + str(time_close))
	avg_arr = int(total_arr / iterations)
	print("Avg Arrivals: " + str(avg_arr))
	avg_max = int(total_max / iterations)
	print("Avg Max Line Length: " + str(avg_max))

main()
