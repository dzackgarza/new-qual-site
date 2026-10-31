---
schema: qual/card@1
id: E-HAT-2.2-35
kind: problem
title: Nonorientable surface or complex with torsion in $H_1$ cannot embed in $\RR^3$ with mapping cylinder neighborhood
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mayer-Vietoris
  - Surfaces
  - Embeddings
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Use the Mayer–Vietoris sequence to show that a nonorientable closed surface, or more generally a finite simplicial complex $X$ for which $H_1(X)$ contains torsion, cannot be embedded as a subspace of $\RR^3$ in such a way as to have a neighborhood homeomorphic to the mapping cylinder of some map from a closed orientable surface to $X$.
[This assumption on a neighborhood is in fact not needed if one deduces the result from Alexander duality in §3.3.]
:::

::: {.solution}
Suppose such an embedding and neighborhood $N$ exist. The mapping cylinder of $f:S\to X$ deformation retracts onto $X$, so $H_1(N)\cong H_1(X)$. Its complement of the base $X$ is the cylinder $S\times[0,1)$, and hence
$$
H_1(N\setminus X)\cong H_1(S).
$$

Because $X$ is compact, it is closed in $\RR^3$. The sets $N$ and $\RR^3\setminus X$ form an excisive cover of $\RR^3$: $N$ contains a neighborhood of every point of $X$, while $\RR^3\setminus X$ is open. The Mayer--Vietoris sequence therefore contains
$$
0=H_2(\RR^3)
\longrightarrow H_1(N\setminus X)
\longrightarrow H_1(N)\oplus H_1(\RR^3\setminus X)
\longrightarrow H_1(\RR^3)=0.
$$
Thus $H_1(S)\cong H_1(X)\oplus H_1(\RR^3\setminus X)$. Since $S$ is a closed orientable surface, $H_1(S)$ is free abelian. Its direct summand $H_1(X)$ is also free abelian, contrary to the torsion hypothesis. A nonorientable closed surface has torsion in $H_1$, so it is included in this conclusion.
:::
