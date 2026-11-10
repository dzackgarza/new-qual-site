---
schema: qual/card@1
id: E-P5AAV
kind: problem
title: '$\RR/\ZZ$ as a familiar topological group'
classification:
  areas:
  - topology
  topics:
  - Topological Groups
  - Quotient Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 6, printed p. 146,
    with Corollary 22.3; the stored statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.6, printed p. 270.
    The identification is his: t -> e^{2 pi i t} is a continuous open surjection whose
    fibres are the cosets of Z, so Corollary 22.3 gives a homeomorphism R/Z -> S^1, which is
    a group isomorphism because the map is a homomorphism. (tmp/sources/munkres-solutions-
    whitman.pdf).
---

::: {.exercise}

The integers $\ZZ$ are a normal subgroup of $(\RR, +)$.
The quotient $\RR/\ZZ$ is a familiar topological group; what is it?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.6, printed p. 270** (`tmp/sources/munkres-solutions-whitman.pdf`); the identification is his.

The quotient $\RR/\ZZ$ of the additive group $\RR$ by the subgroup $\ZZ$ is the circle group $S^{1}=\{z\in\CC\mid\abs z=1\}$ with multiplication.

Consider $q:\RR\to S^{1}$, $q(t)=e^{2\pi it}=(\cos 2\pi t,\ \sin 2\pi t)$, which is continuous and surjective. Its fibres are exactly the cosets of $\ZZ$:
$$
q(s)=q(t)\iff s-t\in\ZZ\iff s+\ZZ=t+\ZZ,
$$
that is, $q^{-1}(\{q(t)\})=t+\ZZ$. Moreover $q$ is open: the images of the intervals $(a,b)$ form a basis of the topology of $S^{1}$ (for $b-a\le1$ the set $q((a,b))$ is an open arc, and the open arcs form a basis), so the image of an open set, a union of intervals, is open.

Hence $q$ is a surjective continuous map with the fibres $q^{-1}(\{z\})$ equal to the cosets, and it is a quotient map because it is open. By Corollary 22.3 (printed p. 142) the induced bijection $f:\RR/\ZZ\to S^{1}$, $f(t+\ZZ)=q(t)$, is a homeomorphism, and it is a group homomorphism since $q(s+t)=q(s)q(t)$. So $\RR/\ZZ\cong S^{1}$ as topological groups.
:::
