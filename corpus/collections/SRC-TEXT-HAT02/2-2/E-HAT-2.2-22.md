---
schema: qual/card@1
id: E-HAT-2.2-22
kind: problem
title: Euler characteristic of $n$-sheeted covering space is $n$ times base
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 22; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete cellular/Euler-characteristic computation checked.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the lifted structure: the restriction of an $n$-sheeted covering over a contractible open
    cell is a trivial covering, so each open cell has exactly $n$ lifts, and the lifted
    characteristic maps give a CW structure with $c_k(\tilde X)=n\,c_k(X)$.
- event: solution-reviewed
  by: claude
  date: 2026-11-08
  note: >-
    Statement matches Exercise 22 as printed on p. 157. The pulled-back cell structure is correct
    and now cites its results: triviality of the covering over an open cell, by the covering
    homotopy property of Proposition 1.30 p. 60 and the lifting criterion Proposition 1.33 p. 61
    (the cell is contractible, so its image subgroup is trivial), and lifting of the
    characteristic maps by Proposition 1.30 again; chi is the alternating sum of cell counts,
    p. 146. What is not covered: the point-set verification that the lifted cells give a CW
    topology (closure finiteness, weak topology) is not written out.
---

::: {.problem}
For $X$ a finite CW complex and $p: \tilde{X} \to X$ an $n$ sheeted covering space, show that $\chi(\tilde{X}) = n\chi(X)$.
:::

::: {.solution}
Give $X$ a finite CW structure. Pull this structure back along the $n$-sheeted covering
$$
p:\widetilde X\to X.
$$

::: pf

::: pf-step

Every open $k$-cell of $X$ has exactly $n$ lifts, each an open $k$-cell of $\widetilde X$.

::: pf-proof

An open cell is contractible and hence simply connected. The restriction of the covering over the cell is therefore a disjoint union of homeomorphic copies of the cell: by the covering homotopy property, Proposition 1.30 (p. 60), the identity map of the open cell lifts to each sheet, starting from any chosen point of that sheet, and by Proposition 1.33 (p. 61) applied to the identity, whose image lies in the image subgroup, such a lift exists over the simply connected cell. Each lift is a homeomorphism from the cell onto a sheet, and the sheets meet no cell in more than one copy. Since each point has exactly $n$ preimages, there are exactly $n$ such copies. The characteristic maps of $X$ lift to $\widetilde X$ by Proposition 1.30 (p. 60), applied to the contractible disk $D^k$ mapping to the $k$-skeleton, and the lifted characteristic maps provide a CW structure on $\widetilde X$.

:::

:::

:::

If $c_k(X)$ denotes the number of $k$-cells, then
$$
c_k(\widetilde X)=n\,c_k(X).
$$
Therefore, with $\chi$ the alternating sum of the numbers of cells of a finite CW complex (p. 146),
$$
\begin{aligned}
\chi(\widetilde X)
&=\sum_k(-1)^k c_k(\widetilde X)\\
&=n\sum_k(-1)^k c_k(X)\\
&=\boxed{n\chi(X)}.
\end{aligned}
$$
The sums are finite because $X$ has finitely many cells.The covering-space Euler count agrees with Sam's §2.2 Exercise 22, printed p. 12: each open cell has exactly $n$ distinct lifted open cells; hence each $c_k(\widetilde X)=n c_k(X)$ and $\chi(\widetilde X)=n\chi(X)$. The present card also justifies existence of the lifted CW structure by Propositions 1.30 and 1.33 of Hatcher, pp. 60--61.


:::
