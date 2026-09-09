---
schema: qual/card@1
id: E-HAT-4.I-3
kind: problem
title: "Skeletons of suspended lens spaces"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.I, Exercise 3 and Proposition 4I.3; the stored statement matches the corrected current source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Extending Proposition 4I.3, show that the $(2k+1)$-skeleton of the suspension of a high-dimensional lens space with fundamental group of order $p^n$ is homotopy equivalent to the wedge sum of the $(2k+1)$-skeleta of the spaces $X_i$, if these $X_i$'s are chosen to have the minimum number of cells in each dimension.

::: {.solution}
Let
\[
K=K(\mathbb Z_{p^n},1)
\]
be the infinite-dimensional lens space, and let
\[
\Sigma K\simeq X_1\vee\cdots\vee X_{p-1}
\tag{1}
\]
be the splitting of Proposition 4I.3. Choose each \(X_i\) in the minimal-cell form described after the proof: one \(0\)-cell and one cell in each dimension congruent to
\[
2i\quad\text{or}\quad2i+1\pmod{2p-2},
\]
and no other positive-dimensional cells.

A lens space of sufficiently high dimension with fundamental group \(\mathbb Z_{p^n}\) is a finite skeleton of the standard infinite lens space \(K\). Thus, provided its dimension is at least \(2k\), its suspension has \((2k+1)\)-skeleton equal to
\[
(\Sigma K)^{(2k+1)}.
\]

Recall the construction of (1). For a generator \(r\in\mathbb F_p^\times\), Proposition 4I.3 constructs maps
\[
m_i:\Sigma K\to\Sigma K
\]
whose mapping telescopes are the \(X_i\)'s; on reduced homology, the \(i\)-th telescope retains exactly the dimensions congruent to \(2i\pmod{2p-2}\) and kills the others. The sum of the natural telescope maps gives a homology equivalence
\[
F:\Sigma K\longrightarrow\bigvee_{i=1}^{p-1}X_i.
\tag{2}
\]
By cellular approximation choose \(F\) cellular. Because the \(X_i\)'s have the minimal cell structures just described, (2) restricts to a cellular map
\[
F^{(2k+1)}:(\Sigma K)^{(2k+1)}\longrightarrow
\bigvee_{i=1}^{p-1}X_i^{(2k+1)}.
\tag{3}
\]
The homology calculation in Proposition 4I.3 is degree-by-degree, so (3) induces an isomorphism on homology in every degree \(\le2k+1\). Above degree \(2k+1\), both sides have zero homology because they are \((2k+1)\)-dimensional CW complexes. Hence (3) is a homology isomorphism in all degrees.

Both sides of (3) are simply connected: they are skeleta of suspensions, with no \(1\)-cells in the minimal models. Therefore the homology Whitehead theorem implies that (3) is a homotopy equivalence. Identifying the source with the corresponding skeleton of the suspension of the chosen high-dimensional lens space gives
\[
\boxed{
(\Sigma L)^{(2k+1)}\simeq
\bigvee_{i=1}^{p-1}X_i^{(2k+1)}.}
\]
This is precisely the finite-skeletal extension of Proposition 4I.3.
:::
