---
schema: qual/card@1
id: P-WESTOP04-04
kind: problem
title: Definition of a covering space and uniqueness of a based lift
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Define a covering space. Let
$$
p:(E,e_0)\to(X,x_0)
$$
be a covering map and let
$$
f:(Y,y_0)\to(X,x_0)
$$
be continuous, where $Y$ is path-connected. Prove that there is at most one based lift
$$
\widetilde f:(Y,y_0)\to(E,e_0)
$$
satisfying
$$
p\circ\widetilde f=f.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A covering map is a continuous map
$$
p:E\to X
$$
such that every point
$$
x\in X
$$
has an open neighborhood
$$
U\subseteq X
$$
for which
$$
p^{-1}(U)
=
\bigsqcup_{\alpha\in A}V_\alpha
$$
is a disjoint union of open subsets of $E$, and each restriction
$$
p\restrict_{V_\alpha}:V_\alpha\longrightarrow U
$$
is a homeomorphism.


::: pf-proof

This is the definition of a covering space
$$
(E,p)
$$
over $X$. Such a neighborhood $U$ is called evenly covered.

:::

:::

::: pf-step

Let
$$
\widetilde f_0,\widetilde f_1:(Y,y_0)\to(E,e_0)
$$
be based lifts of $f$, so
$$
p\circ\widetilde f_0
=
f
=
p\circ\widetilde f_1
$$
and
$$
\widetilde f_0(y_0)
=
e_0
=
\widetilde f_1(y_0).
$$


::: pf-proof

These are arbitrary two candidate based lifts. It is enough to prove that they agree at every point of $Y$.

:::

:::

::: pf-step

Fix
$$
y\in Y.
$$
Since $Y$ is path-connected, there is a path
$$
\gamma:[0,1]\to Y
$$
with
$$
\gamma(0)=y_0,
\qquad
\gamma(1)=y.
$$


::: pf-proof

This is exactly the definition of path-connectedness.

:::

:::

::: {.pf-step #s1-4}

The paths
$$
\widetilde f_0\circ\gamma
\quad\text{and}\quad
\widetilde f_1\circ\gamma
$$
are lifts of the same path
$$
f\circ\gamma
$$
through $p$ and have the same initial point $e_0$.


::: pf-proof

For $j=0,1$,
$$
p\circ(\widetilde f_j\circ\gamma)
=
(p\circ\widetilde f_j)\circ\gamma
=
f\circ\gamma.
$$
Also,
$$
(\widetilde f_j\circ\gamma)(0)
=
\widetilde f_j(y_0)
=
e_0.
$$

:::

:::

::: {.pf-step #s1-5}

By uniqueness of path lifting,
$$
\widetilde f_0\circ\gamma
=
\widetilde f_1\circ\gamma.
$$


::: pf-proof

For a covering map, a path in the base has at most one lift with a prescribed starting point. Step [](#s1-4){.pf-ref} gives two lifts with the same starting point, so they coincide.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\widetilde f_0(y)
=
\widetilde f_1(y).
$$


::: pf-proof

Evaluate the equality from step [](#s1-5){.pf-ref} at
$$
t=1.
$$
Since
$$
\gamma(1)=y,
$$
the two endpoint values are exactly
$$
\widetilde f_0(y)
\quad\text{and}\quad
\widetilde f_1(y).
$$

:::

:::

::: {.pf-step #s1-7}

Hence
$$
\boxed{
\widetilde f_0
=
\widetilde f_1}.
$$


::: pf-proof

The point
$$
y\in Y
$$
was arbitrary. Step [](#s1-6){.pf-ref} therefore proves equality at every point of $Y$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition, and step [](#s1-7){.pf-ref} proves uniqueness of a based lift.

:::

:::

:::
