---
schema: qual/card@1
id: E-HAT-4.2-21
kind: problem
title: "Constructing spaces with arbitrary $\\pi_n$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 21; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Given a sequence of CW complexes $K(G_n, n)$, $n = 1, 2, \ldots$, let $X_n$ be the CW complex formed by the product of the first $n$ of these $K(G_n, n)$'s. Via the inclusions $X_{n-1} \subset X_n$ coming from regarding $X_{n-1}$ as the subcomplex of $X_n$ with $n$th coordinate equal to a basepoint 0-cell of $K(G_n, n)$, we can then form the union of all the $X_n$'s, a CW complex $X$.
Show $\pi_n(X) \approx G_n$ for all $n$.
:::

::: {.solution}
Write
$$
X_N=\prod_{i=1}^N K(G_i,i),
\qquad
X=\bigcup_N X_N.
$$
Each $X_N$ is a subcomplex of $X_{N+1}$. A map from a compact sphere into the CW complex $X$ has image in a finite subcomplex, hence in some $X_N$. The same is true for homotopies. Therefore
$$
\pi_n(X)\cong \varinjlim_N\pi_n(X_N).
$$
For $N\ge n$, the product formula gives
$$
\pi_n(X_N)
\cong
\prod_{i=1}^N\pi_n(K(G_i,i))
\cong G_n,
$$
since $K(G_i,i)$ has only one nonzero homotopy group, in degree $i$. The bonding maps are the identity on this $G_n$-summand. Hence the direct limit stabilizes and
$$
\boxed{\pi_n(X)\cong G_n\quad\text{for every }n\ge1.}
$$
:::
