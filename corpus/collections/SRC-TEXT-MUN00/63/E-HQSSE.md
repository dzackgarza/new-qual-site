---
schema: qual/card@1
id: E-HQSSE
kind: problem
title: Two disjoint simple closed curves separate the sphere into three regions
classification:
  areas:
  - topology
  topics:
  - Jordan Curve Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Munkres §63 Exercise 1, printed p. 393. No complete published solution located; the searches are listed in
    the COMPLAINTS.md entry for §61--§73 of SRC-TEXT-MUN00. The proof is now the hint as printed and needs no
    Jordan--Schoenflies theorem, which the book does not prove and which the earlier version of this card
    invoked. The separation count runs through Theorem 63.3, a general nonseparation theorem (printed p. 390):
    for closed D_1, D_2 with S^2 - D_1 cap D_2 simply connected, if neither D_i separates S^2 then neither does
    the union. Its hypotheses are checked one by one in step 3. Also used: Theorem 63.4 (the Jordan curve
    theorem, printed p. 390) for the two components and their common boundary, Theorem 59.3 (printed p. 369) for
    the simple connectivity of S^2, and the openness of the components of the complement of a compact set, as in
    the proof of Lemma 61.1 (printed p. 377).
---

::: {.exercise}

Let $C_1$ and $C_2$ be disjoint simple closed curves in $S^2$.

(a) Show that $S^2 - C_1 - C_2$ has precisely three components.
[Hint: If $W_1$ is the component of $S^2 - C_1$ disjoint from $C_2$, and if $W_2$ is the component of $S^2 - C_2$ disjoint from $C_1$, show that $\overline{W}_1 \cup \overline{W}_2$ does not separate $S^2$.]

(b) Show that these three components have boundaries $C_1$ and $C_2$ and $C_1 \cup C_2$, respectively.
:::

::: {.solution}

By Theorem 63.4 (the Jordan curve theorem, printed p. 390) the complement $S^2-C_i$ has exactly two components, and each has $C_i$ as its boundary, that is $C_i=\overline{W}-W$ for each of the two. Write $S^2-C_1=W_1\sqcup W_1'$ and $S^2-C_2=W_2\sqcup W_2'$, with $W_1$ the component of $S^2-C_1$ disjoint from $C_2$ and $W_2$ the component of $S^2-C_2$ disjoint from $C_1$. Each of the four sets is open in $S^2$, being a component of an open set in the locally connected space $S^2$ (as in the proof of Lemma 61.1, printed p. 377).

::: pf

::: pf-step

$\overline{W}_1\cap\overline{W}_2=\emptyset$, and $\overline{W}_1$ does not separate $S^2$.

::: pf-proof

$\overline{W}_1=W_1\cup C_1$: one inclusion is clear and $C_1=\overline{W}_1-W_1$ by Theorem 63.4. So $\overline{W}_1$ is connected, contains $C_1$ and is disjoint from $C_2$ (it is $W_1\cup C_1$, and $C_1\cap C_2=\emptyset$). A connected subset of $S^2-C_2$ lies in a single component, so $\overline{W}_1$ lies in the component of $S^2-C_2$ containing $C_1$, which is $W_2'$: the other component $W_2$ is by definition disjoint from $C_1$. Since $W_2'=S^2-\overline{W}_2$, we get $\overline{W}_1\subseteq S^2-\overline{W}_2$, that is $\overline{W}_1\cap\overline{W}_2=\emptyset$; symmetrically $\overline{W}_2\subseteq S^2-\overline{W}_1$. Moreover $S^2-\overline{W}_1=W_1'$ is connected, being a component of $S^2-C_1$, so $\overline{W}_1$ does not separate $S^2$; and symmetrically for $\overline{W}_2$.

:::

:::

::: pf-step

$\overline{W}_1\cup\overline{W}_2$ does not separate $S^2$.

::: pf-proof

Apply Theorem 63.3 (printed p. 390) with $D_1=\overline{W}_1$ and $D_2=\overline{W}_2$. The sets $D_i$ are closed. Neither separates $S^2$, by step 1. And $D_1\cap D_2=\emptyset$ by step 1, so $S^2-D_1\cap D_2=S^2$, which is simply connected by Theorem 59.3 (printed p. 369). The theorem then gives that $D_1\cup D_2$ does not separate $S^2$.

:::

:::

::: pf-step

(a) $S^2-C_1-C_2$ has precisely three components, namely $W_1$, $W_2$ and $R=S^2-(\overline{W}_1\cup\overline{W}_2)$.

::: pf-proof

Put $R=S^2-(\overline{W}_1\cup\overline{W}_2)=(S^2-\overline{W}_1)\cap(S^2-\overline{W}_2)=W_1'\cap W_2'$, which is connected by step 2 and open, as an intersection of open sets. Now $W_1$, $W_2$, $R$ are pairwise disjoint: $W_1\cap W_2=\emptyset$ because $W_1\subseteq S^2-\overline{W}_2$; $W_1\cap R=\emptyset$ and $W_2\cap R=\emptyset$ because $R\subseteq S^2-\overline{W}_i$. Their union is $S^2-C_1-C_2$: a point off $C_1\cup C_2$ lies in $S^2-C_1=W_1\cup W_1'$ and in $S^2-C_2=W_2\cup W_2'$, so it lies in $W_1$, or in $W_2$, or in $W_1'\cap W_2'=R$. Each is nonempty and open in $S^2-C_1-C_2$, and each is connected, so they are exactly the components.

Nonemptiness of $R$: pick $y\in C_2$. Since $C_2\subseteq\overline{W}_2$ we have $y\notin W_2'$, but $C_2=\overline{W}_2'-W_2'$, so $y$ is a limit point of $W_2'$. And $\overline{W}_1$ is closed and misses $C_2$ by step 1, so there is a neighbourhood $U$ of $y$ with $U\cap\overline{W}_1=\emptyset$. Then $U\cap W_2'$ is nonempty and lies in $W_1'$, so it lies in $R$.

:::

:::

::: pf-step

(b) The three components have boundaries $C_1$, $C_2$ and $C_1\cup C_2$.

::: pf-proof

$\partial W_1=C_1$ and $\partial W_2=C_2$ by Theorem 63.4. For $R$: since $R$ is a component of the open set $S^2-C_1-C_2$, its boundary is contained in $S^2-R$ intersected with the closure of the complement, so $\partial R\subseteq C_1\cup C_2$: a point of $S^2-(C_1\cup C_2)$ lies in one of the three open components, hence is not a boundary point of $R$. Conversely let $p\in C_1$; by Theorem 63.4, $C_1$ is the boundary of $W_1'$, so every neighbourhood of $p$ meets $W_1'$. Since $p\notin\overline{W}_2$ by step 1, there is a neighbourhood $U$ of $p$ with $U\cap\overline{W}_2=\emptyset$, and every point of $U\cap W_1'$ lies in $W_1'\cap(S^2-\overline{W}_2)=R$. So every neighbourhood of $p$ meets $R$, and $p\notin R$; thus $C_1\subseteq\partial R$, and symmetrically $C_2\subseteq\partial R$. Hence $\partial R=C_1\cup C_2$.

:::

:::

::: pf-qed

Part (a) is step 3 and part (b) is step 4.

:::

:::
:::
