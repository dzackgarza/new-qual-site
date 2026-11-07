---
schema: qual/card@1
id: E-HAT-3.3-3
kind: problem
title: Covering spaces of orientable manifolds
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: local orientation classes are pulled back along the local homeomorphism
    from a sheet over an evenly covered neighbourhood, and constancy on the sheet follows from
    constancy downstairs.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Source-backed rewrite: the solution now follows the printed solution in the Math 538 homework
    solutions, HMW 3 handwritten page 1 (PDF page 13 of hatcher-math538-homework4-solutions.pdf),
    Hatcher 3.3 #3, namely the chain of excision and local-homeomorphism isomorphisms between
    H_n(M-tilde, M-tilde minus x-tilde) and H_n(M, M minus x) and the local-compatibility step; the
    handout's argument was checked against Hatcher's definition of orientation (p.233) and Lemma
    3.27(a) (p.236), which is what makes the ball class mu_B exist and be unique. No author is
    attributed: the sheet identifies only the course (Math 538) and the host (tkmd.org).
---

::: {.problem}
Show that every covering space of an orientable manifold is an orientable manifold.
:::

::: {.solution}
Let $p:\widetilde M\to M$ be a covering map with $M$ orientable, and fix an orientation of $M$: a locally consistent choice of generator $\mu_x\in H_n(M,M-\{x\})$ for every $x$.

Take $\widetilde x\in\widetilde M$ and put $x=p(\widetilde x)$. Let $B=B_x$ be a ball around $x$ that is evenly covered by $p$, and let $\widetilde B$ be the sheet over $B$ containing $\widetilde x$, so that $p:\widetilde B\to B$ is a homeomorphism. Since $B$ is a neighbourhood of $x$ and $\widetilde B$ one of $\widetilde x$, excision in the form of Hatcher's $H_n(X\,|\,A)=H_n(X,X-A)$ (p. 233) gives isomorphisms
$$
H_n(\widetilde M,\widetilde M-\{\widetilde x\})\cong H_n(\widetilde B,\widetilde B-\{\widetilde x\})\cong H_n(B,B-\{x\})\cong H_n(M,M-\{x\}),
$$
the middle one induced by the homeomorphism $p$. So there is a unique generator $\widetilde\mu_{\widetilde x}$ of the left-hand group corresponding to $\mu_x$ on the right.

For the local consistency, let $\mu_B\in H_n(M\,|\,B)$ be the class restricting to $\mu_y$ for every $y\in B$, which exists and is unique by the local consistency of the given orientation (Lemma 3.27(a), p. 236). Transporting $\mu_B$ back along the two isomorphisms gives a class $\mu_{\widetilde B}\in H_n(\widetilde M\,|\,\widetilde B)$; for $y\in B$ and its preimage $\widetilde y\in\widetilde B$ the same construction gives $\mu_{\widetilde y}$, and the two constructions agree because both reduce to $\mu_y$ under the isomorphism onto $H_n(M,M-\{y\})$. Hence the classes $\widetilde\mu_{\widetilde y}$ are the images of the single class $\mu_{\widetilde B}$, which is exactly the local consistency condition.

Therefore the family $\widetilde x\mapsto\widetilde\mu_{\widetilde x}$ is an orientation of $\widetilde M$, and every covering space of an orientable manifold is orientable.

This is the solution printed in the Math 538 homework solutions, HMW 3, handwritten page 1 (PDF page 13 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 #3: it runs the same chain $H_n(\widetilde M,\widetilde M-\{\widetilde x\})\cong H_n(\widetilde B,\widetilde B-\{\widetilde x\})\cong H_n(B,B-\{x\})\cong H_n(M,M-\{x\})$ of excision and local homeomorphism isomorphisms and concludes "so $\mu_{\widetilde B_{x_i}}\mapsto\mu_{y_i}$ by local compatibility condition".
:::
