---
schema: qual/card@1
id: E-SS7.EX-10
kind: problem
title: Asymptotic expansion of the logarithmic integral
classification:
  areas:
  - complex-analysis
  topics:
  - Prime Number Theorem
relations: []
review: draft
---

::: {.exercise}
In the theory of primes, define
$$
\operatorname{Li}(x)=\int_2^x\frac{dt}{\log t}.
$$

(a) Prove that $\operatorname{Li}(x)=x/\log x+O(x/(\log x)^2)$ as $x\to\infty$, and consequently that $\pi(x)\sim\operatorname{Li}(x)$.

(b) Show that for every integer $N>0$,
$$
\operatorname{Li}(x)=\sum_{k=1}^{N}\frac{(k-1)!x}{(\log x)^k}
+O\left(\frac{x}{(\log x)^{N+1}}\right)
\qquad(x\to\infty).
$$
:::

::: {.hint}
For (a), integrate by parts and split $\int_2^x dt/(\log t)^2$ at $\sqrt{x}$.
:::
