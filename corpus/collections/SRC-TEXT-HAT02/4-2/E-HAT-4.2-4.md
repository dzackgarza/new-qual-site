---
schema: qual/card@1
id: E-HAT-4.2-4
kind: problem
title: "Homotopy of infinite wedge of spheres"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let $X \subset \mathbb{R}^{n+1}$ be the union of the infinite sequence of spheres $S_k^n$ of radius $1/k$ and center $(1/k, 0, \ldots, 0)$.
Show that $\pi_i(X) = 0$ for $i < n$ and construct a homomorphism from $\pi_n(X)$ onto $\prod_k \pi_n(S_k^n)$.
:::

::: {.solution}
For each \(k\), let
\[
r_k:X\to S_k^n
\]
collapse every sphere \(S_j^n\) with \(j\ne k\) to the common tangent point. This is continuous because the diameters of the spheres tend to zero. Hence there is a homomorphism
\[
\Phi:\pi_n(X)\longrightarrow\prod_{k\ge1}\pi_n(S_k^n),
\qquad
\Phi([f])=([r_kf])_k.
\]

First let \(i<n\). Given \(f:S^i\to X\), compactness of the domain and cellular approximation for this shrinking CW-type union allow \(f\) to be homotoped into the \(i\)-skeleton. Each \(S_k^n\) has no positive cells below dimension \(n\), so this skeleton is just the common basepoint. Therefore
\[
\boxed{\pi_i(X)=0\qquad(i<n).}
\]
Equivalently, one may contract each compact image successively off the \(n\)-spheres since \(S^i\to S^n\) is nullhomotopic for \(i<n\), with continuity at the common point guaranteed by the shrinking diameters.

To prove surjectivity of \(\Phi\), choose arbitrary classes
\[
a_k\in\pi_n(S_k^n)\cong\mathbb Z.
\]
Choose pairwise disjoint closed \(n\)-balls \(B_k\subset S^n\) whose diameters tend to zero and which accumulate only at one point \(q\). Collapse the complement of the interiors of all \(B_k\)'s to the common basepoint of \(X\). On each quotient
\[
B_k/\partial B_k\cong S^n
\]
map to \(S_k^n\) by a representative of degree \(a_k\). Since \(\operatorname{diam}(S_k^n)\to0\), these maps fit continuously at the accumulation point \(q\). The resulting map
\[
f:S^n\to X
\]
satisfies
\[
[r_kf]=a_k
\]
for every \(k\). Thus
\[
\boxed{\Phi:\pi_n(X)\twoheadrightarrow\prod_k\pi_n(S_k^n).}
\]
:::
