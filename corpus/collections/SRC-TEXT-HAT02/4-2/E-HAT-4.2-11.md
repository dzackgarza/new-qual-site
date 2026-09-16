---
schema: qual/card@1
id: E-HAT-4.2-11
kind: problem
title: "$\\pi_2(X, X^1)$ and the kernel of $\\pi_1(X^1) \\to \\pi_1(X)$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 11; the stored statement matches. Also checked Hatcher errata for the corrected second half of this exercise.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X$ be a connected CW complex with 1-skeleton $X^1$.
Show that $\pi_2(X, X^1) \approx \pi_2(X) \times K$ where $K$ is the kernel of $\pi_1(X^1) \to \pi_1(X)$, a free group.
Show also that the map $\pi_2'(X) \to \pi_2'(X, X^1)$ need not be injective by considering the case $X = \mathbb{RP}^2$ with its standard CW structure.
:::

::: {.solution}
Since \(X^1\) is a graph,
\[
\pi_2(X^1)=0.
\]
The long exact sequence of the pair gives a short exact sequence
\[
0\longrightarrow\pi_2(X)
\longrightarrow\pi_2(X,X^1)
\xrightarrow{\partial}K\longrightarrow1,
\]
where
\[
K=\ker\bigl(\pi_1(X^1)\to\pi_1(X)\bigr).
\]
The group \(K\) is a subgroup of the free group \(\pi_1(X^1)\), hence is free by Nielsen--Schreier. Choose a free basis of \(K\) and choose one lift in \(\pi_2(X,X^1)\) of each basis element. By the universal property of a free group these lifts extend to a homomorphic section
\[
s:K\to\pi_2(X,X^1)
\]
of \(\partial\).

By Exercise 27, the image of \(\pi_2(X)\) in \(\pi_2(X,X^1)\) is central. Hence the resulting semidirect product is in fact direct:
\[
\boxed{\pi_2(X,X^1)\cong\pi_2(X)\times K.}
\]

For the second assertion take \(X=\mathbb{RP}^2\) with its standard CW structure and \(X^1=S^1\). The action of
\[
\pi_1(X)\cong\mathbb Z/2
\]
on
\[
\pi_2(X)\cong\pi_2(S^2)\cong\mathbb Z
\]
is multiplication by \(-1\). Therefore
\[
\pi_2'(X)\cong\mathbb Z/(a\sim-a)\cong\mathbb Z/2.
\]
On the other hand the pair \((X,X^1)\) is obtained by attaching one \(2\)-cell, so the relative Hurewicz theorem gives
\[
\pi_2'(X,X^1)\cong H_2(X,X^1)\cong\mathbb Z.
\]
The induced homomorphism
\[
\mathbb Z/2\longrightarrow\mathbb Z
\]
must be zero, hence is not injective. This is the required counterexample.
:::
