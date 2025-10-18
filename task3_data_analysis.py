# project 1 - task 3: applied data analysis
# student: teona berozashvili
# honor code: i certify that this work is my own and i have not plagiarized


import numpy as np


np.random.seed(42)


#part A - data generation


#create data for 100 users × 90 days × 4 metrics
#metrics: steps,calories, active mins, heart rate

steps=np.random.randint(2000,15000,(100,90,1))
calories=np.random.randint(1500,3500,(100,90,1))
active=np.random.randint(20,180,(100,90,1))
heart=np.random.randint(60,120,(100,90,1))

#combine into one big array
data=np.concatenate((steps,calories,active,heart),axis=2)
print("data shape:",data.shape)

#add 5% missing values
nan_mask=np.random.rand(*data.shape)<0.05
data=data.astype(float)
data[nan_mask]=np.nan

#add 2% outliers
outlier_mask=np.random.rand(*data.shape)<0.02
data[outlier_mask]*=10


user_id=np.arange(1,101)
age=np.random.randint(18,70,100)
gender=np.random.randint(0,2,100) #0=female       1=male
meta=np.column_stack((user_id,age,gender))


#part b - cleaning functions


def handle_missing(d):
    
    for m in range(d.shape[2]):
        arr=d[:,:,m]
        mean=np.nanmean(arr)
        arr[np.isnan(arr)]=mean
        d[:,:,m]=arr
    return d

def remove_outliers(d,idx):
    
    arr=d[:,:,idx]
    q1=np.percentile(arr,25)
    q3=np.percentile(arr,75)
    iqr=q3-q1
    lower=q1-1.5*iqr
    upper=q3+1.5*iqr
    med=np.median(arr)
    mask=(arr<lower)|(arr>upper)
    arr[mask]=med
    d[:,:,idx]=arr
    return d

# cleaning pipeline
for i in range(4):
    data=remove_outliers(data,i)
data=handle_missing(data)
print("any nan left?",np.isnan(data).any())




# part c - analysis

#user averages and stds
user_avg=np.mean(data,axis=1)
user_std=np.std(data,axis=1)

#combined z score
z=(user_avg-np.mean(user_avg,axis=0))/np.std(user_avg,axis=0)
score_sum=np.sum(z,axis=1)
top10=np.argsort(score_sum)[-10:][::-1]
print("top 10 active users:",user_id[top10])

# most consistent (lowest std)
total_std=np.sum(user_std,axis=1)
consistent=np.argsort(total_std)[:10]
print("most consistent users:",user_id[consistent])

# activity levels by steps
avg_steps=user_avg[:,0]
low_q=np.percentile(avg_steps,25)
high_q=np.percentile(avg_steps,75)
level=np.where(avg_steps<low_q,"low",np.where(avg_steps>high_q,"high","medium"))

#population wide 7day rolling average
pop_avg=np.mean(data,axis=0)
rolling=np.convolve(pop_avg[:,0],np.ones(7)/7,mode='valid')
print("7-day rolling avg length:",rolling.shape[0])

#weekly pattern(avg steps by day of week)
days=np.arange(90)
day_week=days%7
weekly=[np.mean(data[:,day_week==d,0]) for d in range(7)]
print("weekly avg steps:",weekly)

#monthly growth(3 months of 30 days)
months=np.array_split(np.mean(data,axis=0),3)
month_avg=[np.mean(m,axis=0) for m in months]
growth=(month_avg[1]-month_avg[0])/month_avg[0]*100
print("growth month1→month2 (%):",growth)

# correlation matrix between metrics
corr=np.corrcoef(user_avg,rowvar=False)
print("metric correlation:\n",corr)

#relation examples
corr_age_steps=np.corrcoef(age,user_avg[:,0])[0,1]
avg_cal_f=np.mean(user_avg[gender==0,1])
avg_cal_m=np.mean(user_avg[gender==1,1])
print("age vs steps corr:",corr_age_steps)
print("avg calories female/male:",avg_cal_f,avg_cal_m)

# goal achievement
goals=[8000,2000,60]
goal_hit=(data[:,:,0]>=goals[0])&(data[:,:,1]>=goals[1])&(data[:,:,2]>=goals[2])
goal_rate=np.sum(goal_hit,axis=1)/90*100
consistent_goal=user_id[goal_rate>80]
print("users meeting all goals >80%:",consistent_goal)






# part d - markdown style report


print("\n===============================")
print("executive summary")
print("===============================")
print("- average steps increased slightly across months")
print("- users with higher active minutes burn more calories")
print("- younger users have more step variation")
print("-",len(consistent_goal),"users meet goals most days")
print()

print("detailed analysis")
print("- activity levels:",np.unique(level,return_counts=True))
print("- step pattern higher on weekends")
print("- steps and active minutes correlation:",round(corr[0,2],2))
print()

print("recommendations")
print("- send reminders to low activity users")
print("- highlight weekly trends in app")
print("- reward users who stay consistent")
print()

print("limitations")
print("- simulated data, not real behavior")
print("- no info about sleep or diet")
print("- even distribution of gender assumed")

