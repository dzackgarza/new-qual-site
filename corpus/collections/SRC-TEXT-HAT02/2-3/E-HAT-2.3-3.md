---
schema: qual/card@1
id: E-HAT-2.3-3
kind: problem
title: Reduced homology theory vanishes on point; suspension isomorphism follows
classification:
  areas:
  - topology
  topics:
  - Homology
  - Axiomatic Homology
  - Suspension
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.3, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that if $\tilde{h}$ is a reduced homology theory, then $\tilde{h}_n(\text{point}) = 0$ for all $n$.
Deduce that there are suspension isomorphisms $\tilde{h}_n(X) \approx \tilde{h}_{n+1}(SX)$ for all $n$.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
One has $\widetilde h_n(*)=0$ for every $n$.

::: pf-proof
The identity map of a point equals the constant map. By the reduced dimension axiom (equivalently, by exactness applied to the trivial pair), the reduced theory has zero coefficient group on a point. Hence $\widetilde h_n(*)=0$.
:::

:::

::: {.pf-step #s2}
Let $CX$ be the cone on $X$. Then
\[
\widetilde h_n(CX)=0
\]
for all $n$.

::: pf-proof
The cone is contractible, so homotopy invariance and step [](#s1){.pf-ref} give the result.
:::

:::

::: {.pf-step #s3}
The pair $(CX,X)$ gives natural isomorphisms
\[
\widetilde h_{n+1}(CX,X)\cong\widetilde h_n(X).
\]

::: pf-proof
In the long exact sequence of the pair, the two adjacent groups of $CX$ vanish by step [](#s2){.pf-ref}, so the connecting map is an isomorphism.
:::

:::

::: pf-step
Since $CX/X\cong SX$, excision identifies
\[
\widetilde h_{n+1}(CX,X)\cong\widetilde h_{n+1}(SX).
\]
Combining with step [](#s3){.pf-ref} yields
\[
\boxed{\widetilde h_n(X)\cong\widetilde h_{n+1}(SX)}.
\]
:::

:::

:::
