---
schema: qual/card@1
id: P-G2TWX
kind: problem
title: A Galois tower that is not Galois, and a finite-dimensional inseparable extension
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Visually compared both extension requests with June 2010 Fields 2 on PDF page 15, preserving the direction of each field extension."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked strictness and both Galois steps of the radical tower, nonnormality of the total extension, and irreducibility and inseparability of the characteristic-two example."
---

::: problem
Give an example of each of the following:

a. Fields $F \subset K \subset L$ such that $L/K$ and $K/F$ are Galois, $L/F$ is algebraic, but $L/F$ is not Galois.

b. A pair of fields $F \subset K$ such that $K$ is finite dimensional over $F$ but $K$ is not separable over $F$.
:::

::: solution
<1>1. For part (a), take
$$
F=\mathbb Q,\qquad K=\mathbb Q(\sqrt2),
\qquad L=\mathbb Q(\sqrt[4]{2}).
$$

::: proof
Let $a=\sqrt[4]{2}>0$, so $a^2=\sqrt2$.
Eisenstein's criterion at two makes $T^2-2$ and $T^4-2$
irreducible over $\mathbb Q$ [@DF04]. Hence
$[K:F]=2$, $[L:F]=4$, and the tower law gives $[L:K]=2$.
In particular both inclusions are strict and $L/F$ is algebraic.

The field $K$ is the splitting field of $T^2-2$ over $F$,
with distinct roots $\sqrt2,-\sqrt2$.
The field $L=K(a)$ is the splitting field of $T^2-\sqrt2$
over $K$, with distinct roots $a,-a$.
Thus both $K/F$ and $L/K$ are Galois, being splitting
fields of separable polynomials [@DF04].

However, $L\subseteq\mathbb R$ contains $a$ but not the
nonreal root $ia$ of the irreducible polynomial $T^4-2$.
That polynomial therefore does not split over $L$, so
$L/F$ is not normal and hence is not Galois.
:::

<1>2. For part (b), take
$$
F=\mathbb F_2(t),\qquad K=F(u),\qquad u^2=t,
$$
where $t$ is transcendental over $\mathbb F_2$.

::: proof
The polynomial $T^2-t$ has no root in $F$.
Indeed, a root written as $A(t)/B(t)$, with nonzero
$A,B\in\mathbb F_2[t]$, would give $A(t)^2=tB(t)^2$.
The left side has even degree and the right side odd
degree, an impossibility. Since a reducible quadratic
over a field has a root, $T^2-t$ is irreducible.
Thus the quotient $F[T]/(T^2-t)$ is a field, and its
element $u=[T]$ gives the asserted extension $K$ with
$[K:F]=2$.

In characteristic two one has $T^2-t=(T-u)^2$ over $K$.
The minimal polynomial of $u$ over $F$ therefore has a
repeated root and is not separable. Hence $K/F$ is a
finite-dimensional, nonseparable extension, as required.
:::
:::
