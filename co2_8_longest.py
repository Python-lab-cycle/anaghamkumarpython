def longestLength(a):
max1 = len(a[0])
temp = a[0]

# for loop to traverse the list
for i in a:
if(len(i) &gt; max1):

max1 = len(i)
temp = i

print(&quot;The word with the longest length is:&quot;, temp,
&quot; and length is &quot;, max1)

# Driver Program
a = [&quot;one&quot;, &quot;two&quot;, &quot;third&quot;, &quot;four&quot;]
longestLength(a)
