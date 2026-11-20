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

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the orientability of the quotient, which is what Queue D asks for on this card. The quotient-map step, the orientation classes upstairs, the well-definedness of the descended class and the inherited local consistency are separate steps; the well-definedness step is the one the prose asserted in a clause, and it now records that q o g = q is what makes two representatives of the orbit give the same class. A trailing paragraph that repeated the citation after the proof, outside any block, is folded into the lead sentence. No statement repair; the exercise is Hatcher §3.3 Exercise 4, printed p. 257, and the covering-space-action definition cited is on printed p. 72, both checked against the book. The argument is the Math 538 sheet's (HMW 3, handwritten p. 2 = PDF p. 14).
---

::: {.problem}
Given a covering space action of a group $G$ on an orientable manifold $M$ by orientation-preserving homeomorphisms, show that $M/G$ is also orientable.
:::

::: {.solution}
The published solution is **Math 538 homework solutions, HMW 3, handwritten page 2 = PDF p. 14** (`tmp/sources/hatcher-math538-homework4-solutions.pdf`), Hatcher §3.3 Exercise 4: the same disjointness of translates, the observation that an orientation-preserving $g$ carries $\mu_x$ to $\mu_{gx}$, both excisions, and the conclusion that local consistency holds in $B_{(x)}$ because it holds in $B_x$. The statement is Hatcher, *Algebraic Topology* (2002), §3.3 Exercise 4.

::: pf

::: {.pf-step #covering}
$q:M\to M/G$ is a covering map, so $M/G$ is an $n$-manifold and $q$ restricts to a homeomorphism of a small ball $B_x$ onto its image.

::: pf-proof
A covering space action is one in which every point has a neighbourhood $U$ whose translates $gU$, $g\in G$, are pairwise disjoint (Hatcher, printed p. 72); for such an action the quotient map $q$ is a covering map, and $q$ is an open map, so $M/G$ inherits from $M$ the property of being locally Euclidean of dimension $n$. Taking $B_x\subset U$ a ball inside such a neighbourhood, the translates $gB_x$ are pairwise disjoint and $q$ is injective on $B_x$, hence a homeomorphism onto its image.
:::

:::

::: {.pf-step #upstairs-classes}
Let $x\in M$ and let $\mu_x\in H_n(M,M-\{x\})$ be the orientation class at $x$. Every $g\in G$ is orientation preserving, so $g_*\mu_x=\mu_{gx}$; and if $\mu_{B_x}\in H_n(M\mid B_x)$ is the local orientation class over the ball $B_x$, its restriction to $y\in B_x$ is $\mu_y$.

::: pf-proof
An orientation of $M$ is a function $y\mapsto\mu_y$ with $\mu_y$ a generator of $H_n(M,M-\{y\})\cong\ZZ$ and with the local consistency that near each $y$ a single class $\mu_{U}\in H_n(M\mid U)$ restricts to $\mu_z$ for all $z\in U$. A homeomorphism $g$ that preserves orientation carries the local orientation at $x$ to the local orientation at $gx$, which is exactly $g_*\mu_x=\mu_{gx}$; and the local class over the ball restricts to $\mu_y$ for every $y$ in it by the definition of local consistency.
:::

:::

::: {.pf-step #downstairs-class}
The class $\mu_{(x)}\in H_n(M/G,M/G-\{(x)\})$ defined as the image of $\mu_x$ does not depend on which point of the orbit of $x$ is used.

::: pf-proof
The homeomorphism $B_x\to B_{(x)}$ and excision give isomorphisms
$$
H_n(M,M-\{x\})\cong H_n(B_x,B_x-\{x\})\cong H_n\bigl(B_{(x)},B_{(x)}-\{(x)\}\bigr)\cong H_n(M/G,M/G-\{(x)\}),
$$
so the image of $\mu_x$ is a well-defined element. Another preimage of $(x)$ in the orbit is $gx$ with $g\in G$, and $q\circ g=q$, so the image of $\mu_{gx}=g_*\mu_x$ under the same composite equals the image of $\mu_x$: the two agree.
:::

:::

::: {.pf-step #orientation}
$y\mapsto\mu_{(y)}$ is an orientation of $M/G$, so $M/G$ is orientable.

::: pf-proof
Each $\mu_{(y)}$ is a generator of $H_n(M/G,M/G-\{(y)\})\cong\ZZ$, being the image of a generator under an isomorphism. For local consistency, take $y\in B_x$; the local class $\mu_{B_x}$ restricts to $\mu_y$ by step [](#upstairs-classes){.pf-ref}, so its image under the isomorphism of step [](#downstairs-class){.pf-ref} is a class in $H_n(M/G\mid B_{(x)})$ that restricts to $\mu_{(z)}$ for every $z\in B_x$, since the restrictions are compatible with the homeomorphism $B_x\to B_{(x)}$. So every point of $M/G$ has a neighbourhood carrying a single class restricting to the local classes, which is an orientation.
:::

:::

:::
:::
