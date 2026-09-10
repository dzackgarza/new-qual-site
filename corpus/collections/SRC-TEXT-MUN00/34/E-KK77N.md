---
schema: qual/card@1
id: E-KK77N
kind: problem
title: Locally metrizable regular Lindelof spaces are metrizable
classification:
  areas:
  - topology
  topics:
  - Metrizability
  - Countability
relations: []
review: draft
---

::: {.exercise}

Show that a regular Lindelöf space is metrizable if it is locally metrizable.
[Hint: A closed subspace of a Lindelöf space is Lindelöf.] Regularity is essential; where do you use it in the proof?
:::

::: {.solution}
Let \(x\in X\). Choose a metrizable neighborhood \(N_x\) of \(x\), and choose an open set \(U_x\) with
\[
x\in U_x\subset N_x.
\]
Regularity is used now: choose an open \(V_x\) such that
\[
x\in V_x\subset\overline{V_x}\subset U_x.
\]
The subspace \(\overline{V_x}\) is closed in Lindelöf \(X\), hence Lindelöf. It is also a subspace of the metrizable space \(N_x\), so it is metrizable. Every Lindelöf metric space is second countable; therefore \(\overline{V_x}\), and hence its open subspace \(V_x\), has a countable basis.

The family \(\{V_x:x\in X\}\) is an open cover of Lindelöf \(X\). Choose a countable subcover
\[
V_{x_1},V_{x_2},\dots.
\]
For each \(i\), let \(\mathcal B_i\) be a countable basis for \(V_{x_i}\). Since the \(V_{x_i}\) are open in \(X\),
\[
\mathcal B=\bigcup_{i=1}^\infty\mathcal B_i
\]
is a countable basis for \(X\). The space \(X\) is regular and second countable, so the Urysohn metrization theorem implies \(X\) is metrizable.

The essential use of regularity was the shrinking
\[
x\in V_x\subset\overline{V_x}\subset U_x,
\]
which makes \(\overline{V_x}\) a closed Lindelöf subspace while keeping it inside a metrizable neighborhood.
:::
