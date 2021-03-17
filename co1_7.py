l1=[1,2,3]
l2=[1,2,]
print("Lists are same or not ?:",len(l1)==len(l2))
print("Sum of list elements are same or not ?:",sum(l1)==l2)
dupli=[x for x in l1 if x in l2]
if dupli:
    print("Any vale occur in both ?:",dupli)
