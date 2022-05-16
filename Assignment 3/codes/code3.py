'''Let Pr{X = 0} be P_0
       Pr{X = 1} be P_1
       Pr{X = 2} be P_2
       Pr{X = 3} be P_3
       Pr{X = 4} be P_4
'''
P_0 = 13/52
P_1 = 48/52
P_2 = 26/52
P_3 = 39/52
P_4 = 26/52


#checking if all the obtained probabilties lie between 0 and 1.
if P_0<=1 and P_0>=0 and P_1<=1 and P_1>=0 and P_2<=1 and P_2>=0 and P_3<=1 and P_3>=0 and P_4<=1 and P_4>=0 :
    "continue"
    
#checking if the complementary probabilities sum up to 1.
p1 = P_0 + P_3
p2 = P_2 + P_4

if p1 == 1 and p2 == 1:
    print("Pr{X = 0} = 1/4\nPr{X = 1} = 12/13\nPr{X = 2} = 1/2\nPr{X = 3} = 3/4\nPr{X = 4} = 1/2")