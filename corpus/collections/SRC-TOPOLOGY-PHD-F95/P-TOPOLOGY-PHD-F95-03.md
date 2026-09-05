---
schema: qual/card@1
id: P-TOPOLOGY-PHD-F95-03
kind: problem
title: Products of closed sets and the product topology
classification:
  areas:
  - topology
  topics:
  - Product Topology
  - Closure
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-06
  note: Checked all three parts against Section I, problem 3 of the 23 September 1995 topology qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-06
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-06
  note: >-
    Used coordinate projections for closedness, basic neighborhoods for the
    closure identity, and an infinite-product counterexample for openness.
---

::: {.problem}
Let $I$ be a non empty index set, let $\{X_\alpha\mid\alpha\in I\}$ be a family of topological spaces, and let $A_\alpha\subset X_\alpha$ for each $\alpha$.

(a) Show that if $A_\alpha$ is closed in $X_\alpha$ for each $\alpha$, then $\prod A_\alpha$ is closed in $\prod X_\alpha$.

(b) Show that $\overline{\prod A_\alpha}=\prod\overline{A_\alpha}$.

(c) Prove or disprove: If $A_\alpha$ is open in $X_\alpha$ for each $\alpha$, then $\prod A_\alpha$ is open in $\prod X_\alpha$.
:::

::: {.solution}
Write
\[
X=\prod_{\alpha\in I}X_\alpha,
\qquad
A=\prod_{\alpha\in I}A_\alpha,
\]
and let $\pi_\alpha:X\to X_\alpha$ denote the coordinate projection.
We use the usual ZFC convention for arbitrary products.

<1>1. If every $A_\alpha$ is closed in $X_\alpha$, then $A$ is closed in $X$.
::: {.proof}
For every $\alpha\in I$, the coordinate projection $\pi_\alpha$ is continuous in the product topology.
Hence
\[
\pi_\alpha^{-1}(A_\alpha)
\]
is closed in $X$ whenever $A_\alpha$ is closed in $X_\alpha$.
Moreover,
\[
A
=\prod_{\alpha\in I}A_\alpha
=\bigcap_{\alpha\in I}\pi_\alpha^{-1}(A_\alpha).
\]
An arbitrary intersection of closed sets is closed, so $A$ is closed in $X$.
:::

<1>2. One always has
\[
\overline{A}\subseteq\prod_{\alpha\in I}\overline{A_\alpha}.
\]
::: {.proof}
For each $\alpha$,
\[
A_\alpha\subseteq\overline{A_\alpha},
\]
so
\[
A\subseteq\prod_{\alpha\in I}\overline{A_\alpha}.
\]
By <1>1, the product on the right is closed in $X$ because every $\overline{A_\alpha}$ is closed.
Since $\overline A$ is the smallest closed subset of $X$ containing $A$, the claimed inclusion follows.
:::

<1>3. Conversely,
\[
\prod_{\alpha\in I}\overline{A_\alpha}\subseteq\overline A.
\]
::: {.proof}
If the product on the left is empty, there is nothing to prove.
Otherwise let
\[
x=(x_\alpha)_{\alpha\in I}\in\prod_{\alpha\in I}\overline{A_\alpha}.
\]
Then every $A_\alpha$ is nonempty.
Choose once and for all a point
\[
b=(b_\alpha)_{\alpha\in I}\in\prod_{\alpha\in I}A_\alpha;
\]
this is the only place where the usual axiom-of-choice convention for an arbitrary family is used.

Let $U$ be any open neighborhood of $x$ in $X$.
By the definition of the product topology, $U$ contains a basic neighborhood
\[
V=\bigcap_{\alpha\in F}\pi_\alpha^{-1}(U_\alpha),
\]
where $F\subseteq I$ is finite and each $U_\alpha$ is an open neighborhood of $x_\alpha$ in $X_\alpha$.
Since
\[
x_\alpha\in\overline{A_\alpha},
\]
every $U_\alpha$ with $\alpha\in F$ meets $A_\alpha$.
Choose
\[
a_\alpha\in U_\alpha\cap A_\alpha
\qquad(\alpha\in F).
\]
Define $y=(y_\alpha)_{\alpha\in I}$ by
\[
y_\alpha=
\begin{cases}
a_\alpha,&\alpha\in F,\\b_\alpha,&\alpha\notin F.\end{cases}
\]
Then $y\in A$ and $y\in V\subseteq U$.
Thus every neighborhood of $x$ meets $A$, so $x\in\overline A$.
:::

<1>4. Therefore
\[
\boxed{\overline{\prod_{\alpha\in I}A_\alpha}
=\prod_{\alpha\in I}\overline{A_\alpha}}.
\]
::: {.proof}
Combine <1>2 and <1>3.
:::

<1>5. The assertion in part (c) is false for an infinite index set.
::: {.proof}
Take
\[
I=\NN,
\qquad
X_n=\RR,
\qquad
A_n=(-1,1)
\]
for every $n\in\NN$.
Each $A_n$ is open in $X_n$.
Let
\[
A=\prod_{n\in\NN}(-1,1)\subseteq\RR^{\NN}
\]
with the product topology.
The zero sequence $0=(0,0,\ldots)$ lies in $A$.

Suppose $A$ were open.
Then some basic open neighborhood $V$ of $0$ would satisfy
\[
0\in V\subseteq A.
\]
A basic neighborhood in the product topology restricts only finitely many coordinates, so there is a finite set $F\subset\NN$ such that all coordinates outside $F$ are unrestricted.
Choose $m\notin F$ and define $y\in\RR^{\NN}$ by
\[
y_m=2,
\qquad
y_n=0\quad(n\ne m).
\]
Then $y\in V$, because its only nonzero coordinate is unrestricted, but $y\notin A$ because $y_m=2\notin(-1,1)$.
This contradicts $V\subseteq A$.
Hence $A$ is not open.

For comparison, if $I$ is finite, then a product of open subsets is open; more generally, a product $\prod A_\alpha$ with all $A_\alpha$ open is a basic open set whenever $A_\alpha=X_\alpha$ for all but finitely many $\alpha$.
:::
:::
