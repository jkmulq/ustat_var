.. ustat_var documentation master file, created by
   sphinx-quickstart on Wed Jul 16 11:30:32 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ustat_var documentation
=======================

This package contains the non-parametric unbiased estimators of the variance of teacher effects described in `Rose, Schellenberg, and Shem-Tov (2022) <https://domain.invalid/>`__. 
These unbiased estimators are U -statistics, which provide minimum-variance unbiased estimators of population parameters for arbitrary probability distributions. 
The U-statistic approach overcomes several issues experienced by Empirical Bayes (EB) techniques when estimating an agent's 'value-added'.

Authors:
* Evan K. Rose (University of Chicago)
* Jonathan T. Schellenberg (Amazon Web Services)
* Yotam Shem-Tov (UCLA)

To install::

    python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps ustat_var

See :ref:`usage` for examples of how to use the core functions.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

