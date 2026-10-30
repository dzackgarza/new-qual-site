---
schema: qual/card@1
id: P-KSRING17-133
kind: problem
title: A Noetherian ring has finitely many minimal primes
classification:
  areas: [algebra]
  topics:
  - Noetherian Rings
  - Minimal Prime Ideals
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

::: pf

::: pf-step

Suppose, for contradiction, that some ideal of $R$ has infinitely many prime ideals minimal over it.
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


::: pf-proof

This is the negation of the stronger statement that every ideal has only finitely many minimal primes.
In particular, if the theorem itself failed, the zero ideal would belong to $\mathcal B$.

:::

:::

::: {.pf-step #s1-2}

The set $\mathcal B$ has a maximal element under inclusion.


::: pf-proof

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

:::

::: {.pf-step #s1-3}

The ideal $I$ from step [](#s1-2){.pf-ref} is not prime.


::: pf-proof

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

By step [](#s1-3){.pf-ref}, $I$ is not prime.
Since $I$ is proper—an ideal with a prime lying over it must be proper—the failure of primality gives elements
$$
a,b\notin I
$$
with
$$
ab\in I.
$$

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

:::

::: {.pf-step #s1-6}

Each of the ideals
$$
I+(a)
\qquad\text{and}\qquad
I+(b)
$$
has only finitely many minimal primes.


::: pf-proof

The ideal $I$ was chosen maximal in $\mathcal B$.
By step [](#s1-5){.pf-ref}, both displayed ideals properly contain $I$.
Hence neither can lie in $\mathcal B$.
Therefore each has only finitely many minimal primes.

:::

:::

::: {.pf-step #s1-7}

Let
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


::: pf-proof

By step [](#s1-4){.pf-ref},
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

:::

::: {.pf-step #s1-8}

If
$$
a\in P,
$$
then $P$ is minimal over
$$
I+(a).
$$


::: pf-proof

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

:::

::: {.pf-step #s1-9}

If
$$
b\in P,
$$
then $P$ is minimal over
$$
I+(b).
$$


::: pf-proof

This is the same argument as step [](#s1-8){.pf-ref}, with $b$ in place of $a$.

:::

:::

::: {.pf-step #s1-10}

Every prime ideal minimal over $I$ is a minimal prime over one of
$$
I+(a)
\qquad\text{or}\qquad
I+(b).
$$


::: pf-proof

By step [](#s1-7){.pf-ref}, every minimal prime
$$
P
$$
over $I$ contains at least one of $a,b$.
If it contains $a$, apply step [](#s1-8){.pf-ref}.
If it contains $b$, apply step [](#s1-9){.pf-ref}.

:::

:::

::: {.pf-step #s1-11}

The ideal $I$ has only finitely many minimal primes.


::: pf-proof

By step [](#s1-6){.pf-ref}, the set of minimal primes over
$$
I+(a)
$$
is finite, and so is the set of minimal primes over
$$
I+(b).
$$
By step [](#s1-10){.pf-ref}, every minimal prime over $I$ belongs to the union of these two finite sets.
Therefore the set of minimal primes over $I$ is finite.

:::

:::

::: {.pf-step #s1-12}

This contradicts the choice
$$
I\in\mathcal B.
$$


::: pf-proof

Membership in $\mathcal B$ means precisely that $I$ has infinitely many minimal primes, whereas step [](#s1-11){.pf-ref} shows it has only finitely many.

:::

:::

::: {.pf-step #s1-13}

Therefore every ideal of $R$ has only finitely many minimal primes.


::: pf-proof

The assumption that $\mathcal B$ is nonempty leads to the contradiction in step [](#s1-12){.pf-ref}.
Hence
$$
\mathcal B=\varnothing.
$$

:::

:::

::: {.pf-step #s1-14}

In particular, $R$ has only finitely many minimal prime ideals.


::: pf-proof

The minimal prime ideals of $R$ are exactly the prime ideals minimal over the zero ideal
$$
(0).
$$
Apply step [](#s1-13){.pf-ref} to
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

:::

::: pf-qed

Step [](#s1-14){.pf-ref} is the required conclusion.

:::

:::

:::
