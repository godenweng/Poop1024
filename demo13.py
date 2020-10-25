from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_UP, ROUND_DOWN

l1 = [1.4, 2.4, 3.4, 4.4]
l2 = [1.5, 2.5, 3.5, 4.5]
l3 = [1.6, 2.6, 3.6, 4.6]
lists = [l1, l2, l3]

roundings = [ROUND_UP, ROUND_DOWN, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_HALF_EVEN]

for r in roundings:
    for lx in lists:
        for l in lx:
            intput_value = Decimal(l)
            output = Decimal(intput_value.quantize(Decimal(1), rounding=r))
            print("using {} , {} becomes {}".format(r, l, output))
