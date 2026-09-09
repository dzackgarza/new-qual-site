---
schema: qual/card@1
id: E-HAT-4.3-11
kind: problem
title: "Fibration classes and homotopy equivalence"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 11; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

For a space $B$, let $\mathcal{F}(B)$ be the set of fiber homotopy equivalence classes of fibrations $E \to B$.
Show that a map $f: B_1 \to B_2$ induces $f^*: \mathcal{F}(B_2) \to \mathcal{F}(B_1)$ depending only on the homotopy class of $f$, with $f^*$ a bijection if $f$ is a homotopy equivalence.

::: {.solution}
For a fibration \(p:E\to B_2\) and a map \(f:B_1\to B_2\), let
\[
f^*E=\{(b,e):f(b)=p(e)\}\to B_1
\]
be the pullback fibration. Pullback carries fiber-preserving maps and fiber homotopies to fiber-preserving maps and fiber homotopies, so it defines
\[
f^*:\mathcal F(B_2)\to\mathcal F(B_1).
\]

If \(f_0\simeq f_1\) through \(H:B_1\times I\to B_2\), pull back \(E\) along \(H\). The resulting fibration over \(B_1\times I\) restricts at the two ends to \(f_0^*E\) and \(f_1^*E\). Fiber transport along the interval, obtained from the homotopy lifting property, gives mutually inverse fiber homotopy equivalences between these endpoint restrictions. Hence \(f^*\) depends only on the homotopy class of \(f\).

Functoriality of pullback gives
\[
(fg)^*=g^*f^*.
\]
If \(f:B_1\to B_2\) is a homotopy equivalence with homotopy inverse \(g\), then
\[
gf\simeq1_{B_1},
\qquad
fg\simeq1_{B_2},
\]
so homotopy invariance gives
\[
f^*g^*=1,
\qquad
g^*f^*=1.
\]
Thus
\[
\boxed{f^*:\mathcal F(B_2)\xrightarrow{\cong}\mathcal F(B_1)}
\]
is a bijection.
:::
