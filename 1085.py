x, y, w, h = map(int, input().split())
# print(min(x,y,w-x,h-y))

ymin = 0
if h - y > y:
    ymin = y
else:
    ymin = h - y

xmin = 0
if w - x > x:
    xmin = x
else:
    xmin = w - x

if ymin > xmin:
    print(xmin)
else:
    print(ymin)
