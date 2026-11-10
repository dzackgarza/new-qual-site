---
schema: qual/card@1
id: E-OR2SV
kind: problem
title: No two of the unit interval variants are homeomorphic
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §24 Exercise 1, printed p. 157, with Theorem 24.1
    and Example 4; the three parts and the bracketed hint are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 24.1, PDF p. 3. Three spaces are distinguished by
    how many points must be removed to disconnect them: one, two and none; and the halving
    maps give imbeddings (0,1) to (0,1] and back without a homeomorphism, and remove a point
    from R^n minus the origin versus R minus a point in (c). (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

(a) Show that no two of the spaces $(0, 1)$, $(0, 1]$, and $[0, 1]$ are homeomorphic.
[Hint: What happens if you remove a point from each of these spaces?]

(b) Suppose that there exist imbeddings $f: X \to Y$ and $g: Y \to X$.
Show by means of an example that $X$ and $Y$ need not be homeomorphic.

(c) Show that $\RR^n$ and $\RR$ are not homeomorphic if $n > 1$.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 24.1, PDF p. 3** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); the three parts are theirs.

(a) Removing one point from $(0,1)$ leaves a disconnected space; removing the endpoints from $[0,1]$ leaves the connected set $(0,1)$. So if $h:[0,1]\to(0,1]$ were a homeomorphism, its restriction $h'$ to the complement of $h^{-1}(h(0))$ would carry the connected space $(0,1)$ onto $(0,1]-\{h(0)\}$, which is disconnected (a union of two intervals separated by the missing point): contradiction. The same argument separates $(0,1)$ from each of $(0,1]$ and $[0,1]$, since those two have a point whose removal disconnects them.

(b) $f:(0,1)\to(0,1]$, $f(x)=x/2$, is continuous and injective, and its restriction to its image is a homeomorphism onto $(0,1/2)$ with inverse $y\mapsto2y$; so $f$ is an imbedding. Likewise $g:(0,1]\to(0,1)$, $g(x)=x/2$. But $(0,1)$ and $(0,1]$ are not homeomorphic by (a).

(c) If $f:\RR^{n}\to\RR$ were a homeomorphism with $n>1$, the restriction $\RR^{n}-\{0\}\to\RR-\{f(0)\}$ would be a homeomorphism, and $\RR^{n}-\{0\}$ is connected (Example 4 of §24) while $\RR-\{f(0)\}$ is disconnected. So no such homeomorphism exists.
:::
