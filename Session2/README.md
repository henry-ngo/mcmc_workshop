# Session 2

## Update workshop environment

In order to use the most current Parallel Tempering algorithm, we need a new module, `ptemcee`. The current release of `emcee` includes support for Parallel Tempering but the upcoming release will not. So, it makes more sense to just use `ptemcee` now. It is meant to work the same way as `emcee` as is described in (Vousden et al. 2016)[https://academic.oup.com/mnras/article/455/2/1919/1118710]

First, make sure you are in the right environment
```
source activate emcee_workshop
```
(or, on Windows)
```
activate emcee_workshop
```
Then, install the package with `pip`
```
pip install ptemcee
```
And that's it!

## Plan for Session

1. How does detailed balance work?
2. Testing for convergence (convergence_tests.ipynb)
3. MCMC algorithms
4. Multi-modal solutions with Parallel Tempering (parallel_tempering.ipynb)
