---
schema: qual/card@1
id: P-BKS03-9B
kind: problem
title: An uncountable subset of $\RR$ has uncountably many accumulation points
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the retained sheet's argument (Spring 2003
    prelim solutions, Problem 9B, PDF p. 6, the file named in the collection's provenance),
    now cited on the card, which previously carried no citation. Added, since the sheet uses
    them silently: that the set B of accumulation points is closed (proved by a diagonal
    choice of distinct terms approaching the limit), that the complement of B is a countable
    union of closed sets (closed intervals with rational endpoints inside the open set), and
    that an accumulation point of A intersected with C_N is an accumulation point of A. The
    countability bookkeeping for A minus B is also spelled out. Statement unchanged.
---

::: {.problem}
Let $A\subseteq\RR$ be uncountable.

(a) Show that $A$ has at least one accumulation point.

(b) Show that $A$ has uncountably many accumulation points.

(Recall that a point is an accumulation point of $A$ if and only if it is the limit of a sequence of distinct terms from $A$.)
:::

::: {.solution}
The published solution is the collection's own retained sheet, **Spring 2003 prelim solutions, Problem 9B** (`assets/attachments/s03solution.pdf`, the file named in this collection's `provenance`): the split of $\RR$ into the half-open unit intervals, the boundedness argument for (a), and the reduction of (b) to a countable union of closed sets are that solution's. The card supplies three things the sheet uses without proof: that the set of accumulation points is closed, that its complement is a countable union of closed sets, and why an accumulation point of $A\cap C_n$ is one of $A$.

Throughout $A\subseteq\RR$ is uncountable, and by the definition stated in the problem $p$ is an accumulation point of $A$ iff $p$ is the limit of a sequence of distinct terms of $A$. Write $B$ for the set of accumulation points of $A$.

::: pf

::: {.pf-step #part-a}
$A$ has at least one accumulation point.

::: pf-proof
$\RR=\bigcup_{n\in\ZZ}A_n$ with $A_n=A\cap[n,n+1)$. A countable union of countable sets is countable, so $A$ uncountable forces some $A_n$ uncountable, in particular infinite; choose distinct $x_k\in A_n$. The sequence $(x_k)$ lies in the bounded set $[n,n+1)$, so it has a convergent subsequence by Bolzano–Weierstrass, and the limit of that subsequence is a limit of distinct terms of $A$, hence an accumulation point of $A$ by the stated definition.

:::

:::

::: {.pf-step #closed}
$B$ is closed.

::: pf-proof
Let $p_k\in B$ with $p_k\to p$; we show $p\in B$. Let $\delta>0$ and choose $k$ with $\abs{p_k-p}<\delta/2$. Since $p_k$ is a limit of distinct terms of $A$, there are infinitely many $a\in A$ with $\abs{a-p_k}<\delta/2$, hence some $a\in A$ with $\abs{a-p}<\delta$ outside any prescribed finite set. Varying $\delta$ along a sequence tending to $0$ and choosing $a_j$ outside $\theset{a_1,\dots,a_{j-1}}$ gives distinct terms $a_j\in A$ with $a_j\to p$, so $p\in B$.

:::

:::

::: {.pf-step #open-f-sigma}
$\RR\setminus B$ is a countable union of closed sets.

::: pf-proof
$\RR\setminus B$ is open, being the complement of the closed set $B$. Every point of an open set $U$ lies in a closed interval $[a,b]$ with rational endpoints contained in $U$: take $a,b\in\QQ$ with $a<x<b$ and $[a,b]\subset U$, which exists because $U$ is a neighbourhood of $x$. There are countably many such intervals, so $U$ is the union of countably many closed sets.

:::

:::

::: {.pf-step #part-b}
$B$ is uncountable.

::: pf-proof
Suppose $B$ is at most countable. Writing $\RR\setminus B=\bigcup_nC_n$ as in step [](#open-f-sigma){.pf-ref}, the set $A\setminus B$ is uncountable, because $A$ is uncountable and $B$ is at most countable, and $A\setminus B\subseteq\RR\setminus B=\bigcup_nC_n$, so some $C_N$ contains uncountably many points of $A$: otherwise $A\setminus B$ would be a countable union of countable sets. Then $A\cap C_N$ is uncountable, so by step [](#part-a){.pf-ref} it has an accumulation point $p$: a limit of distinct terms $a_j\in A\cap C_N\subseteq A$. Those are distinct terms of $A$, so $p\in B$. But $C_N$ is closed and contains all the $a_j$, so $p\in C_N\subseteq\RR\setminus B$, contradicting $p\in B$.

:::

:::

::: {.pf-step #conclusion}
Every uncountable $A\subseteq\RR$ has at least one, and in fact uncountably many, accumulation points.

::: pf-proof
Steps [](#part-a){.pf-ref} and [](#part-b){.pf-ref} are (a) and (b). Note that (a) is applied to the uncountable set $A\cap C_N$, which is legitimate because the argument of step [](#part-a){.pf-ref} uses only uncountability.

:::

:::

:::
:::
