---
schema: qual/card@1
id: E-HAT-4.2-15
kind: problem
title: "Simply-connected closed 3-manifolds are $S^3$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Show that a closed simply-connected 3-manifold is homotopy equivalent to $S^3$.

::: {.solution}
Let \(M\) be a closed simply-connected \(3\)-manifold. Poincaré duality gives
\[
H_i(M;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,3,\\
0,&i=1,2.
\end{cases}
\]
Thus \(M\) is a homology \(3\)-sphere.

Since \(M\) is simply connected and \(H_2(M)=0\), the Hurewicz theorem implies \(\pi_2(M)=0\): otherwise \(\pi_2\) would be the first nonzero higher homotopy group and would map isomorphically to \(H_2\). Hence \(M\) is \(2\)-connected. Hurewicz now gives
\[
\pi_3(M)\xrightarrow{\cong}H_3(M)\cong\mathbb Z.
\]
Choose
\[
f:S^3\to M
\]
representing a generator. Then \(f_*\) is an isomorphism on \(H_3\), and it is automatically an isomorphism on all other homology groups as well. Both spaces are simply connected CW complexes (or have CW type), so the homology Whitehead theorem implies
\[
\boxed{M\simeq S^3.}
\]
:::
