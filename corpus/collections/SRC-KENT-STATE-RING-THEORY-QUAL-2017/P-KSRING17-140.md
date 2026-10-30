---
schema: qual/card@1
id: P-KSRING17-140
kind: problem
title: Ideals in a Noetherian ring contain products of primes containing them
classification:
  areas: [algebra]
  topics:
  - Noetherian Rings
  - Prime Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 140 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source says every nonzero ideal; $A=R$ is contained in no prime ideal. The statement now says every nonzero proper ideal.
---

::: {.problem}
Let R be a commutative Noetherian ring.
Prove that every nonzero proper ideal A of R contains a product of prime ideals (not necessarily distinct) each of which contains A.
:::

::: {.solution}

Call a nonzero proper ideal
$$
I\trianglelefteq R
$$
\dfn{good} if there exist prime ideals
$$
P_1,\ldots,P_m
$$
with
$$
m\ge1,
\qquad
I\subseteq P_j
\quad
\text{for every }j,
$$
and
$$
P_1P_2\cdots P_m
\subseteq
I.
$$

::: pf

::: pf-step

Suppose, for contradiction, that some nonzero proper ideal is not good.
Let
$$
\mathcal B
\coloneqq
\{
I\trianglelefteq R:
I\ne(0),\ I\ne R,\ I\text{ is not good}
\}.
$$
Then $\mathcal B$ is nonempty.


::: pf-proof

This is exactly the negation of the corrected statement.

:::

:::

::: pf-step

The set $\mathcal B$ has a maximal element under inclusion.


::: pf-proof

Since $R$ is Noetherian, its ideals satisfy the ascending chain condition.
If $\mathcal B$ had no maximal element, one could construct a strictly increasing infinite chain
$$
I_1
\subsetneq
I_2
\subsetneq
I_3
\subsetneq
\cdots
$$
inside $\mathcal B$, contradicting ACC.
Choose a maximal element
$$
I\in\mathcal B.
$$

:::

:::

::: pf-step

The ideal $I$ is not prime.


::: pf-proof

If $I$ were prime, then the one-factor product
$$
I
$$
would be a product of prime ideals, each containing $I$, and would be contained in $I$.
Thus $I$ would be good, contradicting
$$
I\in\mathcal B.
$$

:::

:::

::: {.pf-step #s1-4}

There exist
$$
a,b\in R\setminus I
$$
such that
$$
ab\in I.
$$


::: pf-proof

Because $I$ is proper but not prime, the prime-ideal condition fails.
Thus such $a,b$ exist.

:::

:::

::: {.pf-step #s1-5}

The ideals
$$
I+(a)
\qquad\text{and}\qquad
I+(b)
$$
strictly contain $I$.


::: pf-proof

Since
$$
a,b\notin I,
$$
adjoining either generator strictly enlarges $I$.

:::

:::

::: {.pf-step #s1-6}

The ideal
$$
I+(a)
$$
is proper.


::: pf-proof

Suppose instead that
$$
I+(a)=R.
$$
Then there exist
$$
i\in I,
\qquad
r\in R
$$
such that
$$
1=i+ra.
$$
Multiply by $b$:
$$
b
=
ib+r(ab).
$$
Since
$$
i\in I
$$
and
$$
ab\in I,
$$
both terms on the right lie in $I$.
Hence
$$
b\in I,
$$
contradicting step [](#s1-4){.pf-ref}.
Therefore
$$
I+(a)\ne R.
$$

:::

:::

::: {.pf-step #s1-7}

The ideal
$$
I+(b)
$$
is proper.


::: pf-proof

The argument is symmetric to step [](#s1-6){.pf-ref}.
If
$$
I+(b)=R,
$$
then multiplying a representation
$$
1=i+rb
$$
by $a$ would force
$$
a\in I,
$$
contradicting step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Both
$$
I+(a)
\qquad\text{and}\qquad
I+(b)
$$
are good.


::: pf-proof

By steps [](#s1-5){.pf-ref} through [](#s1-7){.pf-ref}, both are nonzero proper ideals strictly containing the maximal counterexample $I$.
If either were not good, it would belong to $\mathcal B$ and properly contain $I$, contradicting maximality.
Hence both are good.

:::

:::

::: {.pf-step #s1-9}

Choose prime ideals
$$
P_1,\ldots,P_r
$$
and
$$
Q_1,\ldots,Q_s
$$
such that
$$
I+(a)
\subseteq
P_i
\quad
\text{for every }i,
$$
$$
P_1\cdots P_r
\subseteq
I+(a),
$$
and
$$
I+(b)
\subseteq
Q_j
\quad
\text{for every }j,
$$
$$
Q_1\cdots Q_s
\subseteq
I+(b).
$$


::: pf-proof

This is exactly the definition of goodness applied in step [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Every prime ideal among the
$$
P_i
$$
and
$$
Q_j
$$
contains $I$.


::: pf-proof

Each
$$
P_i
$$
contains
$$
I+(a),
$$
which contains $I$.
Likewise each
$$
Q_j
$$
contains
$$
I+(b),
$$
which contains $I$.

:::

:::

::: {.pf-step #s1-11}

One has
$$
(I+(a))(I+(b))
\subseteq
I.
$$


::: pf-proof

Expand:
$$
(I+(a))(I+(b))
\subseteq
I^2+Ia+Ib+(ab).
$$
Because $I$ is an ideal,
$$
I^2,
\ Ia,
\ Ib
\subseteq
I.
$$
By step [](#s1-4){.pf-ref},
$$
ab\in I,
$$
so
$$
(ab)\subseteq I.
$$
Thus the whole product is contained in $I$.

:::

:::

::: {.pf-step #s1-12}

The product
$$
P_1\cdots P_rQ_1\cdots Q_s
$$
is contained in $I$.


::: pf-proof

By step [](#s1-9){.pf-ref},
$$
P_1\cdots P_r
\subseteq
I+(a)
$$
and
$$
Q_1\cdots Q_s
\subseteq
I+(b).
$$
Multiplying these containments gives
$$
P_1\cdots P_rQ_1\cdots Q_s
\subseteq
(I+(a))(I+(b)).
$$
Apply step [](#s1-11){.pf-ref}.

:::

:::

::: {.pf-step #s1-13}

The ideal $I$ is good.


::: pf-proof

By step [](#s1-10){.pf-ref}, every prime factor
$$
P_i
\qquad\text{and}\qquad
Q_j
$$
contains $I.
By step [](#s1-12){.pf-ref}, their product is contained in $I$.
Thus $I$ satisfies the definition of goodness.

:::

:::

::: {.pf-step #s1-14}

This contradicts
$$
I\in\mathcal B.
$$


::: pf-proof

Membership in $\mathcal B$ means that $I$ is not good, whereas step [](#s1-13){.pf-ref} shows that it is good.

:::

:::

::: {.pf-step #s1-15}

Therefore every nonzero proper ideal $A$ of $R$ contains a product of prime ideals, each of which contains $A$.


::: pf-proof

The assumption that a counterexample exists leads to the contradiction in step [](#s1-14){.pf-ref}.
Hence
$$
\boxed{
\text{every nonzero proper ideal }A
\text{ contains }
P_1\cdots P_m
\text{ with }
A\subseteq P_i
\text{ for all }i.
}
$$

:::

:::

::: pf-qed

Step [](#s1-15){.pf-ref} proves the intended corrected statement.

:::

:::

:::
