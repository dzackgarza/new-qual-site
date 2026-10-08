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
\[
\operatorname{Ann}(M):=\{r \in R \mid r \cdot m=0 \text { for all } m \in M\}
\]

a. Prove that $\operatorname{Ann}(M)$ is an ideal in $R$.

b. Conversely, prove that every ideal in $R$ is the annihilator of some $R$-module.

c. Give an example of a module $M$ over a ring $R$ such that each element $m \in M$ has a nontrivial annihilator $\operatorname{Ann}(m):=\{r \in R \mid r \cdot m=0\}$, but $\operatorname{Ann}(M)=\{0\}$
:::

::: {.solution}
<1>1. The annihilator $\operatorname{Ann}(M)$ is an ideal of $R$.

::: {.proof}
The element $0$ annihilates every element of $M$. If $r,s$ annihilate $M$, then $(r-s)m=rm-sm=0$ for every $m\in M$, so the annihilator is an additive subgroup. If $r$ annihilates $M$ and $a\in R$, then $(ar)m=a(rm)=0$ for every $m$, proving closure under multiplication by elements of $R$.
:::

<1>2. Every ideal $I\subseteq R$ is the annihilator of an $R$-module:
\[
\boxed{\operatorname{Ann}(R/I)=I}.
\]

::: {.proof}
For $r\in I$ and $x+I\in R/I$, the product $r(x+I)=rx+I$ is zero, hence $I\subseteq\operatorname{Ann}(R/I)$. Conversely, an element annihilating $R/I$ in particular annihilates $1+I$; thus $r+I=0$, or $r\in I$.
:::

<1>3. For $R=\mathbb Z$ and $M=\mathbb Q/\mathbb Z$, every element of $M$ has a nonzero annihilator, but
\[
\boxed{\operatorname{Ann}(M)=\{0\}}.
\]

::: {.proof}
For every class $a/b+\mathbb Z$ with $b\geq1$, multiplication by $b$ gives zero, so its annihilator contains the nonzero integer $b$. On the other hand, if $n\in\mathbb Z$ annihilates all of $\mathbb Q/\mathbb Z$, then for every $k\geq1$ it annihilates $1/k+\mathbb Z$, which implies $k\mid n$. No nonzero integer is divisible by every positive integer, so $n=0$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 establish parts (a), (b), and (c), respectively.
:::
:::
