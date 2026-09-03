---
schema: qual/card@1
id: E-5VWPC
kind: problem
title: The shrinking lemma for point-finite open coverings
classification:
  areas:
  - topology
  topics:
  - Local Finiteness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

An indexed family $\ts{A_\alpha}$ of subsets of $X$ is said to be a point-finite indexed family if each $x \in X$ belongs to $A_\alpha$ for only finitely many values of $\alpha$.

Lemma (The shrinking lemma).
Let $X$ be a normal space; let $\ts{U_1, U_2, \ldots}$ be a point-finite indexed open covering of $X$.
Then there exists an indexed open covering $\ts{V_1, V_2, \ldots}$ of $X$ such that $\overline{V}_n \subset U_n$ for each $n$.
:::

::: solution
**Goal:** Prove the Shrinking Lemma for countable point-finite open coverings $\{U_n\}_{n=1}^\infty$ on a normal space $X$.

<1>1. Inductive construction of the family $\{V_n\}_{n=1}^\infty$:
    We construct open sets $V_k$ inductively such that for each $k \ge 1$, $\overline{V_k} \subseteq U_k$, and the intermediate family $\{V_1, \dots, V_k, U_{k+1}, U_{k+2}, \dots\}$ covers $X$.
    *Proof:*
    <2>1. **Induction hypothesis for step $k$:**
        Assume $V_1, \dots, V_{k-1}$ have been chosen such that $\overline{V_j} \subseteq U_j$ for all $j < k$, and the family $\{V_1, \dots, V_{k-1}, U_k, U_{k+1}, \dots\}$ is an open cover of $X$. (For $k=1$, this is the original cover $\{U_n\}_{n=1}^\infty$.)
    <2>2. **Construction of closed set $A_k$:**
        Define:
        $$A_k = X \setminus \left( \bigcup_{j=1}^{k-1} V_j \cup \bigcup_{i=k+1}^\infty U_i \right).$$
        As the complement of an open set, $A_k$ is closed in $X$.
    <2>3. **Containment $A_k \subseteq U_k$:**
        If $x \in A_k$, then $x \notin V_j$ for all $j < k$ and $x \notin U_i$ for all $i > k$. Since $\{V_1, \dots, V_{k-1}, U_k, U_{k+1}, \dots\}$ covers $X$, $x$ must belong to $U_k$.
    <2>4. **Application of normality:**
        Because $X$ is normal and $A_k$ is closed with $A_k \subseteq U_k$ (where $U_k$ is open), there exists an open set $V_k \subseteq X$ satisfying:
        $$A_k \subseteq V_k \subseteq \overline{V_k} \subseteq U_k.$$
    <2>5. **Coverage of the updated family:**
        By construction, $V_k \cup \left( \bigcup_{j=1}^{k-1} V_j \cup \bigcup_{i=k+1}^\infty U_i \right) \supseteq A_k \cup (X \setminus A_k) = X$.
        Thus $\{V_1, \dots, V_k, U_{k+1}, U_{k+2}, \dots\}$ covers $X$.

<1>2. Verification that $\{V_n\}_{n=1}^\infty$ covers $X$ via point-finiteness:
    *Proof:*
    <2>1. Let $x \in X$ be an arbitrary point.
    <2>2. Since the original cover $\{U_n\}_{n=1}^\infty$ is point-finite, the index set $S_x = \{n \in \mathbb{Z}_+ \mid x \in U_n\}$ is finite and non-empty.
    <2>3. Let $m = \max S_x$. By definition of $m$, $x \notin U_i$ for all $i > m$.
    <2>4. By <1>1, the family $\{V_1, \dots, V_m, U_{m+1}, U_{m+2}, \dots\}$ covers $X$, so $x$ belongs to this union.
    <2>5. Since $x \notin \bigcup_{i=m+1}^\infty U_i$, it follows that $x \in \bigcup_{j=1}^m V_j$.
    <2>6. Thus $x \in V_j$ for some $j \le m$, proving $\bigcup_{n=1}^\infty V_n = X$.

<1>3. Conclusion:
    The collection $\{V_n\}_{n=1}^\infty$ is an open cover of $X$ satisfying $\overline{V_n} \subseteq U_n$ for every $n \in \mathbb{Z}_+$. Q.E.D.
:::
