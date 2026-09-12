---
schema: qual/card@1
id: P-XNN6S
kind: problem
title: 'Schur''s lemma: endomorphisms of a simple module are zero or isomorphisms'
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Semisimplicity
  - Homomorphisms
relations: []
review: draft
---

::: problem
Let $A$ be a simple module and let
\[
\phi:A\to A
\]
be a module endomorphism. Prove that either $\phi=0$ or $\phi$ is an isomorphism.
:::

::: solution
Both
\[
\ker\phi
\quad\text{and}\quad
\operatorname{im}\phi
\]
are submodules of $A$.

Since $A$ is simple, its only submodules are $0$ and $A$.

If $\operatorname{im}\phi=0$, then $\phi=0$.

Otherwise
\[
\operatorname{im}\phi=A,
\]
so $\phi$ is surjective. In this case $\phi\ne0$, hence
\[
\ker\phi\ne A.
\]
Simplicity therefore forces
\[
\ker\phi=0.
\]
Thus $\phi$ is injective and surjective, hence an isomorphism.

This is Schur's lemma in module form.
:::
