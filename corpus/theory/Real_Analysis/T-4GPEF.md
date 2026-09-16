---
schema: qual/card@1
id: T-4GPEF
kind: theorem
title: Fubini's theorem for integrable functions
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
Let $f\colon\RR^n\times\RR^m\to\CC$ be [[D-R5DL3|integrable]] with respect to Lebesgue measure on $\RR^{n+m}$.
For $x\in\RR^n$ let $f_x\colon\RR^m\to\CC$ be the slice $f_x(y)\coloneqq f(x,y)$.
Then:

- for almost every $x\in\RR^n$, the slice $f_x$ is integrable on $\RR^m$;

- the function $F(x)\coloneqq\int_{\RR^m} f(x,y)\,dy$, defined for almost every $x$, is integrable on $\RR^n$;

- $$
  \int_{\RR^{n+m}} f = \int_{\RR^n}\qty{\int_{\RR^m} f(x,y)\,dy}dx ,
  $$
  and the same holds with the roles of $x$ and $y$ exchanged.

Moreover, if $E\subseteq\RR^{n}\times\RR^m$ is [[D-MDJII|Lebesgue measurable]], then for almost every $x\in\RR^n$ the slice $E_x\coloneqq\theset{y\in\RR^m \suchthat (x, y) \in E}$ is Lebesgue measurable.
:::
