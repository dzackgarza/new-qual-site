---
schema: qual/card@1
id: P-HCAX21
kind: problem
title: Uniqueness in the Riemann mapping theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Mapping Theorem
relations: []
review: draft
---

::: problem
Prove the uniqueness statement in the Riemann mapping theorem after fixing the image of one point and the argument of the derivative there.
:::

::: solution
Let $\Omega\subsetneq\mathbb C$ be simply connected, fix $z_0\in\Omega$, and suppose
\[
f,g:\Omega\longrightarrow\mathbb D
\]
are conformal isomorphisms satisfying
\[
f(z_0)=g(z_0)=0
\]
and
\[
\arg f'(z_0)=\arg g'(z_0).
\]

Consider
\[
h=g\circ f^{-1}:\mathbb D\longrightarrow\mathbb D.
\]
Then $h$ is an automorphism of the disk and $h(0)=0$. By Schwarz's lemma,
\[
|h(z)|\le |z|.
\]
Applying Schwarz's lemma to $h^{-1}$ gives the reverse inequality, so
\[
|h(z)|=|z|
\]
for every $z\in\mathbb D$. The rigidity case of Schwarz's lemma therefore yields
\[
h(z)=e^{i\theta}z
\]
for some real $\theta$.

Differentiating $g=h\circ f$ at $z_0$ gives
\[
g'(z_0)=e^{i\theta}f'(z_0).
\]
Since $f'(z_0)$ and $g'(z_0)$ have the same argument, $e^{i\theta}=1$. Thus $h$ is the identity, and therefore
\[
g=f.
\]

Hence fixing the image of one point and the argument of the derivative there determines the Riemann map uniquely.
:::
