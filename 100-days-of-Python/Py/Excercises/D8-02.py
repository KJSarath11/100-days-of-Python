#paint coverage
import math
def paint_coverage(height,width,coverage):
    num_can=(height*width)/coverage
    round_up_cans=math.ceil(num_can)
    print(f"The no of can required are: {round_up_cans}")

h=int(input("The height is:"))
w=int(input("The width is:"))
c=int(input("Enter the coverage:"))
paint_coverage(height=h,width=w,coverage=c)