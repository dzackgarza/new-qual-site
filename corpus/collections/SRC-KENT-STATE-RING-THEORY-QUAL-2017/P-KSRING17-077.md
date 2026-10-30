---
schema: qual/card@1
id: P-KSRING17-077
kind: problem
title: Nonzero ideals of an integral extension of domains contract to nonzero ideals
classification:
  areas: [algebra]
  topics:
  - Integral Extensions
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 77 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R\subseteq S$ be commutative domains with the same identity, and assume that $S$ is an integral extension of $R$.
Let $I$ be a nonzero ideal of $S$.
Prove that $I\cap R$ is a nonzero ideal of $R$.
:::

::: {.solution}

::: pf

::: pf-step

Choose
$$
0\ne s\in I.
$$


::: pf-proof

The ideal
$$
I
$$
is nonzero by hypothesis, so it contains a nonzero element.

:::

:::

::: {.pf-step #s1-2}

Since $s$ is integral over $R$, there exists a monic relation
$$
s^n+a_{n-1}s^{n-1}+\cdots+a_1s+a_0=0
$$
with
$$
a_i\in R.
$$
Choose such a relation with $n$ minimal.


::: pf-proof

Integrality of
$$
S
$$
over
$$
R
$$
means every element of $S$, in particular $s$, satisfies some monic polynomial over $R$.
The positive integers are well ordered, so among all such monic relations one has minimal degree.

:::

:::

::: {.pf-step #s1-3}

The constant coefficient
$$
a_0
$$
is nonzero.


::: pf-proof

Suppose
$$
a_0=0.
$$
Then the relation in step [](#s1-2){.pf-ref} becomes
$$
s
\left(
s^{n-1}
+a_{n-1}s^{n-2}
+\cdots
+a_1
\right)
=
0.
$$
Because
$$
S
$$
is an integral domain and
$$
s\ne0,
$$
one may cancel $s$ to obtain
$$
s^{n-1}
+a_{n-1}s^{n-2}
+\cdots
+a_1
=
0.
$$
This is a monic relation for $s$ of degree
$$
n-1,
$$
contradicting minimality of $n$.
Therefore
$$
a_0\ne0.
$$

:::

:::

::: {.pf-step #s1-4}

The element
$$
a_0
$$
belongs to $I$.


::: pf-proof

Rearrange the relation from step [](#s1-2){.pf-ref}:
$$
a_0
=
-s
\left(
s^{n-1}
+a_{n-1}s^{n-2}
+\cdots
+a_1
\right).
$$
Since
$$
s\in I
$$
and $I$ is an ideal of $S$, the right-hand side lies in $I$.
Thus
$$
a_0\in I.
$$

:::

:::

::: {.pf-step #s1-5}

The element
$$
a_0
$$
belongs to
$$
I\cap R
$$
and is nonzero.


::: pf-proof

By construction in step [](#s1-2){.pf-ref},
$$
a_0\in R.
$$
By step [](#s1-4){.pf-ref},
$$
a_0\in I.
$$
Hence
$$
a_0\in I\cap R.
$$
Step [](#s1-3){.pf-ref} gives
$$
a_0\ne0.
$$

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
I\cap R
\ne
(0).
}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} exhibits a nonzero element of the intersection.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
