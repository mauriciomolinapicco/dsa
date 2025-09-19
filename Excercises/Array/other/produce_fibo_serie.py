def fib(n):
    serie = [0,1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie

if __name__ == "__main__":
    serie = fib(10)
    for f in serie:
        print(f)