---
schema: qual/card@1
id: E-HAT-2.1-30
kind: problem
title: 'Five-lemma: if all but one map in commutative diagram are isomorphisms, so is the remaining one'
classification:
  areas:
  - topology
  topics:
  - Homology
  - Exact Sequences
  - Five Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 30, including the source diagram on p. 133.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Verified by direct diagram algebra/exactness.
---

In each of the following commutative diagrams assume that all maps but one are isomorphisms. Show that the remaining map must be an isomorphism as well.

$$\begin{array}{lll}
A \to B & A \to B & A \to B \\
\downarrow & \downarrow & \downarrow \\
C \to D & C \to D & C \to D
\end{array}$$

::: {.solution}
Hatcher's three diagrams are respectively a commutative triangle and two commutative squares. In each case the missing map is forced to be a composite of the other maps and their inverses.

<1>1. For the triangle
\[
A\xrightarrow{f}B,
\qquad
A\xrightarrow{g}C\xrightarrow{h}B,
\qquad
f=h g,
\]
if any two of $f,g,h$ are isomorphisms, then so is the third.
::: {.proof}
If $g$ and $h$ are isomorphisms, then $f=hg$ is an isomorphism. If $f$ and $g$ are isomorphisms, then
\[
h=f g^{-1}.
\]
If $f$ and $h$ are isomorphisms, then
\[
g=h^{-1}f.
\]
In every case the remaining map is a composite of isomorphisms.
:::

<1>2. For the square
\[
\begin{array}{ccc}
A&\xrightarrow{f}&B\\
\downarrow g&&\downarrow h\\
C&\xrightarrow{k}&D,
\end{array}
\qquad hf=kg,
\]
if any three of $f,g,h,k$ are isomorphisms, then so is the fourth.
::: {.proof}
Solve the commutativity equation for the unknown map. Explicitly,
\[
f=h^{-1}kg,
\qquad
g=k^{-1}hf,
\qquad h=kgf^{-1},
\qquad k=hfg^{-1},
\]
according to which map is missing. Each expression is a composite of isomorphisms.
:::

<1>3. For the square with the right vertical arrow reversed,
\[
\begin{array}{ccc}
A&\xrightarrow{f}&B\\
\downarrow g&&\uparrow h\\
C&\xrightarrow{k}&D,
\end{array}
\qquad f=hkg,
\]
the same conclusion holds.
::: {.proof}
Again solve for the missing map:
\[
f=hkg,
\qquad g=k^{-1}h^{-1}f,
\qquad h=fg^{-1}k^{-1},
\qquad k=h^{-1}fg^{-1}.
\]
Thus the fourth map is an isomorphism whenever the other three are.
:::

Hence in each of Hatcher's three commutative diagrams, if all maps but one are isomorphisms, the remaining map is necessarily an isomorphism as well.
:::
