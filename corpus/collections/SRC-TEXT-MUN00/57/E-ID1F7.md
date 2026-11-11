---
schema: qual/card@1
id: E-ID1F7
kind: problem
title: The theorem of meteorology
classification:
  areas:
  - topology
  topics:
  - Borsuk-Ulam Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked line by line against Munkres, Topology (2000), Section 57 Exercise 1, printed p. 359,
    with Theorem 57.3, the Borsuk-Ulam theorem for $S^2$. The card applies the theorem to $F=(T,P):S^2\to\RR^2$ and reads the equality of both coordinates as equality of temperature and of pressure at the antipodal pair. No complete published solution was located for this exercise: dbFin's Chapter 9 pages run from Section 51 to Section 56 only, and every set searched is listed in the COMPLAINTS.md entry for Sections 57 to 60. The proof is the card's own and every step was checked against the book.
---

::: {.exercise}

Prove the following "theorem of meteorology": at any given moment in time, there exists a pair of antipodal points on the surface of the earth at which both the temperature and the barometric pressure are equal.
:::

::: {.solution}
Model the surface of the earth by the sphere $S^2$. Assume temperature and barometric pressure vary continuously over the surface at the fixed time in question. Define
$$
F:S^2\to\RR^2,
\qquad
F(x)=(T(x),P(x)),
$$
where $T$ is temperature and $P$ is pressure. By the Borsuk--Ulam theorem, there exists $x\in S^2$ such that
$$
F(x)=F(-x).
$$
Equality of the two coordinates gives
$$
T(x)=T(-x),\qquad P(x)=P(-x).
$$
Thus the antipodal points $x$ and $-x$ have both the same temperature and the same barometric pressure.
:::
