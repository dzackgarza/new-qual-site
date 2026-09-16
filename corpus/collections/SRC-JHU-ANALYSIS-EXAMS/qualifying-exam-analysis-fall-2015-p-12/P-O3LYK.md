---
schema: qual/card@1
id: P-O3LYK
kind: problem
title: "Uniform approximation on the boundary preserves the zero count"
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the boundary nonvanishing and multiplicity convention with Fall 2015 problem 4 in the retained JHU extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the explicit approximation threshold, finiteness of the zero counts, and every hypothesis of Rouche's theorem on the translated disk."
---

::: {.problem}
4. Let $U \subset \mathbb { C }$ be an open set containing $\overline { { \boldsymbol { D } } } ( \boldsymbol { P } , \boldsymbol { r } )$ . Prove that if $f : U \to \mathbb { C }$ is a holomorphic function such that $f$ is nowhere zero on $\partial D ( P , r )$ and $g : U \to \mathbb { C }$ is a holomorphic function sufficiently uniformly close to $f$ on $\partial D ( P , r )$ , then the number of zeros of $f$ in $D ( P , r )$ equals the number of zeros of g in $D ( P , r )$ (counting multiplicity).
:::

::: solution
<1>1. Boundary nonvanishing gives a positive approximation threshold.

::: proof
Write $D=D(P,r)$ and $C=\partial D$. Continuity of $f$
and compactness of $C$ imply that
$$
\delta=\min_{z\in C}|f(z)|>0.
$$
It suffices to require $\sup_C|g-f|<\delta$. For such a $g$,
$$
|g(z)-f(z)|<\delta\leq|f(z)|\qquad(z\in C).
$$
In particular $|g(z)|\geq|f(z)|-|g(z)-f(z)|>0$ on $C$.
:::

<1>2. The two finite zero counts agree, with multiplicities.

::: proof
Both $f$ and $g$ are holomorphic on the open neighborhood
$U$ of $\overline D$. The strict boundary inequality in
step <1>1 allows Rouché's theorem to be applied to $f$
and the perturbation $g-f$. It gives the same number of
zeros for $f$ and $f+(g-f)=g$ inside $C$, counted with
multiplicity [@SS03, Chapter 3, Theorem 4.3].

These counts are finite. Neither function is identically
zero on the component containing the disk, since neither
vanishes on its boundary. Infinitely many distinct zeros
in $\overline D$ would have an accumulation point in that
compact subset of $U$, contradicting the identity theorem.
Every zero has finite multiplicity by its local Taylor
expansion [@SS03]. Thus the equality is of precisely the
finite multiplicity counts requested.
:::
:::
