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
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Twenty-three steps asserted their claim
    with no justification and each now carries one: the Sylow counts for $n_5$ and $n_7$ against the
    divisors of $21$ and $15$, the counting contradiction $1 + 84 + 90 = 175 > 105$, the normality of one
    of $Q, R$ and hence the subgroup $QR$ of order $35$, its cyclicity, the index-$3$ normality of that
    subgroup, the uniqueness of the subgroups of orders $5$ and $7$ in a cyclic group and the
    characteristic-subgroup argument carrying their normality up to $G$, and the direct-product and
    Chinese remainder steps that make $G$ cyclic when $P$ is normal. Checked while writing: the index-$3$
    step needs $3$ to be the smallest prime divisor of $105$ and $9$ not dividing $105$, both of which the
    justification uses. One repair: the closing pf-qed only said that steps 1 to 4 establish parts (a) to
    (d), which STYLE-08 does not admit, so it is gone and part (d) carries the QED. The statement is
    unchanged. The collection retains the UGA algebra qualifying exam of Fall 2019 and no solution sheet,
    so the argument is the card's own.
---
::: {.problem}
Let $G$ be a group of order $105 = 3 \cdot 5 \cdot 7$, and let $P \in \operatorname{Syl}_3(G)$, $Q \in \operatorname{Syl}_5(G)$, and $R \in \operatorname{Syl}_7(G)$ be Sylow 3-, 5-, and 7-subgroups of $G$, respectively.

(a) Prove that at least one of $Q$ and $R$ is normal in $G$.

(b) Prove that $G$ has a cyclic subgroup of order 35.

(c) Prove that both $Q$ and $R$ are normal in $G$.

(d) Prove that if $P$ is normal in $G$, then $G$ is cyclic.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

At least one of $Q$ and $R$ is normal in $G$.

::: pf-proof

::: pf-step

By Sylow's Theorems, the number $n_5$ of Sylow 5-subgroups satisfies $n_5 \equiv 1 \pmod 5$ and $n_5 \mid (3 \cdot 7) = 21$. Thus $n_5 \in \{1, 21\}$.


::: pf-proof
Sylow's third theorem gives $n_5 \equiv 1 \pmod 5$ and $n_5$ dividing the index $105/5 = 21$; the divisors of $21$ are $1, 3, 7, 21$ and only $1$ and $21$ are congruent to $1$ modulo $5$.
:::

:::

::: pf-step

The number $n_7$ of Sylow 7-subgroups satisfies $n_7 \equiv 1 \pmod 7$ and $n_7 \mid (3 \cdot 5) = 15$. Thus $n_7 \in \{1, 15\}$.


::: pf-proof
Likewise $n_7 \equiv 1 \pmod 7$ and $n_7$ divides $105/7 = 15$; the divisors of $15$ are $1, 3, 5, 15$ and only $1$ and $15$ are congruent to $1$ modulo $7$.
:::

:::

::: pf-step

Suppose for contradiction that neither $Q$ nor $R$ is normal in $G$, so $n_5 = 21$ and $n_7 = 15$.


::: pf-proof
A Sylow subgroup is normal exactly when it is the only one of its order, that is when its count is $1$; denying normality of $Q$ and of $R$ therefore says both counts take the other value found in the two steps above.
:::

:::

::: pf-step

$G$ has $84$ elements of order $5$ and $90$ elements of order $7$, and no element has both orders.

::: pf-proof
Each Sylow $5$-subgroup has prime order $5$, so two distinct ones meet only in $\{e\}$, and together they contain $21 \cdot (5 - 1) = 84$ elements of order $5$. Likewise the Sylow $7$-subgroups contain $15 \cdot (7 - 1) = 90$ elements of order $7$. Since $5$ and $7$ are distinct primes, no element has both orders.
:::

:::

::: pf-step

The identity, the elements of order 5, and the elements of order 7 give at least
    $$1 + 84 + 90 = 175 \text{ distinct elements in } G.$$


::: pf-proof
The product count for distinct Sylow subgroups: two distinct subgroups of prime order $5$ meet in a proper subgroup of a group of prime order, hence in $\{e\}$, so the $21$ of them contain $21 \cdot 4 = 84$ elements of order $5$; likewise the $15$ Sylow $7$-subgroups contain $15 \cdot 6 = 90$ elements of order $7$. An element cannot have order both $5$ and $7$, so the two sets are disjoint and neither contains the identity.
:::

:::

::: pf-step

This contradicts $\cardinality{G} = 105$.


