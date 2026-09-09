---
schema: qual/card@1
id: P-RAF07D
kind: problem
title: "Weak and weak* topologies and Alaoglu's theorem"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 4 of the official UCSD Fall 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X$ be a normed space and $X^*$ its dual space.

(a) Define the weak topology and the weak* topology on $X^*$.

(b) State and prove Alaoglu's Theorem.
:::


::: solution
<1>1. Define the weak and weak* topologies on $X^*$.
::: proof
The weak topology on $X^*$ is
\[
\sigma(X^*,X^{**}),
\]
the coarsest topology for which every map
\[
\phi\longmapsto F(\phi),\qquad F\in X^{**},
\]
is continuous. Thus a net $(\phi_\alpha)$ converges weakly to $\phi$ exactly when
\[
F(\phi_\alpha)\to F(\phi)
\qquad\text{for every }F\in X^{**}.
\]

The weak* topology on $X^*$ is
\[
\sigma(X^*,X),
\]
the coarsest topology for which every evaluation map
\[
\phi\longmapsto \phi(x),\qquad x\in X,
\]
is continuous. Thus
\[
\phi_\alpha\overset{w^*}{\longrightarrow}\phi
\quad\Longleftrightarrow\quad
\phi_\alpha(x)\to\phi(x)
\quad\text{for every }x\in X.
\]
Because the canonical embedding $X\hookrightarrow X^{**}$ supplies only some of the weak test functionals, the weak* topology is no stronger than the weak topology.
:::

<1>2. State Banach--Alaoglu.
::: proof
**Banach--Alaoglu theorem.** The closed unit ball
\[
B_{X^*}:=\{\phi\in X^*: \|\phi\|\le1\}
\]
is compact in the weak* topology $\sigma(X^*,X)$.

More generally, every norm-closed ball in $X^*$ is weak* compact.
:::

<1>3. Embed the dual unit ball into a compact product.
::: proof
Let $\mathbb K$ denote the scalar field. For each $x\in X$, set
\[
D_x:=\{z\in\mathbb K:|z|\le\|x\|\}.
\]
Each $D_x$ is compact. Hence, by Tychonoff's theorem,
\[
K:=\prod_{x\in X}D_x
\]
is compact in the product topology.

Define
\[
J:B_{X^*}\to K,
\qquad
J(\phi)=(\phi(x))_{x\in X}.
\]
Since $|\phi(x)|\le\|\phi\|\|x\|\le\|x\|$, this is well defined. It is injective because a linear functional is determined by all its values on $X$.

The product topology restricted to $J(B_{X^*})$ is exactly the weak* topology: the coordinate maps are precisely the evaluations $\phi\mapsto\phi(x)$.
:::

<1>4. Show that the image is closed in the product.
::: proof
A point $a=(a_x)_{x\in X}\in K$ lies in $J(B_{X^*})$ exactly when the assignment
\[
x\longmapsto a_x
\]
is linear. Indeed, the bound $|a_x|\le\|x\|$ then makes it a bounded linear functional of norm at most $1$.

Linearity is expressed by the coordinate identities
\[
a_{x+y}=a_x+a_y
\qquad(x,y\in X)
\]
and
\[
a_{\lambda x}=\lambda a_x
\qquad(x\in X,\ \lambda\in\mathbb K).
\]
For fixed $x,y,\lambda$, each identity defines a closed subset of $K$, because coordinate projections are continuous. Therefore
\[
J(B_{X^*})
\]
is an intersection of closed subsets of $K$, hence is closed.
:::

<1>5. Conclude compactness.
::: proof
Since $K$ is compact and $J(B_{X^*})$ is closed in $K$, the image $J(B_{X^*})$ is compact. Because $J$ is a homeomorphism from $B_{X^*}$ with its weak* topology onto this image,
\[
\boxed{B_{X^*}\text{ is weak* compact}.}
\]
This is Banach--Alaoglu.
:::
:::
