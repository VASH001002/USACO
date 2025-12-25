def main():
    lx1, ly1, lx2, ly2 = map(int, input().split())   # billboard
    bx1, by1, bx2, by2 = map(int, input().split())   # truck

    total = (lx2 - lx1) * (ly2 - ly1)

    # Find overlap rectangle
    ox1 = max(lx1, bx1)
    oy1 = max(ly1, by1)
    ox2 = min(lx2, bx2)
    oy2 = min(ly2, by2)

    if ox1 < ox2 and oy1 < oy2:  # overlap exists
        # Case 1: truck covers entire billboard (both x and y fully)
        if bx1 <= lx1 and bx2 >= lx2 and by1 <= ly1 and by2 >= ly2:
            total = 0
        # Case 2: truck spans billboard fully in X
        elif bx1 <= lx1 and bx2 >= lx2:
            total -= (ox2 - ox1) * (oy2 - oy1)
        # Case 3: truck spans billboard fully in Y
        elif by1 <= ly1 and by2 >= ly2:
            total -= (ox2 - ox1) * (oy2 - oy1)

    print(total)

main()
