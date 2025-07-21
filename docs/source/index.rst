.. ustat_var documentation master file, created by
   sphinx-quickstart on Wed Jul 16 11:30:32 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _index:

Overview
=======================

This package contains the non-parametric unbiased estimators of the variance of teacher effects described in `Rose, Schellenberg, and Shem-Tov (2022) <https://www.nber.org/papers/w30274>`__. 
These unbiased estimators are U -statistics, which provide minimum-variance unbiased estimators of population parameters for arbitrary probability distributions. 
The U-statistic approach overcomes several issues experienced by Empirical Bayes (EB) techniques when estimating an agent's 'value-added'.

Authors: `Evan K. Rose <https://ekrose.github.io/>`__ (University of Chicago), `Jonathan T. Schellenberg <https://sites.google.com/view/jonathanschellenberg/>`__ (Amazon Web Services), and `Yotam Shem-Tov <https://yotamshemtov.github.io/>`__ (UCLA)

To install::

    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps ustat_var

See :ref:`usage` for a brief explanation of how to use the core functions, and see the |user manual| for a detailed explanation of the core functions and the empirical setup.
See :ref:`reference` for a reference guide for each of the package's functions, including helper functions.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   usage
   reference

.. |user manual| replace::
   :download:`user manual </_downloads/ustat_var_user_manual.pdf>`
