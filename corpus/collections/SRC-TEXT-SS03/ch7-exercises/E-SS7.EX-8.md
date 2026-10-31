---
schema: qual/card@1
id: E-SS7.EX-8
kind: problem
title: Infinitely many zeta zeros in the critical strip
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
---

::: {.exercise}
The function $\zeta$ has infinitely many zeros in the critical strip. The book proposes the following argument.

(a) Let $F(s)=\xi(1/2+s)$, where $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$. Show that $F$ is even and that there exists $G$ with $G(s^2)=F(s)$.

(b) Show that $(s-1)\zeta(s)$ is entire of growth order $1$; that is, for every $\varepsilon>0$,
$$
\abs{(s-1)\zeta(s)}\leq A_\varepsilon e^{a_\varepsilon\abs{s}^{1+\varepsilon}}.
$$
As a consequence, show that $G$ has growth order $1/2$.

(c) Deduce that $\zeta$ has infinitely many zeros in the critical strip.
:::

::: {.hint}
For (a) and (b), use the functional equation for $\zeta$. For (c), use the result of Hadamard that an entire function of fractional order has infinitely many zeros (Chapter 5, Exercise 14).
:::

::: {.remark}
As printed, $\xi(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s)$ has simple poles at $s=0$ and $s=1$. Thus $F$ has poles at $s=\pm1/2$, and the $G$ in (a) is meromorphic, so (b) cannot give it an entire growth order. The argument needs a pole-canceling factor before Hadamard's theorem applies.
:::
