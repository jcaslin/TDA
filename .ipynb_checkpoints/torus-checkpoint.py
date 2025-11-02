import numpy as np

def sample_torus_3d(n=1000, R=2.0, r=0.6, mode="random"):
    if mode == "random":
        theta = 2*np.pi*np.random.rand(n)
        phi   = 2*np.pi*np.random.rand(n)
    elif mode == "grid":
        k = int(round(n**0.5))
        tt = np.linspace(0, 2*np.pi, k, endpoint=False)
        pp = np.linspace(0, 2*np.pi, k, endpoint=False)
        theta, phi = np.meshgrid(tt, pp, indexing="ij")
        theta, phi = theta.ravel(), phi.ravel()
    else:
        raise ValueError("mode must be 'random' or 'grid'.")

    x = (R + r*np.cos(phi)) * np.cos(theta)
    y = (R + r*np.cos(phi)) * np.sin(theta)
    z =  r*np.sin(phi)
    return np.column_stack([x, y, z])
