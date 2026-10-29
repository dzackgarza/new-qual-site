---
schema: qual/card@1
id: P-WESTOP12-3
kind: problem
title: Continuous images of Hausdorff and connected spaces
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Prove or disprove each statement:

1. The image of a Hausdorff space under a continuous map is Hausdorff.
2. The image of a connected space under a continuous map is connected.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Statement (1) is false.


::: pf-proof

Let
$$
X=\{0,1\}
$$
with the discrete topology.
Then $X$ is Hausdorff.

Let
$$
Y=\{0,1\}
$$
with the indiscrete topology
$$
\{\varnothing,Y\}.
$$
Then $Y$ is not Hausdorff, since the two distinct points have no disjoint
nonempty open neighborhoods.

Consider the identity set map
$$
f:X\to Y,
\qquad
f(x)=x.
$$
It is continuous because the only open subsets of $Y$ are
$$
\varnothing
$$
and
$$
Y,
$$
whose preimages are open in $X$.

The image is
$$
f(X)=Y,
$$
which is not Hausdorff.
Thus a continuous image of a Hausdorff space need not be Hausdorff.

:::

:::

::: {.pf-step #s1-2}

Statement (2) is true.


::: pf-proof

Let
$$
f:X\to Y
$$
be continuous and suppose $X$ is connected.
We prove
$$
f(X)
$$
is connected in the subspace topology.

Suppose, toward a contradiction, that
$$
f(X)=U\sqcup V
$$
where $U,V$ are disjoint nonempty open subsets of the subspace $f(X)$.

Then
$$
f^{-1}(U)
$$
and
$$
f^{-1}(V)
$$
are open in $X$ because $f$, regarded as a map
$$
X\to f(X),
$$
is continuous.

They are disjoint, nonempty, and
$$
X
=
f^{-1}(U)
\cup
f^{-1}(V).
$$
This is a separation of $X$, contradicting connectedness.

Therefore
$$
\boxed{
f(X)
\text{ is connected}.
}
$$

:::

:::

::: {.pf-step #s1-3}

The final answers are:
$$
\boxed{
\begin{array}{c|cc}
\text{statement}&1&2\\
\hline
\text{true?}&\mathrm{no}&\mathrm{yes}
\end{array}
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives a counterexample to statement (1), and step [](#s1-2){.pf-ref} proves
statement (2).

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} records both conclusions.

:::

:::

:::
