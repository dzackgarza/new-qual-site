---
schema: qual/card@1
id: P-BKF09-9A
kind: problem
title: Locally uniform convergence of $(1+z/n)^n$ to $e^z$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow under the limit and separated the display from the prose against f09solutions.pdf page 4 problem 9A.
---

::: {.problem}
Show that

$$
\lim_{n \to \infty} \left( 1 + \frac{z}{n} \right)^n = e^z
$$

uniformly on compact subsets of $\CC$.
:::

::: {.solution}

The argument is the card's own: take logarithms, bound the error in $\log(1+u)=u+O(u^{2})$, and exponentiate.

::: pf

::: {.pf-step #logbound}

There is $C$ with $\abs{\log(1+u)-u}\le C\abs{u}^{2}$ for $\abs{u}\le\frac12$.

::: pf-proof

$\log(1+u)=\sum_{k\ge1}(-1)^{k+1}u^{k}/k$ for $\abs{u}<1$, so $\log(1+u)-u=\sum_{k\ge2}(-1)^{k+1}u^{k}/k$ and
$$
\abs{\log(1+u)-u}\le\abs{u}^{2}\sum_{k\ge2}\frac{\abs{u}^{k-2}}{k}\le\abs{u}^{2}\sum_{k\ge2}\frac{(1/2)^{k-2}}{k}\le\abs{u}^{2},
$$
taking $C=1$: the sum is at most $\sum_{m\ge0}2^{-m}=2$ divided by $2$, and any fixed constant works.

:::

:::

::: {.pf-step #logn}

For $\abs{z}\le N$ and $n>2N$: $\abs{\log\bigl(1+\frac zn\bigr)^{n}-z}\le \frac{CN^{2}}{n}$.

::: pf-proof

With $u=z/n$ we have $\abs{u}\le N/n<\frac12$, so step [](#logbound){.pf-ref} applies and
$$
\abs{ n\log\Bigl(1+\frac zn\Bigr)-z}=n\abs{\log\Bigl(1+\frac zn\Bigr)-\frac zn}\le nC\frac{\abs{z}^{2}}{n^{2}}\le\frac{CN^{2}}{n}.
$$
(Here $\log(1+z/n)^{n}=n\log(1+z/n)$, the principal branch being used, legitimate since $\abs{z/n}<1$.)

:::

:::

::: {.pf-step #expbound}

$\abs{e^{a}-1}\le e^{\abs{a}}-1$ for all $a\in\CC$.

::: pf-proof

$e^{a}-1=\sum_{k\ge1}a^{k}/k!$, so $\abs{e^{a}-1}\le\sum_{k\ge1}\abs{a}^{k}/k!=e^{\abs{a}}-1$.

:::

:::

::: {.pf-step #uniform}

$\bigl(1+\frac zn\bigr)^{n}\to e^{z}$ uniformly for $\abs{z}\le N$.

::: pf-proof

Write $\bigl(1+\frac zn\bigr)^{n}=e^{z}\exp\bigl(n\log(1+z/n)-z\bigr)$ and put $a=n\log(1+z/n)-z$. By steps [](#logn){.pf-ref} and [](#expbound){.pf-ref},
$$
\abs{\Bigl(1+\frac zn\Bigr)^{n}-e^{z}}=\abs{e^{z}}\abs{e^{a}-1}\le e^{N}\bigl(e^{CN^{2}/n}-1\bigr)
$$
for $\abs{z}\le N$ and $n>2N$. The bound depends on $N$ and $n$ only, not on $z$, and tends to $e^{N}(e^{0}-1)=0$.

:::

:::

::: {.pf-step #conclusion}

$\bigl(1+\frac zn\bigr)^{n}\to e^{z}$ uniformly on compact subsets of $\CC$.

::: pf-proof

A compact $K\subset\CC$ lies in some disc $\abs{z}\le N$. Given $\varepsilon>0$, step [](#uniform){.pf-ref} provides $n_{0}$ with $e^{N}\bigl(e^{CN^{2}/n}-1\bigr)<\varepsilon$ for $n\ge n_{0}$, and then the same bound holds at every $z\in K$:
$$
\boxed{\Bigl(1+\frac zn\Bigr)^{n}\longrightarrow e^{z}\ \text{uniformly on } \abs{z}\le N.}
$$

:::

:::

:::

:::
