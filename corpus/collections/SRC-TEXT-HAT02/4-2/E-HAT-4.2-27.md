---
schema: qual/card@1
id: E-HAT-4.2-27
kind: problem
title: "Image of $\\pi_2(X) \\to \\pi_2(X,A)$ is central"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 27; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that the image of the map $\pi_2(X, x_0) \to \pi_2(X, A, x_0)$ lies in the center of $\pi_2(X, A, x_0)$.
:::

::: {.solution}
Let
\[
j_*:\pi_2(X,x_0)\to\pi_2(X,A,x_0)
\]
be the natural map, and let
\[
a\in\operatorname{im}j_*.
\]
Exactness of the long homotopy sequence of the pair gives
\[
\partial a=0\in\pi_1(A,x_0).
\]
For arbitrary \(b\in\pi_2(X,A,x_0)\), Lemma 4.39 says
\[
a+b-a=(\partial a)b.
\]
Since \(\partial a\) is the identity element of \(\pi_1(A,x_0)\), its action on \(b\) is trivial, so
\[
a+b-a=b.
\]
Hence
\[
a+b=b+a.
\]
Thus every element in the image of \(j_*\) commutes with every element of the relative group:
\[
\boxed{\operatorname{im}\bigl(\pi_2(X)\to\pi_2(X,A)\bigr)
\subseteq Z\bigl(\pi_2(X,A)\bigr).}
\]
:::
