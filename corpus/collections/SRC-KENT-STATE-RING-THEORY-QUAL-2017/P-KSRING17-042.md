---
schema: qual/card@1
id: P-KSRING17-042
kind: problem
title: Every proper ideal lies in a maximal ideal
classification:
  areas: [algebra]
  topics:
  - Maximal Ideals
  - Zorn's Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 42 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a nonzero ring with identity.
Show that every proper ideal of $R$ is contained in a maximal ideal.
:::

::: {.solution}

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

::: {.pf-step #s1-1}

The partially ordered set $\mathcal P$ is nonempty.


::: pf-proof

The ideal
$$
I
$$
itself lies in $\mathcal P$, because it is proper by hypothesis.

:::

:::

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

The ideal $U$ from step [](#s1-2){.pf-ref} is proper.


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

::: {.pf-step #s1-4}

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
because $I$ is contained in every member of $\mathcal C$. By step [](#s1-3){.pf-ref}, $U$ is proper. Hence
$$
U\in\mathcal P
$$
and is an upper bound for $\mathcal C$.

:::

:::

::: {.pf-step #s1-5}

The poset $\mathcal P$ has a maximal element.


::: pf-proof

By step [](#s1-1){.pf-ref}, $\mathcal P$ is nonempty. By step [](#s1-4){.pf-ref}, every chain in $\mathcal P$ has an upper bound in $\mathcal P$. Zorn's lemma therefore gives a maximal element
$$
M\in\mathcal P.
$$

:::

:::

::: {.pf-step #s1-6}

The ideal $M$ from step [](#s1-5){.pf-ref} is a maximal ideal of $R$ containing $I$.


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

::: {.pf-step #s1-7}

Therefore every proper ideal is contained in a maximal ideal.


::: pf-proof

Starting from an arbitrary proper ideal $I$, step [](#s1-6){.pf-ref} constructs a maximal ideal $M$ with
$$
\boxed{
I\subseteq M.
}
$$

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::

::: {.remark}
Smith's exercise (Noetherian rings 7) asks for this with Zorn's lemma for "every ideal".
The unit ideal $R$ lies in no maximal ideal, since maximal ideals are proper, so the statement holds for proper ideals.
:::
