"""Comp 110 Ex01 Part 2!"""
__author__ = "730442926"
R0: float = float(input("Enter R0: "))
t0: int = int(input("Enter t0 Cluster Size: "))
t1: int = round(float(t0 * R0))
Total: int = t0 + t1
print("t1 - New: " + str(t1) + " - Total: " + str(Total))
t2: int = round(float(t1 * R0))
Total: int = t0 + t1 + t2 
print("t2 - New: " + str(t2) + " - Total: " + str(Total))
t3: int = round(float(t2 * R0))
Total: int = t0 + t1 + t2 + t3
print("t3 - New: " + str(t3) + " - Total: " + str(Total))
t4: int = round(float(t3 * R0))
Total: int = t0 + t1 + t2 + t3 + t4
print("t4 - New: " + str(t4) + " - Total: " + str(Total))
