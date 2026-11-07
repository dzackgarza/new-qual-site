---
schema: qual/card@1
id: E-HAT-3.3-4
kind: problem
title: Quotients by orientation-preserving actions
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.3, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.3, Exercise 4; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the construction: the orientation of a sheet is transported to the quotient, and the only
    ambiguity is a deck transformation, which is orientation-preserving by hypothesis, so the
    transported orientation is well defined.
- event: solution-written
  by: claude
  date: 2026-11-07
  note: >-
    Source-backed rewrite from the Math 538 homework solutions, HMW 3 handwritten page 2 (PDF page
    14), Hatcher 3.3 #4: the solution now runs that proof — disjointness of the translates of a ball,
    an orientation-preserving deck transformation carrying mu_x to mu_gx, the two excisions
    H_n(M,M-x) = H_n(B_x,B_x-x) = H_n(B_(x),B_(x)-(x)) = H_n(M/G, M/G-(x)), and the inherited local
    consistency. Checked against Hatcher p.72 for the covering space action and p.233 for the local
    homology notation. The sheet names the course and host only, so no author is attributed.

---

::: {.problem}
Given a covering space action of a group $G$ on an orientable manifold $M$ by orientation-preserving homeomorphisms, show that $M/G$ is also orientable.
:::

::: {.solution}
Let $q:M\to M/G$ be the quotient map; since the action is a covering space action, $q$ is a covering map and $M/G$ is an $n$-manifold.

Fix $x\in M$ and let $B_x$ be a ball around $x$ small enough that the translates $gB_x$, $g\in G$, are pairwise disjoint — this is what a covering space action gives (Hatcher, p. 72). Let $\mu_x\in H_n(M,M-\{x\})$ be the given orientation class. Since every $g$ is orientation preserving, the induced isomorphism $g_*:H_n(M,M-\{x\})\to H_n(M,M-\{gx\})$ carries $\mu_x$ to $\mu_{gx}$; and by the local consistency of $\mu$, the class $\mu_{B_x}\in H_n(M\,|\,B_x)$ restricts to $\mu_y$ for every $y\in B_x$.

Now $q$ restricts to a homeomorphism $B_x\to B_{(x)}$ onto the image of the ball, so excision (in the form $H_n(X\,|\,A)$ of p. 233) gives
$$
H_n(M,M-\{x\})\cong H_n(B_x,B_x-\{x\})\cong H_n(B_{(x)},B_{(x)}-\{(x)\})\cong H_n(M/G,M/G-\{(x)\}),
$$
and the class $\mu_{(x)}$ defined as the image of $\mu_x$ is well defined: any other preimage of $(x)$ in the orbit is $gx$ with $g\in G$, and $\mu_{gx}$ is the image of $\mu_x$ under the orientation-preserving $g_*$, so it maps to the same class downstairs.

Local consistency downstairs is inherited: for $y\in B_x$ the class $\mu_{B_x}$ restricts to $\mu_y$ upstairs, so its image restricts to $\mu_{(y)}$ in $B_{(x)}$. Hence $y\mapsto\mu_{(y)}$ is an orientation of $M/G$, and $M/G$ is orientable.

This is the solution printed in the Math 538 homework solutions, HMW 3, handwritten page 2 (PDF page 14 of `tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher 3.3 #4: the same disjointness of translates, the observation that an orientation-preserving $g$ sends $\mu_x$ to $\mu_{gx}$, both excisions, and the conclusion "local consistency holds in $B_{(x)}$ since it holds in $B_x$".
:::
