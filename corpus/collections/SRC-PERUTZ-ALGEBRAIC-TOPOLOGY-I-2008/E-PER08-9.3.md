---
schema: qual/card@1
id: E-PER08-9.3
kind: problem
title: Mayer--Vietoris in degree one with connected intersection
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Completed from the retained Perutz Algebraic Topology I source and checked against the stated hypotheses.
---

::: {.problem}
Prove or give a counterexample: given two path connected open sets $U$ and $V$ whose union is $X$ and whose intersection $U\cap V$ is path connected, there exists a short exact sequence of abelian groups
\[
0\longrightarrow H_1(U\cap V)\longrightarrow H_1(U)\oplus H_1(V)\longrightarrow H_1(X)\longrightarrow 0.
\]
:::

::: {.solution}
The proposed short exact sequence is false in general.

Take $X=S^2$ and let $U,V$ be slightly enlarged northern and southern hemispheres.
Then $U$ and $V$ are contractible, while
\[
U\cap V\simeq S^1.
\]
Thus
\[
H_1(U\cap V)\cong\mathbb Z,
\qquad
H_1(U)\oplus H_1(V)=0,
\qquad
H_1(X)=0.
\]
The proposed first map would be an injection $\mathbb Z\to0$, impossible.

The Mayer--Vietoris sequence explains the obstruction:
\[
H_2(X)\xrightarrow{\delta}H_1(U\cap V)\to H_1(U)\oplus H_1(V)\to H_1(X)\to H_0(U\cap V).
\]
Path connectedness of $U,V,U\cap V$ makes the last map injective, so the map onto $H_1(X)$ is surjective, but the preceding map need not be injective because the connecting map from $H_2(X)$ can be nonzero.
In the sphere example it is an isomorphism.
:::
