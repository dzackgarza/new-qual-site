---
schema: qual/card@1
id: P-VTB25
kind: problem
title: Even-degree orientable covers of non-orientable manifolds, and $\pi_1$ without
  index-$2$ subgroups
classification:
  areas:
  - topology
  topics:
  - Orientation
  - Covering Spaces
  - Manifolds
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
Let $M$ be a connected topological manifold.
(1) Prove that if $\widetilde{M}$ is an orientable connected manifold and $p: \widetilde{M} \to M$ is a $k$-fold covering map onto a **non-orientable** manifold $M$, then the covering degree $k$ must be **even** (or infinite).
(2) Prove that if $\pi_1(M)$ has no subgroup of index $2$, then $M$ must be **orientable**.
:::

::: solution
Let
$$
w:\pi_1(M)\longrightarrow\{\pm1\}\cong\mathbb Z/2
$$
be the orientation character. Since $M$ is connected, it is orientable exactly when $w$ is trivial.

<1>1. Suppose $M$ is non-orientable and $p:\widetilde M\to M$ is a connected covering with $\widetilde M$ orientable. Put
$$
H=p_*\pi_1(\widetilde M)\le\pi_1(M).
$$
Then
$$
H\subseteq\ker w.
$$
::: proof
A loop in $\widetilde M$ preserves the orientation of $\widetilde M$. Its projection therefore has trivial orientation monodromy in $M$, so its class lies in $\ker w$.
:::

<1>2. Since $M$ is non-orientable, $w$ is surjective, so
$$
[\pi_1(M):\ker w]=2.
$$
Thus, when the covering has finite degree,
$$
k=[\pi_1(M):H]
=[\pi_1(M):\ker w]\,[\ker w:H]
=2[\ker w:H],
$$
so $k$ is even. If $[\ker w:H]$ is infinite, then the covering has infinitely many sheets.

<1>3. If $\pi_1(M)$ has no subgroup of index $2$, then $M$ is orientable.
::: proof
If $M$ were non-orientable, the surjective orientation character would have kernel of index $2$, contradicting the hypothesis.
:::
:::
