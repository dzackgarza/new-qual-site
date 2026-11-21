---
schema: qual/card@1
id: E-SS5.EX-11
kind: problem
title: Picard's little theorem for entire functions of finite order
classification:
  areas:
  - complex-analysis
  topics:
  - Hadamard Factorization
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose, which is the printed hint's route:
    a zero-free entire function of finite order is e^P for a polynomial P (Hadamard
    factorization), a nonconstant polynomial is surjective by the fundamental theorem of
    algebra, and a logarithm of the nonzero b - a then produces a point where f = b. Checked and
    written out in the proof rather than assumed: f - a has the same finite order as f, which is
    what lets the factorization theorem be applied to it, and the hypothesis that f omits both a
    and b is used in the same way in each step. The step asserts nothing about the finite-order
    hypothesis being removable, and the last step says plainly that Picard's little theorem for
    arbitrary entire functions is not proved here. Statement unchanged; no retained solution set
    covers the exercises of Stein-Shakarchi, so the card's solution says the argument is its own.
---

::: {.exercise}
Show that if $f$ is an entire function of finite order that omits two values, then $f$ is constant. This result remains true for any entire function and is known as Picard's little theorem.

[Hint: If $f$ misses $a$, then $f(z) - a$ is of the form $e^{p(z)}$ where $p$ is a polynomial.]
:::

::: {.solution}
The printed hint's route: a zero-free entire function of finite order is the exponential of a polynomial (Hadamard's factorization theorem), and a nonconstant polynomial is surjective, so the exponential would take the omitted second value. The argument is this card's own; no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #setup}
Let $f$ be entire of finite order $\rho$ and suppose $f$ omits the two distinct values $a\ne b$, that is $f(z)\ne a$ and $f(z)\ne b$ for every $z$.

::: pf-proof
This is the hypothesis of the statement. The order of $f$ is the infimum of the $\rho$ with $\abs{f(z)}\le e^{C\abs z^\rho}$ for large $\abs z$; the results used below are applied to the function $g=f-a$, so note at the outset that $g$ has the same finite order as $f$, since $\abs g\le\abs f+\abs a$ and $\abs f\le\abs g+\abs a$.
:::

:::


::: {.pf-step #factor}
$f(z)-a=e^{P(z)}$ for some polynomial $P$.

::: pf-proof
The function $g=f-a$ is entire, of finite order, and zero-free by the hypothesis. Hadamard's factorization theorem for an entire function of finite order with no zeros says that $g=e^{h}$ for an entire $h$, and that $h$ is a polynomial when the order is finite (equivalently, $h'=g'/g$ is a polynomial, as $g$ has finite order and no zeros). So $P:=h$ is a polynomial.
:::

:::


::: {.pf-step #surjective}
Every nonconstant polynomial $P$ and every $\lambda\in\CC$ admit $z_0$ with $P(z_0)=\lambda$.

::: pf-proof
$P-\lambda$ is a nonconstant polynomial, so by the fundamental theorem of algebra it has a complex root $z_0$; then $P(z_0)=\lambda$.
:::

:::


::: {.pf-step #contradiction}
$P$ is constant.

::: pf-proof
Suppose $P$ is nonconstant. The number $b-a$ is nonzero, so it has a logarithm: choose $\lambda\in\CC$ with $e^\lambda=b-a$. By step [](#surjective){.pf-ref} there is $z_0$ with $P(z_0)=\lambda$, and then by step [](#factor){.pf-ref}
$$
f(z_0)-a=e^{P(z_0)}=e^\lambda=b-a,
$$
so $f(z_0)=b$, contrary to the hypothesis that $f$ omits $b$. Hence $P$ is constant.
:::

:::


::: {.pf-step #conclusion}
$f$ is constant.

::: pf-proof
By steps [](#contradiction){.pf-ref} and [](#factor){.pf-ref} there is $c\in\CC$ with $f(z)-a=e^{c}$ for all $z$, so $f\equiv a+e^c$. The statement's conclusion is therefore proved for finite-order $f$; Picard's little theorem removes the finite-order hypothesis, which is not proved here and is not part of what was asked.
:::

:::

:::
:::
