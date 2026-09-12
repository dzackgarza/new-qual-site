---
schema: qual/card@1
id: P-S7NFA
kind: problem
title: Definition of a splitting field, and $[E:F] \le n!$ without the fundamental
  theorem
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-10
  note: "Compared the definition request and the prohibition on the fundamental theorem with page 6 of the original scan, Fields 2."
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: "Checked that the induction works over arbitrary fields, including inseparable polynomials and repeated roots, using only adjoining a root and the tower law."
---

::: problem
Let $F$ be a field and $g(x) \in F[x]$ have degree $n > 0$.

a. Define "$E$ is a splitting field for $g(x)$ over $F$."

b. Prove, without using the Fundamental Theorem of Galois Theory, that if $E$ is a splitting field for $g(x)$ over $F$ then $[E : F] \le n!$.
:::

::: solution
<1>1. A splitting field of $g$ over $F$ is an extension $E/F$ such that
$$
g(x)=a\prod_{i=1}^{n}(x-\alpha_i)
\quad\text{with }a\in F^\times,\ \alpha_i\in E,
\qquad E=F(\alpha_1,\ldots,\alpha_n).
$$
The roots may repeat. The generation condition is essential: merely
containing all the roots does not make an extension a splitting field.

<1>2. Every degree-$n$ polynomial over any field has a splitting field
of degree at most $n!$ over that field; in particular the given $E$
satisfies $[E:F]\leq n!$.

::: proof
We prove the degree bound for every splitting field by induction on
$n$, uniformly over all coefficient fields. Existence follows by
successively adjoining roots, using a quotient by an irreducible factor
at each step.

For $n=1$, the only root already lies in the coefficient field, and
the generation condition gives $E=F$. Thus $[E:F]=1=1!$.

Suppose $n\geq2$ and the bound is known in degree $n-1$. Choose a
root $\alpha\in E$ and put $F_1=F(\alpha)$. The minimal polynomial
of $\alpha$ over $F$ divides $g$, so
$$
[F_1:F]\leq n.
$$
Division by $x-\alpha$ in $F_1[x]$ gives
$$
g(x)=(x-\alpha)h(x),\qquad \deg h=n-1.
$$
All roots of $h$ lie in $E$, and adjoining them to $F_1$ generates
$E$, because together with $\alpha$ they include all the roots of
$g$. Thus $E$ is a splitting field of $h$ over $F_1$. The induction
hypothesis gives $[E:F_1]\leq(n-1)!$. Applying the tower law yields
$$
[E:F]=[E:F_1][F_1:F]\leq(n-1)!\,n=n!.
$$
The argument uses neither separability nor an identification of the
extension degree with the order of an automorphism group.
:::
:::
