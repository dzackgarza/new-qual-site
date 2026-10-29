---
schema: qual/card@1
id: P-MD2U3
kind: problem
title: Classification of groups of order $45$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Sylow Theory
  - Abelian Groups
relations: []
review: draft
---
::: {.problem}
How many isomorphism classes of groups of order 45 are there? Describe a representative from each class with full justification.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every group $G$ of order $45$ has unique (hence normal) Sylow $3$- and $5$-subgroups $P$ and $Q$.

::: pf-proof

::: pf-step

The prime factorization of the group order is $|G| = 45 = 3^2 \cdot 5$.

:::

::: pf-step

Sylow 5-subgroups: Let $n_5$ denote the number of Sylow 5-subgroups of $G$. By the Sylow Theorems, $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 3^2 = 9$. The divisors of 9 are $\{1, 3, 9\}$, and only $1 \equiv 1 \pmod 5$. Thus $n_5 = 1$.

:::

::: pf-step

Sylow 3-subgroups: Let $n_3$ denote the number of Sylow 3-subgroups of $G$. By the Sylow Theorems, $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 5$. The divisors of 5 are $\{1, 5\}$, and only $1 \equiv 1 \pmod 3$. Thus $n_3 = 1$.

:::

::: pf-step

Let $P \in \operatorname{Syl}_3(G)$ and $Q \in \operatorname{Syl}_5(G)$ be the unique Sylow 3- and 5-subgroups. Since they are unique, $P \trianglelefteq G$ and $Q \trianglelefteq G$.

:::

:::

:::

::: {.pf-step #s2}

Every such group decomposes as $G\cong P\times Q$.

::: pf-proof

::: pf-step

Coprime intersection: By Lagrange's Theorem, $|P \cap Q|$ divides both $|P| = 9$ and $|Q| = 5$. Since $\gcd(9, 5) = 1$, $P \cap Q = \{e\}$.

:::

::: pf-step

Group order: Since both $P$ and $Q$ are normal in $G$, the set product $P Q$ is a subgroup of $G$ with cardinality
    $$|P Q| = \frac{|P| |Q|}{|P \cap Q|} = \frac{9 \cdot 5}{1} = 45 = |G|.$$
    Thus $G = P Q$.

:::

::: pf-step

Internal direct product: Since $P, Q \trianglelefteq G$, $P \cap Q = \{e\}$, and $P Q = G$, $G \cong P \times Q$.

:::

:::

:::

::: {.pf-step #s3}

The subgroup $Q$ is cyclic of order five, and $P$ is either cyclic of order nine or isomorphic to $C_3\times C_3$.

::: pf-proof

::: pf-step

The group $Q$ has prime order $|Q| = 5$, so $Q \cong \ZZ/5\ZZ$.

:::

::: pf-step

The group $P$ has order $|P| = 3^2 = 9$. Every group of order $p^2$ for a prime $p$ is abelian.

:::

::: pf-step

By the Fundamental Theorem of Finite Abelian Groups, there are exactly two isomorphism classes of groups of order 9:

:::

$$P \cong \ZZ/9\ZZ \quad \text{or} \quad P \cong \ZZ/3\ZZ \times \ZZ/3\ZZ.$$

:::

:::

::: {.pf-step #s4}

There are exactly two isomorphism classes, represented by
$$
\boxed{C_{45}\qquad\text{and}\qquad C_3\times C_{15}}.
$$

::: pf-proof

::: pf-step

Case 1 ($P \cong \ZZ/9\ZZ$):
    $$G_1 \cong \ZZ/9\ZZ \times \ZZ/5\ZZ \cong \ZZ/45\ZZ$$
    by the Chinese Remainder Theorem, which is the cyclic group of order 45.

:::

::: pf-step

Case 2 ($P \cong \ZZ/3\ZZ \times \ZZ/3\ZZ$):
    $$G_2 \cong \ZZ/3\ZZ \times \ZZ/3\ZZ \times \ZZ/5\ZZ \cong \ZZ/3\ZZ \times \ZZ/15\ZZ.$$

:::

::: pf-step

Non-isomorphism: $G_1$ contains an element of order 45 (a generator), whereas every element $g = (a, b, c) \in G_2$ satisfies $15 g = 0$, so the exponent of $G_2$ is $\operatorname{lcm}(3, 3, 5) = 15 < 45$. Thus $G_1 \not\cong G_2$.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove the classification and distinguish the two groups.

:::

:::

:::
