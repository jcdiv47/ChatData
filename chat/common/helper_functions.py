# -*- coding:utf-8 -*-

def coalesce(*values, default=None):
    """
    Return the first non-None value or `default` if all values are None.
    """
    return next((v for v in values if v is not None), default)
