---
schema: qual/card@1
id: P-PKXBP
kind: problem
title: A normal $p$-subgroup lies in every Sylow $p$-subgroup, and in a maximal subgroup
  or with $p$-power index
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Normal Subgroups
  - p-Groups
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group whose order is divisible by a prime number $p$, and let $P \trianglelefteq G$ be a normal $p$-subgroup of $G$ with $|P| = p^c$ for some integer $c \ge 1$.

(a) Show that $P$ is contained in every Sylow $p$-subgroup of $G$.

(b) Let $M$ be a maximal proper subgroup of $G$. Show that either $P \subseteq M$ or the index satisfies $[G : M] = p^b$ for some integer $1 \le b \le c$.
:::

::: {.hint}
Normality of $P$ buys you a *subgroup* $PS$, not merely a subset. Compute its order.
:::

::: {.solution}
**Goal:** Prove that a normal $p$-subgroup is contained in the intersection of all Sylow $p$-subgroups in (a), and deduce that a maximal subgroup either contains $P$ or has $p$-power index in (b).

::: pf

::: pf-step
Part (a): $P$ is contained in every Sylow $p$-subgroup of $G$.

::: pf-proof

::: pf-step
By the Sylow Theorems, $G$ contains at least one Sylow $p$-subgroup $Q_0 \in \operatorname{Syl}_p(G)$, and every $p$-subgroup of $G$ is contained in some Sylow $p$-subgroup.
:::

::: pf-step
Since $P$ is a $p$-subgroup of $G$, choose a Sylow $p$-subgroup $Q_0 \in \operatorname{Syl}_p(G)$ such that $P \subseteq Q_0$.
:::

::: pf-step
Let $Q \in \operatorname{Syl}_p(G)$ be an arbitrary Sylow $p$-subgroup.
:::

::: pf-step
By the Second Sylow Theorem, all Sylow $p$-subgroups of $G$ are conjugate: there exists an element $g \in G$ such that $Q = g Q_0 g^{-1}$.
:::

::: pf-step
Conjugating the inclusion $P \subseteq Q_0$ by $g$ gives:
$$g P g^{-1} \subseteq g Q_0 g^{-1} = Q.$$
:::

::: pf-step
Since $P$ is normal in $G$, $g P g^{-1} = P$.
:::

::: pf-step
Thus $P \subseteq Q$.
:::

::: pf-step
Since $Q \in \operatorname{Syl}_p(G)$ was arbitrary, $P \subseteq \bigcap_{Q \in \operatorname{Syl}_p(G)} Q$.
:::

:::

:::

::: pf-step
Part (b): Either $P \subseteq M$ or $[G : M] = p^b$ with $1 \le b \le c$.

::: pf-proof

::: pf-step
Let $M < G$ be a maximal proper subgroup.
:::

::: pf-step
If $P \subseteq M$, the first alternative holds.
:::

::: pf-step
Suppose $P \not\subseteq M$.
:::

::: pf-step
Subgroup property of the product: Since $P \trianglelefteq G$ is normal, the set product $M P = \{m p : m \in M, \, p \in P\}$ is a subgroup of $G$.
:::

::: pf-step
Strict inclusion: Since $P \not\subseteq M$, there exists an element $p_0 \in P \setminus M$. Since $e \in M$, $p_0 = e p_0 \in M P$, which implies $M \subsetneq M P \le G$.
:::

::: pf-step
Maximality of $M$: Since $M$ is a maximal proper subgroup and $M \subsetneq M P \le G$, we must have $M P = G$.
:::

::: pf-step
Index calculation: By the Second Isomorphism Theorem for groups (or the product formula $|M P| = \frac{|M| |P|}{|M \cap P|}$):
$$[G : M] = [M P : M] = [P : M \cap P] = \frac{|P|}{|M \cap P|}.$$
:::

::: pf-step
Prime power divisibility: The intersection $M \cap P$ is a subgroup of $P$. Since $|P| = p^c$, Lagrange's Theorem implies $|M \cap P| = p^a$ for some integer $0 \le a \le c$.
:::

::: pf-step
Since $P \not\subseteq M$, $M \cap P \ne P$, so $a < c$.
:::

::: pf-step
Setting $b = c - a$, we obtain
$$[G : M] = \frac{p^c}{p^a} = p^{c - a} = p^b,$$
where $1 \le b \le c$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$P$ lies in every Sylow $p$-subgroup, and any maximal subgroup not containing $P$ has index $p^b$ with $1 \le b \le c$.
:::

:::

:::
:::
