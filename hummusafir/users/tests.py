def zarr(A):
    z = [0] * len(A)
    n = len(A)

    l, r, k = 0, 0, 0

    for i in range(1, len(A)):
        if i > r:
            print(l,r,i)
            l, r, = i, i

            while (r < n and A[r - l] == A[r]):
                r += 1
                print(A[r-1],'1')
            z[i] = r - l
            print(z)
            r -= 1
        else:
            k = i - l
            print(i,l,r,'2')
            if z[k] < r - i + 1:
                z[i] = z[k]
                print(r,i,z)
            else:
                l = i
                while (r < n and A[r - l] == A[r]):
                    r += 1
                z[i] = r - l
                print(z)
                r -= 1

    return z


A='abacabacdabacabacd'

print(zarr(A))