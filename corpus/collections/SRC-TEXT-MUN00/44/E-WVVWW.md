---
schema: qual/card@1
id: E-WVVWW
kind: problem
title: Continuous surjections from $\RR$ onto $\RR^n$
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: Aleksey Zinger, "MAT 530: Topology & Geometry, I",
    Fall 2005, Problem Set 7, "Solution to Problem p274, #2", PDF p. 2
    (tmp/sources/munkres-solutions-zinger-mat530-ps7.pdf, from
    https://www.math.stonybrook.edu/~azinger/mat530/ps7sol.pdf; the sheet prints no page numbers, so the
    PDF page is the locator; the course page lists this problem as p272 #2, which is the sheet's own
    misprint of the book's p. 274). Checked against Munkres, Topology (2000), §44 Exercise 2, printed
    p. 274, with Theorem 44.1 (the Peano curve), Exercise 44.1 for the passage to n coordinates,
    Theorem 18.3 and Exercise 18.9(c) for the pasting of a locally finite closed cover, Theorem 32.2 for
    the normality of a metrizable space, and Theorem 35.1(b). The construction is Zinger's: a continuous
    surjection f_m of [2m-1, 2m] onto [-m, m]^n for each m, the union of these intervals being a closed
    subset S of R, then the pasting of the f_m to a surjection of S onto R^n and its extension to R. What
    was adapted: Zinger extends by Tietze's theorem applied to the coordinates of the pasted map, which
    the card states with the theorem number, and the card also records his own remark that the extension
    can be made linearly over each gap [2m, 2m+1] and constantly on (-infinity, 1], in which case the
    continuity is that of a locally finite closed cover. What the card no longer uses is its earlier
    construction, which reparametrized each q_m to start and end at the origin and pasted at the integers;
    that construction is correct, but the sheet's is the located proof and stops at one composition fewer.
---

::: {.exercise}

Show there is a continuous surjective map $f: \RR \to \RR^n$.
:::

::: {.solution}
By [[E-SADP0]], which is Exercise 44.1 from Theorem 44.1, the cube $I^n$ is a continuous image of $I$; composing with the homeomorphisms $[2m-1,2m]\cong I$ and $I^n\cong[-m,m]^n$ gives, for each $m\ge1$, a continuous surjection
$$
f_m:[2m-1,2m]\longrightarrow[-m,m]^n .
$$

The intervals $[2m-1,2m]$, $m\ge1$, are pairwise disjoint, and their union
$$
S=\bigcup_{m\ge1}[2m-1,2m]
$$
is closed in $\RR$. Define $\tilde f:S\to\RR^n$ by $\tilde f(t)=f_m(t)$ for $t\in[2m-1,2m]$. The family is a locally finite closed cover of $S$, so $\tilde f$ is continuous (Exercise 18.9(c)), and it is surjective because
$$
\tilde f(S)=\bigcup_{m\ge1}[-m,m]^n=\RR^n .
$$

The space $\RR$ is metrizable, hence normal (Theorem 32.2), and $S$ is closed in it. Tietze's theorem (Theorem 35.1(b)) applied to the $n$ coordinate functions of $\tilde f$ extends $\tilde f$ to a continuous map $g:\RR\to\RR^n$. Since $g$ agrees with $\tilde f$ on $S$, its image contains $\tilde f(S)=\RR^n$, so $g$ is a continuous surjection.

The same map can be written without Tietze's theorem, as the sheet cited below remarks: set $g(t)=f_1(1)$ for $t\le1$, let $g$ agree with $f_m$ on $[2m-1,2m]$, and let $g$ map each gap $[2m,2m+1]$ linearly onto the segment from $f_m(2m)$ to $f_{m+1}(2m+1)$. The family of closed sets $(-\infty,1]$, $[2m-1,2m]$, $[2m,2m+1]$ is again locally finite, so Exercise 18.9(c) gives continuity, and surjectivity is unchanged.
:::
