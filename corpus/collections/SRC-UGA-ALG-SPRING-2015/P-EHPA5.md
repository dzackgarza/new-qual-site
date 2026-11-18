---
schema: qual/card@1
id: P-EHPA5
kind: problem
title: A normal subgroup of order $p$ in a finite $p$-group lies in the center
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Normal Subgroups
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured solution of the problem as printed, replacing a bulleted outline with a
    Lamport proof. Checked: normality makes N a union of full G-conjugacy classes; the
    classes are the orbits of conjugation, so orbit-stabilizer gives their sizes as
    divisors of |G| = p^k; one class is {1}, so the remaining sum is p-1 and each remaining
    class has size 1, whence every element of N is central. The earlier outline's size
    comparison ("1 + p > p") is now the explicit inequality $p = 1 + \sum \ge 1 + p$. The
    argument is the card's own: no retained solution set covers this problem.
---

::: {.problem}
For a prime $p$, let $G$ be a finite $p\dash$group and let $N$ be a normal subgroup of $G$ of order $p$.
Prove that $N$ is contained in the center of $G$.
:::

::: {.concept}
\envlist

- Definition of conjugacy class: $[x] = \theset{gx\inverseof{g} \st g\in G}$.

- A conjugacy class $[x]$ is trivial iff $[x] = \theset{ x }$ iff $x\in Z(G)$.

- Sizes of conjugacy classes divide the order of the group they live in.

  - This is orbit-stabilizer: $G\actson G$ by $g\cdot x \coloneqq gx\inverseof{g}$, so $\OO(x) = [x]$.
    Then $\size \OO(x) = \size G / \size \Stab(x)$, so $\size \OO(x)$ divides $\size G$.
:::

::: {.solution}
The argument is the card's own; no retained solution set covers this problem.

Throughout, $G$ acts on itself by conjugation, $g\cdot x\coloneqq gx\inverseof{g}$, so that the orbit of $x$ is its conjugacy class $[x]$ and the orbit-stabilizer theorem gives $\size[x]=\size G/\size\Stab(x)$; the centre $Z(G)$ is the set of points with trivial class.

::: pf

::: {.pf-step #classes}
$N$ is a disjoint union of $G$-conjugacy classes, one of which is $\theset{1_N}$.

::: pf-proof
Let $n\in N$ and $g\in G$. Since $N$ is normal, $gng\inverseof{g}\in N$, so the whole conjugacy class of $n$ lies in $N$; distinct conjugacy classes are either equal or disjoint because they are orbits of one action, and the union of the classes of the elements of $N$ is therefore $N$ itself. The identity $1_N$ is fixed by conjugation, so its class is the singleton $\theset{1_N}$.
:::

:::

::: {.pf-step #sizes}
If $N=[n_1]\cup\cdots\cup[n_m]$ is the decomposition into distinct classes with $[n_1]=\theset{1_N}$, then $p=1+\sum_{i=2}^m\size[n_i]$, and every $\size[n_i]$ is either $1$ or at least $p$.

::: pf-proof
Taking cardinalities in the disjoint decomposition of step [](#classes){.pf-ref} gives $p=\size N=\sum_i\size[n_i]$, and $\size[n_1]=1$, which is the displayed formula. Since $\size[n_i]=\size G/\size\Stab(n_i)$ by orbit-stabilizer, it divides $\size G=p^k$, so it is a power $p^{e}$ with $e\ge0$; such a number is $1$ when $e=0$ and at least $p$ otherwise.
:::

:::

::: {.pf-step}
$N\subset Z(G)$.

::: pf-proof
If some $i\ge2$ had $\size[n_i]\ge p$, then $p=1+\sum_{i\ge2}\size[n_i]\ge1+p$, which is absurd; so every $\size[n_i]=1$ by step [](#sizes){.pf-ref}. A class with one element is a point fixed by conjugation, hence lies in the centre, so every $n\in N$ has $[n]=\theset{n}$ and belongs to $Z(G)$. Thus $N\subset Z(G)$.
:::

:::

:::
:::
