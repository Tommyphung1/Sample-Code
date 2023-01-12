import scipy.stats as stats
from math import sqrt
import statsmodels.api as sm
from statsmodels.formula.api import ols

def hypothesis_testing(sample1, sample2 = None, pop_mean, pop_std , test, alpha, sample_size, two_tailed = False):
    # Test the sample mean to see whether the sample mean comes from the population or from a different population
    # H0: There is no difference between population mean and sample mean
    # HA: There is a difference between population mean and sample mean
    # H0 and HA changes if two tailed
    
    print('Test Conducted: {}-test'.format(test))
    if test == 'z':    #Two sample z test
        sam_mean = np.mean(sample1)
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
        sam_mean = np.mean(sample1)
        sample_size = len(sample1)
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
        return results
    
    elif test == 't2s':   
    # Two sample t test
    # Only one function is needed for this test that only need the two independent samples to calculate
        results = stats.ttest_ind(experimental, control)
        
        print('Results: Failed to reject Null Hypothesis' if results[1] >= alpha else 'Results: Reject Null Hypothesis')
        print('p_val: {}|alpha: {}'.format(round(results[1],4),alpha))
        return results

    elif test == 'w':
    # Welch Test
    # When the variances or sample size arent the same.
    # If variance are the same, the t-test are good enough
        var1 = sample1.var(ddof= 1)
        var2 = sample2.var(ddof= 1)

        diff_mean = np.mean(sample1) - np.mean(sample2)
        pooled_var = var1/len(sample1) + var2/len(sample2)

        num = (var1 / len(sample1) + var2 / len(sample2)) **2
        dem = var1**2/((len(sample1)**2)*(len(sample1)-1)) + var2**2/((len(sample2)**2)*(len(sample2)-1))

        t = np.abs(diff_mean / np.sqrt(pooled_var))    # t statistic
        df = num/dem    # Degree of freedom

        if two_tailed:
            result = (1 - stats.t.cdf(t,df))*2    
        else: 
            result = (1 - stats.t.cdf(t,df))

        print('Results: Failed to reject Null Hypothesis' if result >= alpha else 'Results: Reject Null Hypothesis')
        print('p_val: {}|alpha: {}'.format(round(result,4),alpha))
        return result
    
    elif test = 'ks':
    # Test the distribution is there is a difference between a normal distibution
    # H0: There is no difference between this distribution and a normal distribution
        if sample2 == None:
            results = stats.kstest(sample1, 'norm', N = sample_size)
        else:
            results = stats.ks_2samp(sample1, sample2)

        if results[1] >= alpha:
            print('Results: Failed to reject Null Hypothesis')
            print('There is no difference between this distribution and a normal distibution')
        else:
            print('Results: Reject Null Hypothesis')
            print('There is a difference between this distribution and a normal distibution')

        print('p_val: {}|alpha: {}'.format(round(results[1],4),alpha))
        return results