---
schema: qual/card@1
id: P-KSRING17-042
kind: problem
title: Every proper ideal lies in a maximal ideal
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 42 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a non-zero ring with identity.
Show that every proper ideal of R is contained in a maximal ideal.
:::

Let
$$
I\trianglelefteq R
$$
be a proper ideal.
Define
$$
\mathcal P
\coloneqq
\{
J\trianglelefteq R:
I\subseteq J\subsetneq R
\},
$$
ordered by inclusion.

::: pf

::: pf-step

The partially ordered set $\mathcal P$ is nonempty.


::: pf-proof

The ideal
$$
I
$$
itself lies in $\mathcal P$, because it is proper by hypothesis.

:::

:::

::: pf-step

Let
$$
\mathcal C
\subseteq
\mathcal P
$$
be a chain.
Then
$$
U
\coloneqq
\bigcup_{J\in\mathcal C}J
$$
is an ideal of $R$.


::: pf-proof

The union is nonempty because every member of $\mathcal C$ contains $I$.

Let
$$
x,y\in U.
$$
Then
$$
x\in J_1,
\qquad
y\in J_2
$$
for some
$$
J_1,J_2\in\mathcal C.
$$
Because $\mathcal C$ is totally ordered by inclusion, one of these ideals contains the other. Thus both $x$ and $y$ lie in a common member of the chain, and therefore
$$
x-y\in U.
$$

If
$$
r\in R
$$
and
$$
x\in U,
$$
choose
$$
J\in\mathcal C
$$
with
$$
x\in J.
$$
Since $J$ is a two-sided ideal,
$$
rx,xr\in J\subseteq U.
$$
Hence $U$ is a two-sided ideal.

:::

:::

::: pf-step

The ideal $U$ from step <1>2 is proper.


::: pf-proof

Suppose
$$
U=R.
$$
Then
$$
1_R\in U.
$$
By the definition of the union, there exists
$$
J\in\mathcal C
$$
such that
$$
1_R\in J.
$$
But then
$$
J=R,
$$
contradicting
$$
J\in\mathcal P.
$$
Therefore
$$
U\subsetneq R.
$$

:::

:::

::: pf-step

The ideal $U$ is an upper bound for the chain $\mathcal C$ in $\mathcal P$.


::: pf-proof

Every member
$$
J\in\mathcal C
$$
is contained in the union $U$. Also
$$
I\subseteq U
$$
because $I$ is contained in every member of $\mathcal C$. By step <1>3, $U$ is proper. Hence
$$
U\in\mathcal P
$$
and is an upper bound for $\mathcal C$.

:::

:::

::: pf-step

The poset $\mathcal P$ has a maximal element.


::: pf-proof

By step <1>1, $\mathcal P$ is nonempty. By step <1>4, every chain in $\mathcal P$ has an upper bound in $\mathcal P$. Zorn's lemma therefore gives a maximal element
$$
M\in\mathcal P.
$$

:::

:::

::: pf-step

The ideal $M$ from step <1>5 is a maximal ideal of $R$ containing $I$.


::: pf-proof

By definition of $\mathcal P$,
$$
I\subseteq M\subsetneq R.
$$
Suppose
$$
M\subseteq J\subsetneq R
$$
for some ideal $J$ of $R$. Then
$$
I\subseteq J,
$$
so
$$
J\in\mathcal P.
$$
Maximality of $M$ in $\mathcal P$ forces
$$
J=M.
$$
Thus there is no proper ideal strictly between $M$ and $R$, so $M$ is maximal.

:::

:::

::: pf-step

Therefore every proper ideal is contained in a maximal ideal.


::: pf-proof

Starting from an arbitrary proper ideal $I$, step <1>6 constructs a maximal ideal $M$ with
$$
\boxed{
I\subseteq M.
}
$$

:::

:::

::: pf-qed

Step <1>7 is the required conclusion.

:::

:::
