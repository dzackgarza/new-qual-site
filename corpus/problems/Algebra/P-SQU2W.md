---
schema: qual/card@1
id: P-SQU2W
kind: problem
title: Perfect fields
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Counterexamples
relations: []
review: draft
---

::: problem
What is a perfect field, why is perfection important, and what is an example of a nonperfect field?
:::

::: solution
A field $F$ is **perfect** if every algebraic extension of $F$ is separable. Equivalently, every irreducible polynomial in $F[x]$ is separable.

Every field of characteristic $0$ is perfect, because the derivative of a nonconstant irreducible polynomial cannot vanish identically.

If $\operatorname{char}F=p>0$, then
\[
F\text{ is perfect}\iff F^p=F,
\]
that is, iff the Frobenius map
\[
F\to F,\qquad x\mapsto x^p
\]
is surjective. Indeed, inseparability in characteristic $p$ occurs exactly when an irreducible polynomial has zero derivative, hence is a polynomial in $x^p$.

A standard nonperfect field is
\[
F=\FF_p(t).
\]
The element $t$ is not a $p$th power in $F$, so Frobenius is not surjective. Equivalently,
\[
x^p-t\in F[x]
\]
is irreducible and inseparable.

Perfection matters because over a perfect field all finite algebraic extensions are separable, so normal finite extensions are automatically Galois and the usual finite Galois correspondence applies without inseparability pathologies.
:::
