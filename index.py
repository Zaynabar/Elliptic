A = 0
B = 7
P = 0x3fddbf07bb3bc551
G = (0x69d463ce83b758e, 0x287a120903f7ef5c)

def mod_inverse(num, mod):
    return pow(num, mod - 2, mod)

def point_addition(C, D):
    Xc, Yc = C
    Xd, Yd = D

    if C == D:
        L = (3 * (Xc ** 2) + A) * mod_inverse(2 * Yc, P) % P
    else:
        L = ((Yd - Yc) * mod_inverse(Xd - Xc, P)) % P

    Xs = (L ** 2 - Xc - Xd) % P
    Ys = (L * (Xc - Xs) - Yc) % P
    return (Xs, Ys)

def generate_EC_keys(N, k_values):
    result = []
    for k in k_values:
        k_hex = int(k, 16)
        point = G
        k_binary = bin(k_hex)[2:]
        for bit in k_binary[1:]:
            point = point_addition(point, point)
            if bit == '1':
                point = point_addition(point, G)
        result.append(hex(point[0]))

    return result

N = int(input())
k_values = [input() for _ in range(N)]

keys = generate_EC_keys(N, k_values)
for key in keys:
    print(key)
