totalseconds = int(input("Enter the total number of seconds: "))

hours = int(totalseconds / 3600)
seconds = totalseconds % 3600

minutes = int(seconds / 60)
seconds = seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)