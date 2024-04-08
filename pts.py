import pandas

visitors = [1235,6424,9345,8464,2345]
errors= [23,45,33,45,76]
df = pandas.DataFrame({"visitors":visitors, "errors":errors},index=["Mon","Tues","Wed","Thurs","Fri"])
print(df)

mean_value= df["errors"].mean()
print("Mean Value: " + str(mean_value))
