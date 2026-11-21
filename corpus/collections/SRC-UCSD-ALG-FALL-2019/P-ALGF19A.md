---
schema: qual/card@1
id: P-ALGF19A
kind: problem
title: Non-Sylow $p$-subgroup has $p$ dividing $\cardinality{N_G(P)/P}$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 1 of the official UCSD Algebra Qualifying Exam, Fall 2019 source; the statement agrees with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the fixed-point congruence for the action of P on Q/P and the resulting divisibility through N_Q(P) <= N_G(P).
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Seven steps asserted their claim with no justification and each now carries one: the containment of $P$
    in a strictly larger Sylow $p$-subgroup from Sylow's second and third theorems, the index
    $[Q:P] = p^k$ with $k \ge 1$ from the strictness of the inclusion, the left action of $P$ on the
    cosets together with the fixed point congruence for a finite $p$-group, the identification of $X^P$
    with $N_Q(P)/P$ through conjugation and equality of orders, the consequence $\abs{X^P} \ge p$ and
    hence the divisibility of the index, the tower $P \le N_Q(P) \le N_G(P)$ with multiplicativity of
    indices, and the passage from an index to the order of the quotient. Three container steps carried
    labels and now state the claim their proofs establish, and the closing pf-qed, whose whole content
    repeated the last step's claim, is removed. Sources are cited by numbered statement: Sylow's second
    and third theorems, the fixed point congruence for a $p$-group action, and multiplicativity of the
    index in a tower of subgroups. No page reference is written in the body of this card or in the event
    above. The statement is unchanged. The collection retains the UCSD algebra qualifying exam of Fall
    2019 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Suppose $G$ is a finite group and $P$ is a $p$-subgroup of $G$ which is not a Sylow $p$-subgroup.
Prove that $p$ divides $\cardinality{N_G(P)/P}$.
:::

::: {.solution}

::: pf

