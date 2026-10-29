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

::: pf

::: {.pf-step #s1}

The subgroup $P$ is contained in every Sylow $p$-subgroup of $G$.

::: pf-proof

By Sylow's theorems, some Sylow $p$-subgroup $Q_0$ contains $P$. Every Sylow $p$-subgroup has the form $Q=gQ_0g^{-1}$ for some $g\in G$. Normality of $P$ gives $P=gPg^{-1}\subseteq gQ_0g^{-1}=Q$, as required.

:::

:::

::: {.pf-step #s2}

For every maximal proper subgroup $M<G$, either $P\subseteq M$ or $[G:M]=p^b$ for some $1\leq b\leq c$.

::: pf-proof

Suppose $P\not\subseteq M$. Since $P\trianglelefteq G$, the product $MP$ is a subgroup strictly containing $M$. Maximality forces $MP=G$. The product formula gives
$$
[G:M]=[MP:M]=[P:M\cap P].
$$
Lagrange's theorem gives $|M\cap P|=p^a$ with $0\leq a<c$, since $M\cap P$ is a proper subgroup of the group $P$ of order $p^c$. Hence $[G:M]=p^{c-a}$, with $1\leq c-a\leq c$.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), and step [](#s2){.pf-ref} proves part (b).

:::

:::

:::
