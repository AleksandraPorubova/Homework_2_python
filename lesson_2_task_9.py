var_1 = 37     # 1-й способ
var_2 = 99

var_3 = var_2
var_2 = var_1
var_1 = var_3

print ("var_1 = ", var_1)
print ("var_2 = ", var_2)


var_1 = 37     # 2-й способ
var_2 = 99

var_1 = var_1 + var_2
var_2 = var_1 - var_2
var_1 = var_1 - var_2

print ("var_1 = ", var_1)
print ("var_2 = ", var_2)