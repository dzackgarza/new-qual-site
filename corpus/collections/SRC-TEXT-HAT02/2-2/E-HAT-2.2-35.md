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
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: the mapping cylinder retracts onto $X$
    and its complement is $S\times[0,1)$, giving $H_1(N)\cong H_1(X)$ and $H_1(N\setminus X)\cong H_1(S)$;
    $X$ compact makes it closed, so $N$ and $\RR^3\setminus X$ are excisive with intersection
    $N\setminus X$; Mayer--Vietoris with $\RR^3$ contractible yields the splitting
    $H_1(S)\cong H_1(X)\oplus H_1(\RR^3\setminus X)$; and $H_1(S)=\ZZ^{2g}$ is free, so the finitely
    generated summand $H_1(X)$ is free. Added: the contractibility of $\RR^3$ as the reason the two
    outer groups vanish, the finite generation of $H_1(X)$ as the reason the summand is free, and
    the explicit note that the bracketed Alexander-duality remark is not proved here. The earlier
    audit's caveat that $N$ is treated as open (the mapping cylinder has a boundary) stands and is
    not repaired in this batch. No defect found in the statement, §2.2 Exercise 35. No retained
    solution set covers it.
---

::: {.problem}
Use the Mayer–Vietoris sequence to show that a nonorientable closed surface, or more generally a finite simplicial complex $X$ for which $H_1(X)$ contains torsion, cannot be embedded as a subspace of $\RR^3$ in such a way as to have a neighborhood homeomorphic to the mapping cylinder of some map from a closed orientable surface to $X$.
[This assumption on a neighborhood is in fact not needed if one deduces the result from Alexander duality in §3.3.]
:::

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own; it is the Mayer--Vietoris computation of the printed hint. Suppose $X$ embeds in $\RR^3$ with a neighbourhood $N$ homeomorphic to the mapping cylinder of a map $f\colon S\to X$ from a closed orientable surface $S$.

::: pf

::: {.pf-step #pieces}
$H_1(N)\cong H_1(X)$ and $H_1(N\setminus X)\cong H_1(S)$.

::: pf-proof
The mapping cylinder of $f$ deformation retracts onto its base $X$, and homotopy equivalent spaces have isomorphic homology (Corollary 2.11); so $H_1(N)\cong H_1(X)$. The complement of the base in the mapping cylinder is $S\times[0,1)$, which deformation retracts onto $S\times\{0\}=S$, so $H_1(N\setminus X)\cong H_1(S)$.
:::

:::

::: {.pf-step #mayer-vietoris}
There is an exact sequence $0=H_2(\RR^3)\to H_1(N\setminus X)\to H_1(N)\oplus H_1(\RR^3\setminus X)\to H_1(\RR^3)=0$, hence $H_1(S)\cong H_1(X)\oplus H_1(\RR^3\setminus X)$.

::: pf-proof
$X$ is compact, hence closed in $\RR^3$, so $\RR^3\setminus X$ is open; $N$ contains a neighbourhood of every point of $X$, so $N$ and $\RR^3\setminus X$ are an excisive cover of $\RR^3$ with intersection $N\setminus X$. Mayer--Vietoris (pp. 149--150) gives the exact sequence displayed, with $H_2(\RR^3)=H_1(\RR^3)=0$ because $\RR^3$ is contractible; a short exact sequence with vanishing ends is an isomorphism, so $H_1(N\setminus X)\cong H_1(N)\oplus H_1(\RR^3\setminus X)$. Substituting step [](#pieces){.pf-ref} gives the stated splitting.
:::

:::

::: {.pf-step #free}
$H_1(S)$ is free abelian, and $H_1(X)$ is a finitely generated direct summand of it.

::: pf-proof
$S$ is a closed orientable surface, so $H_1(S)\cong\ZZ^{2g}$ for its genus $g$, by the computation of Example 2.36; in particular it is free abelian. By step [](#mayer-vietoris){.pf-ref} the group $H_1(X)$ is a direct summand of $H_1(S)$, and it is finitely generated because $X$ is a finite simplicial complex. A finitely generated direct summand of a free abelian group is free abelian.
:::

:::

::: {.pf-step}
$\boxed{\text{No such embedding exists when }H_1(X)\text{ has torsion}}$.

::: pf-proof
Under the hypotheses of the exercise, step [](#free){.pf-ref} makes $H_1(X)$ free abelian, contradicting the assumption that $H_1(X)$ contains torsion. A nonorientable closed surface has torsion in $H_1$, since $H_1(N_g)$ has a $\ZZ_2$ summand by Example 2.37, so the stated case of a nonorientable closed surface is included. The bracketed remark that Alexander duality in §3.3 removes the hypothesis on the neighbourhood is recorded and not proved here.
:::

:::

:::
:::
