import itchat
itchat.auto_login()
friends = itchat.get_friends(update=True)[:]
total = len(friends) - 1
male = female = other = 0

for friend in friends[1:]:
    sex = friend["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
print("男性好友：%.2f%%" % (float(male) / total * 100))
print("女性好友：%.2f%%" % (float(female) / total * 100))
print("其他：%.2f%%" % (float(other) / total * 100))

   
# 导入matplotlib库
import matplotlib.mlab as mlab    
import matplotlib.pyplot as plt    
labels=['man','female','unknow']  
X=[ male, female, other]    
fig = plt.figure()  
plt.pie(X,labels=labels,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）  
plt.title("Pie chart")  
plt.show()    
plt.savefig("PieChart.jpg")

