---
schema: qual/card@1
id: P-BERK92S-15
kind: problem
title: An abelian subgroup of $S_{999}$ of order $1111$ has a common fixed point
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
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $G$ be an abelian subgroup of $S_{999}$ of order $1111$. Prove that there is
\[
i\in\{1,\dots,999\}
\]
such that
\[
\sigma(i)=i
\]
for every $\sigma\in G$.
:::

::: {.solution}
Let $G$ act on
$$
\Omega\coloneqq\{1,\ldots,999\}
$$
through its given inclusion in $S_{999}$. Since
$$
\abs{G}=1111=11\cdot101,
$$
the positive divisors of $\abs G$ are $1,11,101,1111$.

::: pf

::: pf-step

Every orbit in $\Omega$ has size $1$, $11$, or $101$.

::: pf-proof

For $i\in\Omega$, the orbit-stabilizer theorem gives
$$
\abs{G\cdot i}=[G:G_i],
$$
so the orbit size divides $\abs G=1111$. Since
$\abs{\Omega}=999<1111$, no orbit can have size $1111$. Thus the only
possible orbit sizes are $1,11,101$.

:::

:::

::: {.pf-step #s2}

There must be an orbit of size $1$.

::: pf-proof

Suppose not. Then the orbit decomposition of $\Omega$ would give
nonnegative integers $a,b$ such that
$$
999=11a+101b.
$$
Reducing modulo $11$ gives
$$
9\equiv2b\pmod{11},
$$
so
$$
b\equiv10\pmod{11}.
$$
On the other hand, $101b\le999$, hence $0\le b\le9$. This is
impossible.

:::

:::

::: {.pf-step #s3}

Some $i\in\Omega$ is fixed by every element of $G$.

::: pf-proof

By step [](#s2){.pf-ref}, there is an orbit $G\cdot i$ of size $1$. Thus
$$
G\cdot i=\{i\},
$$
which means $\sigma(i)=i$ for every $\sigma\in G$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required common fixed point.

:::

:::

:::
