---
schema: qual/card@1
id: E-SS10.EX-7
kind: problem
title: Triangular and septagonal number identities from the Jacobi triple product
classification:
  areas:
  - complex-analysis
  topics:
  - Theta Functions
  - Generating Functions
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
Use the product formula for $\Theta$ to prove:

(a) The "triangular number" identity
$$
\prod_{n=0}^{\infty} (1+x^{n})(1-x^{2n+2}) = \sum_{n=-\infty}^{\infty} x^{n(n+1)/2},
$$
which holds for $\abs{x} < 1$.

(b) The "septagonal number" identity
$$
\prod_{n=0}^{\infty} (1-x^{5n+1})(1-x^{5n+4})(1-x^{5n+5}) = \sum_{n=-\infty}^{\infty} (-1)^{n} x^{n(5n+3)/2},
$$
which holds for $\abs{x} < 1$.
:::

::: {.solution}

The argument is the card's own: no copy of Stein and Shakarchi and no published solution set for this book is retained in `tmp/sources`, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 10, Exercise 7. Here the Jacobi triple product is used in the form $\sum_{n\in\ZZ}z^{n}q^{n(n+1)/2}=\prod_{m\geq1}(1-q^{m})(1+zq^{m})(1+z^{-1}q^{m-1})$ for $\abs{q}<1$; the form was checked numerically at $q=1/2$, $z=3$, where both sides agree to twelve digits.

::: pf

::: {.pf-step #sub}

(a) With $z=1$, $q=x$, the triple product gives $\sum_{n\in\ZZ}x^{n(n+1)/2}=\prod_{m\geq1}(1-x^{m})(1+x^{m})(1+x^{m-1})$.

::: pf-proof

Substitute $z=1$ and $q=x$ in the identity; $\abs{x}<1$ is the hypothesis.

:::

:::

::: {.pf-step #rearr}

(a) The product equals $\prod_{n\geq0}(1+x^{n})(1-x^{2n+2})$.

::: pf-proof

$(1-x^{m})(1+x^{m})=1-x^{2m}$, so the product over $m\geq1$ of those factors is $\prod_{n\geq0}(1-x^{2n+2})$ under $n=m-1$, and the remaining factor is $\prod_{m\geq1}(1+x^{m-1})=\prod_{n\geq0}(1+x^{n})$.

:::

:::

::: {.pf-step #a}

(a) The triangular-number identity holds for $\abs{x}<1$.

::: pf-proof

Steps [](#sub){.pf-ref} and [](#rearr){.pf-ref}.

:::

:::

::: {.pf-step #series-b}

(b) With $q=x^{5}$ and $z=-x^{-1}$, the series side of the triple product is $\sum_{n\in\ZZ}(-1)^{n}x^{n(5n+3)/2}$.

::: pf-proof

The general term is $z^{n}q^{n(n+1)/2}=(-1)^{n}x^{-n}x^{5n(n+1)/2}$, and $-n+\frac{5n(n+1)}{2}=\frac{5n^{2}+5n-2n}{2}=\frac{n(5n+3)}{2}$.

:::

:::

::: {.pf-step #prod-b}

(b) The product side equals $\prod_{n\geq0}(1-x^{5n+1})(1-x^{5n+4})(1-x^{5n+5})$.

::: pf-proof

With $q=x^{5}$ and $z=-x^{-1}$ the factors are $(1-x^{5m})$, $(1-x^{5m-1})$ and $(1-x^{5m-4})$; the last two, reindexed by $n=m-1\geq0$, are $(1-x^{5n+4})$ and $(1-x^{5n+1})$, and the first is $(1-x^{5n+5})$ with the same reindexing.

:::

:::

::: {.pf-step #b}

(b) The septagonal-number identity holds for $\abs{x}<1$.

::: pf-proof

Steps [](#series-b){.pf-ref} and [](#prod-b){.pf-ref} identify the two sides of the triple product for these parameters.

:::

:::

:::

:::
