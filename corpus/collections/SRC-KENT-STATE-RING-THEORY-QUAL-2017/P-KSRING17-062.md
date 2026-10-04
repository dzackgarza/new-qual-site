---
schema: qual/card@1
id: P-KSRING17-062
kind: problem
title: Adjacent prime ideals between two nested primes
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 62 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let R be a commutative ring with identity, and let $P \subset Q$ be prime ideals of R. Prove that there exist prime ideals $P ^ { * } , Q ^ { * }$ satisfying $P \subseteq P ^ { * } \subset Q ^ { * } \subseteq Q$ , such that there are no prime ideals strictly between $P ^ { * }$ and $Q ^ { * }$ . HINT: Fix $x \in Q - P$ and show that there exists a prime ideal $P ^ { * }$ containing P , contained in Q and maximal with respect to not containing x.
:::

::: {.solution}
Choose
$$
x\in Q\setminus P.
$$

<1>1. Let
$$
\mathcal A
\coloneqq
\{
\mathfrak p:
\mathfrak p\text{ is prime},
\ P\subseteq\mathfrak p\subseteq Q,
\ x\notin\mathfrak p
\},
$$
ordered by inclusion.
Then $\mathcal A$ is nonempty.

::: {.proof}
The prime ideal
$$
P
$$
belongs to $\mathcal A$, because
$$
x\notin P
$$
by choice of $x$.
:::

<1>2. Every chain in $\mathcal A$ has an upper bound in $\mathcal A$.

::: {.proof}
Let
$$
\mathcal C\subseteq\mathcal A
$$
be a chain and define
$$
U
\coloneqq
\bigcup_{\mathfrak p\in\mathcal C}\mathfrak p.
$$
The union of a chain of prime ideals is prime: it is an ideal because the chain is totally ordered, and if
$$
ab\in U,
$$
then
$$
ab\in\mathfrak p
$$
for some
$$
\mathfrak p\in\mathcal C,
$$
so
$$
a\in\mathfrak p
\quad\text{or}\quad
b\in\mathfrak p,
$$
and hence
$$
a\in U
\quad\text{or}\quad
b\in U.
$$

Every member of the chain contains $P$, so
$$
P\subseteq U.
$$
Every member lies inside $Q$, so
$$
U\subseteq Q.
$$
Finally,
$$
x\notin U,
$$
because otherwise $x$ would lie in some member of the union, contradicting membership in $\mathcal A$.

Thus
$$
U\in\mathcal A,
$$
and it is an upper bound for the chain.
:::

<1>3. There exists a prime ideal
$$
P^*\in\mathcal A
$$
maximal with respect to inclusion.

::: {.proof}
By steps <1>1--<1>2, Zorn's lemma applies to $\mathcal A$.
Hence there exists a maximal element
$$
P^*\in\mathcal A.
$$
Thus
$$
P\subseteq P^*\subseteq Q
$$
and
$$
x\notin P^*.
$$
Moreover, no larger prime ideal inside $Q$ can still omit $x$.
:::

<1>4. The ideal
$$
P^*+(x)
$$
is contained in $Q$.

::: {.proof}
One has
$$
P^*\subseteq Q
$$
by step <1>3, and
$$
x\in Q
$$
by construction.
Therefore
$$
P^*+(x)\subseteq Q.
$$
:::

<1>5. Let
$$
\mathcal B
\coloneqq
\{
\mathfrak q:
\mathfrak q\text{ is prime},
\ P^*+(x)\subseteq\mathfrak q\subseteq Q
\}.
$$
Then $\mathcal B$ is nonempty.

::: {.proof}
The prime ideal
$$
Q
$$
contains
$$
P^*+(x)
$$
by step <1>4.
Thus
$$
Q\in\mathcal B.
$$
:::

