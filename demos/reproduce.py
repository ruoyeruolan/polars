# -*- encoding: utf-8 -*-
"""
@Introduce  : 
@File       : reproduce.py
@Author     : ryrl
@Email      : ryrl970311@gmail.com
@Time       : 2025/01/29 03:11
@Description: 
"""

import polars as pl
from polars._utils.parse import parse_into_expression
from polars.expr.string import ExprStringNameSpace
pl.__version__

help(pl.col("s").str.extract_many)
# pl.col("s").str._rs

df = pl.DataFrame({'s': ['abc_1', 'abc_2', 'def_1', 'def_2', 'ghi_1', 'ghi_2']})

df.with_columns(extracted=pl.col('s').str.extract_many(['abc', 'ghi']))

help(pl.col("s").str.extract_many)