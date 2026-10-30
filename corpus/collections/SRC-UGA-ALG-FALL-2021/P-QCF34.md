---
schema: qual/card@1
id: P-QCF34
kind: problem
title: The annihilator of a module is an ideal, every ideal is an annihilator, and
  a faithful module of torsion elements
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---
::: {.problem}
Let $R$ be a commutative ring with unit and let $M$ be an $R$-module.
Define the annihilator of $M$ to be
$$
\operatorname{Ann}(M):=\{r \in R \mid r \cdot m=0 \text{ for all } m \in M\}
$$

a. Prove that $\operatorname{Ann}(M)$ is an ideal in $R$.

b. Conversely, prove that every ideal in $R$ is the annihilator of some $R$-module.

c. Give an example of a module $M$ over a ring $R$ such that each element $m \in M$ has a nontrivial annihilator $\operatorname{Ann}(m):=\{r \in R \mid r \cdot m=0\}$, but $\operatorname{Ann}(M)=\{0\}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The annihilator $\operatorname{Ann}(M)$ is an ideal of $R$.

::: pf-proof

The element $0$ annihilates every element of $M$. If $r,s$ annihilate $M$, then $(r-s)m=rm-sm=0$ for every $m\in M$, so the annihilator is an additive subgroup. If $r$ annihilates $M$ and $a\in R$, then $(ar)m=a(rm)=0$ for every $m$, proving closure under multiplication by elements of $R$.

:::

:::

::: {.pf-step #s2}

Every ideal $I\subseteq R$ is the annihilator of an $R$-module:
$$
\boxed{\operatorname{Ann}(R/I)=I}.
$$

::: pf-proof

For $r\in I$ and $x+I\in R/I$, the product $r(x+I)=rx+I$ is zero, hence $I\subseteq\operatorname{Ann}(R/I)$. Conversely, an element annihilating $R/I$ in particular annihilates $1+I$; thus $r+I=0$, or $r\in I$.

:::

:::

::: {.pf-step #s3}

For $R=\ZZ$ and $M=\QQ/\ZZ$, every element of $M$ has a nonzero annihilator, but
$$
\boxed{\operatorname{Ann}(M)=\{0\}}.
$$

::: pf-proof

For every class $a/b+\ZZ$ with $b\geq1$, multiplication by $b$ gives zero, so its annihilator contains the nonzero integer $b$. On the other hand, if $n\in\ZZ$ annihilates all of $\QQ/\ZZ$, then for every $k\geq1$ it annihilates $1/k+\ZZ$, which implies $k\mid n$. No nonzero integer is divisible by every positive integer, so $n=0$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
