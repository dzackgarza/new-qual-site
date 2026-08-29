---
schema: qual/card@1
id: T-TUXBP
kind: theorem
title: Implicit Function Theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Calculus
relations:
- kind: related-to
  target: T-QMGPN
review: draft
---

::: {.theorem}
Let $A \subseteq \RR^{k+n}$ be open and $f: A \to \RR^n$ of class $C^r$.
Write $f$ as $f(\vector x, \vector y)$ with $\vector x\in\RR^k$ and $\vector y \in \RR^n$, so that
\[
Df = \left[\, \dd{f}{\vector x} \quad \dd{f}{\vector y} \,\right]
\]
splits into a $n\times k$ block and an $n\times n$ block.
Suppose $(\vector a, \vector b) \in A$ satisfies $f(\vector a, \vector b) = 0$ and
\[
\det \dd{f}{\vector y}(\vector a, \vector b) \neq 0
.\]
Then there is a neighbourhood $B \subseteq \RR^k$ of $\vector a$ and a unique continuous $g: B \to \RR^n$ with $g(\vector a) = \vector b$ and
\[
f(\vector x, g(\vector x)) = 0 \quad\text{for all } \vector x \in B
,\]
and this $g$ is in fact $C^r$.
:::

::: {.remark}
The invertible block is the one belonging to the variables being **solved for**, not the whole derivative: $Df$ is $n\times(k+n)$ and is never square unless $k=0$.
The count is forced, $n$ equations solve for $n$ unknowns and the other $k$ are free.

Differentiating the identity gives implicit differentiation without ever computing $g$:
\[
\dd{f}{\vector x} + \dd{f}{\vector y}\cdot Dg = 0 \implies Dg(\vector x) = -\left[ \dd{f}{\vector y}(\vector x, g(\vector x)) \right]\inv \cdot \dd{f}{\vector x}(\vector x, g(\vector x))
.\]
The proof applies the inverse function theorem to $F(\vector x, \vector y) \da (\vector x, f(\vector x, \vector y))$, whose derivative is invertible exactly when $\partial f/\partial \vector y$ is.
:::

::: {.concept}
See Munkres, *Analysis on Manifolds*, §9, Theorem 9.2, p. 71; the derivative formula is Theorem 9.1.
:::
