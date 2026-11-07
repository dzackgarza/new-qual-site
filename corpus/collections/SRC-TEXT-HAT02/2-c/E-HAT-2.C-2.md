---
schema: qual/card@1
id: E-HAT-2.C-2
kind: problem
title: 'Lefschetz fixed point theorem: map $S^n \to S^n$ has fixed point unless degree equals antipodal degree'
classification:
  areas:
  - topology
  topics:
  - Lefschetz Fixed Point Theorem
  - Degree
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §2.C Exercise 2, printed page
    184; the statement matches word for word. Proof checked: deg of the antipodal
    map is (-1)^{n+1} (Proposition 2.30, p. 134, as n+1 coordinate reflections), the
    Lefschetz number of f: S^n → S^n is 1 + (-1)^n d since f_* is the identity on
    H_0 and multiplication by d on H_n, and it vanishes exactly when d = (-1)^{n+1};
    Theorem 2C.3 (Lefschetz fixed point theorem, stated p. 179, proved p. 180) then
    gives a fixed point otherwise. The case n = 0 is handled separately, where the
    only fixed-point-free self-map is the antipodal one, of degree -1. No defect.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Uses the published proof by Kenneth DeMason, M382C Full Credit HW Problems (2021), Hatcher
    2.C.2, printed p.84. Every simplex of the approximation has zero reduced homology except in top
    degree, the identity on H_0 comes from path-connectedness with vertices joined by 1-simplices,
    and f_* on H_n is multiplication by d. Hence Lambda(f)=1+(-1)^n d for n>=1; zero exactly means
    d=(-1)^{n+1}, equal to the antipodal degree. The two-point case n=0 is covered by its only
    fixed-point-free map, the antipodal transposition, rather than by applying that formula.

---

::: {.problem}
Use the Lefschetz fixed point theorem to show that a map $f: S^n \to S^n$ has a fixed point unless its degree is equal to the degree of the antipodal map $x \mapsto -x$.
:::

::: {.solution}
Let $a(x)=-x$ denote the antipodal map, and let $d=\deg f\in\ZZ$.

::: pf

::: {.pf-step #s1}

$\deg a=(-1)^{n+1}$.

::: pf-proof

Write $a$ as the composite of the $n+1$ coordinate reflections. A reflection in one coordinate has degree $-1$, so composition gives $(-1)^{n+1}$.
:::

:::

::: {.pf-step #s2}

After applying simplicial approximation, the Lefschetz number of $f$ is $\Lambda(f)=1+(-1)^n d$ for $n\ge1$.

::: pf-proof

Triangulate $S^n$ as a finite simplicial complex. The simplicial approximation theorem asserts that after further barycentric subdivision $f$ is homotopic to a simplicial map; homotopy preserves both degree and Lefschetz number, so I compute for that approximation. As DeMason argues on p. 84, for a path-connected simplicial complex every vertex lies in the same $H_0$ class: a $1$-simplex joining them has boundary their difference. So a simplicial map induces the identity on $H_0$ and has trace $1$ there. In the remaining dimension the homology of a sphere is zero unless $k=n$, and there the induced map is multiplication by $d$. Therefore
$$
\Lambda(f)=1+(-1)^n d.
$$
:::

:::

::: {.pf-step #degzero}

If $d\ne(-1)^{n+1}$, then $f$ has a fixed point.

::: pf-proof

For $n\ge1$, the Lefschetz fixed-point theorem applies to $S^n$. Were there no fixed point,
$$0=\Lambda(f)=1+(-1)^n d,$$
which exactly means $d=(-1)^{n+1}$. For $n=0$ no such formula in $H_0$ is needed: $S^0$ has two points, and the only self-map with no fixed point is their transposition, precisely the antipodal map.
:::

:::

:::


This is **Kenneth DeMason's argument in *M382C Full Credit HW Problems* (2021)**, Hatcher 2.C.2, printed p. 84 of the local file `tmp/sources/demason-m382c-hatcher-20210404.pdf` ([author's PDF](https://math.mcmaster.ca/~demasonk/files/exercises/DeMason%2C%20Kenneth%20M382C%20HW%20Full%20Credit%2020210404.pdf)). The central facts are that $H_0$ contributes trace $1$, $H_n$ contributes $(-1)^n d$ because $f_*$ is multiplication by $d$, and the antipodal degree comes from composition of reflections.
:::

