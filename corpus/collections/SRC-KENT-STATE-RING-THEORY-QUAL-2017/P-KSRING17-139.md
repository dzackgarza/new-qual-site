---
schema: qual/card@1
id: P-KSRING17-139
kind: problem
title: Principal nonzero primes in a Noetherian domain have height one
classification:
  areas: [algebra]
  topics:
  - Noetherian Rings
  - Krull's Principal Ideal Theorem
  - Prime Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 139 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let P be a nonzero prime ideal of the commutative Noetherian domain R. Assume P is principal.
Prove that there does not exist a prime ideal Q satisfying $(0) \subsetneq Q \subsetneq P$.
:::

::: {.solution}

Write
$$
P=(p)
$$
with
$$
p\ne0.
$$
Suppose, for contradiction, that there exists a prime ideal
$$
Q
$$
such that
$$
(0)
\subsetneq
Q
\subsetneq
P.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
p\notin Q.
$$


::: pf-proof

If
$$
p\in Q,
$$
then
$$
(p)=P
\subseteq
Q.
$$
Together with
$$
Q\subsetneq P,
$$
this is impossible.
Hence
$$
p\notin Q.
$$

:::

:::

::: {.pf-step #s1-2}

Choose
$$
0\ne q_0\in Q.
$$
Since
$$
Q\subseteq P=(p),
$$
there exists
$$
q_1\in R
$$
such that
$$
q_0=pq_1.
$$


::: pf-proof

The ideal $Q$ is nonzero, so a nonzero element
$$
q_0
$$
exists.
Because
$$
q_0\in Q\subseteq(p),
$$
the divisibility
$$
p\mid q_0
$$
gives the displayed expression.

:::

:::

::: pf-step

The element
$$
q_1
$$
belongs to $Q$.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
pq_1=q_0\in Q.
$$
Since $Q$ is prime and
$$
p\notin Q
$$
by step [](#s1-1){.pf-ref}, primality forces
$$
q_1\in Q.
$$

:::

:::

::: pf-step

The element
$$
q_1
$$
is nonzero.


::: pf-proof

If
$$
q_1=0,
$$
then
$$
q_0=pq_1=0,
$$
contradicting the choice
$$
q_0\ne0.
$$

:::

:::

::: {.pf-step #s1-5}

Inductively, for every
$$
n\ge0,
$$
there exists a nonzero element
$$
q_n\in Q
$$
such that
$$
q_n=pq_{n+1}.
$$


::: pf-proof

Suppose
$$
0\ne q_n\in Q.
$$
Because
$$
Q\subseteq P=(p),
$$
write
$$
q_n=pq_{n+1}
$$
for some
$$
q_{n+1}\in R.
$$
Since
$$
q_n\in Q
$$
and
$$
p\notin Q,
$$
primality of $Q$ gives
$$
q_{n+1}\in Q.
$$
Because $R$ is a domain and
$$
q_n\ne0,
\qquad
p\ne0,
$$
one must have
$$
q_{n+1}\ne0.
$$
Thus the construction continues indefinitely.

:::

:::

::: {.pf-step #s1-6}

For every
$$
n\ge0,
$$
one has
$$
(q_n)
\subseteq
(q_{n+1}).
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
q_n=pq_{n+1}.
$$
Thus $q_n$ is a multiple of $q_{n+1}$, and therefore every multiple of $q_n$ is a multiple of $q_{n+1}$.
Hence
$$
(q_n)\subseteq(q_{n+1}).
$$

:::

:::

::: {.pf-step #s1-7}

Each containment in step [](#s1-6){.pf-ref} is strict.


::: pf-proof

Suppose for some $n$ that
$$
(q_n)
=(q_{n+1}).
$$
Then
$$
q_{n+1}
=
a q_n
$$
for some
$$
a\in R.
$$
Using
$$
q_n=pq_{n+1},
$$
one gets
$$
q_{n+1}
=
apq_{n+1}.
$$
Hence
$$
q_{n+1}(1-ap)=0.
$$
By step [](#s1-5){.pf-ref},
$$
q_{n+1}\ne0.
$$
Since $R$ is a domain,
$$
1-ap=0.
$$
Thus
$$
ap=1,
$$
so $p$ is a unit.
Then
$$
P=(p)=R,
$$
contradicting the fact that $P$ is prime and therefore proper.

Hence
$$
(q_n)
\subsetneq
(q_{n+1})
$$
for every $n$.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
(q_0)
\subsetneq
(q_1)
\subsetneq
(q_2)
\subsetneq
\cdots
$$
is an infinite strictly ascending chain of ideals.


::: pf-proof

This is exactly steps [](#s1-6){.pf-ref} through [](#s1-7){.pf-ref}.

:::

:::

::: {.pf-step #s1-9}

The chain in step [](#s1-8){.pf-ref} contradicts Noetherianity of $R$.


::: pf-proof

A Noetherian ring satisfies the ascending chain condition on ideals.
The chain from step [](#s1-8){.pf-ref} never stabilizes because every inclusion is strict.
This is impossible.

:::

:::

::: {.pf-step #s1-10}

Hence no such prime ideal $Q$ exists.


::: pf-proof

The assumption
$$
(0)
\subsetneq
Q
\subsetneq
P
$$
leads to the contradiction in step [](#s1-9){.pf-ref}.
Therefore
$$
\boxed{
\text{there is no prime }Q
\text{ with }
(0)<Q<P.
}
$$

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
