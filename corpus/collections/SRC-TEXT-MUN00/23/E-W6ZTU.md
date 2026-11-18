---
schema: qual/card@1
id: E-W6ZTU
kind: problem
title: Discrete spaces are totally disconnected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology, §23 Exercise 5, printed p. 152, with Example 4 for the
    rationals; both questions are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 3" (1 January 2021), Exercise 23.5, PDF p. 2. In a discrete space a subspace
    with two points is separated by a singleton and its complement; the converse fails, the
    rationals being totally disconnected and not discrete. (tmp/sources/munkres-solutions-
    positron-ch3.pdf).
---

::: {.exercise}

A space is totally disconnected if its only connected subspaces are one-point sets.
Show that if $X$ has the discrete topology, then $X$ is totally disconnected.
Does the converse hold?
:::

::: {.solution}

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 3* (1 January 2021), Exercise 23.5, PDF p. 2** (`tmp/sources/munkres-solutions-positron-ch3.pdf`); both halves are theirs. Their sentence "any subspace with two points is separated the same way" is replaced below by the argument that does it for an arbitrary subspace with two points, which is what total disconnectedness requires.

Recall that $X$ is totally disconnected when its only connected subspaces are one-point sets.

::: pf

::: {.pf-step #discrete}
If $X$ is discrete, then $X$ is totally disconnected.

::: pf-proof
Let $Y\subseteq X$ and let $p,q\in Y$ be distinct. The sets $\{p\}$ and $X\setminus\{p\}$ are open in the discrete space $X$, so $Y\cap\{p\}=\{p\}$ and $Y\cap\big(X\setminus\{p\}\big)=Y\setminus\{p\}$ are open in $Y$; they are nonempty, disjoint, and their union is $Y$. Thus every subspace with at least two points has a separation, so the only connected subspaces are the one-point sets.
:::

:::

::: {.pf-step #no-converse}
The converse fails: $\QQ$ with the usual topology is totally disconnected but not discrete.

:::: {.pf-proof}

::: {.pf-step #q-disconnected}
Every subspace of $\QQ$ with at least two points is disconnected.

::: pf-proof
Let $S\subseteq\QQ$ contain distinct $p<q$. Since the irrationals are dense there is an irrational $a$ with $p<a<q$. The sets $S\cap(-\infty,a)$ and $S\cap(a,\infty)$ are open in $S$, being traces of open sets of $\QQ$; they are disjoint, their union is $S$ because $a\notin\QQ$, and they are nonempty because $p$ lies in the first and $q$ in the second. So they form a separation of $S$.
:::

:::

::: {.pf-step #q-not-discrete}
$\QQ$ is not discrete.

::: pf-proof
If $\QQ$ were discrete, the one-point set $\{0\}$ would be open in $\QQ$, so there would be an open interval $(a,b)$ of $\RR$ with $0\in(a,b)$ and $\QQ\cap(a,b)=\{0\}$; but $(a,b)$ contains rationals other than $0$, by density of $\QQ$.
:::

:::

::::

:::

::: {.pf-qed}
A discrete space is totally disconnected by step [](#discrete){.pf-ref}, and the converse fails by step [](#no-converse){.pf-ref}.
:::

:::

:::
