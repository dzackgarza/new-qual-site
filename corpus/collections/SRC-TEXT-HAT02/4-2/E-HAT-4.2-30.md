---
schema: qual/card@1
id: E-HAT-4.2-30
kind: problem
title: "Fiber bundle projections from subspaces of $\\mathbb{R}^2$"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.2, Exercise 30; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Let $E$ be a subspace of $\mathbb{R}^2$ obtained by deleting a subspace of $\{0\} \times \mathbb{R}$.
For which such spaces $E$ is the projection $E \to \mathbb{R}$, $(x, y) \mapsto x$, a fiber bundle?

::: {.solution}
Write
\[
E=\mathbb R^2-\bigl(\{0\}\times A\bigr),
\qquad
p(x,y)=x.
\]
For \(x\ne0\), the fiber is \(\mathbb R\), while
\[
p^{-1}(0)=\mathbb R-A.
\]
If \(p\) is a fiber bundle over the connected base \(\mathbb R\), all fibers are homeomorphic. Hence a necessary condition is
\[
\mathbb R-A\cong\mathbb R.
\]
As a subspace of \(\mathbb R\), a space homeomorphic to \(\mathbb R\) is a connected one-manifold without boundary, hence is an open interval, allowing infinite endpoints. Thus necessarily
\[
\mathbb R-A=(a,b)
\]
for some
\[
-\infty\le a<b\le\infty.
\]

This condition is also sufficient. Put \(I=(a,b)\). Away from \(0\) the projection is already the trivial product. It remains to trivialize over a small interval \((-\varepsilon,\varepsilon)\).

For \(t>0\), choose an increasing homeomorphism
\[
h_t:\mathbb R\to I
\]
which equals the identity on the portion of \(I\) at distance at least \(t\) from each finite endpoint, compresses the left tail into \((a,a+t]\) when \(a\) is finite, and compresses the right tail into \([b-t,b)\) when \(b\) is finite. For example, at a finite left endpoint use
\[
h_t(y)=a+t\exp\!\left(\frac{y-a-t}{t}\right)
\qquad(y\le a+t),
\]
and use the identity for \(y\ge a+t\) until the analogous right-end interpolation begins; at a finite right endpoint use
\[
h_t(y)=b-t\exp\!\left(-\frac{y-b+t}{t}\right)
\qquad(y\ge b-t).
\]
For sufficiently small \(t\) the two transition regions are disjoint. If an endpoint is infinite no compression is needed there. These formulas give a jointly continuous family in \((t,y)\), with
\[
h_t(y)\longrightarrow y
\]
for every \(y\in I\) as \(t\to0\), and points outside \(I\) are sent toward the corresponding missing endpoint.

Define
\[
H:p^{-1}(({-}\varepsilon,\varepsilon))\longrightarrow
(-\varepsilon,\varepsilon)\times I
\]
by
\[
H(x,y)=
\begin{cases}
(x,h_{|x|}(y)),&x\ne0,\\
(0,y),&x=0.
\end{cases}
\]
The displayed limiting behavior gives continuity at the central fiber; the same argument for \(h_t^{-1}\) gives continuity of the inverse. Thus \(H\) is a fiber-preserving homeomorphism.

Therefore
\[
\boxed{p:E\to\mathbb R\text{ is a fiber bundle exactly when }\mathbb R-A\text{ is an open interval (possibly unbounded).}}
\]
:::
