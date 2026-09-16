---
schema: qual/card@1
id: FT-T7OAO
kind: theorem
title: Fubini's theorem
prompts:
- State Fubini's theorem.
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
Let $f\in L^1(\RR^n\times \RR^k)$, and for $y\in\RR^k$ let $f^y\colon\RR^n\to\CC$ be the slice $f^y(x)\coloneqq f(x ,y)$.
Then:

1. For almost every $y\in \RR^k$, the slice $f^y$ is [[D-R5DL3|integrable]]: $f^y \in L^1(\RR^n)$.

2. The function $F(y) \coloneqq \int_{\RR^n} f^y(x) \, dx$, defined for almost every $y$, is integrable: $F\in L^1(\RR^{k})$.

3. The integrals agree:
$$
\int_{\RR^{n+k}} f(x,y) \, d(x,y) = \int_{\RR^k} \qty{ \int_{\RR^n} f(x,y) \, dx} \, dy .
$$

The same statements hold with the roles of $x$ and $y$ exchanged, so the two iterated integrals are equal.
:::

::: {.remark}
The hypothesis is $f\in L^1(\RR^{n+k})$; $f$ may take values of both signs.
[[FT-4JRQX|Tonelli's theorem]] instead assumes $f\geq0$ measurable, with no integrability hypothesis.
:::
