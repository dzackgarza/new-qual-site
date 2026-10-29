---
schema: qual/card@1
id: P-WESTOP11-3
kind: problem
title: Zorn's lemma and existence of maximal ideals
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
1. State Zorn's Lemma.
2. Use Zorn's Lemma to prove that every commutative ring with identity $1\ne0$ has a maximal ideal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Zorn's Lemma.**

Let
$$
(P,\le)
$$
be a partially ordered set. If every chain
$$
C\subseteq P
$$
has an upper bound in $P$, then $P$ contains a maximal element.


::: pf-proof

This is the statement of Zorn's Lemma. Here a chain means a totally ordered
subset of $P$, and an element $m\in P$ is maximal if
$$
m\le x
\quad\Longrightarrow\quad
x=m.
$$

:::

:::

::: {.pf-step #s1-2}

Let $R$ be a commutative ring with identity
$$
1\ne0.
$$
Let
$$
\mathcal P
\coloneqq
\{I\subset R:I\text{ is a proper ideal}\},
$$
ordered by inclusion.
Then
$$
\mathcal P\ne\varnothing.
$$


::: pf-proof

The zero ideal
$$
(0)
$$
is proper because
$$
1\ne0.
$$
Hence
$$
(0)\in\mathcal P.
$$

:::

:::

::: {.pf-step #s1-3}

Let
$$
\mathcal C\subseteq\mathcal P
$$
be a chain. Define
$$
J
\coloneqq
\bigcup_{I\in\mathcal C}I.
$$
Then $J$ is an ideal of $R$.


::: pf-proof

Let
$$
x,y\in J.
$$
Then there exist
$$
I_x,I_y\in\mathcal C
$$
with
$$
x\in I_x,
\qquad
y\in I_y.
$$
Since $\mathcal C$ is a chain, either
$$
I_x\subseteq I_y
$$
or
$$
I_y\subseteq I_x.
$$
Assume, without loss of generality,
$$
I_x\subseteq I_y.
$$
Then
$$
x,y\in I_y,
$$
so
$$
x-y\in I_y\subseteq J.
$$

If
$$
r\in R
$$
and
$$
x\in J,
$$
choose
$$
I\in\mathcal C
$$
with
$$
x\in I.
$$
Since $I$ is an ideal,
$$
rx\in I\subseteq J.
$$
Thus $J$ is an ideal.

:::

:::

::: {.pf-step #s1-4}

The ideal $J$ from step [](#s1-3){.pf-ref} is proper.


::: pf-proof

Suppose, toward a contradiction, that
$$
J=R.
$$
Then
$$
1\in J.
$$
By definition of the union, there would exist some
$$
I\in\mathcal C
$$
such that
$$
1\in I.
$$
But an ideal containing $1$ equals $R$, so
$$
I=R,
$$
contradicting
$$
I\in\mathcal P.
$$
Therefore
$$
J\ne R.
$$

:::

:::

::: {.pf-step #s1-5}

Hence every chain in $\mathcal P$ has an upper bound in
$\mathcal P$.


::: pf-proof

For a chain
$$
\mathcal C\subseteq\mathcal P,
$$
steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} show that
$$
J=\bigcup_{I\in\mathcal C}I
$$
is a proper ideal. Thus
$$
J\in\mathcal P.
$$
Moreover,
$$
I\subseteq J
\qquad
(I\in\mathcal C),
$$
so $J$ is an upper bound for the chain.

:::

:::

::: {.pf-step #s1-6}

By Zorn's Lemma, $\mathcal P$ contains a maximal element
$$
\mathfrak m.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} shows that $\mathcal P$ is nonempty, and step [](#s1-5){.pf-ref} verifies the
chain-upper-bound hypothesis of Zorn's Lemma. Apply step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

The ideal
$$
\mathfrak m
$$
is a maximal ideal of $R$.


::: pf-proof

By construction,
$$
\mathfrak m\ne R.
$$
Suppose
$$
\mathfrak m\subseteq I\subseteq R
$$
for some ideal $I$.

If
$$
I\ne R,
$$
then
$$
I\in\mathcal P.
$$
Since $\mathfrak m$ is maximal in $\mathcal P$,
$$
I=\mathfrak m.
$$
Thus there is no proper ideal strictly between
$$
\mathfrak m
$$
and
$$
R.
$$
This is exactly the definition of a maximal ideal.

:::

:::

::: {.pf-step #s1-8}

Therefore every commutative ring with identity
$$
1\ne0
$$
has a maximal ideal.


::: pf-proof

Step [](#s1-7){.pf-ref} constructs one.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} states Zorn's Lemma, and steps [](#s1-2){.pf-ref} through [](#s1-8){.pf-ref} apply it to prove the
maximal-ideal theorem.

:::

:::

:::
