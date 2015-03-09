"""
.. Copyright (c) 2014, 2015 Marshall Farrier
   license http://opensource.org/licenses/MIT

Options - common (:mod:`pynance.opt.common`)
==================================================

.. currentmodule:: pynance.opt.common
"""

from __future__ import absolute_import

from . import _constants

def _relevant_rows(optdata, multikey, errmsg):
    try:
        return optdata.loc[multikey, :]
    except (TypeError, KeyError):
        # message generated by pandas is cryptic
        raise KeyError(errmsg)

def _getprice(optrow):
    _bid = optrow.loc[:, 'Bid'].values[0]
    _ask = optrow.loc[:, 'Ask'].values[0]
    return round((_bid + _ask) / 2., _constants.NDIGITS_SIG)

def _getkeys(optrow, keys):
    return optrow.loc[:, keys].values.flatten().tolist()
