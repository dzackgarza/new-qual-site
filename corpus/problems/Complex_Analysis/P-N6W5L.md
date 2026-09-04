---
schema: qual/card@1
id: P-N6W5L
kind: problem
title: Number of zeros of $z^3-z+1$ in the right half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Argument Principle
  - Zeros
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Find the number of zeros $z$ with $\Re(z) > 0$ for the following function:
\[
f(z) \da z^3-z+1
.\]
:::

::: {.solution}
Let
\[
M(z)=z^3+1,
\qquad
m(z)=-z,
\]
so that $f=M+m$. Apply Rouché on the boundary of a large right half-disk.

On the semicircular part $|z|=R$ with $R\ge2$,
\[
|M(z)|\ge R^3-1>R=|m(z)|.
\]

On the imaginary-axis part, write $z=it$. Then
\[
|M(it)|^2=|1-it^3|^2=1+t^6,
\qquad
|m(it)|^2=t^2.
\]
If $t^2\le1$, then $1+t^6>t^2$; if $t^2\ge1$, then $t^6\ge t^2$, so again $1+t^6>t^2$. Thus
\[
|M(it)|>|m(it)|
\]
on the entire imaginary axis.

Hence $f$ and $M$ have the same number of zeros in the right half-disk. The roots of
\[
M(z)=z^3+1
\]
are
\[
e^{i\pi/3},\qquad -1,\qquad e^{5i\pi/3}.
\]
Exactly two lie in the open right half-plane. Taking $R$ large enough to contain all zeros of $f$, we conclude that $f$ has exactly two zeros with $\Re z>0$.
:::
