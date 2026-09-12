---
schema: qual/card@1
id: P-XW3UP
kind: problem
title: Stabilizer of a point in the unit disk under conformal automorphisms
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
What is the stabilizer of a point $z_0 \in \mathbb{D}$ in the open unit disk under the group of conformal automorphisms $\operatorname{Aut}(\mathbb{D})$?
Describe the group structure and express the automorphisms explicitly.
:::

::: solution
Let
\[
\phi_{z_0}(z)=\frac{z-z_0}{1-\overline{z_0}z}.
\]
Then $\phi_{z_0}\in\operatorname{Aut}(\mathbb D)$ and $\phi_{z_0}(z_0)=0$.

By Schwarz's lemma, an automorphism of $\mathbb D$ fixing $0$ has the form
\[
z\longmapsto e^{i\theta}z.
\]
Hence
\[
\operatorname{Stab}_{\operatorname{Aut}(\mathbb D)}(0)
=\{z\mapsto e^{i\theta}z\}
\cong U(1).
\]
Conjugating by $\phi_{z_0}$ gives
\[
\operatorname{Stab}(z_0)
=\phi_{z_0}^{-1}\,U(1)\,\phi_{z_0}.
\]
Thus every element of the stabilizer is
\[
f_\theta(z)
=\phi_{z_0}^{-1}\!\left(e^{i\theta}\phi_{z_0}(z)\right),
\]
and
\[
\boxed{\operatorname{Stab}(z_0)\cong U(1)\cong SO(2)}.
\]
:::
