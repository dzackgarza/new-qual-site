---
schema: qual/card@1
id: E-HAT-4.2-20
kind: problem
title: "Trivial $\\pi_1$-action on $\\pi_n$ of products"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m7__proofs-4-2-14-26.md (14-26: 11 correct, 16 and 26 each a single named step; both repaired) and m5__proofs-4-2-27-39.md (27-39: 10 correct, 28, 29 defective single cases, 34 a wrong intermediate assertion; all three repaired). No card in this slice has an unmet piece.

- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 20; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $G$ be a group and $X$ a simply-connected space.
Show that for the product $K(G, 1) \times X$ the action of $\pi_1$ on $\pi_n$ is trivial for all $n > 1$.
:::

::: {.solution}
Let $K=K(G,1)$ and let
$$
p:\widetilde K\times X\longrightarrow K\times X
$$
be the universal covering. Since $X$ is simply connected, the deck group is $G$, acting by
$$
g\cdot(u,x)=(gu,x).
$$
The projection
$$
\widetilde K\times X\to X
$$
is a homotopy equivalence because $\widetilde K$ is contractible. Under the induced identification
$$
\pi_n(K\times X)\cong\pi_n(\widetilde K\times X)\cong\pi_n(X),
\qquad n>1,
$$
every deck transformation acts as the identity on the $X$-factor. Hence it induces the identity on $\pi_n$.

By the description of the $\pi_1$-action via deck transformations,
$$
\boxed{\pi_1(K(G,1)\times X)\text{ acts trivially on }\pi_n(K(G,1)\times X),\ n>1.}
$$
:::
