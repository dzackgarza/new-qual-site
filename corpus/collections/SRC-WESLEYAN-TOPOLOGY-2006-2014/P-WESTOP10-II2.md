---
schema: qual/card@1
id: P-WESTOP10-II2
kind: problem
title: Hausdorff and compactness properties of a covering-space total space
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Let $(\widetilde X,p)$ be a covering space of $X$.

1. Show that if $X$ is Hausdorff, then $\widetilde X$ is Hausdorff.
2. Show that if $X$ is compact and $p^{-1}(x)$ is finite for each $x\in X$, then $X$ is compact.
:::

::: {.remark}
Part 2 is printed as above, with $X$ in the conclusion. The conclusion repeats the hypothesis; the intended conclusion is that $\widetilde X$ is compact, and the solution proves both readings.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Assume
$$
X
$$
is Hausdorff.
Let
$$
\widetilde x_1,
\widetilde x_2
\in
\widetilde X
$$
be distinct.


::: pf-proof

To prove that
$$
\widetilde X
$$
is Hausdorff, it suffices to separate arbitrary distinct points by disjoint
open neighborhoods.

:::

:::

::: {.pf-step #s1-2}

If
$$
p(\widetilde x_1)
\ne
p(\widetilde x_2),
$$
then
$$
\widetilde x_1
$$
and
$$
\widetilde x_2
$$
have disjoint open neighborhoods in
$$
\widetilde X.
$$


::: pf-proof

Since $X$ is Hausdorff, choose disjoint open sets
$$
U_1,U_2\subseteq X
$$
with
$$
p(\widetilde x_j)\in U_j.
$$
Then
$$
p^{-1}(U_1)
\qquad\text{and}\qquad
p^{-1}(U_2)
$$
are disjoint open subsets of
$$
\widetilde X
$$
containing
$$
\widetilde x_1
\qquad\text{and}\qquad
\widetilde x_2,
$$
respectively.

:::

:::

::: {.pf-step #s1-3}

If
$$
p(\widetilde x_1)
=
p(\widetilde x_2)
=
x,
$$
then
$$
\widetilde x_1
$$
and
$$
\widetilde x_2
$$
also have disjoint open neighborhoods.


::: pf-proof

Choose an evenly covered neighborhood
$$
U\ni x.
$$
Then
$$
p^{-1}(U)
=
\bigsqcup_{\lambda\in\Lambda}
V_\lambda,
$$
where each
$$
p\restrict_{V_\lambda}:V_\lambda\to U
$$
is a homeomorphism.

Each sheet contains exactly one point of the fiber over $x$.
Since
$$
\widetilde x_1\ne\widetilde x_2,
$$
they lie in distinct sheets
$$
V_{\lambda_1}
\qquad\text{and}\qquad
V_{\lambda_2}.
$$
These are disjoint open neighborhoods.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
X\text{ Hausdorff}
\quad\Longrightarrow\quad
\widetilde X\text{ Hausdorff}.
}
$$


::: pf-proof

Steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} cover the two possible cases for two distinct points of
$$
\widetilde X.
$$

:::

:::

