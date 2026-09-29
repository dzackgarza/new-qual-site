---
schema: qual/card@1
id: P-VI6QM
kind: problem
title: 'Groups of order $105$: normal Sylow $5$- and $7$-subgroups, a cyclic subgroup
  of order $35$, and cyclicity when the Sylow $3$-subgroup is normal'
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - Cyclic Groups
relations: []
review: draft
---

::: {.problem}
Let $G$ be a group of order $105 = 3 \cdot 5 \cdot 7$, and let $P \in \operatorname{Syl}_3(G)$, $Q \in \operatorname{Syl}_5(G)$, and $R \in \operatorname{Syl}_7(G)$ be Sylow 3-, 5-, and 7-subgroups of $G$, respectively.

(a) Prove that at least one of $Q$ and $R$ is normal in $G$.

(b) Prove that $G$ has a cyclic subgroup of order 35.

(c) Prove that both $Q$ and $R$ are normal in $G$.

(d) Prove that if $P$ is normal in $G$, then $G$ is cyclic.
:::

::: {.solution}
**Goal:** Prove normality of Sylow subgroups, existence of a cyclic subgroup of order 35, and deduce that $G$ is cyclic when all Sylow subgroups are normal.

::: pf

::: pf-step
Part (a): At least one of $Q$ or $R$ is normal in $G$.

::: pf-proof

::: pf-step
By Sylow's Theorems, the number $n_5$ of Sylow 5-subgroups satisfies $n_5 \equiv 1 \pmod 5$ and $n_5 \mid (3 \cdot 7) = 21$. Thus $n_5 \in \{1, 21\}$.
:::

::: pf-step
The number $n_7$ of Sylow 7-subgroups satisfies $n_7 \equiv 1 \pmod 7$ and $n_7 \mid (3 \cdot 5) = 15$. Thus $n_7 \in \{1, 15\}$.
:::

::: pf-step
Suppose for contradiction that neither $Q$ nor $R$ is normal in $G$, so $n_5 = 21$ and $n_7 = 15$.
:::

::: pf-step
Count elements:

- Each Sylow 5-subgroup has prime order 5, so any two distinct Sylow 5-subgroups intersect only in the identity $\{e\}$. Together they contain $21 \cdot (5 - 1) = 84$ elements of order 5.
- Each Sylow 7-subgroup has prime order 7, so any two distinct Sylow 7-subgroups intersect only in $\{e\}$. Together they contain $15 \cdot (7 - 1) = 90$ elements of order 7.
- Since 5 and 7 are distinct primes, no element can have both order 5 and order 7.
:::

::: pf-step
The identity, the elements of order 5, and the elements of order 7 give at least
$$1 + 84 + 90 = 175 \text{ distinct elements in } G.$$
:::

::: pf-step
This contradicts $|G| = 105$.
:::

::: pf-step
Thus $n_5 = 1$ or $n_7 = 1$, so at least one of $Q$ or $R$ is normal in $G$.
:::

:::

:::

::: pf-step
Part (b): $G$ has a cyclic subgroup of order 35.

::: pf-proof

::: pf-step
By Part (a), $Q \trianglelefteq G$ or $R \trianglelefteq G$.
:::

::: pf-step
If one of two subgroups is normal, their set product is a subgroup. Thus $H = Q R \le G$.
:::

::: pf-step
By Lagrange's Theorem, $|Q \cap R|$ divides $\gcd(|Q|, |R|) = \gcd(5, 7) = 1$, so $Q \cap R = \{e\}$.
:::

::: pf-step
The order of $H$ is
$$|H| = \frac{|Q| |R|}{|Q \cap R|} = \frac{5 \cdot 7}{1} = 35.$$
:::

::: pf-step
$H$ is cyclic:

- In $H$, the number of Sylow 7-subgroups $n_7(H)$ satisfies $n_7(H) \equiv 1 \pmod 7$ and $n_7(H) \mid 5 \implies n_7(H) = 1$, so the Sylow 7-subgroup $R \trianglelefteq H$.
- The number of Sylow 5-subgroups $n_5(H)$ satisfies $n_5(H) \equiv 1 \pmod 5$ and $n_5(H) \mid 7 \implies n_5(H) = 1$, so the Sylow 5-subgroup $Q \trianglelefteq H$.
- Since $Q, R \trianglelefteq H$ and $Q \cap R = \{e\}$, $H \cong Q \times R \cong \mathbb{Z}/5\mathbb{Z} \times \mathbb{Z}/7\mathbb{Z} \cong \mathbb{Z}/35\mathbb{Z}$.
:::

::: pf-step
Thus $H$ is a cyclic subgroup of order 35 in $G$.
:::

:::

:::

::: pf-step
Part (c): Both $Q$ and $R$ are normal in $G$.

::: pf-proof

::: pf-step
Let $H \le G$ be the cyclic subgroup of order 35 from Part (b).
:::

::: pf-step
The index of $H$ in $G$ is $[G : H] = \frac{105}{35} = 3$.
:::

::: pf-step
Since 3 is the smallest prime dividing $|G| = 105$, any subgroup of index 3 is normal in $G$. Thus $H \trianglelefteq G$.
:::

::: pf-step
In the cyclic group $H \cong \mathbb{Z}/35\mathbb{Z}$, $Q$ is the unique subgroup of order 5, and $R$ is the unique subgroup of order 7.
:::

::: pf-step
Because $Q$ and $R$ are uniquely determined by their orders in $H$, they are characteristic subgroups of $H$: for every automorphism $\sigma \in \operatorname{Aut}(H)$, $\sigma(Q) = Q$ and $\sigma(R) = R$.
:::

::: pf-step
Since $H \trianglelefteq G$, conjugation by any $g \in G$ restricts to an automorphism of $H$.
:::

::: pf-step
Thus $g Q g^{-1} = Q$ and $g R g^{-1} = R$ for all $g \in G$, proving that both $Q \trianglelefteq G$ and $R \trianglelefteq G$.
:::

:::

:::

::: pf-step
Part (d): If $P \trianglelefteq G$, then $G$ is cyclic.

::: pf-proof

::: pf-step
Assume $P \trianglelefteq G$. By Part (c), $Q \trianglelefteq G$ and $R \trianglelefteq G$.
:::

::: pf-step
All three Sylow subgroups $P, Q, R$ are normal in $G$.
:::

::: pf-step
Since $|P| = 3$, $|Q| = 5$, $|R| = 7$ are pairwise coprime:

- $P \cap (Q R) = \{e\}$ because $|P| = 3$ and $|Q R| = 35$ with $\gcd(3, 35) = 1$.
- $Q \cap R = \{e\}$ because $\gcd(5, 7) = 1$.
:::

::: pf-step
The product $P Q R$ is a subgroup of $G$ with order $|P Q R| = |P| |Q| |R| = 3 \cdot 5 \cdot 7 = 105 = |G|$, so $G = P Q R$.
:::

::: pf-step
Therefore $G$ is isomorphic to the internal direct product:
$$G \cong P \times Q \times R \cong \mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z} \times \mathbb{Z}/7\mathbb{Z}.$$
:::

::: pf-step
By the Chinese Remainder Theorem, $\mathbb{Z}/3\mathbb{Z} \times \mathbb{Z}/5\mathbb{Z} \times \mathbb{Z}/7\mathbb{Z} \cong \mathbb{Z}/105\mathbb{Z}$, which is cyclic.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$Q$ and $R$ are normal in $G$, $G$ contains a cyclic subgroup of order 35, and normality of $P$ implies $G \cong \mathbb{Z}/105\mathbb{Z}$.
:::

:::

:::
:::
