---
schema: qual/card@1
id: P-TOP-WORKSHOP-D3-W3
kind: problem
title: The finite-complement topology and the identity map (workshop warm-up)
classification:
  areas:
  - topology
  topics:
  - Separation Axioms
  - Continuity
  - Point-Set Topology
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Suppose $(X,\tau)$ is a topological space and let $(X,\tau')$ be the same set with the finite complement topology.
Then $X$ is $T_1$ if and only if $\operatorname{id}:(X,\tau)\to(X,\tau')$ is continuous.
:::

::: {.solution}
Let \(\tau_f\) denote the finite-complement topology on \(X\).

Suppose first that \((X,\tau)\) is \(T_1\). Then every finite subset of \(X\) is closed, being a finite union of closed singletons. Hence every cofinite subset is \(\tau\)-open. Therefore
\[
\tau_f\subseteq\tau,
\]
which is exactly the condition that
\[
\operatorname{id}:(X,\tau)\to(X,\tau_f)
\]
be continuous.

Conversely, suppose this identity map is continuous. For every \(x\in X\), the set \(X\setminus\{x\}\) is open in the finite-complement topology, so its inverse image under the identity—namely itself—is \(\tau\)-open. Thus \(\{x\}\) is \(\tau\)-closed. Hence \((X,\tau)\) is \(T_1\).
:::
