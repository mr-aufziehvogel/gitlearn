lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
#Type your answer here.

lst2=list(map(lambda x: int(x.count("a") + x.count("A")),lst1))


print(lst2)

