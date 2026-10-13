---
schema: qual/card@1
id: P-KSRING17-068
kind: problem
title: A ring with exactly one prime ideal is its own localization
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 68 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity that has exactly one prime ideal P . Prove the following.

(a) $R / P$ is a field.

(b) R is isomorphic to $R _ { P }$ , the ring of quotients of R with respect to the multiplicative set $R - P = \{ s \in R \mid s \not \in P \}$
:::

::: {.solution}
<1>1. The prime ideal $P$ is contained in some maximal ideal $M$ of $R$.

::: {.proof}
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

<1>2. The maximal ideal $M$ is prime.

::: {.proof}
Every maximal ideal of a commutative ring with identity is prime.
Thus
$$
M
$$
is a prime ideal.
:::

<1>3. One has
$$
M=P.
$$

::: {.proof}
By hypothesis,
$$
P
$$
is the only prime ideal of $R$.
Step <1>2 shows that $M$ is prime.
Therefore
$$
M=P.
$$
:::

<1>4. The ideal $P$ is maximal.

::: {.proof}
Step <1>3 identifies $P$ with the maximal ideal $M$ from step <1>1.
Hence
$$
\boxed{P\text{ is maximal}.}
$$
:::

<1>5. Therefore
$$
\boxed{R/P\text{ is a field}.}
$$

::: {.proof}
By step <1>4, $P$ is maximal.
The maximal-ideal quotient criterion gives that
$$
R/P
$$
is a field.
:::

<1>6. The ideal $P$ is the unique maximal ideal of $R$.

::: {.proof}
Every maximal ideal is prime.
Since $P$ is the unique prime ideal by hypothesis, there can be no maximal ideal other than $P$.
:::

<1>7. Every element
$$
s\in R\setminus P
$$
is a unit of $R$.

::: {.proof}
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
By step <1>6,
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

<1>8. Let
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

::: {.proof}
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
By step <1>7, $s$ is a unit in $R$.
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

<1>9. The map $\varphi$ is injective.

::: {.proof}
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
By step <1>7, $s$ is a unit.
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

<1>10. Therefore
$$
\boxed{
R
\cong
R_P.
}
$$

::: {.proof}
The natural localization map $\varphi$ is a ring homomorphism.
Steps <1>8--<1>9 show that it is bijective.
Hence it is a ring isomorphism.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>5 proves part (a), and step <1>10 proves part (b).
:::
:::
