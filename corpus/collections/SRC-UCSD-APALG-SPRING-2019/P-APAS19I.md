---
schema: qual/card@1
id: P-APAS19I
kind: problem
title: Center of a finite-dimensional $\mathbb{C}$-algebra acts by scalars
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
---

::: {.problem}
Let $A$ be a finite-dimensional algebra over $\mathbb{C}$ with center $Z(A)$, and let $(V,\rho)$ be an irreducible representation of $A$.
Show that $\rho(z)=\chi(z)I_V$ for each $z\in Z(A)$, where $\chi(z)$ is a scalar.
Show that the map $\chi\colon Z(A)\to\mathbb{C}$ defined by $z\mapsto\chi(z)$ is an algebra homomorphism.
:::

::: {.solution}
For \(z\in Z(A)\), the linear map \(
ho(z)\in\operatorname{End}_{\mathbb C}(V)\) commutes with \(
ho(a)\) for every \(a\in A\), because
\[
\rho(z)\rho(a)=\rho(za)=\rho(az)=\rho(a)\rho(z).
\]
Since \(V\) is an irreducible complex representation, Schur's lemma implies that
\[
\rho(z)=\chi(z)I_V
\]
for a unique scalar \(\chi(z)\in\mathbb C\).

It remains to show that \(\chi\) is an algebra homomorphism. For \(z,w\in Z(A)\) and \(c\in\mathbb C\),
\[
\rho(z+w)=\rho(z)+\rho(w)=(\chi(z)+\chi(w))I_V,
\]
so uniqueness of the scalar gives
\[
\chi(z+w)=\chi(z)+\chi(w).
\]
Similarly,
\[
\rho(zw)=\rho(z)\rho(w)=\chi(z)\chi(w)I_V,
\]
so
\[
\chi(zw)=\chi(z)\chi(w).
\]
Also
\[
\rho(cz)=c\rho(z)=c\chi(z)I_V,
\]
so \(\chi(cz)=c\chi(z)\). Finally, because \(
ho(1_A)=I_V\),
\[
\chi(1_A)=1.
\]
Hence \(\chi:Z(A)\to\mathbb C\) is a unital \(\mathbb C\)-algebra homomorphism.
:::
