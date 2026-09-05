---
schema: qual/card@1
id: P-7XSR6
kind: problem
title: A nonsurjective map $S^3\times S^3\to\RP^3$ is homotopic to a constant
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Covering Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 4 of the official UGA Spring 2017 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Verified the lift to the universal double cover and the contraction inside the complement of a lift of the omitted projective point.
---

::: problem
Suppose that a continuous map $f : S^3 \times S^3 \to \RP^3$ is not surjective.

Prove that $f$ is homotopic to a constant function.
:::

::: {.solution}
Let
\[
\pi:S^3\longrightarrow\RP^3
\]
be the universal double covering map.

<1>1. The map $f$ has a lift
\[
\widetilde f:S^3\times S^3\longrightarrow S^3
\]
with
\[
\pi\circ\widetilde f=f.
\]
::: {.proof}
The space $S^3\times S^3$ is path-connected and simply connected, since each factor is path-connected and simply connected. Hence
\[
f_*\pi_1(S^3\times S^3)=0
\subseteq
\pi_*\pi_1(S^3)=0.
\]
The covering-space lifting criterion therefore gives a lift $\widetilde f$ after choosing a lift of one base point.
:::

<1>2. If $p\in\RP^3$ is omitted by $f$ and $q\in\pi^{-1}(p)$, then
\[
\widetilde f(S^3\times S^3)\subseteq S^3\setminus\{q\}.
\]
::: {.proof}
If $\widetilde f(x)=q$ for some $x\in S^3\times S^3$, then
\[
f(x)=\pi(\widetilde f(x))=\pi(q)=p,
\]
contrary to the choice of $p$.
:::

<1>3. The lift $\widetilde f$ is homotopic to a constant map.
::: {.proof}
Stereographic projection gives a homeomorphism
\[
S^3\setminus\{q\}\cong\RR^3.
\]
Thus $S^3\setminus\{q\}$ is contractible. By <1>2, $\widetilde f$ has image in this contractible subspace, so it is homotopic, through maps into $S^3\setminus\{q\}$, to a constant map.
:::

<1>4. Therefore $f$ is homotopic to a constant map.
::: {.proof}
Let
\[
\widetilde H:(S^3\times S^3)\times I\longrightarrow S^3
\]
be the homotopy from <1>3, with $\widetilde H(-,0)=\widetilde f$ and $\widetilde H(-,1)=q_0$ constant. Then
\[
H=\pi\circ\widetilde H
\]
is a homotopy in $\RP^3$ satisfying
\[
H(-,0)=\pi\circ\widetilde f=f,
\qquad
H(-,1)=\pi(q_0).
\]
Hence $f$ is homotopic to a constant function.
:::
:::
