# a bit more practice with range

#for i in range(0, 11, 1):
#  print(i)

print("=== List Generator ===")
print()
start = int(input("Start at: "))
end = int(input("End before: "))
incr = int(input("Increment by: "))
print()
for i in range(start, end, incr):
    print(f"\033[93m{i}")
