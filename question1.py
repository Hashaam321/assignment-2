temperatures=[25,30,27,22,28,33,29]
days=("monday","tuesday","wednesday","thursday","friday","satursday","sunday")

temperature_data=list(zip(days,temperatures))
for day , temp in temperature_data:
    print(f"{day}:{temp}°C")

max_temp=max(temperatures)
max_temp_day=days[temperatures.index(max_temp)]

print(" the maximum temperature:")
print(f"Temperature :{max_temp}°C")
print(f"day:{max_temp_day}")
total_temp=sum(temperatures)
num_days=len(temperatures)
average_temp=total_temp/num_days
print(f"The average temeprature is :{average_temp:2f}°C")