<1>6. Order $\mathcal B$ by reverse inclusion:
$$
\mathfrak q_1\preceq\mathfrak q_2
\quad\Longleftrightarrow\quad
\mathfrak q_2\subseteq\mathfrak q_1.
$$
Every chain has an upper bound in this order.

::: {.proof}
Let
$$
\mathcal D\subseteq\mathcal B
$$
be a chain and set
$$
L
\coloneqq
\bigcap_{\mathfrak q\in\mathcal D}\mathfrak q.
$$
The intersection of a chain of prime ideals is prime.
Indeed, if
$$
ab\in L
$$
and
$$
a\notin L,
\qquad
b\notin L,
$$
choose
$$
\mathfrak q_a,\mathfrak q_b\in\mathcal D
$$
with
$$
a\notin\mathfrak q_a,
\qquad
b\notin\mathfrak q_b.
$$
Since the chain is linearly ordered by inclusion, suppose
$$
\mathfrak q_a\subseteq\mathfrak q_b.
$$
Then
$$
b\notin\mathfrak q_b
$$
implies
$$
b\notin\mathfrak q_a,
$$
while
$$
ab\in L\subseteq\mathfrak q_a,
$$
contradicting primality of $\mathfrak q_a$.

Every member of $\mathcal D$ contains
$$
P^*+(x),
$$
so
$$
P^*+(x)\subseteq L.
$$
Also
$$
L\subseteq Q.
$$
Thus
$$
L\in\mathcal B.
$$

For every
$$
\mathfrak q\in\mathcal D,
$$
one has
$$
L\subseteq\mathfrak q,
$$
which means
$$
\mathfrak q\preceq L
$$
in the reverse order.
Hence $L$ is an upper bound.
:::

<1>7. There exists a prime ideal
$$
Q^*\in\mathcal B
$$
minimal under ordinary inclusion.

::: {.proof}
By steps <1>5--<1>6, Zorn's lemma gives a maximal element of $\mathcal B$ with respect to the reverse-inclusion order.
Call it
$$
Q^*.
$$
Maximality in the reverse order is exactly minimality under ordinary inclusion.
Thus
$$
P^*+(x)\subseteq Q^*\subseteq Q,
$$
and no smaller prime ideal inside $Q$ contains
$$
P^*+(x).
$$
:::

<1>8. One has
$$
P^*\subsetneq Q^*.
$$

::: {.proof}
By step <1>3,
$$
x\notin P^*.
$$
By step <1>7,
$$
x\in P^*+(x)\subseteq Q^*.
$$
Therefore
$$
P^*\ne Q^*.
$$
Since
$$
P^*\subseteq Q^*,
$$
the inclusion is strict.
:::

<1>9. There is no prime ideal strictly between
$$
P^*
$$
and
$$
Q^*.
$$

::: {.proof}
Suppose
$$
T
$$
is prime and
$$
P^*
\subsetneq
T
\subsetneq
Q^*.
$$

If
$$
x\notin T,
$$
then
$$
P\subseteq P^*\subsetneq T\subseteq Q^*\subseteq Q,
$$
so
$$
T\in\mathcal A.
$$
This contradicts maximality of
$$
P^*
$$
in $\mathcal A$.

If
$$
x\in T,
$$
then
$$
P^*+(x)\subseteq T\subsetneq Q^*.
$$
Thus
$$
T\in\mathcal B
$$
is a prime ideal properly contained in $Q^*$, contradicting minimality of $Q^*$ in $\mathcal B$.

Both alternatives are impossible.
Therefore no such $T$ exists.
:::

<1>10. Hence there exist prime ideals
$$
\boxed{
P\subseteq P^*
\subsetneq
Q^*\subseteq Q
}
$$
with no prime ideal strictly between $P^*$ and $Q^*$.

::: {.proof}
Steps <1>3, <1>7, <1>8, and <1>9 establish all required properties.
:::

<1>11. Q.E.D.

::: {.proof}
Step <1>10 is the desired conclusion.
:::
:::
