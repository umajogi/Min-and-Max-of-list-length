#min and max values and its length from the list
l=[[1,2],[3,4],[10,20,5],[10,20,30]]
minv=min(l,key=len)
maxv=max(l,key=len)
print(l.index(minv),minv)
print(l.index(maxv),maxv)
