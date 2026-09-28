---
schema: qual/card@1
id: E-SS3.EX-11
kind: problem
title: $\int_0^{2\pi}\log\abs{1-ae^{i\theta}}\,d\theta=0$ for $\abs a\le1$
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
As $r\uparrow1$, these functions converge pointwise off $\theta=0,2\pi$ to $\log\abs{1-e^{i\theta}}$. For $\frac12\le r<1$,
\[
|1-re^{i\theta}|^2=(1-r)^2+4r\sin^2\frac\theta2,
\]
which lies between $2\sin^2\frac\theta2$ and $4$. Hence $\abs{\log|1-re^{i\theta}|}\le\log2+\abs{\log\bigl(\sqrt2\,\abs{\sin\frac\theta2}\bigr)}$, an integrable function of $\theta$ on $[0,2\pi]$. By dominated convergence, the integrals converge to the boundary integral, which is therefore also $0$.
:::
