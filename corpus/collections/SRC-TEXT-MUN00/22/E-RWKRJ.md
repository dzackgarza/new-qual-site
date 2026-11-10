---
schema: qual/card@1
id: E-RWKRJ
kind: problem
title: Continuous maps with continuous sections are quotient maps
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Exercise 2, printed p. 144, with the
    definition of quotient map printed there; both parts are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 22.2, PDF p. 27. A continuous section makes the
    map a quotient, since U = (p o f)^{-1}(U) = f^{-1}(p^{-1}(U)); a retraction is a
    quotient map because the inclusion is a continuous section of it. (tmp/sources/munkres-
    solutions-positron-ch2.pdf).
---

::: {.exercise}

(a) Let $p: X \to Y$ be a continuous map.
Show that if there is a continuous map $f: Y \to X$ such that $p \circ f$ equals the identity map of $Y$, then $p$ is a quotient map.

(b) If $A \subset X$, a retraction of $X$ onto $A$ is a continuous map $r: X \to A$ such that $r(a) = a$ for each $a \in A$.
Show that a retraction is a quotient map.
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 22.2, PDF p. 27** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); both parts are theirs. Whitman, printed p. 252, gives the same two arguments.

(a) Let $p:X\to Y$ be continuous and let $f:Y\to X$ be continuous with $p\circ f=\mathrm{id}_{Y}$. We show $p$ is a quotient map. It is continuous and surjective ($p(f(y))=y$). If $U\subset Y$ and $p^{-1}(U)$ is open in $X$, then
$$
U=\mathrm{id}_{Y}^{-1}(U)=(p\circ f)^{-1}(U)=f^{-1}\big(p^{-1}(U)\big)
$$
is open in $Y$ because $f$ is continuous. So $U$ is open in $Y$ exactly when $p^{-1}(U)$ is open in $X$.

(b) Let $r:X\to A$ be a retraction, that is, $r$ is continuous and $r(a)=a$ for $a\in A$; regard $r$ as a map onto $A$. The inclusion $i:A\to X$ is continuous and $r\circ i=\mathrm{id}_{A}$, so by (a) with $p=r$ and $f=i$, the map $r$ is a quotient map.
:::
