---
schema: qual/card@1
id: P-CASP05E
kind: problem
title: "Roots of z^n - e^{z-λ} = 0 via Rouché's theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $n$ be a positive integer and $\lambda > 1$ a real number.
Consider the equation $$(**)\quad z^n - e^{z - \lambda} = 0.$$

(a) Find all the roots of (**) with $|z| = 1$.

(b) Show that there are exactly $n$ distinct simple roots of (**) with $|z| < 1$.
:::

::: {.solution}
Put
\[
F(z)=z^n-e^{z-\lambda}.
\]
On $|z|=1$,
\[
|e^{z-\lambda}|=e^{\operatorname{Re}z-\lambda}
\le e^{1-\lambda}<1=|z^n|.
\]
Hence $F$ has no zeros on the unit circle, answering (a), and Rouché's theorem
shows that $F$ has exactly $n$ zeros in $|z|<1$, counted with multiplicity.

They are all simple. If $z$ were a multiple zero, then
\[
z^n=e^{z-\lambda},
\qquad
nz^{n-1}=e^{z-\lambda}.
\]
Since a zero cannot be $0$, division gives $z=n$, which is not in the open unit
disk. Thus the $n$ zeros in $\mathbb D$ are distinct and simple.
:::
