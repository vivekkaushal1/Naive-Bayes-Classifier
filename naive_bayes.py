import math
print "Test Data for prediction:"
h = input("height : ")
w = input("weight : ")
a = input("age : ")


data = open('SampleData.csv','r')
all_data = data.readlines()
for i in range(0,len(all_data)):
    all_data[i] = all_data[i][0:-1]
    all_data[i] = all_data[i].split(',')

avg_height_m = 0.0
avg_height_w = 0.0
avg_weight_m = 0.0
avg_weight_w = 0.0
avg_age_m = 0.0
avg_age_w = 0.0

var_height_m = 0.0
var_height_w = 0.0
var_weight_m = 0.0
var_weight_w = 0.0
var_age_m = 0.0
var_age_w = 0.0

total_m = 0.0
total_w = 0.0

for i in range(0,len(all_data)):
    if all_data[i][3] == 'M':
        total_m += 1
        avg_height_m += int(all_data[i][0])
        avg_weight_m += int(all_data[i][1])
        avg_age_m += int(all_data[i][1])
    else:
        total_w += 1
        avg_height_w += int(all_data[i][0])
        avg_weight_w += int(all_data[i][1])
        avg_age_w += int(all_data[i][1])

prior_m = total_m / len(all_data)
prior_w = total_w / len(all_data)

avg_height_m = avg_height_m / total_m
avg_height_w = avg_height_w / total_w
avg_weight_m = avg_weight_m / total_m
avg_weight_w = avg_weight_w / total_w
avg_age_m = avg_age_m / total_m
avg_age_w = avg_age_w / total_w


for i in range(0,len(all_data)):
    if all_data[i][3] == 'M':
        var_height_m += pow((int(all_data[i][0]) - avg_height_m),2)
        var_weight_m += pow((int(all_data[i][1]) - avg_weight_m),2)
        var_age_m += pow((int(all_data[i][2]) - avg_age_m),2)
    else:
        var_height_w += pow((int(all_data[i][0]) - avg_height_w),2)
        var_weight_w += pow((int(all_data[i][1]) - avg_weight_w),2)
        var_age_w += pow((int(all_data[i][2]) - avg_age_w),2)

var_height_m /= (total_m-1)
var_weight_m /= (total_m-1)
var_age_m /= (total_m-1)
var_height_w /= (total_w-1)
var_weight_w /= (total_w-1)
var_age_w /= (total_w-1)


cons_h_m = (1 / math.sqrt(2*math.pi*var_height_m))
cons_w_m = (1 / math.sqrt(2*math.pi*var_weight_m))
cons_a_m = (1 / math.sqrt(2*math.pi*var_age_m))
cons_h_w = (1 / math.sqrt(2*math.pi*var_height_w))
cons_w_w = (1 / math.sqrt(2*math.pi*var_weight_w))
cons_a_w = (1 / math.sqrt(2*math.pi*var_age_w))




cm = math.log(prior_m,math.e)+math.log(cons_h_m,math.e)+math.log(cons_w_m,math.e)+math.log(cons_a_m,math.e)
cw = math.log(prior_w,math.e)+math.log(cons_h_w,math.e)+math.log(cons_w_w,math.e)+math.log(cons_a_w,math.e)


epp_m = (-0.5)*((pow((h-avg_height_m),2)/var_height_m) + (pow((w-avg_weight_m),2)/var_weight_m) + (pow((a-avg_age_m),2)/var_age_m))
post_prob_m = cm+epp_m

epp_w = (-0.5)*((pow((h-avg_height_w),2)/var_height_w) + (pow((w-avg_weight_w),2)/var_weight_w) + (pow((a-avg_age_w),2)/var_age_w))
post_prob_w = cw+epp_w

if post_prob_m > post_prob_w:
    print "\n\nClass : M\n\n"
else:
    print "\n\nClass : W\n\n"
