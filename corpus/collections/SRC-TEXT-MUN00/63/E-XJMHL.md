---
schema: qual/card@1
id: E-XJMHL
kind: problem
title: Separation by topologist's sine curve variants on the sphere
classification:
  areas:
  - topology
  topics:
  - Jordan Curve Theorem
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

(a) Let $D$ be a subspace of $S^2$ homeomorphic to the topologist's sine curve $\overline{S}$.
(See §24.) Show that $D$ does not separate $S^2$.
[Hint: Let $h: \overline{S} \to D$ be the homeomorphism. Given $0 < c < 1$, let $\overline{S}_c$ equal the intersection of $\overline{S}$ with the set $\ts{(x, y) \mid x \leq c}$. Show that given $a, b \in S^2 - D$, there is, for some value of $c$, a path in $S^2 - h(\overline{S}_c)$ from $a$ to $b$. Conclude that there is a path in $S^2 - D$ from $a$ to $b$.]

(b) Let $C$ be a subspace of $S^2$ homeomorphic to the closed topologist's sine curve.
Show that $C$ separates $S^2$ into precisely two components, of which $C$ is the common boundary.
[Hint: Let $h$ be the homeomorphism of the closed topologist's sine curve with $C$. Let $C_0 = h(0 \times [-1, 1])$.
Show first, using the argument of Theorem 63.4, that each point of $C - C_0$ lies in the boundary of each component of $S^2 - C$.]
:::

::: {.solution}
Write
\[
\overline S=\bigl\{(x,\sin(1/x)):0<x\le1\bigr\}\cup(\{0\}\times[-1,1]).
\]

**(a)** We first show that the standard \(\overline S\subset S^2\) does not separate the sphere. Its complement in \(\mathbb R^2\) is path connected. Indeed, if \(0<x\le1\), a point above the graph can be joined vertically to the line \(y=2\), while a point below the graph can be joined vertically to \(y=-2\); neither segment crosses the graph. Points with \(x\le0\) or \(x>1\) can likewise be joined to one of these two horizontal lines while avoiding the vertical limiting segment. The two lines \(y=2\) and \(y=-2\) are joined through the half-plane \(x>1\), which misses \(\overline S\). Thus all points of \(\mathbb R^2-\overline S\) lie in one path component. Adding the point at infinity does not change connectedness, so \(S^2-\overline S\) is connected.

Now let \(h:\overline S\to D\subset S^2\) be the given homeomorphism. The Borsuk lemma from §62 says that an injective continuous image of a compact nonseparating subset of \(S^2\) is again nonseparating. Hence \(D=h(\overline S)\) does not separate \(S^2\). This proves (a).

**(b)** Let \(A\) denote the standard closed topologist's sine curve. It is obtained from \(\overline S\) by adjoining the broken-line arc \(P\) from \((0,-1)\) to \((1,\sin1)\), chosen so that
\[
P\cap\overline S=\{(0,-1),(1,\sin1)\}.
\]
Let \(h:A\to C\) be the given homeomorphism and put
\[
D=h(\overline S),\qquad Q=h(P).
\]
By part (a), \(D\) is closed and connected and \(S^2-D\) has one component. The arc-attachment result proved earlier in this section says that adjoining an arc whose intersection with a closed connected set consists exactly of the two endpoints increases the number of complementary components by one. Hence
\[
S^2-C=S^2-(D\cup Q)
\]
has exactly two components; call them \(U\) and \(V\).

It remains to prove that \(C\) is the boundary of both. Let
\[
C_0=h(\{0\}\times[-1,1]).
\]
Every point of \(C-C_0\) is locally an ordinary point of an embedded arc. The local argument in the proof of Theorem 63.4 applies there: a sufficiently small disk meets \(C\) in a single crosscut, and its two sides lie in the two distinct components \(U\) and \(V\). Consequently
\[
C-C_0\subset \partial U\cap\partial V.
\]
Every point of \(C_0\) is a limit of points of the oscillating graph, hence a limit of points of \(C-C_0\). Since boundaries are closed,
\[
C_0\subset\partial U\cap\partial V.
\]
Thus \(C\subset\partial U\cap\partial V\).

Conversely, \(U\) and \(V\) are components of the open set \(S^2-C\). Since open subsets of the locally connected sphere have open components, both \(U\) and \(V\) are open in \(S^2\). Hence no point of \(S^2-C\) can lie in the boundary of either component, so
\[
\partial U\cup\partial V\subset C.
\]
Therefore
\[
\boxed{\partial U=\partial V=C},
\]
and \(C\) separates \(S^2\) into precisely two components with common boundary \(C\).
:::
