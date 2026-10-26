---
schema: qual/card@1
id: P-UGAP08F-07
kind: problem
title: Every additive subgroup of $\mathbb Z$ is $k\mathbb Z$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $S\subseteq\mathbb Z$ be nonempty and closed under addition and additive inverses. Prove that there is an integer $k$ such that
\[
S=\{nk:n\in\mathbb Z\}.
\]
You may use the division algorithm for $\mathbb Z$, but no more advanced theorem.
:::

::: pf

::: pf-step

If $S=\{0\}$, then
$$
S=0\ZZ.
$$


::: pf-proof

This is immediate because $0\ZZ=\{0\}$.

:::

:::

::: pf-step

Suppose $S\ne\{0\}$. Then $S$ contains a least positive integer $k$.


::: pf-proof

Choose a nonzero $s\in S$. Since $S$ is closed under additive inverses, either $s$ or $-s$ is a positive element of $S$. Thus the set of positive elements of $S$ is nonempty, so by the well-ordering principle it has a least element; call it $k$.

:::

:::

::: pf-step

Every element of $S$ is an integer multiple of $k$.


::: pf-proof

Let $s\in S$. By the division algorithm, there are integers $q,r$ with
$$
s=qk+r,
\qquad
0\le r<k.
$$
Because $S$ is closed under addition and additive inverses, it is closed under integer multiples; hence $qk\in S$ and
$$
r=s-qk\in S.
$$
If $r>0$, then $r$ would be a positive element of $S$ smaller than the least positive element $k$, a contradiction. Therefore $r=0$, so $s=qk$.

:::

:::

::: pf-step

Every integer multiple of $k$ belongs to $S$.


::: pf-proof

Since $k\in S$ and $S$ is closed under addition and additive inverses, $nk\in S$ for every $n\in\ZZ$.

:::

:::

::: pf-step

There is an integer $k$ such that
$$
\boxed{S=\{nk:n\in\ZZ\}=k\ZZ}.
$$


::: pf-proof

If $S=\{0\}$, use step <1>1. Otherwise choose $k$ as in step <1>2. Step <1>3 gives $S\subseteq k\ZZ$, and step <1>4 gives $k\ZZ\subseteq S$.

:::

:::

::: pf-qed

Step <1>5 is the required conclusion.

:::

:::
