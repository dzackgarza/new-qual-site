---
schema: qual/card@1
id: E-SS5.EX-13
kind: problem
title: $e^z=z$ has infinitely many solutions
classification:
  areas:
  - complex-analysis
  topics:
  - Hadamard Factorization
  - Zeros
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 5 growth-order convention.
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
Show that the equation $e^z - z = 0$ has infinitely many solutions in $\CC$.

[Hint: Apply Hadamard's theorem.]
:::

::: {.solution}

The argument is the card's own: the book is retained in this repository as `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, and no published solution set of this exercise is retained, so nothing below is transcribed. The statement is the exercise the collection index records as Stein and Shakarchi, *Complex Analysis* (2003), Ch. 5, Exercise 13. Here $F(z)=e^{z}-z$ is entire of order $1$, and Hadamard's factorization theorem for an entire function of order $\leq1$ with finitely many zeros $z_1,\dots,z_m$ states that $F(z)=e^{az+b}Q(z)$ with $Q(z)=\prod_{j}(1-z/z_j)$ a polynomial of degree $m$.

::: pf

::: {.pf-step #hadamard}

Suppose $F$ has only finitely many zeros; then $F(z)=e^{az+b}Q(z)$ with $\deg Q=m$.

::: pf-proof

Hadamard's theorem, applied to the entire function $F$ of order $1$ with finitely many zeros.

:::

:::

::: {.pf-step #negl}

$\log\abs{F(x)}=\log\abs{x}+o(1)$ as $x\to-\infty$ along the real axis.

::: pf-proof

$F(x)=e^{x}-x=x(e^{x}/x-1)$ and $e^{x}/x\to0$ as $x\to-\infty$; so $\abs{F(x)}/\abs{x}\to1$ and the logarithm of the ratio tends to $0$.

:::

:::

::: {.pf-step #formula}

$\log\abs{F(x)}=(\Re a)x+m\log\abs{x}+O(1)$ for real $x$.

::: pf-proof

Taking moduli in step [](#hadamard){.pf-ref}, $\abs{F(x)}=e^{(\Re a)x+\Re b}\abs{Q(x)}$ and $\abs{Q(x)}=\abs{x}^{m}(1+O(1/x))$ for large $\abs{x}$.

:::

:::

::: {.pf-step #compare}

$\Re a=0$ and $m=1$.

::: pf-proof

Comparing steps [](#negl){.pf-ref} and [](#formula){.pf-ref} as $x\to-\infty$: if $\Re a<0$ the right side of step [](#formula){.pf-ref} grows linearly in $\abs{x}$; if $\Re a>0$ it decays exponentially; in either case it cannot equal $\log\abs{x}+o(1)$. So $\Re a=0$, and then the coefficient of $\log\abs{x}$ forces $m=1$.

:::

:::

::: {.pf-step #contra}

Contradiction on the positive axis.

::: pf-proof

For $x\to+\infty$, $F(x)=e^{x}(1-xe^{-x})\sim e^{x}$, so $\log\abs{F(x)}=x+o(1)$; but steps [](#formula){.pf-ref} and [](#compare){.pf-ref} give $\log\abs{F(x)}=\log x+O(1)$, and $x+o(1)$ is not $O(\log x)$.

:::

:::

::: {.pf-step #done}

$e^{z}-z$ has infinitely many zeros.

::: pf-proof

Step [](#contra){.pf-ref} contradicts step [](#hadamard){.pf-ref}, so the supposition of finitely many zeros fails.

:::

:::

:::

:::
