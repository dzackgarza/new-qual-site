---
schema: qual/card@1
id: E-SS10.PR-6
kind: problem
title: Eight squares from an Eisenstein series
classification:
  areas:
  - complex-analysis
  topics:
  - Sums of Squares
  - Modular Forms
relations: []
review: draft
---

::: {.exercise}
Let $r_8(n)$ count representations of $n$ as a sum of eight squares. Prove $r_8(n)=16\sigma_3^*(n)$, where $\sigma_3^*(n)=\sum_{d\mid n}d^3$ for odd $n$, while for even $n$,
$$
\sigma_3^*(n)=\sum_{d\mid n}(-1)^d d^3.
$$
Define
$$
E_4^*(\tau)=\sum_{\substack{m,n\in\ZZ\\m,n\text{ of opposite parity}}}
\frac1{(n+m\tau)^4},\qquad
E_4(\tau)=\sum_{(m,n)\ne(0,0)}\frac1{(n+m\tau)^4}.
$$

(a) Show that the formula for $r_8(n)$ is equivalent to $\theta(\tau)^8=48\pi^{-4}E_4^*(\tau)$.

(b) Show that $E_4^*(\tau)=E_4(\tau)-2^{-4}E_4((\tau-1)/2)$.

(c) Show that $E_4^*(\tau+2)=E_4^*(\tau)$.

(d) Show that $E_4^*(\tau)=\tau^{-4}E_4^*(-1/\tau)$.

(e) Show that $(48/\pi^4)E_4^*(\tau)\to1$ as $\Im\tau\to\infty$.

(f) Show that $\abs{E_4^*(1-1/\tau)}\asymp\abs{\tau}^4\abs{e^{2\pi i\tau}}$ as $\Im\tau\to\infty$.

Use these properties and the corresponding properties of $\theta^8$ to conclude that $48\pi^{-4}E_4^*/\theta^8$ is identically $1$.
:::

::: {.hint}
For (a), use $E_4(\tau)=2\zeta(4)+(2\pi)^4\sum_{k\geq1}\sigma_3(k)e^{2\pi ik\tau}/3$ and $\zeta(4)=\pi^4/90$. For (f), verify $E_4^*(1-1/\tau)=\tau^4(E_4(\tau)-E_4(2\tau))$.
:::
