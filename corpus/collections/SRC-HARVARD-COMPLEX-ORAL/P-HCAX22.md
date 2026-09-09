---
schema: qual/card@1
id: P-HCAX22
kind: problem
title: Conformal automorphisms of the disk
classification:
  areas:
  - complex-analysis
  topics:
  - Mobius Transformations
relations: []
review: draft
---

::: problem
Determine all conformal automorphisms of the unit disk.
:::

::: solution
For $a\in\mathbb D$, define
\[
\phi_a(z)=\frac{z-a}{1-\overline a z}.
\]
This is a Möbius transformation carrying $\mathbb D$ biholomorphically onto itself and sending $a$ to $0$.

Let $F\in\operatorname{Aut}(\mathbb D)$ and set
\[
a=F^{-1}(0).
\]
Then
\[
H=F\circ\phi_a^{-1}
\]
is an automorphism of $\mathbb D$ fixing $0$. Schwarz's lemma applied to $H$ and $H^{-1}$ gives
\[
|H(z)|=|z|,
\]
so the rigidity case gives
\[
H(z)=e^{i\theta}z
\]
for some $\theta\in\mathbb R$. Hence
\[
\boxed{
F(z)=e^{i\theta}\frac{z-a}{1-\overline a z},
\qquad a\in\mathbb D,
\ \theta\in\mathbb R.}
\]

Conversely, every map of this form is a composition of the disk automorphism $\phi_a$ with a rotation, hence is a conformal automorphism of $\mathbb D$.
:::
