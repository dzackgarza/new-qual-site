---
schema: qual/card@1
id: P-KSRING17-068
kind: problem
title: A ring with exactly one prime ideal is its own localization
classification:
  areas: [algebra]
  topics:
  - Local Rings
  - Localization
  - Prime Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 68 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring with identity that has exactly one prime ideal $P$. Prove the following.

(a) $R/P$ is a field.

(b) $R$ is isomorphic to $R_{P}$, the ring of quotients of $R$ with respect to the multiplicative set $R - P = \{s \in R \st s \notin P\}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The prime ideal $P$ is contained in some maximal ideal $M$ of $R$.


::: pf-proof

The ideal $P$ is proper because it is prime.
Every proper ideal in a commutative ring with identity is contained in a maximal ideal.
Hence there exists a maximal ideal
$$
M
$$
with
$$
P\subseteq M.
$$

:::

:::

::: {.pf-step #s1-2}

The maximal ideal $M$ is prime.


::: pf-proof

Every maximal ideal of a commutative ring with identity is prime.
Thus
$$
M
$$
is a prime ideal.

:::

:::

::: {.pf-step #s1-3}

One has
$$
M=P.
$$


::: pf-proof

By hypothesis,
$$
P
$$
is the only prime ideal of $R$.
Step [](#s1-2){.pf-ref} shows that $M$ is prime.
Therefore
$$
M=P.
$$

:::

:::

::: {.pf-step #s1-4}

The ideal $P$ is maximal.


::: pf-proof

Step [](#s1-3){.pf-ref} identifies $P$ with the maximal ideal $M$ from step [](#s1-1){.pf-ref}.
Hence
$$
\boxed{P\text{ is maximal}.}
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{R/P\text{ is a field}.}
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, $P$ is maximal.
The maximal-ideal quotient criterion gives that
$$
R/P
$$
is a field.

:::

:::

::: {.pf-step #s1-6}

The ideal $P$ is the unique maximal ideal of $R$.


::: pf-proof

Every maximal ideal is prime.
Since $P$ is the unique prime ideal by hypothesis, there can be no maximal ideal other than $P$.

:::

:::

::: {.pf-step #s1-7}

Every element
$$
s\in R\setminus P
$$
is a unit of $R$.


::: pf-proof

Suppose
$$
s\notin P
$$
were not a unit.
Then the principal ideal
$$
(s)
$$
would be proper.
Every proper ideal is contained in a maximal ideal, so
$$
(s)\subseteq M
$$
for some maximal ideal $M$.
By step [](#s1-6){.pf-ref},
$$
M=P.
$$
Hence
$$
s\in P,
$$
contradicting the choice of $s$.
Therefore every element outside $P$ is a unit.

:::

:::

::: {.pf-step #s1-8}

Let
$$
S
\coloneqq
R\setminus P.
$$
Define
$$
\varphi:R\to S^{-1}R=R_P
$$
by
$$
\varphi(r)
\coloneqq
\frac r1.
$$
Then $\varphi$ is surjective.


::: pf-proof

Let
$$
\frac rs
\in
R_P
$$
with
$$
s\in S.
$$
By step [](#s1-7){.pf-ref}, $s$ is a unit in $R$.
Hence
$$
s^{-1}\in R.
$$
In the localization,
$$
\frac rs
=
\frac{rs^{-1}}1
=
\varphi(rs^{-1}).
$$
Thus every element of $R_P$ lies in the image of $\varphi$.

:::

:::

::: {.pf-step #s1-9}

The map $\varphi$ is injective.


::: pf-proof

Suppose
$$
\varphi(r)
=
\frac r1
=
0
$$
in $R_P$.
By the definition of equality in a localization, there exists
$$
s\in S
$$
such that
$$
sr=0.
$$
By step [](#s1-7){.pf-ref}, $s$ is a unit.
Multiplying by
$$
s^{-1}
$$
gives
$$
r=0.
$$
Hence
$$
\ker\varphi=0,
$$
so $\varphi$ is injective.

:::

:::

::: {.pf-step #s1-10}

Therefore
$$
\boxed{
R
\cong
R_P.
}
$$


::: pf-proof

The natural localization map $\varphi$ is a ring homomorphism.
Steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref} show that it is bijective.
Hence it is a ring isomorphism.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves part (a), and step [](#s1-10){.pf-ref} proves part (b).

:::

:::

:::
