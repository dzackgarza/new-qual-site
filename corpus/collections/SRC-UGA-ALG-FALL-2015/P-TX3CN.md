---
schema: qual/card@1
id: P-TX3CN
kind: problem
title: A finite-index subgroup contains a finite-index normal subgroup contained in
  every conjugate
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Group Actions
  - Cosets and Lagrange
relations: []
review: draft
---
::: {.problem}
Let $G$ be a group containing a proper subgroup $H \lneq G$ of finite index $[G : H] < \infty$.

Prove that $G$ contains a normal subgroup $N \trianglelefteq G$ of finite index that is contained in every conjugate of $H$.
:::

::: {.solution}
Put $n=[G:H]$ and $X=G/H$, the set of left cosets.

::: pf

::: pf-step

Left translation defines a homomorphism $\rho:G\to\operatorname{Sym}(X)\cong S_n$.

::: pf-proof

For each $g\in G$ let $\rho(g)(xH)=gxH$. This is well-defined on cosets, its inverse is $\rho(g^{-1})$, and $\rho(gh)(xH)=ghxH=\rho(g)(\rho(h)(xH))$. Thus it is a permutation representation on the finite set of $n$ cosets.

:::

:::

::: {.pf-step #s2}

Its kernel is the normal core
$$
\boxed{N=\ker\rho=\bigcap_{x\in G}xHx^{-1}}.
$$

::: pf-proof

An element $g\in G$ lies in $\ker\rho$ exactly when $gxH=xH$ for every $x\in G$. This is equivalent to $x^{-1}gx\in H$ for all $x$, or $g\in xHx^{-1}$ for all $x$. Thus the kernel is precisely the displayed intersection, so it lies in every conjugate of $H$.

:::

:::

::: {.pf-step #s3}

The subgroup $N$ is normal in $G$ and has finite index at most $n!$.

::: pf-proof

It is a kernel, hence normal. By the first isomorphism theorem, $G/N\cong\operatorname{im}\rho\leq S_n$, so $[G:N]=\cardinality{\operatorname{im}\rho}\leq n!<\infty$.

:::

:::

::: pf-qed

Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} establish the required containment, normality, and finite index.

:::

:::

:::
