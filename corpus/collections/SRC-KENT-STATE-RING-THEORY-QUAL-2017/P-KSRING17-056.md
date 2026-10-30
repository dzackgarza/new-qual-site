---
schema: qual/card@1
id: P-KSRING17-056
kind: problem
title: Every prime ideal contains a minimal prime ideal
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 56 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Let $R$ be a commutative ring and $P$ a prime ideal of $R$. Show that there is a prime ideal $P_{0} \subseteq P$ that does not properly contain any prime ideal.
:::

::: {.solution}

Let
$$
\mathcal P
\coloneqq
\{
Q\trianglelefteq R:
Q\text{ is prime and }Q\subseteq P
\}.
$$
Order $\mathcal P$ by reverse inclusion:
$$
Q_1\preceq Q_2
\quad\Longleftrightarrow\quad
Q_2\subseteq Q_1.
$$

::: pf

::: {.pf-step #s1-1}

The poset $\mathcal P$ is nonempty.


::: pf-proof

The given prime ideal
$$
P
$$
belongs to $\mathcal P$.

:::

:::

::: {.pf-step #s1-2}

Let
$$
\mathcal C
\subseteq
\mathcal P
$$
be a chain with respect to $\preceq$.
Then
$$
Q_\mathcal C
\coloneqq
\bigcap_{Q\in\mathcal C}Q
$$
is a prime ideal.


::: pf-proof

A chain for the reverse-inclusion order is also a chain under ordinary inclusion.
The intersection of a chain of prime ideals is prime:
if
$$
ab
\in
\bigcap_{Q\in\mathcal C}Q
$$
and both
$$
a
\notin
\bigcap_{Q\in\mathcal C}Q,
\qquad
b
\notin
\bigcap_{Q\in\mathcal C}Q,
$$
choose
$$
Q_a,Q_b\in\mathcal C
$$
with
$$
a\notin Q_a,
\qquad
b\notin Q_b.
$$
Since the chain is linearly ordered by inclusion, assume without loss of generality that
$$
Q_a\subseteq Q_b.
$$
Then
$$
b\notin Q_b
$$
implies
$$
b\notin Q_a.
$$
But
$$
ab
\in
\bigcap_{Q\in\mathcal C}Q
\subseteq
Q_a,
$$
contradicting primality of $Q_a$.

Thus the intersection satisfies the prime-product condition.
It is proper because it is contained in every member of the nonempty chain, each of which is proper.

:::

:::

::: {.pf-step #s1-3}

One has
$$
Q_\mathcal C
\subseteq
P.
$$


::: pf-proof

Every member
$$
Q\in\mathcal C
$$
lies in $\mathcal P$, so
$$
Q\subseteq P.
$$
Therefore their intersection is also contained in $P$.

:::

:::

::: {.pf-step #s1-4}

The ideal
$$
Q_\mathcal C
$$
is an upper bound for $\mathcal C$ with respect to $\preceq$.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
Q_\mathcal C
\in
\mathcal P.
$$
For every
$$
Q\in\mathcal C,
$$
one has
$$
Q_\mathcal C
\subseteq
Q.
$$
By the definition of the reverse order, this means
$$
Q
\preceq
Q_\mathcal C.
$$
Hence $Q_\mathcal C$ is an upper bound of the chain.

:::

:::

::: {.pf-step #s1-5}

There exists a maximal element
$$
P_0
$$
of the poset
$$
(\mathcal P,\preceq).
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the poset is nonempty, and by step [](#s1-4){.pf-ref} every chain has an upper bound in the poset.
Zorn's lemma therefore gives a maximal element
$$
P_0\in\mathcal P.
$$

:::

:::

::: {.pf-step #s1-6}

The prime ideal $P_0$ is minimal under ordinary inclusion among prime ideals contained in $P$.


::: pf-proof

Suppose
$$
Q
$$
is a prime ideal with
$$
Q\subsetneq P_0.
$$
Then, because
$$
P_0\subseteq P,
$$
one also has
$$
Q\subseteq P,
$$
so
$$
Q\in\mathcal P.
$$
But
$$
Q\subsetneq P_0
$$
means
$$
P_0
\prec
Q
$$
in the reverse order, contradicting maximality of $P_0$.
Thus no prime ideal is properly contained in $P_0$.

:::

:::

::: {.pf-step #s1-7}

Therefore there exists a prime ideal
$$
\boxed{
P_0\subseteq P
}
$$
that does not properly contain any prime ideal.


::: pf-proof

Step [](#s1-5){.pf-ref} constructs $P_0\subseteq P$, and step [](#s1-6){.pf-ref} proves its minimality.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the required conclusion.

:::

:::

:::
