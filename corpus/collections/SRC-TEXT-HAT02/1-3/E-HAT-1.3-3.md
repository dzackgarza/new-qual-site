---
schema: qual/card@1
id: E-HAT-1.3-3
kind: problem
title: "Compactness lifts through finite-fiber covering spaces"
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.3, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Proved Hausdorffness by separating points through the base or disjoint sheets, then proved compactness using finitely many shrunken evenly covered neighborhoods with compact closures.
---

Let $p: \tilde{X} \to X$ be a covering space with $p^{-1}(x)$ finite and nonempty for all $x \in X$.
Show that $\tilde{X}$ is compact Hausdorff if $X$ is compact Hausdorff.

::: {.solution}
Assume $X$ is compact Hausdorff and every fiber of
\[
p:\widetilde X\to X
\]
is finite and nonempty.

<1>1. The space $\widetilde X$ is Hausdorff.
::: {.proof}
Let $\widetilde x\ne\widetilde y$.

If
\[
p(\widetilde x)\ne p(\widetilde y),
\]
choose disjoint open neighborhoods $U,V\subseteq X$ of these two image points, using Hausdorffness of $X$.
Then
\[
p^{-1}(U),\qquad p^{-1}(V)
\]
are disjoint open neighborhoods of $\widetilde x$ and $\widetilde y$.

If
\[
p(\widetilde x)=p(\widetilde y)=x,
\]
choose an evenly covered neighborhood $U$ of $x$.
Distinct points in the same fiber lie in distinct sheets over $U$ because each sheet maps injectively to $U$.
Those sheets are disjoint open neighborhoods of $\widetilde x$ and $\widetilde y$.

Thus any two distinct points of $\widetilde X$ have disjoint open neighborhoods.
:::

<1>2. For every $x\in X$, there are open sets
\[
x\in V_x\subseteq\overline{V_x}\subseteq U_x
\]
with $U_x$ evenly covered.
::: {.proof}
Choose an evenly covered open neighborhood $U_x$ of $x$.
A compact Hausdorff space is regular, so there is an open neighborhood $V_x$ of $x$ whose closure satisfies
\[
\overline{V_x}\subseteq U_x.
\]
:::

<1>3. For each $x$, the set
\[
p^{-1}(\overline{V_x})
\]
is compact.
::: {.proof}
Write the evenly covered decomposition
\[
p^{-1}(U_x)=\coprod_{\lambda\in\Lambda_x}W_\lambda,
\]
with each
\[
p|_{W_\lambda}:W_\lambda\to U_x
\]
a homeomorphism.

The number of sheets is exactly the cardinality of the fiber over $x$:
each sheet contains exactly one point over $x$.
By hypothesis this fiber is finite, so $\Lambda_x$ is finite.

For each sheet,
\[
W_\lambda\cap p^{-1}(\overline{V_x})
\]
is homeomorphic via $p$ to $\overline{V_x}$.
Since $X$ is compact Hausdorff, the closed subset $\overline{V_x}$ is compact.
Therefore $p^{-1}(\overline{V_x})$ is a finite union of compact sets and is compact.
:::

<1>4. Finitely many of the sets $V_x$ cover $X$.
::: {.proof}
The family
\[
\{V_x:x\in X\}
\]
is an open cover of the compact space $X$.
Hence there are points $x_1,\dots,x_m$ such that
\[
X=V_{x_1}\cup\cdots\cup V_{x_m}.
\]
:::

<1>5. The space $\widetilde X$ is compact.
::: {.proof}
From <1>4,
\[
\widetilde X
=p^{-1}(X)
=\bigcup_{i=1}^m p^{-1}(V_{x_i})
\subseteq
\bigcup_{i=1}^m p^{-1}(\overline{V_{x_i}})
\subseteq\widetilde X.
\]
Thus equality holds:
\[
\widetilde X
=
\bigcup_{i=1}^m p^{-1}(\overline{V_{x_i}}).
\]
Each set on the right is compact by <1>3, so their finite union is compact.
:::

<1>6. Hence $\widetilde X$ is compact Hausdorff.
::: {.proof}
Hausdorffness is <1>1 and compactness is <1>5.
:::
:::
