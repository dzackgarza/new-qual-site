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
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 2.2, Exercise 35.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the argument: the mapping cylinder retracts to $X$ and its complement of the base is
    $S\times[0,1)$; the open mapping cylinder and the open complement of the compact $X$ form an
    excisive cover of $\RR^3$, and Mayer-Vietoris gives
    $H_1(S)\cong H_1(X)\oplus H_1(\RR^3\setminus X)$, so $H_1(X)$ is a direct summand of a free
    group and cannot have torsion.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 35 as printed on p. 158, bracketed remark included. The argument is
    correct and now cites its inputs: Corollary 2.11 p. 111 for H_1(N) = H_1(X) from the
    deformation retraction of the mapping cylinder, the Mayer-Vietoris sequence of pp. 149-150,
    Example 2.36 p. 141 for H_1 of a closed orientable surface being free, and Example 2.37
    p. 141 for the Z_2 summand of a nonorientable one. Added the missing finiteness: H_1(X) is
    finitely generated because X is a finite simplicial complex, which is what makes a direct
    summand of a free abelian group free. What is not covered: N is treated as open (the
    mapping cylinder itself has a boundary), and the bracketed Alexander-duality remark is not
    proved.
---

::: {.problem}
Use the Mayer–Vietoris sequence to show that a nonorientable closed surface, or more generally a finite simplicial complex $X$ for which $H_1(X)$ contains torsion, cannot be embedded as a subspace of $\RR^3$ in such a way as to have a neighborhood homeomorphic to the mapping cylinder of some map from a closed orientable surface to $X$.
[This assumption on a neighborhood is in fact not needed if one deduces the result from Alexander duality in §3.3.]
:::

::: {.solution}
Suppose such an embedding and neighborhood $N$ exist. The mapping cylinder of $f:S\to X$ deformation retracts onto $X$, so the deformation retraction induces $H_1(N)\cong H_1(X)$ by Corollary 2.11 (p. 111). Its complement of the base $X$ is the cylinder $S\times[0,1)$, and hence
$$
H_1(N\setminus X)\cong H_1(S).
$$

Because $X$ is compact, it is closed in $\RR^3$. The sets $N$ and $\RR^3\setminus X$ form an excisive cover of $\RR^3$: $N$ contains a neighborhood of every point of $X$, while $\RR^3\setminus X$ is open. The Mayer--Vietoris sequence of pp. 149--150 therefore contains
$$
0=H_2(\RR^3)
\longrightarrow H_1(N\setminus X)
\longrightarrow H_1(N)\oplus H_1(\RR^3\setminus X)
\longrightarrow H_1(\RR^3)=0.
$$
Thus $H_1(S)\cong H_1(X)\oplus H_1(\RR^3\setminus X)$. Since $S$ is a closed orientable surface, $H_1(S)$ is free abelian, being $\ZZ^{2g}$ for a surface of genus $g$ by Example 2.36 (p. 141). The group $H_1(X)$ is finitely generated because $X$ is a finite simplicial complex, and a finitely generated direct summand of a free abelian group is free abelian. Hence $H_1(X)$ is free abelian, contrary to the torsion hypothesis. A nonorientable closed surface has torsion in $H_1$, since $H_1(N_g)$ contains a $\ZZ_2$ summand by Example 2.37 (p. 141), so it is included in this conclusion.
:::
