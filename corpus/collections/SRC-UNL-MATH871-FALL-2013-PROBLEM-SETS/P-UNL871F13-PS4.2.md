---
schema: qual/card@1
id: P-UNL871F13-PS4.2
kind: problem
title: Restrictions of closed maps and non-closed product projections
classification:
  areas: [topology]
  topics: [Continuity, Product Topology]
relations: []
review: draft
---

::: {.problem}
A map $f:X\to Y$ is called closed if $f(F)$ is closed in $Y$ for every closed subset $F\subseteq X$.

1. Suppose $f:X\to Y$ is closed and $f(X)\subseteq B\subseteq Y$.
   Show that the corestriction
   \[
   f^B:X\to B
   \]
   is a closed map when $B$ has the subspace topology.

2. Let $\{X_\alpha\}_{\alpha\in I}$ be topological spaces and give $\prod_{\alpha\in I}X_\alpha$ the product topology.
   Show by example that a coordinate projection
   \[
   \pi_\beta:\prod_{\alpha\in I}X_\alpha\to X_\beta
   \]
   need not be a closed map.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose
\[
f:X\to Y
\]
is closed and
\[
f(X)\subseteq B\subseteq Y.
\]
Let
\[
f^B:X\to B
\]
be the corestriction.
Then
\[
\boxed{
f^B\text{ is closed}.
}
\]


::: pf-proof

Let
\[
F\subseteq X
\]
be closed.
Since $f$ is a closed map,
\[
f(F)
\]
is closed in $Y$.

Because
\[
f(F)\subseteq f(X)\subseteq B,
\]
the image under the corestriction is the same set:
\[
f^B(F)
=
f(F).
\]

In the subspace topology on $B$,
\[
f(F)
=
B\cap f(F).
\]
The right-hand side is the intersection of $B$ with a closed subset of $Y$,
so it is closed in $B$.
Thus every closed subset of $X$ has closed image under $f^B$.

:::

:::

::: {.pf-step #s1-2}

Coordinate projections from products need not be closed.


::: pf-proof

Take
\[
X_1=X_2=\RR
\]
with the usual topology and consider
\[
\pi_1:
\RR^2
\to
\RR,
\qquad
\pi_1(x,y)=x.
\]

Let
\[
F
\coloneqq
\{(x,y)\in\RR^2:xy=1\}.
\]
The function
\[
\varphi:\RR^2\to\RR,
\qquad
\varphi(x,y)=xy
\]
is continuous, and
\[
F
=
\varphi^{-1}(\{1\}).
\]
Since
\[
\{1\}
\]
is closed in $mathbb R$, the set $F$ is closed in $mathbb R^2$.

Its projection is
\[
\pi_1(F)
=
\RR\setminus\{0\},
\]
because for every
\[
x\ne0
\]
the point
\[
(x,1/x)
\]
lies in $F$, while no point of $F$ has first coordinate $0$.

But
\[
\RR\setminus\{0\}
\]
is not closed in $mathbb R$, since
\[
0
\]
is a limit point.
Therefore
\[
\pi_1
\]
is not a closed map.

:::

:::

::: pf-step

Thus the answer is:

1. corestricting a closed map to any subspace containing its image preserves
   closedness;
2. coordinate projections in product spaces need not be closed.


::: pf-proof

This is exactly the content of steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves part (1), and step [](#s1-2){.pf-ref} supplies the required counterexample
for part (2).

:::

:::

:::
