print "split your and last name"
name = "guy jacks"

# split returns a list of strings
print name.split()
print "/n"

print "split a comma separated list of colors"
colors = "yellow, black, blue"
print colors.split(',')
print "\n"

print "get the 3rd character of the word banana"
print "banana"[2]
print "\n"

blue_moon = "Blue Moon"

print "get the first character of Blue Moon.  get the last."
print blue_moon[0]
print blue_moon[-1]
print "\n"

print "get the last four characters of Blue Moon"
print blue_moon[4:]
print "\n"

print "get the first four characters of Blue Moon"
print blue_moon[:4]
print "\n"

print "get \"Moo\" from Blue Moon"
print blue_moon[5:8]
print "\n"

print "replace Blue with Full in Blue Moon"
print blue_moon.replace("Blue", "Full")
print "\n"

print "covert Blue Moon to lowercase.  uppercase"
print blue_moon.lower()
print blue_moon.upper()
