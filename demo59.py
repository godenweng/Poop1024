try:
    file1 = open('help/demo59','w')
    print("after open, prepare write")
    file1.write("Hollo world !!!!{}".format(5/0))
    print("write success")
except ValueError as Error:
    print("value error as:",Error)
except ZeroDivisionError as Error:
    print("divide by 0 error",Error)
except IOError as Error:
    print("OOPS exception happer",Error)
print("program proceed")

