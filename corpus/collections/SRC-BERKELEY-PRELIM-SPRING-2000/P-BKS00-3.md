---
schema: qual/card@1
id: P-BKS00-3
kind: problem
title: The group $\QQ/\ZZ$ has no proper subgroup of finite index
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    If H has finite index m, the quotient G/H has order m and hence is
    annihilated by m. Divisibility of Q/Z writes every x as my, forcing
    every coset x+H to vanish.
---

::: {.problem}
Prove that the additive group $\mathbb Q/\mathbb Z$ has no proper subgroup of finite index.
:::

::: {.solution}
Write
$$
G=\QQ/\ZZ.
$$

::: pf

::: {.pf-step #s1}

For every positive integer $m$, multiplication by $m$ on $G$ is
surjective.

::: pf-proof

Let $x=q+\ZZ\in G$, where $q\in\QQ$. Then
$$
y=\frac{q}{m}+\ZZ
$$
satisfies
$$
my=q+\ZZ=x.
$$

:::

:::

::: {.pf-step #s2}

If $H\leq G$ has finite index
$$
[G:H]=m,
$$
then every coset in $G/H$ is zero.

::: pf-proof

The quotient group $G/H$ has order $m$, so Lagrange's theorem gives
$$
m(g+H)=H
$$
for every $g\in G$.

Now fix $x\in G$. By step [](#s1){.pf-ref}, there exists $y\in G$ such that
$x=my$. Therefore
$$
x+H
=
m(y+H)
=
H.
$$
Thus every coset is the identity coset.

:::

:::

::: {.pf-step #s3}

The subgroup $H$ equals $G$.

::: pf-proof

Step [](#s2){.pf-ref} shows that $x\in H$ for every $x\in G$. Hence $H=G$.

:::

:::

::: pf-qed

Every finite-index subgroup of $G$ is all of $G$ by step [](#s3){.pf-ref}, so
$\QQ/\ZZ$ has no proper subgroup of finite index.

:::

:::

:::
