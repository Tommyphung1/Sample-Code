import scipy.stats as stats
from math import sqrt

def hypothesis_testing(sample, pop_mean, pop_std , test, alpha, sample_size, two_tailed = False):
    # Test the sample mean to see whether the sample mean comes from the population or from a different population
    # H0: There is no difference between population mean and sample mean
    # HA: There is a difference between population mean and sample mean
    # H0 and HA changes if two tailed
    
    print('Test Conducted: {}-test'.format(test))
    if test == 'z':    #Two sample z test
        sam_mean = np.mean(sample)
        if two_tailed:
            None
        else:    #One sample z test
            # 1. Find the sample z-score
            num = sam_mean - pop_mean
            dem = pop_std / np.sqrt(sample_size)
            z =  num/dem
            # 2. Calculate p-value using the z-score
            if sam_mean > pop_mean:
                p_val = 1 - stats.norm.cdf(z)
            else: 
                p_val = stats.norm.cdf(z)
        print('Results: Failed to reject Null Hypothesis' if p_val >= alpha else 'Results: Reject Null Hypothesis')
        print('p_val: {}|alpha: {}'.format(round(p_val,4), alpha))
        return p_val
    
    elif test == 't':   
    # Use for small sample size or population std is not known
    # Test to see if means are different
    # Can be solved with p_value or t_stat
        sam_mean = np.mean(sample)
        sample_size = len(sample)
        num = sam_mean - pop_mean
        dem = np.std(sample, ddof= 1)/np.sqrt(sample_size)
        t = num/dem
        t_crit = stats.t.ppf(1-alpha, sample_size - 1)
        p_val = stats.t.sf(t, sample_size - 1)
        results = stats.ttest_1samp(sample, pop_mean)
        if not two_tailed:
            p_val = results[1]/2
        else:
            p_val = results[1]
    print('Results: Failed to reject Null Hypothesis' if p_val >= alpha else 'Results: Reject Null Hypothesis')
    print('p_val: {}|alpha: {} t_stat: {}|t_crit: {}'.format(round(p_val,4),alpha, round(t, 4), round(t_crit, 4)))
    return p_val
