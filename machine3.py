def comp_midpoint(a,b,n,f):
    h = (b-a)/(n+2)
    sum = 0
    for j in range(0,n/2):
        xj = a + ((j+1)*h)
        sum += f(xj)
    return sum *= (2*h)


def main():
    comp_midpoint(0,2,8,)

if __name__ == "__main__":
    main()