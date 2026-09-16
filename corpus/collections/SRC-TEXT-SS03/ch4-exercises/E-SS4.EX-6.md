---
schema: qual/card@1
id: E-SS4.EX-6
kind: problem
title: "SS 4.6: A partial-fraction sum evaluating to coth of pi-a"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
6. Prove that

$$
\frac {1}{\pi} \sum_ {n = - \infty} ^ {\infty} \frac {a}{a ^ {2} + n ^ {2}} = \sum_ {n = - \infty} ^ {\infty} e ^ {- 2 \pi a | n |}
$$

whenever $a > 0$ . Hence show that the sum equals coth $\pi a$
:::

::: {.solution}
From Exercise 3, for
\[
f(x)=\frac1\pi\frac{a}{a^2+x^2},\qquad a>0,
\]
we have
\[
\widehat f(\xi)=e^{-2\pi a|\xi|}.
\]
Both $f$ and $\widehat f$ are of moderate decrease, so the Poisson summation formula applies:
\[
\sum_{n\in\mathbb Z}f(n)=\sum_{n\in\mathbb Z}\widehat f(n).
\]
Therefore
\[
\frac1\pi\sum_{n=-\infty}^{\infty}\frac{a}{a^2+n^2}
=\sum_{n=-\infty}^{\infty}e^{-2\pi a|n|}.
\]
The latter sum is geometric:
\[
\sum_{n\in\mathbb Z}e^{-2\pi a|n|}
=1+2\sum_{n=1}^{\infty}e^{-2\pi an}
=1+\frac{2e^{-2\pi a}}{1-e^{-2\pi a}}
=\frac{e^{\pi a}+e^{-\pi a}}{e^{\pi a}-e^{-\pi a}}
=\coth(\pi a).
\]
Hence both displayed sums equal $\coth(\pi a)$.
:::
