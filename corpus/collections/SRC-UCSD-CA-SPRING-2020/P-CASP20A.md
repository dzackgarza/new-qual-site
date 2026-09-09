---
schema: qual/card@1
id: P-CASP20A
kind: problem
title: "Count roots of pi^2 z^5 e^{-2z} - 1 in the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomial Roots
  - Argument Principle
relations: []
review: draft
---

::: problem
Let $f(z) = \pi^2 z^5 e^{-2z} - 1$.
How many roots does $f$ have in $\mathbb{D}$?
How many simple roots does $f$ have in $\mathbb{D}$?

Hint: $e < \pi$.
:::

::: solution
On $|z|=1$,
\[
\left|\pi^2 z^5 e^{-2z}\right|
=\pi^2 e^{-2\operatorname{Re}z}
\ge \frac{\pi^2}{e^2}>1.
\]
Therefore, by Rouché's theorem,
\[
f(z)=\pi^2z^5e^{-2z}-1
\]
has the same number of zeros in $\mathbb D$ as
$\pi^2z^5e^{-2z}$, namely five counted with multiplicity.

To test simplicity,
\[
f'(z)=\pi^2e^{-2z}z^4(5-2z).
\]
A multiple zero of $f$ would have to satisfy $f=f'=0$. Since a zero of $f$
is nonzero, this forces $z=5/2$, which is not in $\mathbb D$. Hence all five
zeros in the unit disk are simple.

Thus
\[
\boxed{5\text{ roots in }\mathbb D,\text{ all }5\text{ simple}.}
\]
:::
