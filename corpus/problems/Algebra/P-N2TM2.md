---
schema: qual/card@1
id: P-N2TM2
kind: problem
title: Orbits, stabilizers, and kernels of the standard $G$-actions
classification:
  areas:
  - algebra
  topics:
  - Group Actions
  - Orbit-Stabilizer
  - Conjugacy
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
For each standard action below, identify the orbits, stabilizers, global fixed points, kernel, and image in the relevant symmetric group:

1. left translation of $G$ on itself;
2. conjugation of $G$ on itself;
3. conjugation of $G$ on its set of subgroups;
4. left translation of $G$ on $G/H$ for a fixed subgroup $H\le G$.
:::

::: {.solution}
<1>1. Left translation on $G$.
::: {.proof}
The action is transitive, so there is one orbit, namely $G$. The stabilizer of every $x\in G$ is trivial because
\[
gx=x\iff g=e.
\]
Hence the kernel is trivial and the image is the left regular copy of $G$ in $\Sym(G)$. If $G\ne1$, there are no global fixed points.
:::

<1>2. Conjugation on $G$.
::: {.proof}
The orbit of $x$ is its conjugacy class
\[
\operatorname{Cl}_G(x).
\]
Its stabilizer is the centralizer
\[
C_G(x).
\]
The global fixed points are exactly $Z(G)$. The kernel consists of elements conjugating every $x$ trivially, hence is also $Z(G)$. Therefore the image is
\[
\Inn(G)\cong G/Z(G).
\]
:::

<1>3. Conjugation on the set of subgroups.
::: {.proof}
The orbit of $H$ is the conjugacy class of the subgroup,
\[
\{gHg^{-1}:g\in G\}.
\]
The stabilizer is its normalizer
\[
N_G(H).
\]
The global fixed points are precisely the normal subgroups of $G$. The kernel is
\[
\bigcap_{H\le G}N_G(H),
\]
the subgroup of elements normalizing every subgroup of $G$. Thus the image is the quotient of $G$ by this kernel.
:::

<1>4. Left translation on $G/H$.
::: {.proof}
The action is transitive. The stabilizer of the coset $xH$ is
\[
xHx^{-1}.
\]
The kernel is the core of $H$,
\[
\operatorname{core}_G(H)
=\bigcap_{x\in G}xHx^{-1},
\]
the largest normal subgroup of $G$ contained in $H$. Hence the image is
\[
G/\operatorname{core}_G(H).
\]
If $H<G$, there is no global fixed coset; if $H=G$, the unique coset is fixed.
:::
:::
