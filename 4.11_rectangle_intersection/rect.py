
class Rect:
    def __init__(self, x, y, w, h) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __eq__(self, o) -> bool:
        return self.x == o.x and \
        self.y == o.y  and \
        self.w == o.w  and \
        self.h == o.h

    def __str__(self) -> str:
        return str((self.x,self.y,self.w,self.h))

def intersection(r1, r2):
    if  (r2.x >= r1.x and r2.x <= r1.x + r1.w) and \
        (r2.y >= r1.y and r2.y <= r1.y + r1.w):
        # at least one point within bounds
        r = Rect(
            x = max(r1.x, r2.x),
            y = max(r1.y, r2.y),
            w = min(r1.x + r1.w, r2.x + r2.w) - max(r1.x, r2.x),
            h = min(r1.y + r1.h, r2.y + r2.h) - max(r1.y, r2.y),
        )
        return r
    else:
        return None

assert intersection(Rect(0,0,1,1),Rect(2,2,1,1)) == None
assert intersection(Rect(0,0,4,4),Rect(2,2,4,4)) == Rect(2,2,2,2)
assert intersection(Rect(0,0,4,4),Rect(4,4,4,4)) == Rect(4,4,0,0)
assert intersection(Rect(0,0,4,4),Rect(4,4,4,4)) == Rect(4,4,0,0)
assert intersection(Rect(0,0,4,4),Rect(1,0,2,2)) == Rect(1,0,2,2)
