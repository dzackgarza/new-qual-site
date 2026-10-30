---
schema: qual/card@1
id: P-DCR24
kind: problem
title: Sylow subgroups of $A_5$, their normalizers, and subgroups of orders $6$, $10$,
  and $15$
classification:
  areas:
  - prelim
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---
::: {.problem}
a. Find Sylow subgroups $P_2, P_3$, and $P_5$ for the three primes $2, 3, 5$ dividing the order of $A_5$.
(It suffices to find generators of each of these groups.)

b. Find the normalizers in $A_5$ of each of the three groups you found in part (a).

c. For each of the divisors $d = 6, 10, 15$ of 60, either find a subgroup of $A_5$ of order $d$ or explain why none exists for that choice of $d$.
:::

::: {.solution}
Since $\cardinality{A_5}=5!/2=60=2^2\cdot3\cdot5$, Sylow subgroups have
orders $4$, $3$, and $5$.

::: pf

::: {.pf-step #s1}

For part (a), one may take
$$
\begin{aligned}
P_2&=\langle(12)(34),(13)(24)\rangle,\\
P_3&=\langle(123)\rangle,\\
P_5&=\langle(12345)\rangle.
\end{aligned}
$$

::: pf-proof

The first subgroup is
$$
\{1,(12)(34),(13)(24),(14)(23)\},
$$
so it has order $4$. The other two displayed generators have orders $3$
and $5$, respectively. These are the full powers of $2$, $3$, and $5$
dividing $\cardinality{A_5}$, so the three subgroups are Sylow subgroups.

:::

:::

::: {.pf-step #s2}

The normalizer of $P_2$ is
$$
N_{A_5}(P_2)
=\{g\in A_5:g(5)=5\}
\cong A_4,
$$
and has order $12$.

::: pf-proof

The three nonidentity elements of $P_2$ are precisely the double
transpositions fixing $5$. Their common fixed-point set is therefore
$\{5\}$. If $g$ normalizes $P_2$, conjugation by $g$ permutes these three
elements, so it preserves their common fixed-point set; hence $g(5)=5$.
Thus
$$
N_{A_5}(P_2)\subseteq\{g\in A_5:g(5)=5\}.
$$

Conversely, the even permutations fixing $5$ identify with $A_4$ acting on
$\{1,2,3,4\}$, and the Klein four subgroup of double transpositions is
normal in this $A_4$. Hence every such permutation normalizes $P_2$.

:::

:::

::: {.pf-step #s3}

The normalizer of $P_3$ is
$$
N_{A_5}(P_3)
=\langle(123),(12)(45)\rangle
\cong S_3,
$$
and has order $6$.

::: pf-proof

If $g$ normalizes $P_3=\langle(123)\rangle$, then
$g(123)g^{-1}$ is either $(123)$ or $(132)$. Hence $g$ preserves the
support $\{1,2,3\}$ and therefore also $\{4,5\}$. There are
$3!\,2!/2=6$ even permutations preserving this partition.

The displayed subgroup lies in $A_5$, preserves that partition, and has
six elements because $(123)$ has order $3$, $(12)(45)$ has order $2$, and
conjugation by $(12)(45)$ inverts $(123)$. Thus it is the full normalizer
and is isomorphic to $S_3$.

:::

:::

::: {.pf-step #s4}

The normalizer of $P_5$ is
$$
N_{A_5}(P_5)
=\langle(12345),(25)(34)\rangle
\cong D_{10},
$$
the dihedral group of order $10$.

::: pf-proof

There are $(5-1)!=24$ five-cycles in $S_5$, all of which are even.
Each Sylow $5$-subgroup contains four nonidentity five-cycles, so
$$
n_5=24/4=6.
$$
Orbit-stabilizer for conjugation gives
$$
\cardinality{N_{A_5}(P_5)}=\cardinality{A_5}/n_5=60/6=10.
$$

Let $r=(12345)$ and $s=(25)(34)$. Then $s$ is even,
$s^2=1$, and direct conjugation gives
$$
srs=r^{-1}.
$$
Hence $\langle r,s\rangle$ is a dihedral subgroup of order $10$ that
normalizes $P_5=\langle r\rangle$. By the preceding order calculation it
is the whole normalizer.

:::

:::

::: {.pf-step #s5}

For part (c), $A_5$ has subgroups of orders $6$ and $10$, namely
$N_{A_5}(P_3)$ and $N_{A_5}(P_5)$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that these normalizers have the required orders.

:::

:::

::: {.pf-step #s6}

The group $A_5$ has no subgroup of order $15$.

::: pf-proof

Suppose $H\leq A_5$ had order $15$. Sylow's theorems inside $H$ give
$$
n_5\mid3,qquad n_5\equiv1\pmod5,
$$
so $n_5=1$, and
$$
n_3\mid5,qquad n_3\equiv1\pmod3,
$$
so $n_3=1$. Thus both Sylow subgroups are normal. Their intersection is
trivial, and normal subgroups of coprime orders commute elementwise.
Therefore
$$
H\cong C_3\times C_5\cong C_{15}.
$$
In particular $A_5$ would contain an element of order $15$.

But the possible cycle types in $A_5$ are the identity, a double
transposition, a $3$-cycle, and a $5$-cycle, with orders
$1,2,3,5$. Hence no element of order $15$ exists, a contradiction.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} answers part (a), steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} answer part (b), and
steps [](#s5){.pf-ref} and [](#s6){.pf-ref} answer part (c).

:::

:::

:::
