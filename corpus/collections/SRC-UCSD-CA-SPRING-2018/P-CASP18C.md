---
schema: qual/card@1
id: P-CASP18C
kind: problem
title: "An analytic self-map of a simply connected region that is not the identity has at most one fixed point"
classification:
  areas:
  - complex-analysis
  topics:
  - Fixed Points
  - Riemann Mapping Theorem
  - Holomorphic Functions
relations: []
review: draft
---

::: problem
Show that if $G \neq \mathbb{C}$ is a simply connected subset of $\mathbb{C}$, $f : G \to G$ is analytic, and $f(z)$ is not identically equal to $z$, then $f$ has at most one fixed point in $G$.
:::

::: solution
By the Riemann mapping theorem, choose a conformal bijection
\[
\phi:G\to\mathbb D.
\]
Then
\[
F=\phi\circ f\circ\phi^{-1}
\]
is a holomorphic self-map of $\mathbb D$.

If $f$ had two distinct fixed points, then $F$ would have two distinct fixed
points $a,b\in\mathbb D$. Let $T$ be a disk automorphism with $T(a)=0$ and
set
\[
H=T\circ F\circ T^{-1}.
\]
Then $H(0)=0$ and $H(T(b))=T(b)\ne0$. Schwarz's lemma gives
$|H(z)|\le|z|$, and equality at a nonzero point forces
\[
H(z)=e^{i\theta}z.
\]
The nonzero fixed point then forces $e^{i\theta}=1$, so $H$, hence $F$, hence
$f$, is the identity, contrary to hypothesis. Therefore $f$ has at most one
fixed point.
:::
