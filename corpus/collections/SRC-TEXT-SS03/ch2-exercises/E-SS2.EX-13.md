---
schema: qual/card@1
id: E-SS2.EX-13
kind: problem
title: An entire function with a vanishing Taylor coefficient at every point is a polynomial
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
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
Suppose $f$ is an analytic function defined everywhere in $\CC$ and such that for each $z_0 \in \CC$ at least one coefficient in the expansion
$$
f(z) = \sum_{n=0}^{\infty} c_n (z - z_0)^n
$$
is equal to $0$. Prove that $f$ is a polynomial.

[Hint: Use the fact that $c_n n! = f^{(n)}(z_0)$ and use a countability argument.]
:::

::: {.solution}

The argument is the card's own: the book is retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, and no published solution set of this exercise is retained, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 2, Exercise 13. Here $f$ is entire and at every $z_0\in\CC$ at least one Taylor coefficient $c_n=f^{(n)}(z_0)/n!$ vanishes; $Z_n=\theset{z\in\CC\mid f^{(n)}(z)=0}$.

::: pf

::: {.pf-step #cover}

$\CC=\bigcup_{n\geq0}Z_n$.

::: pf-proof

At each $z_0$ some coefficient $c_n=f^{(n)}(z_0)/n!$ is zero, which is the same as $f^{(n)}(z_0)=0$, that is $z_0\in Z_n$.

:::

:::

::: {.pf-step #notpoly}

If $f$ is not a polynomial then $f^{(n)}\not\equiv0$ for every $n$.

::: pf-proof

If $f^{(n)}$ vanished identically then $f$ would be a polynomial of degree at most $n-1$, its derivatives of order $\geq n$ being zero.

:::

:::

::: {.pf-step #countable}

If $f$ is not a polynomial then each $Z_n$ is countable.

::: pf-proof

By step [](#notpoly){.pf-ref} $f^{(n)}$ is a holomorphic function not identically zero, so its zeros are isolated: each point of $Z_n$ has a disc containing no other zero of $f^{(n)}$. Shrinking, each point of $Z_n$ carries a disc with rational centre and rational radius meeting $Z_n$ in that point alone, and distinct points give distinct discs, so $Z_n$ injects into the countable set of rational discs.

:::

:::

::: {.pf-step #uncountable}

$\CC$ is uncountable.

::: pf-proof

The interval $(0,1)$ embeds in $\CC$, and a countable union of countable sets is countable; the union in step [](#cover){.pf-ref} being $\CC$, not every $Z_n$ can be finite or empty, and more directly $\CC$ is uncountable by Cantor's theorem applied to the decimal expansion.

:::

:::

::: {.pf-step #done}

$f$ is a polynomial.

::: pf-proof

If $f$ were not a polynomial, step [](#cover){.pf-ref} would express the uncountable set $\CC$ as a countable union of countable sets, which is countable; that contradiction shows some $f^{(n)}$ vanishes identically, and by step [](#notpoly){.pf-ref} $f$ is a polynomial of degree at most $n-1$.

:::

:::

:::

:::
