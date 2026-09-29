---
schema: qual/card@1
id: P-BERK98S-06
kind: problem
title: Unique cyclic subgroups of each finite order in $\QQ/\ZZ$
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
Let $G=\mathbb Q/\mathbb Z$. Show that for every positive integer $t$, the group $G$ has a unique cyclic subgroup of order $t$.
:::

::: {.solution}
Fix a positive integer $t$ and put
$$
H_t\coloneqq
\left(\frac1t\ZZ\right)\big/\ZZ
\subseteq\QQ/\ZZ.
$$

::: pf

::: {.pf-step #s1}

The subgroup $H_t$ is cyclic of order $t$.

::: pf-proof

The class
$$
\frac1t+\ZZ
$$
generates $H_t$, since every element of $H_t$ has the form
$$
\frac{k}{t}+\ZZ
$$
for some $k\in\ZZ$. Moreover,
$$
t\left(\frac1t+\ZZ\right)=0,
$$
while for $1\leq k<t$,
$$
k\left(\frac1t+\ZZ\right)
=\frac{k}{t}+\ZZ
\neq0.
$$
Thus the generator has order exactly $t$.

:::

:::

::: {.pf-step #s2}

Every element of $\QQ/\ZZ$ killed by $t$ belongs to $H_t$.

::: pf-proof

Let $q+\ZZ\in\QQ/\ZZ$ and suppose
$$
t(q+\ZZ)=0.
$$
Then $tq\in\ZZ$, so
$$
q=\frac{tq}{t}\in\frac1t\ZZ.
$$
Hence $q+\ZZ\in H_t$.

:::

:::

::: {.pf-step #s3}

Every subgroup of $\QQ/\ZZ$ of order $t$ is equal to $H_t$.

::: pf-proof

Let $K\subseteq\QQ/\ZZ$ have order $t$. By Lagrange's theorem, every
$x\in K$ satisfies
$$
tx=0.
$$
Step [](#s2){.pf-ref} therefore gives
$$
K\subseteq H_t.
$$
By step [](#s1){.pf-ref}, both groups have exactly $t$ elements, so $K=H_t$.

:::

:::

::: {.pf-step #s4}

Therefore $\QQ/\ZZ$ has the unique cyclic subgroup of order $t$
given by
$$
\boxed{
H_t=
\left(\frac1t\ZZ\right)\big/\ZZ
}.
$$

::: pf-proof

Existence follows from step [](#s1){.pf-ref}. Step [](#s3){.pf-ref} gives uniqueness, even among all
subgroups of order $t$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
