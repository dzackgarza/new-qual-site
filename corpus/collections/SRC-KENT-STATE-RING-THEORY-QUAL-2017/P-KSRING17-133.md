---
schema: qual/card@1
id: P-KSRING17-133
kind: problem
title: A Noetherian ring has finitely many minimal primes
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 133 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative Noetherian ring with identity.
Prove that there are only finitely many minimal prime ideals of R.
:::

::: {.solution}
For an ideal
$$
I\trianglelefteq R,
$$
call a prime ideal
$$
P
$$
\dfn{minimal over $I$} if
$$
I\subseteq P
$$
and there is no prime ideal
$$
Q
$$
with
$$
I\subseteq Q\subsetneq P.
$$

<1>1. Suppose, for contradiction, that some ideal of $R$ has infinitely many prime ideals minimal over it.
Let
$$
\mathcal B
\coloneqq
\{
I\trianglelefteq R:
I\text{ has infinitely many minimal primes}
\}.
$$
Then $\mathcal B$ is nonempty.

::: {.proof}
This is the negation of the stronger statement that every ideal has only finitely many minimal primes.
In particular, if the theorem itself failed, the zero ideal would belong to $\mathcal B$.
:::

<1>2. The set $\mathcal B$ has a maximal element under inclusion.

::: {.proof}
Because $R$ is Noetherian, its ideals satisfy the ascending chain condition.
If $\mathcal B$ had no maximal element, starting from any
$$
I_1\in\mathcal B
$$
one could choose
$$
I_1\subsetneq I_2\subsetneq I_3\subsetneq\cdots
$$
with every
$$
I_n\in\mathcal B,
$$
contradicting the ascending chain condition.
Thus some
$$
I\in\mathcal B
$$
is maximal.
:::

<1>3. The ideal $I$ from step <1>2 is not prime.

::: {.proof}
If $I$ were prime, then the only prime ideal minimal over $I$ would be $I$ itself.
Indeed, any prime
$$
P
$$
with
$$
I\subseteq P
$$
and minimal over $I$ must equal $I$, because $I$ is already a prime ideal between $I$ and $P$.
Thus $I$ would have exactly one minimal prime, contradicting
$$
I\in\mathcal B.
$$
:::

<1>4. There exist
$$
a,b\in R\setminus I
$$
such that
$$
ab\in I.
$$

::: {.proof}
By step <1>3, $I$ is not prime.
Since $I$ is proper—an ideal with a prime lying over it must be proper—the failure of primality gives elements
$$
a,b\notin I
$$
with
$$
ab\in I.
$$
:::

<1>5. The ideals
$$
I+(a)
\qquad\text{and}\qquad
I+(b)
$$
strictly contain $I$.

::: {.proof}
Because
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

<1>6. Each of the ideals
$$
I+(a)
\qquad\text{and}\qquad
I+(b)
$$
has only finitely many minimal primes.

::: {.proof}
The ideal $I$ was chosen maximal in $\mathcal B$.
By step <1>5, both displayed ideals properly contain $I$.
Hence neither can lie in $\mathcal B$.
Therefore each has only finitely many minimal primes.
:::

<1>7. Let
$$
P
$$
be a prime ideal minimal over $I$.
Then
$$
a\in P
\quad\text{or}\quad
b\in P.
$$

::: {.proof}
By step <1>4,
$$
ab\in I\subseteq P.
$$
Since $P$ is prime,
$$
a\in P
\quad\text{or}\quad
b\in P.
$$
:::

<1>8. If
$$
a\in P,
$$
then $P$ is minimal over
$$
I+(a).
$$

::: {.proof}
The containment
$$
I+(a)\subseteq P
$$
is immediate.
Suppose
$$
Q
$$
is prime and
$$
I+(a)
\subseteq
Q
\subseteq
P.
$$
Then in particular
$$
I\subseteq Q\subseteq P.
$$
Since $P$ is minimal over $I$,
$$
Q=P.
$$
Thus no smaller prime lies between
$$
I+(a)
$$
and $P$, so $P$ is minimal over
$$
I+(a).
$$
:::

<1>9. If
$$
b\in P,
$$
then $P$ is minimal over
$$
I+(b).
$$

::: {.proof}
This is the same argument as step <1>8, with $b$ in place of $a$.
:::

<1>10. Every prime ideal minimal over $I$ is a minimal prime over one of
$$
I+(a)
\qquad\text{or}\qquad
I+(b).
$$

::: {.proof}
By step <1>7, every minimal prime
$$
P
$$
over $I$ contains at least one of $a,b$.
If it contains $a$, apply step <1>8.
If it contains $b$, apply step <1>9.
:::

<1>11. The ideal $I$ has only finitely many minimal primes.

::: {.proof}
By step <1>6, the set of minimal primes over
$$
I+(a)
$$
is finite, and so is the set of minimal primes over
$$
I+(b).
$$
By step <1>10, every minimal prime over $I$ belongs to the union of these two finite sets.
Therefore the set of minimal primes over $I$ is finite.
:::

<1>12. This contradicts the choice
$$
I\in\mathcal B.
$$

::: {.proof}
Membership in $\mathcal B$ means precisely that $I$ has infinitely many minimal primes, whereas step <1>11 shows it has only finitely many.
:::

<1>13. Therefore every ideal of $R$ has only finitely many minimal primes.

::: {.proof}
The assumption that $\mathcal B$ is nonempty leads to the contradiction in step <1>12.
Hence
$$
\mathcal B=\varnothing.
$$
:::

<1>14. In particular, $R$ has only finitely many minimal prime ideals.

::: {.proof}
The minimal prime ideals of $R$ are exactly the prime ideals minimal over the zero ideal
$$
(0).
$$
Apply step <1>13 to
$$
I=(0).
$$
Thus
$$
\boxed{
R\text{ has only finitely many minimal prime ideals}.
}
$$
:::

<1>15. Q.E.D.

::: {.proof}
Step <1>14 is the required conclusion.
:::
:::
