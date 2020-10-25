from decimal import Decimal
v1 = Decimal(13/7)
print(v1)
print(v1.quantize(Decimal(1)))
print(v1.quantize(Decimal('0.1'))) #小數點後一位
print(v1.quantize(Decimal('0.01'))) #小數點後兩位