---
schema: qual/card@1
id: P-HCAX1
kind: problem
title: A continuous isolated singularity is removable
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked the differentiability at the
    centre: with h(a) = 0 the quotient (h(z)-h(a))/(z-a) is exactly (z-a) f(z), bounded in modulus
    by |z-a| (|f(a)|+1) on a disc where f is bounded, which is legitimate because f is continuous
    at a; so h'(a) = 0 and h has a zero of order at least two. Added the construction of g as the
    power series with the two leading coefficients divided out, which the prose only asserted,
    and the two continuity statements that identify g(a) with f(a). Statement unchanged; the card
    says the argument is its own.
---

::: {.problem}
Let $f$ be continuous on a disk and holomorphic away from its center.
Prove that $f$ is holomorphic on the entire disk.
:::

::: {.solution}
Multiply $f$ by $(z-a)^2$: the product is holomorphic on the punctured disc and its difference quotient at $a$ is $(z-a)f(z)$, which tends to $0$ because $f$ is continuous at $a$; so the product is holomorphic on the whole disc with a double zero at $a$, and dividing out the square returns a holomorphic function equal to $f$ off $a$ and equal to $f(a)$ at $a$. The argument is this card's own: the checkout retains no solution set for this oral exam.

::: pf

::: {.pf-step #bounded}
$f$ is bounded on a disc $D(a,r)$ contained in the given disc $D$.

::: pf-proof
$f$ is continuous at $a$, so with $\varepsilon=1$ there is $r>0$ with $\abs{f(z)-f(a)}<1$ for $\abs{z-a}<r$; then $\abs{f(z)}\le\abs{f(a)}+1$ on that disc, which may be taken inside $D$ since $D$ is open.
:::

:::


::: {.pf-step #product}
$h(z)=(z-a)^2f(z)$ is holomorphic on all of $D$, with $h(a)=0$ and $h$ having a zero of order at least $2$ at $a$.

::: pf-proof
On $D\setminus\{a\}$ the function $h$ is a product of holomorphic functions, hence holomorphic. At $a$, put $h(a)=0$; then for $z\ne a$,
$$
\frac{h(z)-h(a)}{z-a}=\frac{(z-a)^2f(z)}{z-a}=(z-a)f(z),
$$
whose modulus is at most $\abs{z-a}(\abs{f(a)}+1)$ on the disc of step [](#bounded){.pf-ref}, hence tends to $0$ as $z\to a$. So $h$ is complex differentiable at $a$ with $h'(a)=0$, hence holomorphic on $D$; and $h(a)=h'(a)=0$ says the zero at $a$ has order at least $2$.
:::

:::


::: {.pf-step #factor}
There is a holomorphic $g$ on $D$ with $h(z)=(z-a)^2g(z)$ for all $z\in D$, and $g(z)=f(z)$ for $z\ne a$.

::: pf-proof
Since $h$ is holomorphic on the disc $D$ with a zero of order at least $2$ at $a$, its power series about $a$ is $h(z)=\sum_{n\ge2}c_n(z-a)^n=(z-a)^2\sum_{n\ge2}c_n(z-a)^{n-2}$, and $g(z):=\sum_{n\ge2}c_n(z-a)^{n-2}$ is holomorphic on $D$ because it has the same radius of convergence as the series for $h$ about $a$, which is at least the radius of $D$ about $a$. For $z\ne a$ we may divide the identity $h(z)=(z-a)^2f(z)$ by the nonzero number $(z-a)^2$ and get $g(z)=f(z)$.
:::

:::


::: {.pf-step #conclusion}
$g=f$ on $D$, and therefore $f$ is holomorphic on $D$, including at the centre $a$.

::: pf-proof
Steps [](#factor){.pf-ref} gives $g=f$ off $a$. At $a$, $g$ is continuous there and $f$ is given to be continuous there, so
$$
g(a)=\lim_{z\to a}g(z)=\lim_{z\to a}f(z)=f(a),
$$
the first equality by continuity of the holomorphic $g$ and the second by continuity of $f$. Hence $g=f$ everywhere on $D$, and $g$ is holomorphic, so $f$ is holomorphic at $a$ as well as away from it.
:::

:::

:::
:::
