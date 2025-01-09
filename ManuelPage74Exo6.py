def unzip(t):
    tx = [x for (x, _) in t]
    ty = [y for (_, y) in t]
    return (tx, ty)

def zip_points(tx, ty):
    return [(x, y) for x, y in zip(tx, ty)]

t = [(0, 0), (0, 100), (50, 150), (100, 100), (100, 0)]

# 1) Dézipper (unzip)
tx, ty = unzip(t)
print("tx =", tx)  # [0, 0, 50, 100, 100]
print("ty =", ty)  # [0, 100, 150, 100, 0]

# 2) Recomposer (zip)
points_recup = zip_points(tx, ty)
print("points_recup =", points_recup)  
