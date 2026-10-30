---
schema: qual/card@1
id: P-WESTOP04-08
kind: problem
title: Zero-dimensional spaces are exactly subspaces of generalized Cantor cubes
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The retained extraction mangles the displayed exponent in the definition of generalized Cantor space, but explicitly names a cardinal kappa and the two-point discrete space {0,1}. The standard notation {0,1}^kappa is used while recording this extraction loss.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source defines zero-dimensional as having a basis of clopen sets, under which the two-point indiscrete space is a counterexample to the converse. The definition now also requires T_0.
---

::: {.problem}
A generalized Cantor space is a space homeomorphic to
$$
\{0,1\}^{\kappa},
$$
where $\{0,1\}$ is discrete and $\kappa$ is a cardinal. A space is zero-dimensional if it is $T_0$ and has a basis of clopen sets.

Outline a proof that a space is zero-dimensional if and only if it is homeomorphic to a subspace of a generalized Cantor space.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every subspace of a generalized Cantor space is $T_0$.


::: pf-proof

The space $\{0,1\}$ is discrete, hence Hausdorff, and a product of Hausdorff spaces is Hausdorff. Every subspace of a Hausdorff space is Hausdorff, hence $T_0$.

:::

:::

::: {.pf-step #s1-2}

Every subspace of a generalized Cantor space has a basis of clopen sets.


::: pf-proof

Let
$$
Y\subseteq\{0,1\}^{\kappa}.
$$
For a finite set
$$
F\subseteq\kappa
$$
and a function
$$
s:F\to\{0,1\},
$$
define the cylinder
$$
C(F,s)
\coloneqq
\{
x\in\{0,1\}^{\kappa}:
x\restrict_F=s
\}.
$$
Because
$$
\{0,1\}
$$
is discrete, each coordinate condition
$$
x(\alpha)=s(\alpha)
$$
defines a clopen set. A finite intersection of such sets is clopen, so every cylinder
$$
C(F,s)
$$
is clopen.

The finite-coordinate cylinders form a basis for the product topology. Therefore
$$
\{
Y\cap C(F,s)
\}
$$
is a basis of clopen subsets for the subspace topology on $Y$.

:::

:::

::: {.pf-step #s1-3}

Let $X$ be $T_0$ and let
$$
\mathcal B
$$
be a basis of clopen subsets of $X$. Then the members of
$$
\mathcal B
$$
separate distinct points.


::: pf-proof

Let
$$
x\ne y.
$$
Since $X$ is $T_0$, there is an open set containing one of the two points but not the other. After interchanging $x$ and $y$ if necessary, choose an open set
$$
U
$$
with
$$
x\in U,
\qquad
y\notin U.
$$
Because
$$
\mathcal B
$$
is a basis, there is
$$
B\in\mathcal B
$$
such that
$$
x\in B\subseteq U.
$$
Then
$$
y\notin B.
$$
Thus a clopen basis element separates the two points.

:::

:::

::: {.pf-step #s1-4}

Define
$$
e:X\longrightarrow\{0,1\}^{\mathcal B}
$$
by
$$
\boxed{
e(x)(B)
=
\begin{cases}
1,&x\in B,\\
0,&x\notin B.
\end{cases}}
$$
for every
$$
B\in\mathcal B.
$$


::: pf-proof

For each point
$$
x\in X,
$$
the rule assigns one element of
$$
\{0,1\}
$$
to every coordinate
$$
B\in\mathcal B.
$$
Hence
$$
e(x)
$$
is an element of the product
$$
\{0,1\}^{\mathcal B}.
$$

:::

:::

::: {.pf-step #s1-5}

The map $e$ is continuous.


::: pf-proof

For each coordinate
$$
B\in\mathcal B,
$$
let
$$
\pi_B:
\{0,1\}^{\mathcal B}
\to
\{0,1\}
$$
be the coordinate projection. Then
$$
(\pi_B\circ e)^{-1}(\{1\})
=
B
$$
and
$$
(\pi_B\circ e)^{-1}(\{0\})
=
X\setminus B.
$$
Both sets are open because
$$
B
$$
is clopen. Therefore every coordinate
$$
\pi_B\circ e
$$
is continuous. By the universal property of the product topology,
$$
e
$$
is continuous.

:::

:::

::: {.pf-step #s1-6}

The map $e$ is injective.


::: pf-proof

If
$$
x\ne y,
$$
step [](#s1-3){.pf-ref} gives
$$
B\in\mathcal B
$$
with, say,
$$
x\in B,
\qquad
y\notin B.
$$
Then
$$
e(x)(B)=1
$$
and
$$
e(y)(B)=0.
$$
Hence
$$
e(x)\ne e(y).
$$

:::

:::

::: {.pf-step #s1-7}

The map
$$
e:X\to e(X)
$$
is a homeomorphism.


::: pf-proof

It remains to prove that the inverse
$$
e^{-1}:e(X)\to X
$$
is continuous.

For each
$$
B\in\mathcal B,
$$
let
$$
C_B
\coloneqq
\{
u\in\{0,1\}^{\mathcal B}:
u(B)=1
\}.
$$
This is a clopen cylinder. By definition of
$$
e,
$$
$$
e(B)
=
e(X)\cap C_B.
$$
Thus
$$
e(B)
$$
is open in the subspace
$$
e(X).
$$

Since
$$
\mathcal B
$$
is a basis for
$$
X,
$$
the image under
$$
e
$$
of every open subset of
$$
X
$$
is a union of the open sets
$$
e(B).
$$
Hence
$$
e:X\to e(X)
$$
is an open bijection. Its inverse is therefore continuous.

:::

:::

::: {.pf-step #s1-8}

Taking
$$
\kappa=\cardinality{\mathcal B},
$$
the space $X$ is homeomorphic to a subspace of
$$
\{0,1\}^{\kappa}.
$$


::: pf-proof

Step [](#s1-7){.pf-ref} embeds
$$
X
$$
homeomorphically as
$$
e(X)
\subseteq
\{0,1\}^{\mathcal B}.
$$
Any indexing set of cardinality
$$
\cardinality{\mathcal B}
$$
gives a canonically homeomorphic product, so this is a generalized Cantor cube of exponent
$$
\kappa=\cardinality{\mathcal B}.
$$

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that every subspace of a generalized Cantor space is zero-dimensional, and steps [](#s1-3){.pf-ref} through [](#s1-8){.pf-ref} embed every zero-dimensional space in one.

:::

:::

:::
