from scipy import stats
import math

def confidence_interval_ratio(p, n, conf):
    diff = stats.norm.cdf(conf / 2) * math.sqrt(p * (1 - p) / n)
    return (min(p - diff, p + diff), max(p - diff, p + diff))

def confidence_interval_mean(mu, sd, n, conf):
    diff = stats.norm.cdf(conf / 2) * (sd / math.sqrt(n))
    return (min(mu - diff, mu + diff), max(mu - diff, mu + diff))

def confidence_interval_var(s, n, conf):
    part1 = ((n - 1) * s * s) / (stats.chi2.ppf(conf / 2, n - 1))
    part2 = ((n - 1) * s * s) / (stats.chi2.ppf(1 - (conf / 2), n - 1))
    return (min(part1, part2), max(part1, part2))

print(confidence_interval_ratio(0.3, 50, .95))
print(confidence_interval_mean(54, 3, 30, .97))
print(confidence_interval_var(4.2, 10, .95))

print(stats.poisson.pmf(k=0, mu=4))


