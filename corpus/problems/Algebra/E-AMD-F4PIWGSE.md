---
schema: qual/card@1
id: E-AMD-F4PIWGSE
kind: problem
title: Sylow subgroups of a group of order $240$, and subgroups of order $15$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Semidirect Products
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Suppose $|G| = 240 = 2^4 \cdot 3 \cdot 5$.

- How many Sylow-$p$ subgroups does $G$ have for $p\in \{2, 3, 5\}$?

- Show that if $G$ has a subgroup of order 15, it has an element of order 15.

- Show that if $G$ does not have such a subgroup, the number of Sylow-$3$ subgroups is either 10 or 40.
:::

::: solution
**Goal:** Determine candidate Sylow $p$-subgroup counts for $|G| = 240$, prove that any subgroup of order $15$ is cyclic, and prove that if no subgroup of order $15$ exists, then $n_3 \in \{10, 40\}$.

<1>1. Possible values for $n_p$:
    *Proof:*
    <2>1. The prime factorization is $|G| = 240 = 2^4 \cdot 3 \cdot 5$.
    <2>2. **For $p = 2$:** $n_2 \equiv 1 \pmod 2$ and $n_2 \mid 15$. The divisors of $15$ are $\{1, 3, 5, 15\}$, all of which are odd:
        $$n_2 \in \{1, 3, 5, 15\}.$$
    <2>3. **For $p = 3$:** $n_3 \equiv 1 \pmod 3$ and $n_3 \mid 80$. The divisors of $80$ congruent to $1 \pmod 3$ are:
        $$n_3 \in \{1, 4, 10, 16, 40\}.$$
    <2>4. **For $p = 5$:** $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 48$. The divisors of $48$ congruent to $1 \pmod 5$ are:
        $$n_5 \in \{1, 6, 16\}.$$

<1>2. Subgroups of order $15$ are cyclic:
    *Proof:*
    <2>1. Let $H \le G$ with $|H| = 15 = 3 \cdot 5$.
    <2>2. In $H$, the Sylow counts satisfy $n_5(H) \equiv 1 \pmod 5, n_5(H) \mid 3 \implies n_5(H) = 1$, and $n_3(H) \equiv 1 \pmod 3, n_3(H) \mid 5 \implies n_3(H) = 1$.
    <2>3. Thus the unique Sylow 3-subgroup and Sylow 5-subgroup of $H$ are both normal in $H$.
    <2>4. Therefore $H \cong \mathbb{Z}_3 \times \mathbb{Z}_5 \cong \mathbb{Z}_{15}$.
    <2>5. Being cyclic of order $15$, $H$ (and hence $G$) contains an element of order $15$.

<1>3. If $G$ has no subgroup of order $15$, then $n_3 \in \{10, 40\}$:
    *Proof:*
    <2>1. Let $Q \in \operatorname{Syl}_5(G)$ be a Sylow 5-subgroup of $G$ (so $|Q| = 5$).
    <2>2. Consider the conjugation action of $Q$ on the set $\operatorname{Syl}_3(G)$ of size $n_3$:
        $$q \cdot P = q P q^{-1} \quad \text{for } q \in Q, \, P \in \operatorname{Syl}_3(G).$$
    <2>3. Because $|Q| = 5$ is prime, every orbit under this action has size $1$ or $5$.
    <2>4. An orbit of size $1$ corresponds to a fixed point $P \in \operatorname{Syl}_3(G)$ normalized by $Q$ ($q P q^{-1} = P$ for all $q \in Q$).
    <2>5. If such a fixed point $P$ exists, the product $P Q$ forms a subgroup of $G$ of order $\frac{|P| |Q|}{|P \cap Q|} = \frac{3 \cdot 5}{1} = 15$.
    <2>6. By hypothesis, $G$ contains no subgroup of order $15$, so there are no fixed points.
    <2>7. Every orbit has size $5$, so $5$ divides the total number of Sylow 3-subgroups: $5 \mid n_3$.
    <2>8. Filtering the candidate list $n_3 \in \{1, 4, 10, 16, 40\}$ for multiples of $5$ yields:
        $$n_3 \in \{10, 40\}.$$

<1>4. Conclusion:
    The counts $n_p$ are restricted as listed, subgroups of order $15$ are cyclic, and the absence of such subgroups forces $n_3 \in \{10, 40\}$. Q.E.D.
:::
