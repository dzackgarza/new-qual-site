---
schema: qual/card@1
id: E-PQ7NC
kind: problem
title: Complement of the disc to $\mathbb{H}$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Geometry
relations: []
review: draft
---

::: {.exercise}
Find a conformal map $\DD^c\cap\HH\to\HH$, where $\DD^c=\{z:|z|>1\}$.
:::

::: {.solution}
The Joukowski map
\[
J(z)=z+{1\over z}
\]
works.
Write $z=re^{i\theta}$ with $r>1$ and $0<\theta<\pi$.
Then
\[
\Im J(z)=\qty{r-r^{-1}}\sin\theta>0,
\]
so $J$ maps the domain into $\HH$.

It is injective there.
Indeed,
\[
J(z_1)=J(z_2)
\iff
(z_1-z_2)\qty{1-{1\over z_1z_2}}=0.
\]
Since $|z_1z_2|>1$, the second factor cannot vanish; hence $z_1=z_2$.

It is also onto.
Given $w\in\HH$, the equation $J(z)=w$ is
\[
z^2-wz+1=0.
\]
Its two roots have product $1$.
Neither root lies on $|z|=1$, because $J(e^{i\theta})=2\cos\theta\in\RR$.
Hence exactly one root has modulus greater than $1$.
For that root, the identity
\[
\Im w=\qty{|z|-|z|^{-1}}\sin(\arg z)>0
\]
forces $0<\arg z<\pi$, so the root lies in $\DD^c\cap\HH$.

Finally,
\[
J'(z)=1-{1\over z^2},
\]
which vanishes only at $z=\pm1$, outside the domain.
Thus $J$ is a biholomorphic, hence conformal, map from $\DD^c\cap\HH$ onto $\HH$.
:::
