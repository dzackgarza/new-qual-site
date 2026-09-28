---
schema: qual/card@1
id: P-CASP20B
kind: problem
title: "Existence of a holomorphic function with a prescribed derivative on |z|>3"
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residue Theorem
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Prove or disprove the following statement.

Let $U = \{z \in \mathbb{C} : |z| > 3\}$.
There exists a holomorphic function $f$ in $U$ such that
$$
f'(z) = \frac{z^2 + 2}{z(z-1)(z-2)}.
$$
:::

::: {.solution}
The statement is false. If such an $f$ existed, then its derivative would have
zero integral around every closed curve in $U$. Let
\[
R(z)=\frac{z^2+2}{z(z-1)(z-2)}.
\]
For a large positively oriented circle $|z|=r>3$,
\[
\int_{|z|=r}R(z)\,dz
=-2\pi i\operatorname{Res}_{\infty}R.
\]
Since
\[
R(z)=\frac1z+O(z^{-2})
\qquad(z\to\infty),
\]
we have $\operatorname{Res}_{\infty}R=-1$, and therefore
\[
\int_{|z|=r}R(z)\,dz=2\pi i\ne0.
\]
Hence $R$ has no single-valued holomorphic primitive on $U$, so no such $f$
exists.
:::
