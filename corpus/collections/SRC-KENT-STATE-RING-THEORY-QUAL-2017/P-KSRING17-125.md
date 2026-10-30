---
schema: qual/card@1
id: P-KSRING17-125
kind: problem
title: Extension of prime ideals to a localization of a domain
classification:
  areas: [algebra]
  topics:
  - Localization
  - Prime Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 125 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be an integral domain, $S$ a multiplicative set, and let $S^{-1}R = \{\frac{r}{s} \st r \in R,\ s \in S\}$ (contained in the field of fractions of $R$). Show that if $P$ is a prime ideal of $R$, then $S^{-1}P$ is either a prime ideal of $S^{-1}R$ or else equals $S^{-1}R$.
:::

::: {.solution}

Recall
$$
S^{-1}P
\coloneqq
\left\{
\frac ps:
p\in P,\ s\in S
\right\}.
$$

::: pf

::: {.pf-step #s1-1}

If
$$
P\cap S\ne\varnothing,
$$
then
$$
S^{-1}P
=
S^{-1}R.
$$


::: pf-proof

Choose
$$
s\in P\cap S.
$$
Then
$$
\frac ss
=
1
$$
belongs to
$$
S^{-1}P.
$$
Any ideal containing the identity is the whole ring.
Therefore
$$
S^{-1}P
=
S^{-1}R.
$$

:::

:::

::: {.pf-step #s1-2}

Assume now that
$$
P\cap S=\varnothing.
$$
If
$$
\frac as
\in
S^{-1}P,
$$
then
$$
a\in P.
$$


::: pf-proof

Membership in
$$
S^{-1}P
$$
means there exist
$$
p\in P,
\qquad
t\in S
$$
such that
$$
\frac as
=
\frac pt
$$
in the field of fractions of $R$.
Because $R$ is a domain,
$$
at=ps.
$$
The right-hand side lies in $P$, so
$$
at\in P.
$$
Since
$$
t\in S
$$
and
$$
P\cap S=\varnothing,
$$
one has
$$
t\notin P.
$$
Primality of $P$ therefore forces
$$
a\in P.
$$

:::

:::

::: {.pf-step #s1-3}

Conversely, if
$$
a\in P
$$
and
$$
s\in S,
$$
then
$$
\frac as
\in
S^{-1}P.
$$


::: pf-proof

This is immediate from the definition of
$$
S^{-1}P.
$$

:::

:::

::: {.pf-step #s1-4}

Under the assumption
$$
P\cap S=\varnothing,
$$
one has
$$
\boxed{
\frac as\in S^{-1}P
\iff
a\in P.
}
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Under the same assumption,
$$
S^{-1}P
$$
is proper.


::: pf-proof

The identity is
$$
1=\frac11.
$$
Since
$$
P
$$
is proper,
$$
1\notin P.
$$
By step [](#s1-4){.pf-ref},
$$
\frac11
\notin
S^{-1}P.
$$
Thus
$$
S^{-1}P
\ne
S^{-1}R.
$$

:::

:::

::: {.pf-step #s1-6}

Let
$$
\frac as,\frac bt
\in
S^{-1}R
$$
and suppose
$$
\frac as\frac bt
\in
S^{-1}P.
$$
Then
$$
ab\in P.
$$


::: pf-proof

The product is
$$
\frac{ab}{st}.
$$
Since
$$
s,t\in S,
$$
one has
$$
st\in S.
$$
By step [](#s1-4){.pf-ref},
$$
\frac{ab}{st}
\in
S^{-1}P
$$
implies
$$
ab\in P.
$$

:::

:::

::: {.pf-step #s1-7}

Under the assumptions of step [](#s1-6){.pf-ref},
$$
a\in P
\quad\text{or}\quad
b\in P.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} gives
$$
ab\in P.
$$
Since
$$
P
$$
is prime,
$$
a\in P
\quad\text{or}\quad
b\in P.
$$

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\frac as
\in
S^{-1}P
\quad\text{or}\quad
\frac bt
\in
S^{-1}P.
$$


::: pf-proof

Apply step [](#s1-4){.pf-ref} to the conclusion of step [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

Hence, if
$$
P\cap S=\varnothing,
$$
then
$$
\boxed{
S^{-1}P
\text{ is a prime ideal of }S^{-1}R.
}
$$


::: pf-proof

Step [](#s1-5){.pf-ref} gives properness.
Steps [](#s1-6){.pf-ref} through [](#s1-8){.pf-ref} give the prime-product condition.

:::

:::

::: {.pf-step #s1-10}

Consequently,
$$
\boxed{
S^{-1}P
\text{ is either prime or equal to }S^{-1}R.
}
$$


::: pf-proof

If
$$
P\cap S\ne\varnothing,
$$
step [](#s1-1){.pf-ref} gives the whole ring.
If
$$
P\cap S=\varnothing,
$$
step [](#s1-9){.pf-ref} gives a prime ideal.
These are the two exhaustive cases.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
