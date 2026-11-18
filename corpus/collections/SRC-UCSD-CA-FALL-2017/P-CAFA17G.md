---
schema: qual/card@1
id: P-CAFA17G
kind: problem
title: "Bezout-type identity for entire functions without common zeros"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and the degenerate cases supplied. The prose began "let {a_j} be the zeros of f" and applied Mittag-Leffler to a set that is not discrete when f is identically zero, so the argument as written silently assumed f and g nowhere zero. The card now treats f = 0 (then the hypothesis forces g zero-free, whose reciprocal is entire) and g = 0 separately, states that "no common zeros" is read pointwise, proves that the zeros of f have no accumulation point, that g does not vanish at them, derives the orders of the prescribed principal parts, and shows B = fh and A = 1/f - hg extend to entire functions at those points. Under the pointwise reading the printed statement is true as printed, so no counterexample is needed; the card says so rather than weakening the statement.
---

::: {.problem}
Assume that $f$ and $g$ are entire functions without common zeros.
Show that there exist entire functions $A$, $B$ such that $Af + Bg = 1$.

Hint: Ensure that $A = (1 - Bg)/f$ is entire by matching the principal parts of $1/f$ and $Bg/f$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, following the hint.

"No common zeros" is read pointwise: there is no $z$ with $f(z)=g(z)=0$. Under that reading the statement is true as printed, including the degenerate cases treated in the first step.

::: pf

::: {.pf-step #degenerate}
If $f\equiv0$ then $A=0$, $B=1/g$ solve the problem; symmetrically if $g\equiv0$.

::: pf-proof
If $f\equiv0$ then every $z$ is a zero of $f$, so the hypothesis forces $g(z)\ne0$ for all $z$: $g$ is a zero-free entire function. A zero-free entire function has an entire reciprocal (its logarithm exists, $g=e^h$, so $1/g=e^{-h}$). Then $Af+Bg=0+1=1$. The case $g\equiv0$ is the same with the roles exchanged.
:::

:::

::: {.pf-step #zeros}
Assume $f\not\equiv0$ and $g\not\equiv0$. The zeros $a_1,a_2,\dots$ of $f$ form a set without accumulation point in $\CC$, and $g(a_j)\ne0$ at each of them.

::: pf-proof
The zeros of a nonzero entire function have no accumulation point in $\CC$ (otherwise the identity theorem would force $f\equiv0$). Each $a_j$ is a zero of $f$, so by the hypothesis it is not a zero of $g$.
:::

:::

::: {.pf-step #hl}
There is a meromorphic $h$ on $\CC$, holomorphic off the set of the $a_j$, whose principal part at each $a_j$ equals that of $1/(fg)$, and which has no other poles.

::: pf-proof
Since $g(a_j)\ne0$, the function $1/(fg)$ is holomorphic near $a_j$ after multiplication by $(z-a_j)^{m_j}$, where $m_j$ is the order of the zero of $f$ at $a_j$; so $1/(fg)$ has a pole of order $m_j$ at $a_j$ with a finite principal part $p_j(1/(z-a_j))$. The set $\{a_j\}$ has no accumulation point, so the Mittag-Leffler theorem applies: there is a meromorphic $h$ on $\CC$ whose principal part at $a_j$ is the prescribed one and whose only poles are the $a_j$. (Repeated zeros contribute one index each; multiplicities are carried by the order $m_j$.)
:::

:::

::: {.pf-step #bentire}
$B=fh$ is entire.

::: pf-proof
Off the $a_j$, both $f$ and $h$ are holomorphic, so $B$ is. At $a_j$, $f$ has a zero of order $m_j$ and $h$ has a pole of order $m_j$ by step [](#hl){.pf-ref}, so the product is holomorphic there; the singularities of $B$ are therefore removable, and $B$ is entire.
:::

:::

::: {.pf-step #aentire}
$A=\dfrac1f-hg$ extends to an entire function.

::: pf-proof
Off the zeros of $f$ the formula defines a holomorphic function, since $1/f$ and $hg$ are holomorphic there. At a zero $a_j$ of $f$,
$$
A=-g\left(h-\frac1{fg}\right),
$$
and $h-\frac1{fg}$ is holomorphic at $a_j$ because $h$ and $1/(fg)$ have the same principal part there by step [](#hl){.pf-ref}; so the product with the holomorphic $g$ extends holomorphically over $a_j$. Hence $A$ has removable singularities at the $a_j$ and is entire.
:::

:::

::: {.pf-step #identity}
$Af+Bg=1$.

::: pf-proof
Where $f\ne0$, $Af=f\left(\frac1f-hg\right)=1-fhg=1-Bg$, so $Af+Bg=1$ there; both sides are entire (steps [](#bentire){.pf-ref} and [](#aentire){.pf-ref}), so the identity holds on all of $\CC$ by continuity.
:::

:::

:::
:::
