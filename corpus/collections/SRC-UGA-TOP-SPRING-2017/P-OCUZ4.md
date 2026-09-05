---
schema: qual/card@1
id: P-OCUZ4
kind: problem
title: Fixed points of self-maps of $\RP^2\vee\RP^2$
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homology
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 9 of the official UGA Spring 2017 topology exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the mod-2 matrix argument by the ordinary Lefschetz-number computation over Q; the wedge has no positive-degree rational homology, so every self-map has Lefschetz number 1.
---

::: problem
Prove or disprove:

Every map from $\RP^2 \lor \RP^2$ to itself has a fixed point.
:::

::: {.solution}
Let
\[
X=\RP^2\vee\RP^2
\]
and let $f:X\to X$ be continuous.

<1>1. The rational homology of $X$ is
\[
H_i(X;\QQ)\cong
\begin{cases}
\QQ, & i=0,\\
0, & i>0.
\end{cases}
\]
::: {.proof}
The integral homology of the real projective plane is
\[
H_i(\RP^2;\ZZ)\cong
\begin{cases}
\ZZ, & i=0,\\
\ZZ/2, & i=1,\\
0, & i\ge2.
\end{cases}
\]
Tensoring with $\QQ$ kills the $2$-torsion, so
\[
\widetilde H_i(\RP^2;\QQ)=0
\]
for every $i$.
Reduced homology takes a wedge of based CW complexes to the direct sum in positive degrees, hence
\[
\widetilde H_i(X;\QQ)
\cong
\widetilde H_i(\RP^2;\QQ)
\oplus
\widetilde H_i(\RP^2;\QQ)
=0.
\]
Since $X$ is connected, $H_0(X;\QQ)\cong\QQ$.
:::

<1>2. Every self-map $f:X\to X$ has Lefschetz number
\[
L(f)=1.
\]
::: {.proof}
By definition,
\[
L(f)=\sum_{i\ge0}(-1)^i
\operatorname{tr}\left(
f_*:H_i(X;\QQ)\longrightarrow H_i(X;\QQ)
\right).
\]
By <1>1, all positive-degree rational homology groups vanish.
On
\[
H_0(X;\QQ)\cong\QQ,
\]
the induced map is the identity because $X$ is connected.
Therefore
\[
L(f)=\operatorname{tr}(\operatorname{id}_{\QQ})=1.
\]
:::

<1>3. Every self-map of $\RP^2\vee\RP^2$ has a fixed point.
::: {.proof}
The space $X$ is a finite CW complex, hence a compact polyhedron.
By the Lefschetz fixed point theorem, a self-map of $X$ with nonzero Lefschetz number has a fixed point.
By <1>2,
\[
L(f)=1\ne0.
\]
Thus $f$ has a fixed point.
The proposed statement is true.
:::
:::
