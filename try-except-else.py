try:
    print(1)
except Exception as e:
    print("except",e)
else:
    print("else")
finally:
    print("finally")