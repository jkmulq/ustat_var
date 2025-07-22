.. ustat_var documentation master file, created by
   sphinx-quickstart on Wed Jul 16 11:30:32 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _index:

Overview
=======================

This package contains the non-parametric unbiased estimators of the variance of teacher effects described in `Rose, Schellenberg, and Shem-Tov (2022) <https://www.nber.org/papers/w30274>`__. 
These unbiased estimators are :math:`U\text{-}\mathrm{statistics}`, which provide minimum-variance unbiased estimators of population variances and covariances of latent parameters. 
The approach overcomes several issues experienced by Empirical Bayes (EB) techniques when estimating the distribution of teachers' 'value-added,' but can applied in any setting where the researcher seeks to estimate the distribution of agent-specific efefct.

Empirical setup
===============

`Rose, Schellenberg, and Shem-Tov (2022) <https://www.nber.org/papers/w30274>`__ employed a non-parametric U-statistic approach in the context of estimating teachers' value-added across multiple outcomes (e.g., test scores, suspensions, and future crime). 
Throughout the package and its documentation, we use the same 'teacher' vocabulary, but the estimators in the ``ustat_var`` package would also apply in other settings.

The package assumes the researcher observes for each teacher $j = 1, 2, ..., J$ and outcome $k = 1, 2, ..., K$:

$$y^k_j = (y^k_{j1}, ..., y^k_{jT_j})'$$

where $y^k_{jt} = a_j^k + e_{jt}^k$. The parameter $a_j^k$ represents teacher j's effect on outcome k. The term $e_{jt}^k$ represents estimation error. The key asumptions are that: $E[e_{jt}^k | a_j^k] = 0$ for all $j,k,t$ that $E[e_{jt}^ke_{jt'}^{l}] = 0$ for $t \ne t'$ and all $j,k,l$.

The package produces estimates of $Var(a_j^k$ and $Cov(a_j^k,a_j^l)$, as well as estimates of their sampling variance. There are options to equally weight each $j$ in these parameters as well as apply user-given weights. It can also accomodate heavily unbalanced data, where $T_j$ differs across teachers and across outcomes within teacher.

- The |user manual| summarises the formulae for these unbiased estimators (used in the core ``ustat_var`` package functions) for transparency.
- `Rose, Schellenberg, and Shem-Tov (2022) <https://www.nber.org/papers/w30274>`__ contains the full discussion of the empirical setup and the required assumptions to interpret the estimates causally. 

**Authors**

- `Evan K. Rose <https://ekrose.github.io/>`__ (University of Chicago)
- `Jonathan T. Schellenberg <https://sites.google.com/view/jonathanschellenberg/>`__ (Amazon Web Services)
- `Yotam Shem-Tov <https://yotamshemtov.github.io/>`__ (UCLA)

Installation
------------

To install, execute 

.. code-block:: bash

    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps ustat_var


Contents
--------

- :ref:`usage` for a brief explanation of how to use the core functions.
- :ref:`reference` for a reference guide for each of the package's functions, including helper functions.

.. toctree::
   :maxdepth: 1
   :caption: Pages:
   :hidden:

   usage
   reference

.. |user manual| replace::
   :download:`user manual </_downloads/ustat_var_user_manual.pdf>`
