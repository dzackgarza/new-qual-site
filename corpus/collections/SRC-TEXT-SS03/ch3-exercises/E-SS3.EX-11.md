---
schema: qual/card@1
id: E-SS3.EX-11
kind: problem
title: "SS 3.11: The mean value of log of 1 minus a e^(i-theta)"
classification:
  areas:
  - complex-analysis
  topics: ['Meromorphic Functions', 'Residue Theorem', 'Argument Principle']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
11. Show that $\mathrm { i f } \ | a | < 1$ , then

$$
\int_ {0} ^ {2 \pi} \log | 1 - a e ^ {i \theta} | d \theta = 0.
$$

Figure 10. Contour in Exercise 10

Then, prove that the above result remains true if we assume only that $| a | \le 1$
:::

::: {.solution}
First suppose $|a|<1$. The power series
\[
\Log(1-w)=-\sum_{n\ge1}\frac{w^n}{n},\qquad |w|<1,
\]
converges uniformly on $|w|\le |a|$. Hence
\[
\log|1-ae^{i\theta}|=\Re\Log(1-ae^{i\theta})
=-\Re\sum_{n\ge1}\frac{a^n e^{in\theta}}n.
\]
Termwise integration is justified by uniform convergence, and every exponential term has integral $0$ over $[0,2\pi]$. Thus the integral is $0$.

Now let $|a|=1$. Write $a=e^{i\phi}$. By translation of $\theta$ it is enough to treat $a=1$. Since
\[
|1-e^{i\theta}|=2\left|\sin\frac\theta2\right|,
\]
we need to show
\[
\int_0^{2\pi}\log\!\left(2\left|\sin\frac\theta2\right|\right)d\theta=0.
\]
For $0<r<1$, the already-proved case gives
\[
\int_0^{2\pi}\log|1-re^{i\theta}|\,d\theta=0.
\]
As $r\uparrow1$, these functions converge pointwise off $\theta=0,2\pi$ to the boundary integrand. Moreover, splitting off a small neighborhood of $0$ and using
\[
|1-re^{i\theta}|^2=(1-r)^2+2r(1-\cos\theta)\asymp (1-r)^2+\theta^2,
\]
shows the logarithms are uniformly integrable there; away from $0$ convergence is uniform. Hence the integrals converge to the boundary integral, which is therefore also $0$.
:::
