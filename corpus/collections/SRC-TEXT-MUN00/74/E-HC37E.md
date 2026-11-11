---
schema: qual/card@1
id: E-HC37E
kind: problem
title: Nonabelian fundamental groups of higher-genus tori
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
    Checked against Munkres, Topology (2000), Section 74 Exercise 6, printed p. 454. The homomorphism of the printed hint sends the relator to [gamma,gamma][delta,delta]^{n-1} = 1 and is onto the nonabelian free group F(gamma,delta); checked with Theorem 74.3 and the free-group results of Section 68. No complete published solution of this exercise was located: dbFin's index ends at Section 67 and has no Chapter 12 or 13 page, 9beach stops at Chapter 4, and every set searched is listed in the COMPLAINTS.md entry for Sections 74 to 85. The proof is the card's own, checked against the book's numbered theorems.
---

::: {.exercise}

If $n > 1$, show that the fundamental group of the $n$-fold torus is not abelian.
[Hint: Let $G$ be the free group on the set $\theset{\alpha_1, \beta_1, \ldots, \alpha_n, \beta_n}$; let $F$ be the free group on the set $\theset{\gamma, \delta}$. Consider the homomorphism of $G$ onto $F$ that sends $\alpha_1$ and $\beta_1$ to $\gamma$ and all other $\alpha_i$ and $\beta_i$ to $\delta$.]
:::

::: {.solution}
For the $n$-fold torus,
$$
\pi_1(T^{\# n})\cong
\left\langle \alpha_1,\beta_1,\ldots,\alpha_n,\beta_n\ \presentationbar\
\prod_{i=1}^n[\alpha_i,\beta_i]=1\right\rangle.
$$
Let $F=F(\gamma,\delta)$ be the free group on two generators. Define a homomorphism from the free group on the surface generators by
$$
\alpha_1,\beta_1\mapsto\gamma,
\qquad
\alpha_i,\beta_i\mapsto\delta\quad(i\ge2).
$$
The defining relator maps to
$$
[\gamma,\gamma]\,[\delta,\delta]^{\,n-1}=1,
$$
so the map factors through $\pi_1(T^{\# n})$. Since $n>1$, both $\gamma$ and $\delta$ occur in the image, so the induced homomorphism onto $F(\gamma,\delta)$ is surjective. A quotient of an abelian group is abelian, while $F(\gamma,\delta)$ is nonabelian. Hence $\pi_1(T^{\# n})$ is nonabelian.
:::
