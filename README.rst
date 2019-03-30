Vincenty
========

Calculate the geographical distance (in kilometers or miles) between 2 points
with extreme accuracy.

This library implements Vincenty's solution to the inverse geodetic problem. It
is based on the WGS 84 reference ellipsoid and is accurate to within 1 mm (!) or
better.

This formula is widely used in geographic information systems (GIS) and is much
more accurate than methods for computing the great-circle distance (which assume
a spherical Earth).

CUDA-friendly
=============
This repo is modification of `vincenty <https://github.com/maurycyp/vincenty>`_
package. Since CUDA has some limitations (it doesn't understand try...except,
for example) original code can't run on GPU.

Example: distance between Boston and New York City
--------------------------------------------------

.. code:: python

   >>> from cuda_friendly_vincenty import vincenty
   >>> boston = (-71.0693514, 42.3541165)
   >>> newyork = (-73.9680804, 40.7791472)
   >>> vincenty(*boston, *newyork)
   298396.06


Installation
------------

.. code:: bash

   $ pip install cuda_friendly_vincenty


References
----------

* https://en.wikipedia.org/wiki/Vincenty's_formulae
* https://en.wikipedia.org/wiki/World_Geodetic_System
