---
schema: qual/card@1
id: E-Y75ZB
kind: problem
title: A countable rational rectangle basis for the plane
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Bases
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 6, printed p. 92, with Theorem 15.1
    on printed p. 87 and Exercise 13.8(a); the collection is stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 16.6, printed p. 153.
    The reduction is his: the rational open intervals are a basis for R (Exercise 13.8(a)),
    so by Theorem 15.1 the products of two of them are a basis for the product topology on R
    x R, and that collection is exactly the one in the exercise. (tmp/sources/munkres-
    solutions-whitman.pdf).
---

::: {.exercise}

Show that the countable collection

$$
\theset{(a, b) \times (c, d) \mid a < b \text{ and } c < d, \text{ and } a, b, c, d \text{ rational}}
$$

is a basis for $\RR^2$.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 16.6, printed p. 153** (`tmp/sources/munkres-solutions-whitman.pdf`); the reduction is his.

By Exercise 13.8(a), the countable collection
$$
\mathcal{B}=\{(a,b)\mid a<b,\ a,b\in\QQ\}
$$
is a basis for the standard topology on $\RR$. By Theorem 15.1 (printed p. 87), if $\mathcal{B}$ is a basis for $X$ and $\mathcal{C}$ is a basis for $Y$, then
$$
\mathcal{D}=\{B\times C\mid B\in\mathcal{B},\ C\in\mathcal{C}\}
$$
is a basis for the product topology on $X\times Y$. Taking $X=Y=\RR$ and $\mathcal{C}=\mathcal{B}$,
$$
\mathcal{D}=\{(a,b)\times(c,d)\mid a<b,\ c<d,\ a,b,c,d\in\QQ\},
$$
which is therefore a basis for $\RR^{2}$; it is countable, being a product of two countable collections.
:::
