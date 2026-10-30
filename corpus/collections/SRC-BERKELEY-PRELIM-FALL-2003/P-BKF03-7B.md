---
schema: qual/card@1
id: P-BKF03-7B
kind: problem
title: Counting commuting pairs in a finite group and in $S_5$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 7B of the vendored Fall 2003 Berkeley prelim and independently reviewed the accompanying source solution.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the centralizer sum by conjugacy classes and the seven partition types in S_5.
---

::: {.problem}
(a) Let G be a finite group and let X be the set of pairs of commuting elements of $G \mathrm { : }$

$$
X = \{ ( g , h ) \in G \times G : g h = h g \} .
$$

Prove that $\cardinality{ X } = c \cardinality{ G }$ where c is the number of conjugacy classes in G.

(b) Compute the number of pairs of commuting permutations on five letters.
:::


::: {.solution}

::: pf

::: {.pf-step #centralizer-count}
For each $g\in G$, the number of elements commuting with $g$ is $\cardinality{C_G(g)}$.

::: pf-proof
By definition,
$$
C_G(g)=\{h\in G:hg=gh\}.
$$
Thus for fixed $g$, exactly $\cardinality{C_G(g)}$ pairs in $X$ have first coordinate $g$.
Consequently
$$
\cardinality{X}=\sum_{g\in G}\cardinality{C_G(g)}.
$$
:::

:::

::: {.pf-step #conjugacy-class-contributes-G}
Each conjugacy class contributes exactly $\cardinality{G}$ to this sum.

::: pf-proof
Let $K$ be the conjugacy class of an element $g$.
Centralizer size is constant on conjugacy classes, so
$$
\sum_{x\in K}\cardinality{C_G(x)}=\cardinality{K}\,\cardinality{C_G(g)}.
$$
By the orbit-stabilizer theorem for the conjugation action,
$$
\cardinality{K}=[G:C_G(g)],
$$
and hence
$$
\cardinality{K}\,\cardinality{C_G(g)}=\cardinality{G}.
$$
:::

:::

::: {.pf-step #X-equals-cG}
If $c$ is the number of conjugacy classes of $G$, then
$$
\cardinality{X}=c\cardinality{G}.
$$

::: pf-proof
Partition the sum in step [](#centralizer-count){.pf-ref} by conjugacy classes.
By step [](#conjugacy-class-contributes-G){.pf-ref} each of the $c$ classes contributes $\cardinality{G}$, giving the formula.
:::

:::

::: {.pf-step #S5-value}
For $G=S_5$, there are $840$ commuting ordered pairs.

::: pf-proof
Conjugacy classes in $S_5$ are determined by cycle type, hence by partitions of $5$.
The seven partitions are
$$
5,\ 4+1,\ 3+2,\ 3+1+1,\ 2+2+1,\ 2+1+1+1,\ 1+1+1+1+1.
$$
Thus $c=7$.
Since $\cardinality{S_5}=5!=120$, step [](#X-equals-cG){.pf-ref} gives
$$
\cardinality{X}=7\cdot120=\boxed{840}.
$$
:::

:::

:::

:::

