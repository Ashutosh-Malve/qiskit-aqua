# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2018, 2019.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
Variational Forms (:mod:`qiskit.chemistry.components.variational_forms`)
========================================================================
These are chemistry specific Aqua Variational Forms where they inherit from
Aqua :class:`VariationalForm`. As they rely on chemistry specific knowledge
and/or functions they live here rather than in Aqua.

.. currentmodule:: qiskit.chemistry.components.variational_forms

Variational Forms
=================

.. autosummary::
   :toctree: ../stubs/
   :nosignatures:

   UCCSD

"""
from .uccsd import UCCSD

__all__ = ['UCCSD']
