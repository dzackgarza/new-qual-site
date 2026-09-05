---
schema: qual/card@1
id: P-5AXU3
kind: problem
title: Maps $X\to S^1$ are nullhomotopic when $\pi_1(X)$ is finite
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Fundamental Group
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked the statement against Section B, problem B1 of the January 18, 2002 topology qualifying exam.
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Repaired the covering-space basepoint: choose t0 in R above f(x0), rather
    than using 0 unless f(x0)=1. The finite image of f_* in pi_1(S^1) = Z is
    trivial, so the lifting criterion gives a lift to R, which contracts by a
    straight-line homotopy.
---

::: {.problem}
Show that if $X$ is a path-connected, locally path-connected topological space with finite fundamental group $\pi_1(X, x_0)$, then every continuous map $f : X \to S^1$ is **homotopic to a constant map** (nullhomotopic).
:::

::: {.solution}
Fix a basepoint $x_0\in X$ and let
\[
p:\mathbb R\longrightarrow S^1,
\qquad
p(t)=e^{2\pi i t},
\]
be the standard universal covering map.
Choose $t_0\in\mathbb R$ such that
\[
p(t_0)=f(x_0).
\]

<1>1. The induced homomorphism
\[
f_*:\pi_1(X,x_0)
\longrightarrow
\pi_1(S^1,f(x_0))\cong\mathbb Z
\]
is trivial.
::: {.proof}
The group $\pi_1(X,x_0)$ is finite by hypothesis, so its homomorphic image
\[
f_*(\pi_1(X,x_0))
\]
is finite.
But every nontrivial subgroup of $\mathbb Z$ is infinite.
Therefore
\[
f_*(\pi_1(X,x_0))=\{0\}.
\]
:::

<1>2. The map $f$ lifts to a continuous map
\[
\widetilde f:X\longrightarrow\mathbb R
\]
with $\widetilde f(x_0)=t_0$ and $p\circ\widetilde f=f$.
::: {.proof}
Because $\mathbb R$ is simply connected,
\[
p_*\bigl(\pi_1(\mathbb R,t_0)\bigr)
\]
is the trivial subgroup of $\pi_1(S^1,f(x_0))$.
By <1>1,
\[
f_*\bigl(\pi_1(X,x_0)\bigr)
\subseteq
p_*\bigl(\pi_1(\mathbb R,t_0)\bigr).
\]
Since $X$ is path-connected and locally path-connected, the covering-space lifting criterion applied with the chosen point $t_0\in p^{-1}(f(x_0))$ gives the required lift.
:::

<1>3. The lift $\widetilde f$ is homotopic to the constant map with value $t_0$.
::: {.proof}
Define
\[
H:X\times[0,1]\longrightarrow\mathbb R,
\qquad
H(x,s)=(1-s)\widetilde f(x)+s t_0.
\]
This is continuous, and
\[
H(x,0)=\widetilde f(x),
\qquad
H(x,1)=t_0.
\]
Thus $H$ is a homotopy from $\widetilde f$ to the constant map $x\mapsto t_0$.
:::

<1>4. The original map $f$ is homotopic to the constant map with value $f(x_0)$.
::: {.proof}
Compose the homotopy in <1>3 with $p$:
\[
F=p\circ H:X\times[0,1]\longrightarrow S^1.
\]
At the endpoints,
\[
F(x,0)
=p(\widetilde f(x))
=f(x)
\]
by <1>2, while
\[
F(x,1)
=p(t_0)
=f(x_0)
\]
is constant in $x$.
Hence $f$ is nullhomotopic.
:::
:::
