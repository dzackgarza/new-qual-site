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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the passage from the space-filling curve of
    Exercise 44.1 (card E-SADP0) to a surjection of [2m-1,2m] onto [-m,m]^n, the pairwise
    disjointness and closedness of the intervals with the local finiteness of the family,
    continuity of the pasted map by Section 18 Exercise 9(c), and both routes to a map on
    all of R: Tietze on the n coordinate functions (R normal by Theorem 32.2, S closed) and
    the explicit piecewise-linear filling. The argument is the card's own; no retained set
    covers this exercise. No repair needed.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The solution section said "the argument is the card's own; no retained solution set covers this
    exercise", contradicting the card's own solution-written event of 2026-11-11, which records the
    transcription from Zinger's Problem Set 7 solution of Munkres §44 Exercise 2 (p. 274), PDF p. 2,
    and names what was adapted. The retained file was re-read and does carry that construction. The
    solution section now names the set and the adaptations. The earlier note is left as written; this
    event is the correction.
---

::: {.exercise}

Show there is a continuous surjective map $f: \RR \to \RR^n$.
:::

::: {.solution}
The argument is transcribed from the retained solution of Aleksey Zinger, *MAT 530: Topology & Geometry, I*, Fall 2005, Problem Set 7, "Solution to Problem p274, #2", PDF p. 2 (`tmp/sources/munkres-solutions-zinger-mat530-ps7.pdf`), which builds a continuous surjection of $[2m-1,2m]$ onto $[-m,m]^{n}$ for each $m$, pastes these, and extends to $\RR$. Its one input from the book is the space-filling curve of §44: by [[E-SADP0]], which is Exercise 44.1 obtained from Theorem 44.1, the cube $I^{n}$ is a continuous image of $I$. Where the card departs from Zinger: he extends by Tietze's theorem applied to the coordinates of the pasted map, and the card states that theorem by number, and it records his remark that the extension may be taken linear over each gap and constant on $(-\infty,1]$.

::: pf

::: {.pf-step #block}
For each $m\ge1$ there is a continuous surjection $f_{m}:[2m-1,2m]\to[-m,m]^{n}$.

::: pf-proof
By [[E-SADP0]] there is a continuous surjection $I\to I^{n}$, with $I=[0,1]$. The affine maps $[2m-1,2m]\to I$ and $I^{n}\to[-m,m]^{n}$ are homeomorphisms, so composing gives a continuous surjection of $[2m-1,2m]$ onto $[-m,m]^{n}$.
:::

:::

::: {.pf-step #cover}
With $S=\bigcup_{m\ge1}[2m-1,2m]$, the family $\{[2m-1,2m]\mid m\ge1\}$ is a locally finite closed cover of $S$, and $\tilde f:S\to\RR^{n}$ defined by $\tilde f(t)=f_{m}(t)$ for $t\in[2m-1,2m]$ is a well-defined continuous surjection onto $\RR^{n}$.

::: pf-proof
The intervals $[2m-1,2m]$ are pairwise disjoint, since $2m<2(m+1)-1$, so $\tilde f$ is well defined; each is closed in $\RR$, so each is closed in $S$; and the family is locally finite, because a neighbourhood of a point $t$ contained in an interval of length less than $1$ around $t$ meets at most two of them. Hence $\tilde f$ is continuous by Munkres §18 Exercise 9(c). It is onto: $\tilde f(S)=\bigcup_{m\ge1}[-m,m]^{n}=\RR^{n}$.
:::

:::

::: {.pf-step #tietze}
There is a continuous surjection $g:\RR\to\RR^{n}$ extending $\tilde f$.

::: pf-proof
$\RR$ is metrizable, hence normal (Theorem 32.2), and $S$ is closed in $\RR$, being the complement of the open set $(-\infty,1)\cup\bigcup_{m\ge1}(2m,2m+1)$. Each of the $n$ coordinate functions of $\tilde f$ is continuous and real valued on the closed subspace $S$, so by the Tietze theorem (Theorem 35.1(b)) it extends to a continuous function on $\RR$; assembling the $n$ extensions gives a continuous $g:\RR\to\RR^{n}$ with $g\restrict_{S}=\tilde f$. Then $g(\RR)\supset g(S)=\tilde f(S)=\RR^{n}$, so $g$ is onto.
:::

:::

::: {.pf-step #explicit}
The same conclusion holds without Tietze's theorem, by an explicit piecewise-linear filling.

::: pf-proof
Set $g(t)=f_{1}(1)$ for $t\le1$; set $g(t)=f_{m}(t)$ for $t\in[2m-1,2m]$; and on each gap $[2m,2m+1]$ let $g$ run linearly from $f_{m}(2m)$ to $f_{m+1}(2m+1)$. The closed sets $(-\infty,1]$, $[2m-1,2m]$ and $[2m,2m+1]$ form a locally finite cover of $\RR$ on which $g$ is defined and continuous, agreeing on overlaps, so $g$ is continuous by Munkres §18 Exercise 9(c); and $g$ still maps $S$ onto $\RR^{n}$, hence is onto.
:::

:::

::: {.pf-step}
There is a continuous surjective map $f:\RR\to\RR^{n}$.

::: pf-proof
Step [](#tietze){.pf-ref} produces one through the Tietze theorem, and step [](#explicit){.pf-ref} produces one by an explicit formula; either answers the exercise.
:::

:::

:::
:::
