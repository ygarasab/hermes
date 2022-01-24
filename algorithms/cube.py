import numpy as np

def get_strained_point(anchor,s):

    o = np.array(anchor)

    v_r = np.array([299,0])

    v_r -= o

    u_r = v_r / np.linalg.norm(v_r)

    p_r = (s * u_r) + o

    w = list(int(i) for i in p_r)
    return w

def draw_plane(anchor, s):

    o = np.array(anchor)

    v_r = np.array([299,149])
    v_l = np.array([0,149])

    v_r -= o
    v_l -= o

    u_r = v_r / np.linalg.norm(v_r)
    u_l = v_l / np.linalg.norm(v_l)

    p_r = (s * u_r) + o
    p_l = (s * u_l) + o

    w = list(int(i) for i in p_r)
    z = list(int(i) for i in p_l)
    return ( anchor, w, z)


def get_damn_point(p, q):

    p = np.array(p)
    q = np.array(q)

    v_r = np.array([0,149])
    v_l = np.array([299,149])

    v_r -= p
    v_l -= q

    a_r = v_r[1] / v_r[0]
    a_l = v_l[1] / v_l[0]

    b_r = p[1] - a_r * p[0]
    b_l = q[1] - a_l * q[0]

    a = np.array([[a_r, -1], [a_l, -1]])
    k = np.linalg.solve(a, [-b_r,-b_l])

    return list( int(i) for i in np.linalg.solve(a, [-b_r,-b_l]))

def get_damn_point_one(p,q):
    p = np.array(p)

    v_r = np.array([299,0])

    v_r -= p

    a_r = v_r[1] / v_r[0]

    b_r = p[1] - a_r * p[0]
    a = np.array([[a_r, -1], [0, -1]])
    k = np.linalg.solve(a, [-b_r,-q[1]])

    return list( int(i) for i in np.linalg.solve(a, [-b_r,-q[1]]))
