---
schema: qual/card@1
id: E-B74TA
kind: problem
title: Nonabelian fundamental groups of higher projective planes
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Checked against Munkres, Topology (2000), Section 74 Exercise 7, printed p. 454. The homomorphism of the printed hint sends the relator of Theorem 74.4 to a^2b^2 = 1 in C_2*C_2 and is onto it, and C_2*C_2 is nonabelian. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

If $m > 1$, show the fundamental group of the $m$-fold projective plane is not abelian.
[Hint: There is a homomorphism mapping this group onto the group $\ZZ/2 * \ZZ/2$.]
:::

::: {.solution}
For the $m$-fold projective plane,
$$
\pi_1(P^{2\# m})\cong
\left\langle \alpha_1,\ldots,\alpha_m\ \presentationbar\
\alpha_1^2\alpha_2^2\cdots\alpha_m^2=1\right\rangle.
$$
Let
$$
D_\infty\cong C_2*C_2=\langle a,b\mid a^2=b^2=1\rangle.
$$
For $m>1$, send
$$
\alpha_1\mapsto a,\qquad \alpha_2\mapsto b,\qquad
\alpha_i\mapsto1\quad(i\ge3).
$$
The surface relator maps to $a^2b^2=1$, so this defines a surjective homomorphism
$$
\pi_1(P^{2\# m})\twoheadrightarrow C_2*C_2.
$$
The group $C_2*C_2$ is nonabelian: its reduced words $ab$ and $ba$ are distinct. Therefore the source cannot be abelian. Hence $\pi_1(P^{2\# m})$ is nonabelian for every $m>1$.
:::
