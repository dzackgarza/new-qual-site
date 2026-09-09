---
schema: qual/card@1
id: P-YMVNK
kind: problem
title: Stabilizer subgroups of two points in a $G$-set are conjugate
classification:
  areas:
  - algebra
  topics:
  - Orbit-Stabilizer
  - Conjugacy
  - Group Actions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Let $X$ be a $G$-set with group action $G \times X \to X$.
(1) Prove that if $x_1, x_2 \in X$ belong to the same $G$-orbit ($x_2 = g \cdot x_1$ for some $g \in G$), then their stabilizer subgroups $\operatorname{Stab}_G(x_1)$ and $\operatorname{Stab}_G(x_2)$ are **conjugate** in $G$:
$$\operatorname{Stab}_G(g \cdot x_1) = g \operatorname{Stab}_G(x_1) g^{-1}.$$
(2) Note that if $x_1, x_2$ lie in different orbits, their stabilizers need not be conjugate.
:::

::: solution
For $h\in G$,
\[
\begin{aligned}
h\in\operatorname{Stab}_G(gx)
&\iff h(gx)=gx\\
&\iff (g^{-1}hg)x=x\\
&\iff g^{-1}hg\in\operatorname{Stab}_G(x)\\
&\iff h\in g\operatorname{Stab}_G(x)g^{-1}.
\end{aligned}
\]
Hence
\[
\operatorname{Stab}_G(gx)=g\operatorname{Stab}_G(x)g^{-1}.
\]
Thus points in the same orbit have conjugate stabilizers.

For different orbits this can fail. For example, let $S_3$ act on
\[
\{1,2,3\}\sqcup\{*\}
\]
in the usual way on the first orbit and trivially on $*$. Then
\[
\operatorname{Stab}(1)\cong C_2,
\qquad
\operatorname{Stab}(*)=S_3,
\]
so the stabilizers are not conjugate.
:::
