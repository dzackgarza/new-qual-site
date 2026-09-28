---
schema: qual/card@1
id: E-HAT-4.B-2
kind: problem
title: "Fiber bundles $S^k \\to S^m \\to S^n$ and the Hopf invariant"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.B, Exercise 2 and its hint; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that if $S^k \to S^m \xrightarrow{p} S^n$ is a fiber bundle, then $m = 2n-1$, $k = n-1$, and, when $n > 1$, $H(p) = \pm 1$.
:::

::: {.solution}
Suppose
\[
S^k\longrightarrow S^m\xrightarrow{p}S^n
\]
is a fiber bundle.

First compare dimensions. Since a fiber bundle is locally a product, the total space is locally modeled on
\[
\mathbb R^n\times\mathbb R^k,
\]
so
\[
m=n+k.
\tag{1}
\]

Assume first that \(n>1\). Then the base is simply connected. The fiber cannot be \(S^0\), since a bundle with discrete two-point fiber over a simply connected base is the trivial double cover, whose total space is disconnected. Hence \(k>0\), and by (1), \(m>n\) and \(m>k\).

The long exact homotopy sequence of the bundle contains
\[
\pi_n(S^m)\longrightarrow\pi_n(S^n)
\longrightarrow\pi_{n-1}(S^k).
\]
Since \(m>n\), the first group is zero, while
\[
\pi_n(S^n)\cong\mathbb Z.
\]
Thus \(\pi_{n-1}(S^k)\ne0\), forcing
\[
k\le n-1.
\tag{2}
\]
On the other hand, if \(k<n-1\), then the segment
\[
\pi_{k+1}(S^n)\longrightarrow\pi_k(S^k)
\longrightarrow\pi_k(S^m)
\]
would be
\[
0\longrightarrow\mathbb Z\longrightarrow0,
\]
a contradiction. Hence
\[
k\ge n-1.
\tag{3}
\]
From (2) and (3),
\[
\boxed{k=n-1},
\]
and then (1) gives
\[
\boxed{m=2n-1}.
\]
For \(n=1\), the same dimension relation and the homotopy sequence force \(k=0\), hence \(m=1\), which is the exceptional double-cover case.

Now suppose \(n>1\), so the bundle has the form
\[
S^{n-1}\longrightarrow S^{2n-1}\xrightarrow{p}S^n.
\]
Consider the mapping cone
\[
C_p=S^n\cup_p CS^{2n-1}.
\]
This is a closed \(2n\)-manifold. Indeed, away from the copy of \(S^n\) and the cone point this is clear. Near a point of the copy of \(S^n\), choose a bundle trivialization over a small ball \(U\subset S^n\). Coning each fiber \(S^{n-1}\) produces a disk \(D^n\), so a neighborhood is
\[
U\times D^n\cong\mathbb R^{2n}.
\]
A neighborhood of the cone point is the cone on \(S^{2n-1}\), hence a \(2n\)-disk.

The cellular cohomology of the mapping cone has
\[
H^n(C_p;\mathbb Z)\cong\mathbb Z,
\qquad
H^{2n}(C_p;\mathbb Z)\cong\mathbb Z.
\]
Let \(\alpha\) and \(\beta\) be generators in these degrees. By definition of the Hopf invariant,
\[
\alpha^2=H(p)\,\beta.
\]
Since \(C_p\) is a closed orientable \(2n\)-manifold, Poincaré duality says that the middle-dimensional intersection pairing
\[
H^n(C_p;\mathbb Z)\times H^n(C_p;\mathbb Z)
\longrightarrow H^{2n}(C_p;\mathbb Z)\cong\mathbb Z
\]
is unimodular. As the middle cohomology has rank one, its matrix is the \(1\times1\) matrix \((H(p))\). Unimodularity therefore forces
\[
\boxed{H(p)=\pm1}.
\]

Thus every such sphere bundle satisfies
\[
\boxed{m=2n-1,\qquad k=n-1,}
\]
and for \(n>1\) its projection has Hopf invariant \(\pm1\).
:::
