"""
Demonstration script showing that varcovar and varcovar_balanced
give the same results in a balanced setting, both with and without weights.
"""

# Dependencies
import numpy as np
# Load the functions from the ustat_var package
# from ustat_var import generate_data
# from ustat_var import varcovar
# from ustat_var import varcovar_ustat
# from ustat_var import varcovar_balanced


def demonstrate_varcovar_equivalence(n_teachers=20, n_time=5, seed=42):
    """
    Demonstrates that varcovar and varcovar_balanced give the same results
    in a balanced setting, both with and without weights.
    
    Parameters
    ----------
    n_teachers : int
        Number of teachers (rows).
    n_time : int
        Number of time periods (columns).
    seed : int
        Random seed for reproducibility.
    
    Returns
    -------
    dict
        Dictionary containing comparison results.
    """
    # Generate balanced data (no NaNs, so it's balanced)
    arrays, mu = generate_data(n_teachers=n_teachers, n_time=n_time, 
                                n_arrays=2, var_fixed=1.0, var_noise=1.0, 
                                cov_factor=0.5, seed=seed)
    
    X = arrays[0]
    Y = arrays[1]
    
    print("=" * 70)
    print("Demonstration: varcovar vs varcovar_balanced in balanced setting")
    print("=" * 70)
    
    # Case 1: Without weights
    print("-" * 70)
    print("Case 1: WITHOUT weights")
    print("-" * 70)
    
    result_varcovar_unweighted = varcovar(X, Y, w=None, quiet=False)
    result_balanced_unweighted = varcovar_balanced(X, Y, w=None, quiet=False)
    
    print(f"\nvarcovar result:        {result_varcovar_unweighted:.10f}")
    print(f"varcovar_balanced result: {result_balanced_unweighted:.10f}")
    print(f"Difference:              {abs(result_varcovar_unweighted - result_balanced_unweighted):.2e}")
    
    if np.allclose(result_varcovar_unweighted, result_balanced_unweighted, rtol=1e-10):
        print("✓ Results match! (within numerical precision)\n")
    else:
        print("✗ Results do NOT match!\n")
    
    # Case 2: With weights
    print("-" * 70)
    print("Case 2: WITH weights")
    print("-" * 70)
    
    # Generate random weights
    np.random.seed(seed + 1)
    weights = np.random.rand(n_teachers)
    weights = weights / weights.sum() * n_teachers  # Normalize but keep reasonable scale
    
    result_varcovar_weighted = varcovar(X, Y, w=weights, quiet=False)
    result_balanced_weighted = varcovar_balanced(X, Y, w=weights, quiet=False)
    
    print(f"\nvarcovar result:        {result_varcovar_weighted:.10f}")
    print(f"varcovar_balanced result: {result_balanced_weighted:.10f}")
    print(f"Difference:              {abs(result_varcovar_weighted - result_balanced_weighted):.2e}")
    
    if np.allclose(result_varcovar_weighted, result_balanced_weighted, rtol=1e-10):
        print("✓ Results match! (within numerical precision)\n")
    else:
        print("✗ Results do NOT match!\n")
    
    print("=" * 70)

    # Case 3: With weights and missing values that are the same for both X and Y
    print("-" * 70)
    print("Case 3: WITH weights and missing values that are the same for both X and Y")
    print("-" * 70)
    
    # Generate random weights
    np.random.seed(seed + 2)
    weights = np.random.rand(n_teachers)
    weights = weights / weights.sum() * n_teachers  # Normalize but keep reasonable scale
    
    # Generate missing values that are the same for both X and Y
    missing_values = np.random.rand(n_teachers, n_time) < 0.5
    X[missing_values] = np.nan
    Y[missing_values] = np.nan
    
    result_varcovar_weighted_missing = varcovar(X, Y, w=weights, quiet=False)
    result_balanced_weighted_missing = varcovar_balanced(X, Y, w=weights, quiet=False)
    
    print("=" * 70)
    print(f"\nvarcovar result:        {result_varcovar_weighted_missing:.10f}")
    print(f"varcovar_balanced result: {result_balanced_weighted_missing:.10f}")
    print(f"Difference:              {abs(result_varcovar_weighted_missing - result_balanced_weighted_missing):.2e}")
    
    if np.allclose(result_varcovar_weighted_missing, result_balanced_weighted_missing, rtol=1e-10):
        print("✓ Results match! (within numerical precision)\n")
    else:
        print("✗ Results do NOT match!\n")
    
    print("=" * 70)
    

    results = {
        'unweighted': {
            'varcovar': result_varcovar_unweighted,
            'varcovar_balanced': result_balanced_unweighted,
            'match': np.allclose(result_varcovar_unweighted, result_balanced_unweighted, rtol=1e-10)
        },
        'weighted': {
            'varcovar': result_varcovar_weighted,
            'varcovar_balanced': result_balanced_weighted,
            'match': np.allclose(result_varcovar_weighted, result_balanced_weighted, rtol=1e-10)
        },
        'weighted_missing': {
            'varcovar': result_varcovar_weighted_missing,
            'varcovar_balanced': result_balanced_weighted_missing,
            'match': np.allclose(result_varcovar_weighted_missing, result_balanced_weighted_missing, rtol=1e-10)
        }
    }
    
    return results # Return the results as a dictionary


if __name__ == "__main__":
    # Run demonstration when script is executed directly
    demonstrate_varcovar_equivalence()
