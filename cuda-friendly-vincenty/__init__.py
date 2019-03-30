import math

# WGS 84
a = 6378137  # meters
f = 1 / 298.257223563
b = 6356752.314245  # meters; b = (1 - f)a

MAX_ITERATIONS = 200
CONVERGENCE_THRESHOLD = 1e-12  # .000,000,000,001


def vincenty_inverse(lng0, lat0, lng1, lat1):
    """
    Vincenty's formula (inverse method) to calculate the distance (in
    kilometers or miles) between two points on the surface of a spheroid

    Doctests:
    >>> vincenty(0.0, 0.0, 0.0, 0.0)  # coincident points
    0.0
    >>> vincenty(0.0, 0.0, 1.0, 0.0)
    111319.49
    >>> vincenty(0.0, 0.0, 0.0, 1.0)
    110574.39
    >>> vincenty(0.0, 0.0, 179.5, 0.5)  # slow convergence
    19936288.58
    >>> vincenty(0.0, 0.0, 179.7, 0.5)  # failure to converge
    -1
    >>> boston = (-71.0693514, 42.3541165)
    >>> newyork = (-73.9680804, 40.7791472)
    >>> vincenty(*boston, *newyork)
    298396.06
    """

    # short-circuit coincident points
    if lng0 == lng1 and lat0 == lat1:
        return 0.0

    U1 = math.atan((1 - f) * math.tan(lat0 * math.pi / 180))
    U2 = math.atan((1 - f) * math.tan(lat1 * math.pi / 180))
    L = (lng1 - lng0) * math.pi / 180
    Lambda = L

    sinU1 = math.sin(U1)
    cosU1 = math.cos(U1)
    sinU2 = math.sin(U2)
    cosU2 = math.cos(U2)

    for _ in range(MAX_ITERATIONS):
        sinLambda = math.sin(Lambda)
        cosLambda = math.cos(Lambda)
        sinSigma = math.sqrt((cosU2 * sinLambda) ** 2 +
                             (cosU1 * sinU2 - sinU1 * cosU2 * cosLambda) ** 2)
        if sinSigma == 0:
            return 0.0  # coincident points

        cosSigma = sinU1 * sinU2 + cosU1 * cosU2 * cosLambda
        sigma = math.atan2(sinSigma, cosSigma)
        sinAlpha = cosU1 * cosU2 * sinLambda / sinSigma
        cosSqAlpha = 1 - sinAlpha ** 2

        if cosSqAlpha == 0:
            cos2SigmaM = 0
        else:
            cos2SigmaM = cosSigma - 2 * sinU1 * sinU2 / cosSqAlpha

        C = f / 16 * cosSqAlpha * (4 + f * (4 - 3 * cosSqAlpha))
        LambdaPrev = Lambda
        Lambda = L + (1 - C) * f * sinAlpha * (sigma + C * sinSigma *
                                               (cos2SigmaM + C * cosSigma *
                                                (-1 + 2 * cos2SigmaM ** 2)))
        if abs(Lambda - LambdaPrev) < CONVERGENCE_THRESHOLD:
            break  # successful convergence
    else:
        return -1  # failure to converge

    uSq = cosSqAlpha * (a ** 2 - b ** 2) / (b ** 2)
    A = 1 + uSq / 16384 * (4096 + uSq * (-768 + uSq * (320 - 175 * uSq)))
    B = uSq / 1024 * (256 + uSq * (-128 + uSq * (74 - 47 * uSq)))
    deltaSigma = B * sinSigma * (
        cos2SigmaM + B / 4 *
        (cosSigma * (-1 + 2 * cos2SigmaM ** 2) - B / 6 * cos2SigmaM *
         (-3 + 4 * sinSigma ** 2) * (-3 + 4 * cos2SigmaM ** 2)))

    s = b * A * (sigma - deltaSigma)

    return round(s, 2)


vincenty = vincenty_inverse

if __name__ == '__main__':
    import doctest
    doctest.testmod()
