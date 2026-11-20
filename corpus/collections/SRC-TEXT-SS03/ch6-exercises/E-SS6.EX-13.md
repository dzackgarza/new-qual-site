---
schema: qual/card@1
id: E-SS6.EX-13
kind: problem
title: $\frac{d^2}{ds^2}\log\Gamma(s)=\sum_{n\ge0}(s+n)^{-2}$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the card's prose argument into numbered steps without changing the mathematics, and
    re-checked each step against the definitions and theorems it invokes. What was not checked: no
    copy of Stein and Shakarchi and no solution set for it is retained in tmp/sources (the
    collection provenance is the Google Books ISBN link), so the printed statement and page were
    not re-read; the exercise number is the one the collection index records. No published
    solution is transcribed; the argument remains the card's own, as its solution section says.
---

::: {.exercise}
Prove that
$$
\frac{d^2 \log\Gamma(s)}{ds^2} = \sum_{n=0}^{\infty} \frac{1}{(s + n)^2}
$$
whenever $s$ is a positive number. Show that if the left-hand side is interpreted as $(\Gamma'/\Gamma)'$, then the above formula also holds for all complex numbers $s$ with $s \neq 0, -1, -2, \ldots$.
:::

::: {.solution}

The argument is the card's own: the book is retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, and no published solution set of this exercise is retained, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 6, Exercise 13. Here $\gamma$ is Euler's constant and the Weierstrass product used is $1/\Gamma(s)=se^{\gamma s}\prod_{n\geq1}(1+s/n)e^{-s/n}$, which converges locally uniformly on $\CC$.

::: pf

::: {.pf-step #log}

On a compact set avoiding $0,-1,-2,\dots$, $\log(1/\Gamma(s))=\log s+\gamma s+\sum_{n\geq1}(\log(1+s/n)-s/n)$ and the series converges locally uniformly.

::: pf-proof

The product converges locally uniformly and its factors are nonzero on such a set, so a branch of the logarithm of the product is the sum of the logarithms of the factors; the logarithmic series converges locally uniformly because $\log(1+s/n)-s/n=O(\abs{s}^{2}/n^{2})$ uniformly on a bounded set.

:::

:::

::: {.pf-step #first}

$-\frac{\Gamma'(s)}{\Gamma(s)}=\frac1s+\gamma+\sum_{n\geq1}\left(\frac1{s+n}-\frac1n\right)$.

::: pf-proof

Differentiate termwise the identity of step [](#log){.pf-ref}; termwise differentiation is legitimate by local uniform convergence of the differentiated series, whose terms are $\frac1s+\gamma$ and $\frac{1}{s+n}-\frac1n$.

:::

:::

::: {.pf-step #second}

$\left(\frac{\Gamma'}{\Gamma}\right)'(s)=\sum_{n\geq0}\frac{1}{(s+n)^{2}}$.

::: pf-proof

Differentiate step [](#first){.pf-ref} once more, again termwise on compact sets avoiding the poles: the derivative of $\frac1s$ is $-\frac1{s^{2}}$, that of $\frac1{s+n}-\frac1n$ is $-\frac{1}{(s+n)^{2}}$, and $\gamma$ is constant; multiplying by $-1$ gives $\sum_{n\geq0}(s+n)^{-2}$.

:::

:::

::: {.pf-step #real}

For positive real $s$, $\frac{d^{2}\log\Gamma}{ds^{2}}(s)=\sum_{n\geq0}\frac{1}{(s+n)^{2}}$.

::: pf-proof

On $(0,\infty)$ one has $\Gamma>0$, so $\log\Gamma$ is a genuine logarithm and $(\Gamma'/\Gamma)'=(\log\Gamma)''$; step [](#second){.pf-ref} gives the formula.

:::

:::

::: {.pf-step #done}

For $s\in\CC\setminus\theset{0,-1,-2,\dots}$ the formula holds with $(\Gamma'/\Gamma)'$ on the left.

::: pf-proof

Step [](#second){.pf-ref} was derived on an arbitrary compact subset of that open set, and the series converges locally uniformly there, since $\sum\abs{s+n}^{-2}$ converges uniformly on compact sets meeting $\ZZ_{\leq0}$ nowhere.

:::

:::

:::

:::
