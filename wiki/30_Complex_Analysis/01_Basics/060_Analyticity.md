---
order: 51
---

# Analytic Functions

[[D-V6UQJ]]

[[PR-QNDSD]]

[[T-K66DJ]]

[[C-7S2CO]]

[[T-SRY2V]]

:::{.proof}
Reduce to $z\in \DD$, then for a fixed $z$ and any $w\in S^1$,
\[
{1\over w-z} = {1\over w} \qty{ 1 + \qty{z\over w} + \qty{z\over w}^2 + \cdots}
,\]
which converges uniformly on $S^1$.
Then
\[
f(z)=\frac{1}{2 \pi i} \int_{S^{1}} \frac{f(w) }{w-z} \dw 
= \sum z^{k} \frac{1}{2 \pi i} \int_{S^{1}} \frac{f(w)}{w^{k+1}} \dw 
=\sum c_{k} z^{k}
.\]

:::

:::{.proof title="Holomorphic implies analytic, alternative"}

![](../../../../assets/assets/figures/2021-12-14_16-53-51.png)

:::

[[PR-4BVDD]]

:::{.proof}
Apply the estimate
\[  
\abs{e^z} \leq \sum {\abs {z}^n \over n!} = e^{\abs{z}}
.\]
Now by the $M\dash$test, 
\[  
\abs{z} \leq R < \infty \implies \abs{\sum {z^n \over n!}} \leq e^R < \infty
.\]

:::

# Exercises

[[E-EG3W7]]
