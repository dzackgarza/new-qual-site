---
schema: qual/card@1
id: P-KSRING17-130
kind: problem
title: Maximal and minimal elements in sets of prime ideals
classification:
  areas: [algebra]
  topics:
  - Prime Ideals
  - Zorn's Lemma
  - Chains of Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 130 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked problem 130 on Ring_Theory_Qual_Problems.pdf PDF page 16 and added an erratum because the statement is false for arbitrary sets of prime ideals.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source asks to prove that any non-empty set of prime ideals has maximal and minimal elements, which fails for $\{(x_1,\ldots,x_n)\}$ and $\{(x_n,x_{n+1},\ldots)\}$ in $k[x_1,x_2,\ldots]$. The statement now assumes the set contains the union and the intersection of each of its non-empty chains.
---

::: {.problem}
Let $R$ be a commutative ring with identity.
Let $\mathcal S$ be a non-empty set of prime ideals of $R$ that contains the union and the intersection of each of its non-empty chains. Prove that $\mathcal S$ contains maximal *and* minimal elements.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The union of a chain of prime ideals is an ideal.

::: pf-proof

Let
$$
\mathcal C
$$
be a chain under inclusion, and set
$$
U
\coloneqq
\bigcup_{P\in\mathcal C}P.
$$
Let
$$
x,y\in U.
$$
Then
$$
x\in P,
\qquad
y\in Q
$$
for some
$$
P,Q\in\mathcal C.
$$
Since the collection is a chain, either
$$
P\subseteq Q
$$
or
$$
Q\subseteq P.
$$
Thus $x$ and $y$ lie in a common member of the chain, so
$$
x-y\in U.
$$
If
$$
r\in R
$$
and
$$
x\in U,
$$
choose
$$
P\in\mathcal C
$$
with
$$
x\in P.
$$
Then
$$
rx\in P\subseteq U.
$$
Hence $U$ is an ideal.

:::

:::

::: pf-step

The union of a nonempty chain of prime ideals is prime.

::: pf-proof

Let
$$
U
=
\bigcup_{P\in\mathcal C}P.
$$
By step [](#s1-1){.pf-ref}, $U$ is an ideal.
It is proper: if
$$
1\in U,
$$
then
$$
1\in P
$$
for some
$$
P\in\mathcal C,
$$
contradicting properness of the prime ideal $P$.

Now suppose
$$
ab\in U.
$$
Then
$$
ab\in P
$$
for some
$$
P\in\mathcal C.
$$
Since $P$ is prime,
$$
a\in P
\quad\text{or}\quad
b\in P.
$$
Hence
$$
a\in U
\quad\text{or}\quad
b\in U.
$$
Thus $U$ is prime.

:::

:::

::: {.pf-step #s1-3}

The poset
$$
(\mathcal S,\subseteq)
$$
has a maximal element.

::: pf-proof

The poset is nonempty by hypothesis.
Let
$$
\mathcal C
\subseteq
\mathcal S
$$
be a nonempty chain.
By the closure hypothesis,
$$
U
\coloneqq
\bigcup_{P\in\mathcal C}P
$$
belongs to $\mathcal S$.
Clearly every
$$
P\in\mathcal C
$$
satisfies
$$
P\subseteq U.
$$
Thus $U$ is an upper bound for the chain.

The empty chain has an upper bound because $\mathcal S$ is nonempty.
Therefore every chain has an upper bound in $\mathcal S$.
Zorn's lemma yields a maximal element.

:::

:::

::: pf-step

The intersection of a chain of prime ideals is an ideal.

::: pf-proof

An arbitrary intersection of ideals is an ideal.
Thus
$$
I
\coloneqq
\bigcap_{P\in\mathcal C}P
$$
is an ideal.

:::

:::

::: pf-step

The intersection of a nonempty chain of prime ideals is prime.

::: pf-proof

Set
$$
I
\coloneqq
\bigcap_{P\in\mathcal C}P.
$$
It is proper because it is contained in every prime ideal of the nonempty chain.

Suppose
$$
ab\in I
$$
and, for contradiction,
$$
a\notin I,
\qquad
b\notin I.
$$
Choose
$$
P,Q\in\mathcal C
$$
such that
$$
a\notin P,
\qquad
b\notin Q.
$$
Since $\mathcal C$ is a chain, assume without loss of generality that
$$
P\subseteq Q.
$$
Then
$$
b\notin Q
$$
implies
$$
b\notin P.
$$
But
$$
ab\in I\subseteq P,
$$
contradicting primality of $P$.
Therefore
$$
a\in I
\quad\text{or}\quad
b\in I.
$$
Hence $I$ is prime.

:::

:::

::: {.pf-step #s1-6}

Order $\mathcal S$ by reverse inclusion:
$$
P\preceq Q
\quad\Longleftrightarrow\quad
Q\subseteq P.
$$
Then every chain has an upper bound.

::: pf-proof

Let
$$
\mathcal C
$$
be a nonempty chain in the reverse order.
It is also a chain under ordinary inclusion.
By the closure hypothesis,
$$
I
\coloneqq
\bigcap_{P\in\mathcal C}P
$$
belongs to $\mathcal S$.
For every
$$
P\in\mathcal C,
$$
one has
$$
I\subseteq P,
$$
which means
$$
P\preceq I.
$$
Thus $I$ is an upper bound in the reverse order.

Again, the empty chain has an upper bound because $\mathcal S$ is nonempty.

:::

:::

::: {.pf-step #s1-7}

The family $\mathcal S$ has a minimal element under ordinary inclusion.

::: pf-proof

Apply Zorn's lemma to the reverse-inclusion order from step [](#s1-6){.pf-ref}.
There is a maximal element with respect to
$$
\preceq.
$$
Maximality in reverse inclusion is exactly minimality in ordinary inclusion.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{
\mathcal S
\text{ contains both a maximal and a minimal element}.
}
$$

::: pf-proof

Step [](#s1-3){.pf-ref} gives a maximal element, and step [](#s1-7){.pf-ref} gives a minimal element.

:::

:::

:::

:::
