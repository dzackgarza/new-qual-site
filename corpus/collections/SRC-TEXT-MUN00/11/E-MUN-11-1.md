---
schema: qual/card@1
id: E-MUN-11-1
kind: problem
title: The rational-difference partial order and its maximal chains
classification:
  areas:
  - topology
  topics:
  - Maximum Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §11 Exercise 1, printed p. 70; the stored
    statement matches.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 11.1,
    printed pp. 118-119 (tmp/sources/munkres-solutions-whitman.pdf). His answer is that
    the maximal simply ordered subsets are the cosets A_x = {y : x - y rational}; the
    two inclusions of A = B are his, with the irrationality of a rational plus an
    irrational doing the work in the second.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into Lamport steps and checked the statement against Munkres, *Topology* (2000), §11 Exercise 1, printed p. 71. The argument is transcribed from the retained set: Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.1, printed pp. 118--119. Checked: irreflexivity and transitivity of $\prec$; comparability inside a coset via $z-y=(x-y)-(x-z)$; incomparability of an element outside a coset with every element of it; and the two inclusions showing a maximal simply ordered set is a coset.
---

::: {.exercise}

If $a$ and $b$ are real numbers, define $a \prec b$ if $b - a$ is positive and rational. Show this is a strict partial order on $\RR$. What are the maximal simply ordered subsets?
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 11.1** (`tmp/sources/munkres-solutions-whitman.pdf`); the identification of the maximal simply ordered subsets as the cosets of $\QQ$ is his, and the statement is Munkres, *Topology* (2000), §11 Exercise 1.

::: pf

::: {.pf-step #irreflexive}
Never $a\prec a$.

::: pf-proof
$a-a=0$ is not positive, so the defining condition fails.
:::
:::

::: {.pf-step #transitive}
If $a\prec b$ and $b\prec c$ then $a\prec c$.

::: pf-proof
By hypothesis $b-a$ and $c-b$ are positive rationals, so $c-a=(c-b)+(b-a)$ is a sum of positive rationals, hence a positive rational.
:::
:::

::: {.pf-step #order}
$\prec$ is a strict partial order on $\RR$.

::: pf-proof
Steps [](#irreflexive){.pf-ref} and [](#transitive){.pf-ref} are the two defining properties of a strict partial order.
:::
:::

::: {.pf-step #cosets}
For $x\in\RR$ the set $A_x\coloneqq\{y\in\RR\st x-y\in\QQ\}$ is simply ordered by $\prec$.

::: pf-proof
Let $y\neq z$ lie in $A_x$. Then $x-y$ and $x-z$ are rational, so $z-y=(x-y)-(x-z)$ is rational, and it is nonzero because $y\neq z$. Hence either $z-y>0$, giving $y\prec z$, or $y-z>0$, giving $z\prec y$; so any two elements are comparable.
:::
:::

::: {.pf-step #maximal-coset}
Each $A_x$ is maximal among simply ordered subsets.

::: pf-proof
Let $z\notin A_x$. Then $x-z\notin\QQ$, and for every $y\in A_x$ the difference $z-y=(z-x)+(x-y)$ is a sum of an irrational and a rational, hence irrational, and in particular not a positive rational; likewise $y-z$ is irrational. So $z$ is incomparable with every element of $A_x$, and no simply ordered set strictly containing $A_x$ exists.
:::
:::

::: {.pf-step #converse}
Every maximal simply ordered subset $B$ equals $A_x$ for any $x\in B$.

::: pf-proof
First $B\neq\varnothing$: if $B=\varnothing$ then $B\cup\{a\}$ is simply ordered for any $a$, contradicting maximality. Choose $x\in B$. If $y\in B$ then $y=x$ or, $B$ being simply ordered, $y\prec x$ or $x\prec y$; in each case $x-y\in\QQ$, so $y\in A_x$ and $B\subset A_x$. Conversely let $y\in A_x$; if $y\neq x$ then $x-y$ is a nonzero rational, so $y$ is comparable with $x$, and $y$ is comparable with every element of $B$ because $B\subset A_x$ and $A_x$ is simply ordered by step [](#cosets){.pf-ref}. Thus $B\cup\{y\}$ is simply ordered, and maximality of $B$ gives $y\in B$. Hence $B=A_x$.
:::
:::

::: {.pf-step}
$\prec$ is a strict partial order on $\RR$ and its maximal simply ordered subsets are exactly the cosets $A_x$ of $\QQ$.

::: pf-proof
Step [](#order){.pf-ref} gives the order and steps [](#cosets){.pf-ref}, [](#maximal-coset){.pf-ref} and [](#converse){.pf-ref} show each coset is a maximal simply ordered subset and that there are no others.
:::
:::

:::
:::
