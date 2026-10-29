---
schema: qual/card@1
id: P-WESTOP10-I4
kind: problem
title: Examples separating connectedness, metrizability, countability, and regularity properties
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Give an infinite space satisfying each requested combination of properties:

1. connected, but neither path-connected nor metrizable;

2. normal, Hausdorff, and first countable, but neither metrizable nor connected;

3. metrizable, first countable, and second countable;

4. completely regular, but neither compact, connected, nor first countable.
:::

::: {.solution}

Write
$$
S_\Omega
$$
for the long ray without its final endpoint and
$$
\overline{S_\Omega}
=
S_\Omega\cup\{\Omega\}
$$
for the closed long ray.

::: pf

::: {.pf-step #s1-1}

For item (1), take
$$
\boxed{
X_1=\overline{S_\Omega}.
}
$$


::: pf-proof

The preceding problem establishes that the closed long ray is connected.

It is not path-connected because the final point
$$
\Omega
$$
cannot be joined by a path to any point below it: a path image is separable, while any connected subset containing both a point
$$
x<\Omega
$$
and
$$
\Omega
$$
must contain the nonseparable interval
$$
[x,\Omega].
$$

It is not metrizable because it is not first countable at
$$
\Omega,
$$
whereas every metric space is first countable.

Thus $X_1$ is infinite, connected, neither path-connected nor metrizable.

:::

:::

::: {.pf-step #s1-2}

The open long ray
$$
S_\Omega
$$
is Hausdorff, normal, and first countable.


::: pf-proof

It is a linearly ordered topological space, hence Hausdorff and hereditarily normal.

Every point of
$$
S_\Omega
$$
lies below a countable ordinal stage.
Locally the long ray is homeomorphic to an interval in
$$
\RR
$$
(with a half-interval at its initial endpoint).
Therefore every point has a countable neighborhood base.
Hence
$$
S_\Omega
$$
is first countable.

:::

:::

::: {.pf-step #s1-3}

The open long ray is not compact.


::: pf-proof

For each
$$
\alpha<\omega_1,
$$
let
$$
U_\alpha
$$
be the initial open segment consisting of points whose ordinal coordinate is less than
$$
\alpha+1.
$$
These sets form an open cover of
$$
S_\Omega.
$$
Any finite subfamily has a largest ordinal index and therefore covers only a bounded initial segment of the long ray.
Thus there is no finite subcover.

:::

:::

::: {.pf-step #s1-4}

Every sequence in
$$
S_\Omega
$$
has a convergent subsequence.


::: pf-proof

Let
$$
(x_n)
$$
be a sequence in the long ray.
The set of ordinal coordinates appearing among the $x_n$ is countable, so its supremum is some countable ordinal
$$
\beta<\omega_1.
$$
Hence the whole sequence lies in a closed bounded interval
$$
[0,b]
\subset S_\Omega
$$
for a point $b$ above the $\beta$th stage.

Such a closed order interval is compact and metrizable because it involves only countably many ordinal stages.
Therefore
$$
(x_n)
$$
has a convergent subsequence.

:::

:::

::: {.pf-step #s1-5}

The open long ray is not metrizable.


::: pf-proof

Suppose
$$
S_\Omega
$$
were metrizable.
By step [](#s1-4){.pf-ref} it would be sequentially compact.
For metric spaces, sequential compactness implies compactness.
This contradicts step [](#s1-3){.pf-ref}. Thus the long ray is not metrizable.

:::

:::

::: {.pf-step #s1-6}

For item (2), take the topological disjoint union
$$
\boxed{
X_2
=
S_\Omega
\sqcup
S_\Omega.
}
$$


::: pf-proof

Each summand is Hausdorff, normal, and first countable by step [](#s1-2){.pf-ref}. Topological disjoint unions preserve these three properties: each component is open and closed, so neighborhoods and separation can be constructed componentwise.

The space $X_2$ is disconnected because it is the union of two nonempty disjoint clopen summands.

If $X_2$ were metrizable, each clopen subspace
$$
S_\Omega
$$
would be metrizable.
This contradicts step [](#s1-5){.pf-ref}.

Hence $X_2$ is normal, Hausdorff, first countable, neither metrizable nor connected.

:::

:::

::: {.pf-step #s1-7}

For item (3), take
$$
\boxed{
X_3=\RR
}
$$
with its usual topology.


::: pf-proof

The Euclidean metric makes
$$
\RR
$$
metrizable.
Every metric space is first countable.

A countable basis is given by intervals
$$
(p,q),
\qquad
p,q\in\QQ,
\quad
p<q.
$$
Thus
$$
\RR
$$
is also second countable.

:::

:::

::: {.pf-step #s1-8}

For item (4), take
$$
\boxed{
X_4
=
\overline{S_\Omega}
\sqcup
\NN,
}
$$
where
$$
\NN
$$
has the discrete topology.


::: pf-proof

The closed long ray is completely regular, and every discrete space is completely regular.
Topological sums of completely regular spaces are completely regular: a point and a disjoint closed set can be separated inside the component containing the point, and the separating function can be defined componentwise on the other clopen components.
Hence $X_4$ is completely regular.

It is disconnected because the two summands are nonempty clopen subsets.

It is not first countable because the point
$$
\Omega
$$
in the closed-long-ray summand has no countable local base.
A local base in the topological sum would restrict to one in that clopen summand.

Finally, $X_4$ is not compact.
The family
$$
\left\{
\overline{S_\Omega}
\right\}
\cup
\left\{
\{n\}:n\in\NN
\right\}
$$
is an open cover of $X_4$ with no finite subcover.

:::

:::

::: {.pf-step #s1-9}

Thus the four requested examples are
$$
\boxed{
\begin{array}{c|l}
1&\overline{S_\Omega},\\
2&S_\Omega\sqcup S_\Omega,\\
3&\RR,\\
4&\overline{S_\Omega}\sqcup\NN.
\end{array}
}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref}, [](#s1-6){.pf-ref}, and [](#s1-7){.pf-ref}, and [](#s1-8){.pf-ref} verify all requested property combinations.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} records the complete answer.

:::

:::

:::