::: {.pf-step #sylow}

Some Sylow $p$-subgroup $Q$ of $G$ contains $P$ strictly.

::: pf-proof

::: pf-step
By the Sylow Theorems, every $p$-subgroup of a finite group $G$ is contained in some Sylow $p$-subgroup.
Since $P$ is not a Sylow $p$-subgroup, there exists a Sylow $p$-subgroup $Q \le G$ such that:
$$
P \subsetneq Q.
$$

::: pf-proof
Sylow's second and third theorems together say every $p$-subgroup is contained in a Sylow $p$-subgroup, of order $\abs{G}_p$ the full $p$-part of $\abs{G}$. If $P$ were the only such subgroup containing it, $P$ would have that maximal order and be Sylow itself; since it is not, some Sylow $p$-subgroup $Q$ contains $P$ strictly.
:::

:::

:::

:::

::: {.pf-step #action}

The set $X = Q/P$ has $p^k$ elements with $k \ge 1$, and the action of $P$ on it by left multiplication has $p \mid \abs{X^P}$ with $X^P = N_Q(P)/P$.

::: pf-proof

::: pf-step
Let $X = Q/P = \{xP \mid x \in Q\}$ be the set of left cosets of $P$ in $Q$.
Because $P \subsetneq Q$ and $Q$ is a $p$-group, $\cardinality{X} = [Q : P] = p^k$ for some integer $k \ge 1$.

::: pf-proof
The left cosets of $P$ in $Q$ partition $Q$, and the number of them is the index $[Q:P] = \abs{Q}/\abs{P}$. Both orders are powers of $p$, so the index is $p^k$; it is at least $2$, hence $k \ge 1$, because $P \subsetneq Q$.
:::

:::

::: pf-step
Let $P$ act on $X$ by left multiplication: $y \cdot (xP) = (yx)P$ for $y \in P, x \in Q$.
Since $P$ is a $p$-group, the number of fixed points satisfies the fixed point congruence:
$$
\cardinality{X^P} \equiv \cardinality{X} \equiv 0 \pmod p.
$$

::: pf-proof
Left multiplication by an element of $P$ sends the coset $xP$ to $yxP$, which is another coset of $P$ and depends only on $y$ and $xP$; associativity gives $y'(y xP) = (y'y)xP$ and $e xP = xP$, so this is an action of $P$. For a finite $p$-group acting on a finite set, the fixed points satisfy $\abs{X^P} \equiv \abs{X} \pmod p$, because every orbit has size a power of $p$ and the orbits of size $1$ are exactly the fixed points.
:::

:::

::: pf-step
A coset $xP \in X$ is fixed by $P$ if and only if:
$$
y x P = x P \quad \forall y \in P \iff x^{-1} P x \subseteq P.
$$
Since $P$ is finite, $x^{-1}Px$ and $P$ have the same order, so the inclusion is an equality. Thus the last condition is equivalent to $x\in N_Q(P)$.
Therefore the fixed point set is $X^P = N_Q(P) / P$.

::: pf-proof
The coset $xP$ is fixed by all $y \in P$ exactly when $yxP = xP$ for all such $y$, that is $x^{-1}yx \in P$ for all $y \in P$, that is $x^{-1}Px \subseteq P$. Conjugation by $x$ is an isomorphism onto $x^{-1}Px$, so the two groups have equal order, and an inclusion of finite groups of equal order is an equality; hence the condition is $x^{-1}Px \subseteq P$, equivalently $x \in N_G(P)$, and since also $x \in Q$ this is $x \in N_G(P) \cap Q$. The fixed cosets are therefore the cosets of $P$ by elements of $N_Q(P)$, which is $N_Q(P)/P$.
:::

:::

::: pf-step
The coset $eP = P$ is always fixed, so $\cardinality{X^P} \ge 1$.
Since $p \mid \cardinality{X^P}$ and $\cardinality{X^P} \ge 1$, we have $\cardinality{X^P} = [N_Q(P) : P] \ge p$, and:
$$
p \mid [N_Q(P) : P].
$$

::: pf-proof
The identity coset $eP$ is fixed by every $y \in P$ because $ye \in P$, so the fixed set is nonempty and its cardinality is at least $1$; the congruence of the action gives $p \mid \abs{X^P}$, and the only positive multiple of $p$ is at least $p$, so $\abs{X^P} \ge p$. By the identification of the fixed set with $N_Q(P)/P$, the index $[N_Q(P):P]$ is that cardinality and $p$ divides it.
:::

:::

:::

:::

::: {.pf-step #divisibility}

$p$ divides $\cardinality{N_G(P)/P}$.

::: pf-proof

::: pf-step
Since $N_Q(P) = N_G(P) \cap Q$, we have the tower of subgroups $P \le N_Q(P) \le N_G(P)$.
By the multiplicativity of subgroup indices:
$$
\cardinality{N_G(P) / P} = [N_G(P) : P] = [N_G(P) : N_Q(P)] \cdot [N_Q(P) : P].
$$

::: pf-proof
The normalizer of $P$ in $G$ meets $Q$ in the elements of $Q$ that normalize $P$, which is by definition $N_Q(P)$; and $P$ normalizes itself, so $P \le N_Q(P)$. Also $N_Q(P) \le N_G(P)$ because an element of $Q$ normalizing $P$ is an element of $G$ normalizing $P$. For a tower $P \le N_Q(P) \le N_G(P)$ of finite groups the index is multiplicative: $[N_G(P):P] = [N_G(P):N_Q(P)]\,[N_Q(P):P]$, since $\abs{N_G(P)} = [N_G(P):N_Q(P)]\abs{N_Q(P)}$ and $\abs{N_Q(P)} = [N_Q(P):P]\abs{P}$.
:::

:::

::: pf-step
Since $p$ divides $[N_Q(P) : P]$, $p$ divides $\cardinality{N_G(P)/P}$.

::: pf-proof
The order $\abs{N_G(P)/P}$ is the index $[N_G(P):P]$ of the subgroup $P$ in $N_G(P)$, because $P$ is normal in $N_G(P)$. That index is a product of two integers, one of which is divisible by $p$, so the product is divisible by $p$.
:::

:::

:::

:::

:::
:::
