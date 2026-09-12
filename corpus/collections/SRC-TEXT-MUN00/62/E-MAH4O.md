---
schema: qual/card@1
id: E-MAH4O
kind: problem
title: Winding of a curve about the origin from its position in the complement
classification:
  areas:
  - topology
  topics:
  - Invariance of Domain
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}

Let $C$ be a simple closed curve in $\mathbb{R}^2 - 0$; let $j: C \to \mathbb{R}^2 - 0$ be the inclusion mapping.
Show that $j_*$ is trivial if $0$ lies in the unbounded component of $\mathbb{R}^2 - C$, and is nontrivial otherwise.
(In fact, $j_*$ is an isomorphism in the latter case, as we shall prove in §65.)
:::

::: {.solution}
Choose a homeomorphism \(\gamma:S^1\to C\). Since \(\mathbb R^2-\{0\}\simeq S^1\), the homomorphism
\[
j_*:\pi_1(C)\longrightarrow\pi_1(\mathbb R^2-\{0\})\cong\mathbb Z
\]
is trivial exactly when the loop \(j\circ\gamma\) is nullhomotopic in \(\mathbb R^2-\{0\}\).

Assume first that \(0\) lies in the unbounded component \(U\) of \(\mathbb R^2-C\). Choose a closed disk \(B_R\) containing \(C\) in its interior. Since \(U\) is an open connected subset of the plane, it is path connected. Choose \(q\in U\setminus B_R\) and a polygonal path in \(U\) from \(0\) to \(q\). By deleting loops, we may take a simple polygonal arc. Truncate it at its first intersection with \(\partial B_R\), then append a polygonal ray from that point to infinity lying outside \(B_R\). We obtain a proper polygonal ray \(L\) beginning at \(0\), disjoint from \(C\).

The complement of a polygonal ray in the plane is homeomorphic to the complement of the standard ray \([0,\infty)\times\{0\}\), hence is simply connected. Since
\[
C\subset\mathbb R^2-L\subset\mathbb R^2-\{0\},
\]
the loop \(j\circ\gamma\) is nullhomotopic in \(\mathbb R^2-L\), and therefore in \(\mathbb R^2-\{0\}\). Hence \(j_*\) is trivial.

Conversely, suppose \(0\) does not lie in the unbounded component of \(\mathbb R^2-C\). If \(j_*\) were trivial, then \(j\circ\gamma\), and hence the inclusion \(j:C\hookrightarrow\mathbb R^2-\{0\}\), would be nullhomotopic. The Borsuk lemma proved in this section says that for a compact embedded set in the punctured plane, nullhomotopy of this inclusion forces the puncture to lie in the unbounded component of the complement. Applied to \(C\), this would put \(0\) in the unbounded component of \(\mathbb R^2-C\), a contradiction. Therefore \(j_*\) is nontrivial.

Thus \(j_*\) is trivial exactly when \(0\) lies in the unbounded component of \(\mathbb R^2-C\).
:::
