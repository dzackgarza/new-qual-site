---
schema: qual/card@1
id: E-HAT-4.1-15
kind: problem
title: "Every self-map of $S^n$ is a multiple of the identity"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09

---

Show that every map $f: S^n \to S^n$ is homotopic to a multiple of the identity map by the following steps.

(a) Use Lemma 4.10 (or simplicial approximation, Theorem 2C.1) to reduce to the case that there exists a point $q \in S^n$ with $f^{-1}(q) = \{p_1, \ldots, p_k\}$ and $f$ is an invertible linear map near each $p_i$.

(b) For $f$ as in (a), consider the composition $gf$ where $g: S^n \to S^n$ collapses the complement of a small ball about $q$ to the basepoint.
Use this to reduce (a) further to the case $k = 1$.

(c) Finish the argument by showing that an invertible $n \times n$ matrix can be joined by a path of such matrices to either the identity matrix or the matrix of a reflection.

::: {.solution}
Let \(f:S^n\to S^n\).

### (a) Reduction to finitely many regular preimages

By Lemma 4.10 (equivalently, after simplicial approximation and a small local modification), \(f\) is homotopic to a map for which there is a point \(q\in S^n\) such that
\[
f^{-1}(q)=\{p_1,\dots,p_k\},
\]
and, in coordinate balls around each \(p_i\) and around \(q\), the map is given by an invertible linear map. Choose pairwise disjoint small balls \(B_i\) about the \(p_i\)'s and a ball \(B\) about \(q\) so that
\[
f|_{B_i}:B_i\to B
\]
is linear and invertible in these coordinates.

### (b) Split into one-preimage pieces

Let
\[
g:S^n\to S^n
\]
collapse the complement of the interior of \(B\) to the basepoint. This quotient map has degree \(1\), hence is homotopic to the identity. Thus
\[
gf\simeq f.
\]

The map \(gf\) is constant off the union of the \(B_i\)'s. Collapsing the complement of the interiors of the \(B_i\)'s identifies the domain with a wedge
\[
S^n\vee\cdots\vee S^n
\]
of \(k\) spheres, and \(gf\) factors as
\[
S^n\xrightarrow{\text{pinch}}\bigvee_{i=1}^k S^n
\xrightarrow{h_1\vee\cdots\vee h_k}S^n,
\]
where each \(h_i\) has exactly one preimage of \(q\) and is linear near that point. In \(\pi_n(S^n)\), this says
\[
[f]=[h_1]+\cdots+[h_k].
\]
So it remains to classify the case \(k=1\).

### (c) The one-preimage case

For such a map, the local model near the unique preimage is an invertible matrix
\[
A\in GL_n(\mathbb R).
\]
The group \(GL_n(\mathbb R)\) has exactly two path-components, distinguished by the sign of the determinant. Gaussian elimination through invertible matrices (or polar decomposition) gives a path in \(GL_n(\mathbb R)\) from \(A\) to
\[
I\quad\text{if }\det A>0,
\]
and to a reflection
\[
R=\operatorname{diag}(-1,1,\dots,1)
\quad\text{if }\det A<0.
\]
Using this path inside the local ball and keeping the map constant outside gives a homotopy of \(h_i\) to the identity map when \(\det A>0\), and to a reflection when \(\det A<0\). The latter represents \(-[\operatorname{id}_{S^n}]\) in \(\pi_n(S^n)\).

Hence, if
\[
\varepsilon_i=\operatorname{sign}(\det Df_{p_i})\in\{\pm1\},
\]
then
\[
[f]=\sum_{i=1}^k\varepsilon_i[\operatorname{id}_{S^n}].
\]
Writing
\[
d=\sum_i\varepsilon_i\in\mathbb Z,
\]
we obtain
\[
\boxed{f\simeq d\cdot\operatorname{id}_{S^n}.}
\]
Thus every self-map of \(S^n\) is homotopic to an integral multiple of the identity.
:::
