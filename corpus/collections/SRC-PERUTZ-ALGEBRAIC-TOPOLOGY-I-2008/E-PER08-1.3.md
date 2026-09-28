---
schema: qual/card@1
id: E-PER08-1.3
kind: problem
title: Convex subsets of Euclidean space are contractible
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 1.3 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified that the straight-line homotopy stays inside the convex set and contracts it to an arbitrary basepoint.
---

::: {.problem}
Show that any convex subset of $\mathbb R^n$ is contractible.
:::

::: {.solution}
Let $C\subseteq\mathbb R^n$ be convex. If $C=\varnothing$, there is nothing to prove under the usual convention that contractibility is defined for nonempty spaces. Assume therefore that $C\neq\varnothing$, and choose $x_0\in C$.

<1>1. Define the straight-line homotopy
\[
H:[0,1]\times C\to C,
\qquad
H(t,x)=(1-t)x_0+tx.
\]
::: {.proof}
For every $t\in[0,1]$ and $x\in C$, the point $(1-t)x_0+tx$ is a convex combination of $x_0$ and $x$. Since $C$ is convex,
\[
(1-t)x_0+tx\in C.
\]
Thus $H$ is well defined. It is continuous because it is the restriction of the continuous affine map
\[
[0,1]\times\mathbb R^n\to\mathbb R^n,
\qquad
(t,x)\mapsto(1-t)x_0+tx.
\]
:::

<1>2. The homotopy $H$ joins the constant map at $x_0$ to the identity.
::: {.proof}
For every $x\in C$,
\[
H(0,x)=x_0=c_{x_0}(x)
\]
and
\[
H(1,x)=x=\operatorname{id}_C(x).
\]
Hence
\[
c_{x_0}\simeq\operatorname{id}_C.
\]
:::

By the contractibility criterion, $C$ is contractible.
:::
