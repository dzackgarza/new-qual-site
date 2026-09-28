---
schema: qual/card@1
id: E-HAT-4.2-19
kind: problem
title: "$\\pi_n(X^n)$ is free abelian for $K(\\pi,1)$'s"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 19; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
If $X$ is a $K(G, 1)$ CW complex, show that $\pi_n(X^n)$ is free abelian for $n \geq 2$.
:::

::: {.solution}
Let \(p:\widetilde X\to X\) be the universal cover. Since \(X\) is a \(K(G,1)\), \(\widetilde X\) is contractible. The inverse image \(\widetilde X^{\,n}=p^{-1}(X^n)\) is the \(n\)-skeleton of \(\widetilde X\).

The pair \((\widetilde X,\widetilde X^{\,n})\) has no relative cells in dimensions at most \(n\). Hence
\[
\pi_i(\widetilde X,\widetilde X^{\,n})=0\qquad(i\le n).
\]
Since \(\widetilde X\) is contractible, the long exact sequence gives
\[
\pi_i(\widetilde X^{\,n})=0\qquad(i<n).
\]
Thus \(\widetilde X^{\,n}\) is \((n-1)\)-connected. Hurewicz gives
\[
\pi_n(\widetilde X^{\,n})\cong H_n(\widetilde X^{\,n};\mathbb Z).
\]
Because \(\widetilde X^{\,n}\) has no \((n+1)\)-cells,
\[
H_n(\widetilde X^{\,n})=\ker\bigl(d_n:C_n\to C_{n-1}\bigr),
\]
a subgroup of the free abelian group \(C_n\), hence itself free abelian.

Covering maps induce isomorphisms on \(\pi_n\) for \(n\ge2\), so
\[
\boxed{\pi_n(X^n)\cong\pi_n(\widetilde X^{\,n})\text{ is free abelian}.}
\]
:::
