---
schema: qual/card@1
id: P-KSRING17-136
kind: problem
title: Nonzero ideals of a Noetherian domain contain products of nonzero primes
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 136 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative Noetherian domain with identity.
Prove that every nonzero ideal of R contains a product of nonzero prime ideals of R.
:::

::: {.remark}
Erratum: under the usual convention that the product has at least one prime-ideal factor, the statement needs the additional hypothesis that $R$ is not a field.
Indeed, if $R$ is a field, then $R$ is its only nonzero ideal and $R$ has no nonzero prime ideals.
The proof below establishes the intended non-field statement.
:::

::: {.solution}
Assume that $R$ is not a field.
Call an ideal
$$
I\trianglelefteq R
$$
\dfn{good} if it contains a finite product
$$
P_1P_2\cdots P_m
$$
of nonzero prime ideals of $R$, with
$$
m\ge1.
$$

<1>1. The unit ideal $R$ is good.

::: {.proof}
Because $R$ is not a field, there exists a nonzero nonunit
$$
a\in R.
$$
The principal ideal
$$
(a)
$$
is nonzero and proper.
Hence it is contained in a maximal ideal
$$
M.
$$
Since $R$ is commutative, $M$ is prime.
Also
$$
M\ne(0),
$$
because it contains the nonzero element $a$.
Thus
$$
M
$$
is a nonzero prime ideal, and
$$
M\subseteq R.
$$
Therefore $R$ is good.
:::

<1>2. Suppose, for contradiction, that some nonzero ideal of $R$ is not good.
Let
$$
\mathcal B
\coloneqq
\{
I\trianglelefteq R:
I\ne(0)
\text{ and }I\text{ is not good}
\}.
$$
Then $\mathcal B$ is nonempty.

::: {.proof}
This is exactly the negation of the desired conclusion.
:::

<1>3. The poset $\mathcal B$, ordered by inclusion, has a maximal element.

::: {.proof}
Because $R$ is Noetherian, its ideals satisfy the ascending chain condition.
If $\mathcal B$ had no maximal element, starting from some
$$
I_1\in\mathcal B
$$
one could choose a strictly increasing chain
$$
I_1
\subsetneq
I_2
\subsetneq
I_3
\subsetneq
\cdots
$$
inside $\mathcal B$.
This contradicts the ascending chain condition.
Hence $\mathcal B$ has a maximal element.
Choose one and call it
$$
I.
$$
:::

<1>4. The ideal $I$ is proper.

::: {.proof}
Step <1>1 shows that
$$
R
$$
is good.
Since
$$
I\in\mathcal B
$$
is not good,
$$
I\ne R.
$$
:::

<1>5. The ideal $I$ is not prime.

::: {.proof}
If $I$ were prime, then because
$$
I\ne(0)
$$
by definition of $\mathcal B$, the one-factor product
$$
I
$$
would be a product of nonzero prime ideals contained in $I$.
Thus $I$ would be good, contradicting
$$
I\in\mathcal B.
$$
Therefore $I$ is not prime.
:::

<1>6. There exist
$$
a,b\in R\setminus I
$$
such that
$$
ab\in I.
$$

::: {.proof}
By steps <1>4--<1>5, the ideal $I$ is proper but not prime.
The negation of the prime-ideal condition therefore gives such elements $a$ and $b$.
:::

<1>7. The ideals
$$
I+(a)
\qquad\text{and}\qquad
I+(b)
$$
strictly contain $I$.

::: {.proof}
Since
$$
a\notin I,
$$
one has
$$
I\subsetneq I+(a).
$$
Similarly,
$$
b\notin I
$$
gives
$$
I\subsetneq I+(b).
$$
:::

<1>8. Each of the ideals
$$
I+(a)
\qquad\text{and}\qquad
I+(b)
$$
is good.

::: {.proof}
Both ideals strictly contain the maximal counterexample $I$ from step <1>3.
They are also nonzero because they contain the nonzero ideal $I$.

If either were not good, it would belong to $\mathcal B$ and properly contain $I$, contradicting maximality.
Therefore both are good.
:::

<1>9. Choose nonzero prime ideals
$$
P_1,\ldots,P_r
$$
and
$$
Q_1,\ldots,Q_s
$$
such that
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

::: {.proof}
This is exactly the meaning of step <1>8.
:::

<1>10. One has
$$
(I+(a))(I+(b))
\subseteq
I.
$$

::: {.proof}
Expand the product of ideals:
$$
(I+(a))(I+(b))
\subseteq
I^2+Ib+Ia+(ab).
$$
Because $I$ is an ideal,
$$
I^2\subseteq I,
\qquad
Ib\subseteq I,
\qquad
Ia\subseteq I.
$$
By step <1>6,
$$
ab\in I,
$$
so
$$
(ab)\subseteq I.
$$
Hence the entire product ideal is contained in $I$.
:::

<1>11. The product
$$
P_1\cdots P_rQ_1\cdots Q_s
$$
is contained in $I$.

::: {.proof}
By step <1>9,
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
Multiplying the containments gives
$$
P_1\cdots P_rQ_1\cdots Q_s
\subseteq
(I+(a))(I+(b)).
$$
Apply step <1>10.
:::

<1>12. The product ideal
$$
P_1\cdots P_rQ_1\cdots Q_s
$$
is nonzero.

::: {.proof}
Each prime ideal
$$
P_i
\qquad\text{and}\qquad
Q_j
$$
is nonzero.
Choose nonzero elements
$$
p_i\in P_i,
\qquad
q_j\in Q_j.
$$
Because $R$ is an integral domain,
$$
p_1\cdots p_rq_1\cdots q_s
\ne
0.
$$
This element lies in
$$
P_1\cdots P_rQ_1\cdots Q_s.
$$
Hence the product ideal is nonzero.
:::

<1>13. The ideal $I$ is good.

::: {.proof}
By step <1>11,
$$
I
$$
contains the finite product
$$
P_1\cdots P_rQ_1\cdots Q_s
$$
of nonzero prime ideals.
Thus, by definition, $I$ is good.
:::

<1>14. This contradicts the choice
$$
I\in\mathcal B.
$$

::: {.proof}
Membership in
$$
\mathcal B
$$
means that $I$ is not good, whereas step <1>13 shows that it is good.
:::

<1>15. Therefore every nonzero ideal of a non-field Noetherian domain contains a product of nonzero prime ideals.

::: {.proof}
The assumption that
$$
\mathcal B\ne\varnothing
$$
leads to the contradiction in step <1>14.
Hence
$$
\mathcal B=\varnothing.
$$
Thus
$$
\boxed{
\text{every nonzero ideal of }R
\text{ contains a finite product of nonzero prime ideals}.
}
$$
:::

<1>16. Q.E.D.

::: {.proof}
Step <1>15 proves the intended statement under the necessary non-field qualification recorded in the remark.
:::
:::
