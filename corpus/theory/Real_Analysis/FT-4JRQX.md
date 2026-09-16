---
schema: qual/card@1
id: FT-4JRQX
kind: theorem
title: Tonelli's theorem
prompts:
- State Tonelli's theorem.
classification:
  areas:
  - real-analysis
  topics:
  - Fubini-Tonelli
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $f\colon\RR^{n}\times \RR^k\to[0,\infty]$ be [[D-DHFN4|Lebesgue measurable]] on $\RR^{n+k}$.
For $y\in\RR^k$, let $f^y\colon\RR^n\to[0,\infty]$ be the slice $f^y(x) \coloneqq f(x, y)$.
Then:

1. For almost every $y\in \RR^k$, the slice $f^y$ is measurable on $\RR^n$.

2. The function $F(y) \coloneqq \int_{\RR^n} f^y(x) \, dx$, defined for almost every $y$, is measurable on $\RR^k$.

3. In $[0,\infty]$,
$$
\int_{\RR^{n+k}} f(x,y) \, d(x,y) = \int_{\RR^k} \qty{\int_{\RR^n} f(x,y) \,dx}\, dy .
$$

The same statements hold with the roles of $x$ and $y$ exchanged, so the two iterated integrals are equal.
:::

::: {.remark}
The hypotheses are that $f$ is nonnegative and measurable; $f$ need not be integrable, and all three integrals in (3) may be $+\infty$.
Fubini's theorem instead assumes $f\in L^1(\RR^{n+k})$ and allows $f$ to take values of both signs.
:::
