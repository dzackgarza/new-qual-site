---
schema: qual/card@1
id: E-QSI4Y
kind: problem
title: The Tietze extension theorem implies the Urysohn lemma
classification:
  areas:
  - topology
  topics:
  - Urysohn Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solutions: "Doug's World", "Munkres - Topology - Chapter
    4 Solutions" (30 August 2017), Problem 35.1, printed p. 12
    (tmp/sources/munkres-solutions-dougsworld-ch4.pdf), and dbFin, "Section 35: Problem 1 Solution",
    https://dbfin.com/topology/munkres/chapter-4/section-35-the-tietze-extension-theorem/problem-1-solution/
    (read 2026-11-10; kept at
    tmp/sources/dbfin/section-35-the-tietze-extension-theorem/problem-1-solution.txt); checked
    against Munkres, Topology (2000), Section 35 Exercise 1, printed p. 223, Theorem 35.1 and the
    pasting lemma (Theorem 18.3). The argument is the card's: on the closed union A cup B the
    function equal to 0 on A and 1 on B is continuous because A and B are disjoint closed, hence
    also open, in the union; Tietze extends it to X; truncation puts the values in [0,1]. No
    correction to the mathematics was needed.
---

::: {.exercise}

Show that the Tietze extension theorem implies the Urysohn lemma.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, and it is the standard derivation, with the pasting lemma and the truncation made explicit.

Let $X$ be normal and let $A,B\subseteq X$ be disjoint closed sets; the goal is a continuous $u:X\to[0,1]$ with $u(A)=0$ and $u(B)=1$.

::: pf

::: {.pf-step #model}
Define $f:A\cup B\to[-1,1]$ by $f(a)=0$ for $a\in A$ and $f(b)=1$ for $b\in B$. Then $f$ is continuous and $A\cup B$ is closed in $X$.

::: pf-proof
$A$ and $B$ are disjoint and closed in $X$, so each is closed in the subspace $A\cup B$, and each is also open in it: $A=(A\cup B)\setminus B$ and $B=(A\cup B)\setminus A$ are complements of closed sets of the subspace. The restrictions $f\restriction_A$ and $f\restriction_B$ are constant, hence continuous, and they agree on $A\cap B=\varnothing$ vacuously; so $f$ is continuous by the pasting lemma (Theorem 18.3) applied to the two closed subsets $A$, $B$ of $A\cup B$. A union of two closed sets is closed, so $A\cup B$ is closed in $X$.
:::

:::

::: {.pf-step #extend}
$f$ extends to a continuous $F:X\to[-1,1]$.

::: pf-proof
$X$ is normal, $A\cup B$ is a closed subset of $X$ by step [](#model){.pf-ref}, and $f$ takes values in the closed interval $[-1,1]$; so the Tietze extension theorem (Theorem 35.1) gives a continuous $F:X\to[-1,1]$ with $F\restriction_{A\cup B}=f$.
:::

:::

::: {.pf-step #truncate}
$u=t\circ F:X\to[0,1]$, where $t(s)=\min\theset{1,\max\theset{0,s}}$, is continuous, with $u(A)=0$ and $u(B)=1$.

::: pf-proof
$t:\RR\to[0,1]$ is continuous, being built from the continuous maps $\max\theset{0,s}$ and $\min\theset{1,s}$; so $u$ is continuous (Theorem 18.2(c)) and takes values in $[0,1]$. For $a\in A$, $F(a)=f(a)=0$ and $t(0)=0$, so $u(a)=0$; for $b\in B$, $F(b)=1$ and $t(1)=1$, so $u(b)=1$.
:::

:::

::: {.pf-qed}
A continuous $u:X\to[0,1]$ with $u(A)=0$ and $u(B)=1$ exists by step [](#truncate){.pf-ref}, which is the Urysohn lemma for the disjoint closed sets $A$, $B$. So the Tietze extension theorem implies it.
:::

:::

:::
