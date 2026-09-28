---
schema: qual/card@1
id: E-PER08-1.1
kind: problem
title: Homotopy equivalence is an equivalence relation
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 1.1 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the reflexive, symmetric, and transitive cases directly from the definition of homotopy equivalence and functoriality of composition with homotopies.
---

::: {.problem}
Show that homotopy equivalence defines an equivalence relation on spaces.
:::

::: {.solution}
Write $X\simeq Y$ when there is a homotopy equivalence $f:X\to Y$.

<1>1. The relation is reflexive.
::: {.proof}
For every space $X$, the identity map $\operatorname{id}_X:X\to X$ is a homotopy equivalence: it is its own inverse, and
\[
\operatorname{id}_X\circ \operatorname{id}_X=\operatorname{id}_X.
\]
Hence $X\simeq X$.
:::

<1>2. The relation is symmetric.
::: {.proof}
Suppose $X\simeq Y$. Then there are maps
\[
f:X\to Y,
\qquad
g:Y\to X
\]
with
\[
g\circ f\simeq \operatorname{id}_X,
\qquad
f\circ g\simeq \operatorname{id}_Y.
\]
The same two homotopies say precisely that $g$ is a homotopy equivalence with homotopy inverse $f$. Therefore $Y\simeq X$.
:::

<1>3. The relation is transitive.
::: {.proof}
Suppose $X\simeq Y$ and $Y\simeq Z$. Choose homotopy equivalences
\[
f:X\to Y,
\qquad
h:Y\to Z
\]
with homotopy inverses
\[
g:Y\to X,
\qquad
k:Z\to Y.
\]
Thus
\[
gf\simeq \operatorname{id}_X,
\quad
fg\simeq \operatorname{id}_Y,
\quad
kh\simeq \operatorname{id}_Y,
\quad
hk\simeq \operatorname{id}_Z.
\]
We claim that $h\circ f:X\to Z$ has homotopy inverse $g\circ k:Z\to X$.
Indeed, composition on either side preserves homotopies, so
\[
(gk)(hf)=g(kh)f
\simeq g\operatorname{id}_Y f
=gf
\simeq \operatorname{id}_X.
\]
Similarly,
\[
(hf)(gk)=h(fg)k
\simeq h\operatorname{id}_Y k
=hk
\simeq \operatorname{id}_Z.
\]
Therefore $h\circ f$ is a homotopy equivalence, so $X\simeq Z$.
:::

By <1>1--<1>3, homotopy equivalence is reflexive, symmetric, and transitive, hence an equivalence relation on spaces.
:::
