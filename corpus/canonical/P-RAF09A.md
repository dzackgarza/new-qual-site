---
schema: qual/card@1
id: P-RAF09A
kind: problem
title: "True/false on convergence, Fubini, measurability, and weak compactness"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Determine if the statements below are True or False.
If True, give a brief proof.
If False, give a counterexample (or prove your assertion in another way, if you prefer).

(a) Let $(X, \mathcal{M}, \mu)$ be a complete measure space.
If $f_n, g_n, g, f \in L^1$, $f_n \to f$ and $g_n \to g$ a.e., $|f_n| \leq g_n$ and $\int g_n\,d\mu = A < \infty$ for some $A > 0$, then $\int f_n\,d\mu \to \int f\,d\mu$.

(b) The iterated integrals
$$
\int_{-1}^{1} \left[\int_{-1}^{1} \frac{xy}{(x^2+y^2)^2}\,dx\right]dy = \int_{-1}^{1} \left[\int_{-1}^{1} \frac{xy}{(x^2+y^2)^2}\,dy\right]dx.
$$
Hence by the Fubini-Tonelli theorem $\frac{xy}{(x^2+y^2)^2}$ is (Lebesgue) integrable on $[-1,1] \times [-1,1]$.

(c) Assume that $f$ is a continuous real-valued function on $\mathbb{R}$ and $g$ is Lebesgue measurable, then $f > g$ is Lebesgue measurable.

(d) Let $X$ be an infinite-dimensional Banach space.
Then every nonempty weak*-open set in $X^*$ is unbounded with respect to the induced norm.

(e) A bounded sequence in a Hilbert space contains a weakly convergent subsequence.
:::
