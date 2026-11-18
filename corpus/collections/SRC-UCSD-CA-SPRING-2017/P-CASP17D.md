---
schema: qual/card@1
id: P-CASP17D
kind: problem
title: Entire and meromorphic functions with prescribed zeros, poles, and residues
classification:
  areas:
  - complex-analysis
  topics:
  - Weierstrass Theorem
  - Mittag-Leffler Theorem
  - Entire Functions
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: both sequences are
    strictly increasing (t + 1/t has positive derivative on t > 1) and unbounded, so the sets
    are closed and discrete; sum |a_n|^-3 <= sum n^-3/2 converges, which is the genus-2
    criterion used for the canonical product; E_2 has its only zero, simple, at 1, so F has
    simple zeros exactly at the a_n; and Mittag-Leffler with principal parts sqrt(n)/(z - n
    sqrt(n)) gives the meromorphic function of part (ii). The convergence estimate,
    distinctness and the applicability of both theorems were asserted in the prose and are now
    steps. Both constructed objects are correct as stated. The collection's provenance is the
    examination paper only, so no retained solution set covers the exercise and the argument is
    the card's own.
---

::: {.problem}
(i) Construct an entire function with simple zeros at $\left\{\sqrt{n} + \frac{1}{\sqrt{n}} : n = 1, 2, \ldots\right\}$ and no other zeroes.

(ii) Construct a meromorphic function with simple poles at $z = n\sqrt{n}$ and residues equal to $\sqrt{n}$ for $n = 1, 2, \ldots$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Write $a_n\coloneqq\sqrt n+\frac{1}{\sqrt n}$, $b_n\coloneqq n\sqrt n$ and $E_2(w)\coloneqq(1-w)e^{w+w^2/2}$.

::: pf

::: {.pf-step #discrete}
$(a_n)$ and $(b_n)$ are strictly increasing sequences tending to $\infty$, so each of the sets $\{a_n\}$ and $\{b_n\}$ is closed and discrete in $\CC$.

::: pf-proof
$t\mapsto t+\frac1t$ is strictly increasing on $[1,\infty)$ because its derivative $1-\frac1{t^2}\ge0$ is positive for $t>1$, and $t\mapsto t^3$ is strictly increasing, so both sequences are strictly increasing; both tend to $\infty$. A strictly increasing unbounded sequence of positive reals has no accumulation point in $\CC$, so its set of values is closed and discrete.
:::

:::

::: {.pf-step #convergence}
$\sum_n\abs{a_n}^{-3}<\infty$.

::: pf-proof
$a_n\ge\sqrt n$, so $\abs{a_n}^{-3}\le n^{-3/2}$, and $\sum_n n^{-3/2}$ converges because $\frac32>1$.
:::

:::

::: {.pf-step #product}
$F(z)\coloneqq\prod_{n\ge1}E_2\!\left(\frac{z}{a_n}\right)$ is entire, converges normally on compact subsets of $\CC$, and has simple zeros exactly at the points $a_n$.

::: pf-proof
$E_2$ is entire with the single simple zero $w=1$. Since $\sum\abs{a_n}^{-3}$ converges, the standard convergence criterion for canonical products of genus $2$ gives normal convergence of the product on every compact set, hence an entire $F$; the zeros of $F$ are the zeros of the factors, that is the points $a_n$, and each is simple because exactly one factor vanishes there and it does so to first order.
:::

:::

::: {.pf-step #mittag-leffler}
There is a meromorphic $G$ on $\CC$ whose poles are exactly the points $b_n$, all simple, with $\operatorname{Res}(G,b_n)=\sqrt n$.

::: pf-proof
Step [](#discrete){.pf-ref} makes $\{b_n\}$ a closed discrete set, and the prescribed principal parts $\frac{\sqrt n}{z-b_n}$ are finite sums of terms $\frac{c}{(z-b)^k}$ with $1\le k\le1$. Mittag--Leffler's theorem then supplies a meromorphic $G$ with exactly these principal parts, the corresponding series being made locally uniformly convergent by subtracting from each term its Taylor polynomial of sufficiently high order at $0$.
:::

:::

::: {.pf-step}
(i) $F$ is an entire function with simple zeros exactly at $\sqrt n+\frac{1}{\sqrt n}$ and no others; (ii) $G$ is meromorphic with simple poles at $n\sqrt n$ and residues $\sqrt n$.

::: pf-proof
Part (i) is step [](#product){.pf-ref}. Part (ii) is step [](#mittag-leffler){.pf-ref}: at a simple pole the residue is the coefficient of $(z-b_n)^{-1}$ in the principal part, which is $\sqrt n$.
:::

:::

:::
:::
