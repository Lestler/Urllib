import urllib.request, urllib.parse, urllib.error
web=input("Enter - ")
fhand=urllib.request.urlopen(web)

for line in fhand:
    print(line.decode().strip())
