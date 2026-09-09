---
schema: qual/card@1
id: P-CASP20E
kind: problem
title: Biholomorphisms between $\mathbb D\setminus\{0,1/2\}$ and $\mathbb D\setminus\{0,-1/2\}$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Automorphisms
  - Biholomorphic Maps
relations: []
review: draft
---

::: problem
Let $A_1 = \mathbb{D} \setminus \left\{0, \frac{1}{2}\right\}$ and $A_2 = \mathbb{D} \setminus \left\{0, -\frac{1}{2}\right\}$.
Find all bijective analytic maps from $A_1$ to $A_2$.
:::

::: solution
Let $F:A_1\to A_2$ be biholomorphic. Since $F$ is bounded, its singularities
at $0$ and $1/2$ are removable, so it extends holomorphically to a map
\[
\widetilde F:\mathbb D\to\mathbb D.
\]
The inverse extends similarly. Their compositions equal the identity on the
punctured domains and therefore, by the identity theorem, on all of
$\mathbb D$. Thus $\widetilde F$ is an automorphism of the unit disk and must
map
\[
\{0,1/2\}\quad\text{onto}\quad\{0,-1/2\}.
\]

If $\widetilde F(0)=0$, then
$\widetilde F(z)=e^{i\theta}z$, and
$\widetilde F(1/2)=-1/2$ forces $e^{i\theta}=-1$. Hence
\[
F_1(z)=-z.
\]

If $\widetilde F(1/2)=0$, then
\[
\widetilde F(z)=e^{i\theta}\frac{z-1/2}{1-z/2}.
\]
The condition $\widetilde F(0)=-1/2$ forces $e^{i\theta}=1$. Hence
\[
F_2(z)=\frac{z-1/2}{1-z/2}.
\]
These two maps indeed restrict to biholomorphisms $A_1\to A_2$, and they are
the only ones.
:::
