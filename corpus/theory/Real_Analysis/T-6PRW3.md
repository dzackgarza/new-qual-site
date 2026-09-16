---
schema: qual/card@1
id: T-6PRW3
kind: theorem
title: Tonelli's theorem for nonnegative measurable functions
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
Let $f\colon\RR^n\times\RR^m\to[0,\infty]$ be [[D-DHFN4|Lebesgue measurable]] on $\RR^{n+m}$.
For $x\in\RR^n$ let $f_x\colon\RR^m\to[0,\infty]$ be the slice $f_x(y)\coloneqq f(x,y)$.
Then:

- for almost every $x\in\RR^n$, the slice $f_x$ is Lebesgue measurable on $\RR^m$;

- the function $F(x)\coloneqq\int_{\RR^m} f(x,y)\,dy\in[0,\infty]$, defined for almost every $x$, is Lebesgue measurable on $\RR^n$;

- $$
  \int_{\RR^{n+m}} f = \int_{\RR^n} F(x)\,dx = \int_{\RR^n}\qty{\int_{\RR^m} f(x,y)\,dy}dx \in[0,\infty],
  $$
  and the same holds with the roles of $x$ and $y$ exchanged.

Moreover, if $E\subseteq\RR^{n}\times\RR^m$ is [[D-MDJII|Lebesgue measurable]], then for almost every $x\in\RR^n$ the slice $E_x\coloneqq\theset{y\in\RR^m \suchthat (x, y) \in E}$ is Lebesgue measurable.
:::