::: pf-proof
The identity, the $84$ elements of order $5$ and the $90$ elements of order $7$ are pairwise distinct, so $G$ contains at least $1 + 84 + 90 = 175$ elements.
:::

:::

::: pf-step

Thus $n_5 = 1$ or $n_7 = 1$, so at least one of $Q$ or $R$ is normal in $G$.


::: pf-proof
A set of $105$ elements cannot contain $175$ distinct elements, so the supposition that both counts exceed $1$ is false.
:::

:::

:::

:::

::: {.pf-step #s2}

The group $G$ contains a cyclic subgroup of order $35$.

::: pf-proof

::: pf-step

By Part (a), $Q \trianglelefteq G$ or $R \trianglelefteq G$.


::: pf-proof
If $n_5 = 1$ the unique Sylow $5$-subgroup $Q$ is normal, and if $n_7 = 1$ the same holds for $R$; one of the two alternatives holds by the previous step.
:::

:::

::: pf-step

If one of two subgroups is normal, their set product is a subgroup. Thus $H = Q R \le G$.


::: pf-proof
By step [](#s1){.pf-ref} at least one of $Q$, $R$ is normal. If $A, B \le G$ and $A$ is normal, the set $AB$ contains $e$, is closed under inverses since $(ab)^{-1} = b^{-1}a^{-1}$ with $b^{-1}a^{-1} = a' b^{-1}$ for some $a' \in A$ by normality, and is closed under products for the same reason; so $AB$ is a subgroup, and $H = QR \le G$.
:::

:::

::: pf-step

By Lagrange's Theorem, $\cardinality{Q \cap R}$ divides $\gcd(\cardinality{Q}, \cardinality{R}) = \gcd(5, 7) = 1$, so $Q \cap R = \{e\}$.


::: pf-proof
Lagrange's theorem makes $\cardinality{Q \cap R}$ divide both $5$ and $7$, hence divide $\gcd(5,7) = 1$; a subgroup of order $1$ is $\{e\}$.
:::

:::

::: pf-step

The order of $H$ is
    $$\cardinality{H} = \frac{\cardinality{Q} \cardinality{R}}{\cardinality{Q \cap R}} = \frac{5 \cdot 7}{1} = 35.$$


::: pf-proof
For subgroups with trivial intersection the set product has $\abs{A}\abs{B}$ elements, since $ab = a'b'$ forces $a^{-1}a' = b b'^{-1} \in A \cap B = \{e\}$; here that gives $5 \cdot 7 = 35$.
:::

:::

::: pf-step

$H$ is cyclic.

::: pf-proof
In $H$, the number $n_7(H)$ of Sylow $7$-subgroups satisfies $n_7(H) \equiv 1 \pmod 7$ and $n_7(H) \mid 5$, so $n_7(H) = 1$ and $R \trianglelefteq H$. Likewise $n_5(H) \equiv 1 \pmod 5$ and $n_5(H) \mid 7$, so $n_5(H) = 1$ and $Q \trianglelefteq H$. Since $Q, R \trianglelefteq H$ and $Q \cap R = \{e\}$, $H \cong Q \times R \cong \ZZ/5\ZZ \times \ZZ/7\ZZ \cong \ZZ/35\ZZ$.
:::

:::

::: pf-step

Thus $H$ is a cyclic subgroup of order 35 in $G$.


::: pf-proof
The previous steps give a subgroup $H = QR$ of order $35$ containing $Q$ and $R$; this is the cyclic subgroup that part (b) asserts.
:::

:::

:::

:::

::: {.pf-step #s3}

Both $Q$ and $R$ are normal in $G$.

::: pf-proof

::: pf-step

Let $H \le G$ be the cyclic subgroup of order 35 from Part (b).


::: pf-proof
Part (b) produced a cyclic subgroup of order $35$; this step fixes it and names it $H$, so that the following steps have a definite object to work with.
:::

:::

::: pf-step

The index of $H$ in $G$ is $[G : H] = \frac{105}{35} = 3$.


::: pf-proof
Lagrange's theorem gives $\abs{G} = \abs{H}[G:H]$, so the index is $105/35 = 3$.
:::

:::

::: pf-step

Since 3 is the smallest prime dividing $\cardinality{G} = 105$, any subgroup of index 3 is normal in $G$. Thus $H \trianglelefteq G$.


::: pf-proof
A subgroup of index $p$, where $p$ is the smallest prime dividing $\abs{G}$, is normal: the action on the cosets gives a homomorphism $G \to S_p$ whose kernel lies in $H$, its image has order dividing both $105$ and $6$, so the image has order $1$ or $3$ because no smaller prime divides $105$ and $9$ does not divide $105$; in either case the kernel has order at least $35$ and lies in $H$, so it equals $H$ and $H$ is normal.
:::

:::

::: pf-step

In the cyclic group $H \cong \ZZ/35\ZZ$, $Q$ is the unique subgroup of order 5, and $R$ is the unique subgroup of order 7.


::: pf-proof
In a cyclic group of order $35$ the subgroup of order $d$ is unique for each divisor $d$ of $35$, being generated by $g^{35/d}$ where $g$ generates; so there is exactly one subgroup of order $5$ and one of order $7$, namely $Q$ and $R$.
:::

:::

::: pf-step

Because $Q$ and $R$ are uniquely determined by their orders in $H$, they are characteristic subgroups of $H$: for every automorphism $\sigma \in \operatorname{Aut}(H)$, $\sigma(Q) = Q$ and $\sigma(R) = R$.


::: pf-proof
A characteristic subgroup is one carried to itself by every automorphism, and a subgroup that is the only one of its order is carried to a subgroup of the same order, hence to itself; so $\sigma(Q) = Q$ and $\sigma(R) = R$ for every $\sigma \in \Aut(H)$.
:::

:::

::: pf-step

Since $H \trianglelefteq G$, conjugation by any $g \in G$ restricts to an automorphism of $H$.


::: pf-proof
Normality of $H$ means $gHg^{-1} = H$ for every $g \in G$, so conjugation by $g$ is a bijective homomorphism of $H$ onto itself, that is an automorphism of $H$.
:::

:::

::: pf-step

Thus $g Q g^{-1} = Q$ and $g R g^{-1} = R$ for all $g \in G$, proving that both $Q \trianglelefteq G$ and $R \trianglelefteq G$.


::: pf-proof
By the previous two steps $gQg^{-1} = \sigma_g(Q) = Q$ and $gRg^{-1} = \sigma_g(R) = R$ for every $g \in G$, which is exactly the normality of $Q$ and of $R$ in $G$.
:::

:::

:::

:::

::: {.pf-step #s4}

If $P$ is normal in $G$, then $G$ is cyclic.

::: pf-proof

::: pf-step

Assume $P \trianglelefteq G$. By Part (c), $Q \trianglelefteq G$ and $R \trianglelefteq G$.


::: pf-proof
This part assumes $P$ is normal, and part (c) proved unconditionally that $Q$ and $R$ are normal, so all three are.
:::

:::

::: pf-step

All three Sylow subgroups $P, Q, R$ are normal in $G$.


::: pf-proof
The assumption of this part supplies $P$ and the step above supplies $Q$ and $R$.
:::

:::

::: pf-step

$P \cap (Q R) = \{e\}$ and $Q \cap R = \{e\}$.

::: pf-proof
The orders $\abs{P} = 3$, $\abs{Q} = 5$, $\abs{R} = 7$ are pairwise coprime. An intersection of two subgroups has order dividing both orders, and $\gcd(3, 35) = \gcd(5, 7) = 1$.
:::

:::

::: pf-step

The product $P Q R$ is a subgroup of $G$ with order $\cardinality{P Q R} = \cardinality{P} \cardinality{Q} \cardinality{R} = 3 \cdot 5 \cdot 7 = 105 = \cardinality{G}$, so $G = P Q R$.


::: pf-proof
The three subgroups are normal with pairwise coprime orders and trivial pairwise intersections, as the previous step records, so their product is a subgroup of order $3 \cdot 5 \cdot 7 = 105$; a subgroup whose order equals that of the finite group is the group itself.
:::

:::

::: pf-step

Therefore $G$ is isomorphic to the internal direct product:
    $$G \cong P \times Q \times R \cong \ZZ/3\ZZ \times \ZZ/5\ZZ \times \ZZ/7\ZZ.$$


::: pf-proof
A group that is the product of normal subgroups with pairwise trivial intersections is their direct product, since each element factors uniquely and the factors commute; each subgroup has prime order and so is cyclic, which gives $G \cong \ZZ/3\ZZ \times \ZZ/5\ZZ \times \ZZ/7\ZZ$.
:::

:::

::: pf-step

By the Chinese Remainder Theorem, $\ZZ/3\ZZ \times \ZZ/5\ZZ \times \ZZ/7\ZZ \cong \ZZ/105\ZZ$, which is cyclic.


::: pf-proof
The Chinese remainder theorem for the pairwise coprime moduli $3$, $5$ and $7$ identifies that product with $\ZZ/105\ZZ$, which is cyclic because $1$ generates it additively.
:::

:::

:::

:::

:::

:::
