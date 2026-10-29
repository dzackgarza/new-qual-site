---
schema: qual/card@1
id: P-UGAP08F-07
kind: problem
title: Every additive subgroup of $\ZZ$ is $k\ZZ$
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
Let $S\subseteq\ZZ$ be nonempty and closed under addition and additive inverses. Prove that there is an integer $k$ such that
\[
S=\{nk:n\in\ZZ\}.
\]
You may use the division algorithm for $\ZZ$, but no more advanced theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $S=\{0\}$, then
$$
S=0\ZZ.
$$


::: pf-proof

This is immediate because $0\ZZ=\{0\}$.

:::

:::

::: {.pf-step #s1-2}

Suppose $S\ne\{0\}$. Then $S$ contains a least positive integer $k$.


::: pf-proof

Choose a nonzero $s\in S$. Since $S$ is closed under additive inverses, either $s$ or $-s$ is a positive element of $S$. Thus the set of positive elements of $S$ is nonempty, so by the well-ordering principle it has a least element; call it $k$.

:::

:::

::: {.pf-step #s1-3}

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

::: {.pf-step #s1-4}

Every integer multiple of $k$ belongs to $S$.


::: pf-proof

Since $k\in S$ and $S$ is closed under addition and additive inverses, $nk\in S$ for every $n\in\ZZ$.

:::

:::

::: {.pf-step #s1-5}

There is an integer $k$ such that
$$
\boxed{S=\{nk:n\in\ZZ\}=k\ZZ}.
$$


::: pf-proof

If $S=\{0\}$, use step [](#s1-1){.pf-ref}. Otherwise choose $k$ as in step [](#s1-2){.pf-ref}. Step [](#s1-3){.pf-ref} gives $S\subseteq k\ZZ$, and step [](#s1-4){.pf-ref} gives $k\ZZ\subseteq S$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
