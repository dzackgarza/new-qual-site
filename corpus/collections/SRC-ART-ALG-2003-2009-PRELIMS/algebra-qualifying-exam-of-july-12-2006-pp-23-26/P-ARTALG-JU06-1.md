---
schema: qual/card@1
id: P-ARTALG-JU06-1
kind: problem
title: Class equation and nontrivial center of p-group
classification:
  areas:
  - algebra
  topics:
  - Group Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both parts with July 2006 Groups 1 in the retained source extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the conjugacy-class coset bijection and divisibility of every noncentral class size by p."
---

::: {.problem}
(a) State the class equation for finite groups.

(b) Use the class equation to show that if a finite group $G$ has order $p^k$ for some prime $p$ and $k \geq 1$, then $G$ has a nontrivial center.
:::

::: {.solution}
<1>1. If $x_1,\ldots,x_r$ represent the noncentral conjugacy classes
of a finite group $G$, then its class equation is
$$
|G|=|Z(G)|+\sum_{j=1}^r [G:C_G(x_j)],
$$
where $C_G(x)=\{g\in G:gx=xg\}$.

::: {.proof}
Conjugacy is an equivalence relation, so its classes partition $G$.
An element has a singleton conjugacy class precisely when it commutes
with every element of $G$, that is, when it belongs to $Z(G)$.
For any $x\in G$, the map
$$
G/C_G(x)\longrightarrow\{gxg^{-1}:g\in G\},\qquad
gC_G(x)\longmapsto gxg^{-1}
$$
is well-defined and surjective. It is injective because
$gxg^{-1}=hxh^{-1}$ is equivalent to $h^{-1}g\in C_G(x)$,
which is equivalent to equality of the two left cosets.
Thus each noncentral class has the displayed index as its size.
Adding the class sizes gives the formula.
:::

<1>2. If $|G|=p^k$ with $k\geq1$, then $|Z(G)|\geq p$.

::: {.proof}
Each centralizer has order dividing $p^k$ by Lagrange's theorem [@DF04],
so each index $[G:C_G(x_j)]$ is a power of $p$. Since $x_j$ is
noncentral, its centralizer is proper, and that power is greater
than $1$. Hence every term in the sum in step <1>1 is divisible
by $p$. The same equation implies $p\mid |Z(G)|$.
The center contains the identity, so its size is a positive multiple
of $p$ and therefore at least $p>1$. In particular it is nontrivial.
:::
:::
