---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1-P6
kind: problem
title: Residually finite group yields a finite-sheeted cover killing any nontrivial loop
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Groups
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
(May 2016) A group $G$ is called residually finite if for every $g\in G$ with $g\neq 1$, there is a finite group $H$ and a (surjective) homomorphism $\varphi\colon G\to H$ with $\varphi(g)\neq 1$.
Let $G$ be a residually finite group and let $X$ be the presentation complex for a presentation of $G$, with vertex $x_0$.
Show that for any loop $\gamma\colon I\to X$ at $x_0$ with $1\neq[\gamma]\in\pi_1(X,x_0)$, there is a finite-sheeted covering space $p\colon\widetilde X\to X$ and a basepoint $\widetilde x_0\in p^{-1}(\{x_0\})$ such that $\gamma$ does not lift to a loop at $\widetilde x_0$.
:::

::: {.solution}
Identify
\[
\pi_1(X,x_0)\cong G.
\]
Let \(g=[\gamma]\ne1\). Since \(G\) is residually finite, there is a finite group \(H\) and a surjective homomorphism
\[
\varphi:G\twoheadrightarrow H
\]
with \(\varphi(g)\ne1\). Put
\[
K=\ker\varphi.
\]
Then \(K\) has finite index
\[
[G:K]=|H|.
\]

Because a presentation complex is a connected CW complex, the covering-space classification gives a connected based covering
\[
p:(\widetilde X,\widetilde x_0)\to(X,x_0)
\]
whose associated subgroup is
\[
p_*\pi_1(\widetilde X,\widetilde x_0)=K.
\]
The number of sheets is the subgroup index, so this cover is finite-sheeted.

A based loop at \(x_0\) lifts to a loop at \(\widetilde x_0\) exactly when its homotopy class lies in \(K\). But
\[
g=[\gamma]\notin K,
\]
since \(\varphi(g)\ne1\). Hence the lift of \(\gamma\) beginning at \(\widetilde x_0\) does not end at \(\widetilde x_0\). Thus \(\gamma\) does not lift to a loop at the chosen basepoint.
:::
