---
schema: qual/card@1
id: P-KSRING17-014
kind: problem
title: Ideals of a valuation ring are totally ordered
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 14 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a subring of a field $F$ such that for each $x$ in $F$ either $x \in R$ or $x^{-1} \in R$. Prove that if $I$ and $J$ are two ideals of $R$, then either $I \subseteq J$ or $J \subseteq I$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that neither
$$
I\subseteq J
$$
nor
$$
J\subseteq I.
$$
Then there exist
$$
a\in I\setminus J,
\qquad
b\in J\setminus I.
$$


::: pf-proof

Failure of
$$
I\subseteq J
$$
means that some
$$
a\in I
$$
does not lie in $J$. Failure of
$$
J\subseteq I
$$
similarly gives
$$
b\in J\setminus I.
$$
Since
$$
0\in I\cap J,
$$
both $a$ and $b$ are nonzero.

:::

:::

::: {.pf-step #s1-2}

The element
$$
\frac ab\in F
$$
satisfies either
$$
\frac ab\in R
$$
or
$$
\frac ba\in R.
$$


::: pf-proof

Apply the defining hypothesis on $R\subseteq F$ to the nonzero field element
$$
x=\frac ab.
$$
Either
$$
x\in R
$$
or
$$
x^{-1}=\frac ba\in R.
$$

:::

:::

::: {.pf-step #s1-3}

The first alternative in step [](#s1-2){.pf-ref} is impossible.


::: pf-proof

If
$$
\frac ab\in R,
$$
then, since
$$
b\in J
$$
and $J$ is an ideal,
$$
a
=
\left(\frac ab\right)b
\in J.
$$
This contradicts
$$
a\notin J.
$$

:::

:::

::: {.pf-step #s1-4}

The second alternative in step [](#s1-2){.pf-ref} is impossible.


::: pf-proof

If
$$
\frac ba\in R,
$$
then, since
$$
a\in I
$$
and $I$ is an ideal,
$$
b
=
\left(\frac ba\right)a
\in I.
$$
This contradicts
$$
b\notin I.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
I\subseteq J
\quad\text{or}\quad
J\subseteq I.
}
$$


::: pf-proof

If the two ideals were incomparable, step [](#s1-1){.pf-ref} would produce $a,b$, while step [](#s1-2){.pf-ref} says one of the two alternatives in steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} must hold. Both alternatives are impossible. Hence the ideals are comparable.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
