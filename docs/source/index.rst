.. ustat_var documentation master file, created by
   sphinx-quickstart on Wed Jul 16 11:30:32 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _index:

Overview
=======================

This package contains the non-parametric unbiased estimators of the variance of teacher effects described in `Rose, Schellenberg, and Shem-Tov (2022) <https://www.nber.org/papers/w30274>`__. 
These unbiased estimators are :math:`U\text{-}\mathrm{statistics}`, which provide minimum-variance unbiased estimators of population variances and covariances of latent parameters. 
The approach overcomes several issues experienced by Empirical Bayes (EB) techniques when estimating the distribution of teachers' ``value-added," but can applied in any setting where the researcher seeks to estimate the distribution of agent-specific efefct.

Empirical setup
===============

`Rose, Schellenberg, and Shem-Tov (2022) <https://www.nber.org/papers/w30274>`__ employed a non-parametric U-statistic approach in the context of estimating teachers' value-added across multiple outcomes (e.g., test scores, suspensions, and future crime). 
Throughout the package and its documentation, we use the same 'teacher' vocabulary, but the estimators in the ``ustat_var`` package would also apply in other settings.

Suppose you observe a vector of average student outcomes

.. math::

   y_{jt} = (y^A_{jt}, y^B_{jt}, ...) = \mathbf{\alpha}_{j} + \mathbf{X}_{jt}'\Gamma + \varepsilon_{jt}
   
for each teacher :math:`j = 1, 2, ..., J` over :math:`t=1,2,..., T_j`. Here, the vector :math:`\alpha_j = (\alpha_j^A, \alpha_j^B, ...)` represents teacher j's effect on each outcome (e.g. grades and arrests), while :math:`\mathbf{X}_{jt}` represent controls. 
We assuming that :math:`\operatorname{E}(\varepsilon_{jt}\varepsilon_{jt'}) = 0` for all :math:`t \neq t'`. We want unbiasedly estimate :math:`\operatorname{Cov}(\alpha_j^A, \alpha_j^B)`
(which is the covariance of teacher j's effect between any two outcomes A and B) and its sampling variance. 

Essentially, we do this by computing the residuals :math:`\bar{Y}_{jt} =  y_{jt} - \mathbf{X}_{jt}'\beta = \alpha_j + \bar{v}_{jt}`, which are then used as inputs into unbiased estimators of :math:`\operatorname{Cov}(\alpha_j^A, \alpha_j^B)` and its sampling variance.
The ``ustat_var`` package contains functions to compute unbiased estimators of these variances and sampling variance.

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
