.. _example_plot_irreducible_fraction.py:


.. image:: /images/IrreducibleFraction_800.png
    :align: center

Una fracción de la forma :math:`\frac{a}{a+bi}`, con :math:`a,b \in \mathbb{Z}`,
se dice **irreducible** si

.. math::

    \gcd(a,b)=1.

En tal caso, se grafica el valor complejo

.. math::

    z = \frac{a}{a+bi}

para todos los pares enteros primitivos :math:`(a,b)`. El patrón generado refleja la estructura aritmética de :math:`\mathbb{Z}[i]`.


**Python source code:** :download:`plot_irreducible_fraction.py <plot_irreducible_fraction.py>`

.. literalinclude:: plot_irreducible_fraction.py
    :lines: 2-