::: {.pf-step #s1-5}

The literal second statement in the source is tautological.


::: pf-proof

Its hypotheses already include
$$
X\text{ is compact}.
$$
Its conclusion is again
$$
X\text{ is compact}.
$$
Thus no proof beyond repeating the hypothesis is needed.

:::

:::

::: {.pf-step #s1-6}

The standard intended theorem is:

if
$$
X
$$
is compact and every fiber
$$
p^{-1}(x)
$$
is finite, then
$$
\boxed{
\widetilde X
\text{ is compact}.
}
$$


::: pf-proof

We prove this in steps [](#s1-7){.pf-ref} through [](#s1-12){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Let
$$
\mathcal O
$$
be an arbitrary open cover of
$$
\widetilde X.
$$
Fix
$$
x\in X
$$
and choose an evenly covered neighborhood
$$
U\ni x.
$$


::: pf-proof

Such a neighborhood exists by the definition of a covering map.

:::

:::

::: {.pf-step #s1-8}

Because
$$
p^{-1}(x)
$$
is finite, the evenly covered set
$$
p^{-1}(U)
$$
has only finitely many sheets.


::: pf-proof

Every sheet
$$
V_\lambda
$$
over $U$ maps homeomorphically onto $U$ and therefore contains exactly one
point of the fiber over $x$.
Conversely, every point of the fiber lies in exactly one sheet.
Thus the set of sheets is in bijection with
$$
p^{-1}(x),
$$
which is finite.

:::

:::

::: {.pf-step #s1-9}

Enumerate the sheets as
$$
V_1,\dots,V_m,
$$
and let
$$
\widetilde x_j
$$
be the unique point of
$$
V_j\cap p^{-1}(x).
$$
Choose
$$
O_j\in\mathcal O
$$
with
$$
\widetilde x_j\in O_j.
$$


::: pf-proof

The cover
$$
\mathcal O
$$
covers every point of
$$
\widetilde X,
$$
in particular each fiber point.

:::

:::

::: {.pf-step #s1-10}

For each $j$, there is an open neighborhood
$$
W_j\subseteq U
$$
of $x$ such that
$$
(p\restrict_{V_j})^{-1}(W_j)
\subseteq
O_j.
$$


::: pf-proof

The set
$$
O_j\cap V_j
$$
is open in the sheet $V_j$ and contains
$$
\widetilde x_j.
$$
Since
$$
p\restrict_{V_j}:V_j\xrightarrow{\cong}U
$$
is a homeomorphism, its image
$$
W_j
\coloneqq
p(O_j\cap V_j)
$$
is open in $U$ and contains
$$
x.
$$
By construction,
$$
(p\restrict_{V_j})^{-1}(W_j)
=
O_j\cap V_j
\subseteq
O_j.
$$

:::

:::

::: {.pf-step #s1-11}

Define
$$
W_x
\coloneqq
W_1\cap\cdots\cap W_m.
$$
Then
$$
W_x
$$
is an open neighborhood of $x$, and
$$
p^{-1}(W_x)
$$
is covered by the finite family
$$
O_1,\dots,O_m.
$$


::: pf-proof

The intersection is finite, so $W_x$ is open and contains $x$.

For every sheet $V_j$,
$$
(p\restrict_{V_j})^{-1}(W_x)
\subseteq
(p\restrict_{V_j})^{-1}(W_j)
\subseteq
O_j.
$$
Since the sheets exhaust
$$
p^{-1}(U),
$$
and
$$
W_x\subseteq U,
$$
the full inverse image
$$
p^{-1}(W_x)
$$
is contained in
$$
O_1\cup\cdots\cup O_m.
$$

:::

:::

::: {.pf-step #s1-12}

Compactness of $X$ gives a finite subcover of
$$
\widetilde X
$$
from
$$
\mathcal O.
$$


::: pf-proof

The neighborhoods
$$
\{W_x:x\in X\}
$$
form an open cover of $X$.
Since $X$ is compact, choose
$$
x_1,\dots,x_r
$$
such that
$$
X
=
W_{x_1}
\cup\cdots\cup
W_{x_r}.
$$

For each $k$, step [](#s1-11){.pf-ref} gives finitely many members of
$$
\mathcal O
$$
covering
$$
p^{-1}(W_{x_k}).
$$
The union of these finitely many finite families is finite and covers
$$
\begin{aligned}
\widetilde X
&=
p^{-1}(X)\\
&=
\bigcup_{k=1}^r
p^{-1}(W_{x_k}).
\end{aligned}
$$
Thus every open cover of
$$
\widetilde X
$$
has a finite subcover.

:::

:::

::: {.pf-step #s1-13}

Hence, under the standard intended reading,
$$
\boxed{
X\text{ compact and all fibers finite}
\quad\Longrightarrow\quad
\widetilde X\text{ compact}.
}
$$


::: pf-proof

Step [](#s1-12){.pf-ref} proves compactness of the total space.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} prove the Hausdorff assertion.
Step [](#s1-5){.pf-ref} answers the literal repeated compactness statement.
Steps [](#s1-6){.pf-ref} through [](#s1-13){.pf-ref} prove the standard intended finite-sheeted compactness
theorem.

:::

:::

:::
