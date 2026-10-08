---
schema: qual/card@1
id: P-6KHMF
kind: problem
title: Maximal ideals, non-units, and prime annihilators of module elements
classification:
  areas:
  - algebra
  topics:
  - Maximal Ideals
  - Prime Ideals
  - Modules
relations: []
review: draft
---

::: {.problem}
Let $R$ be a commutative ring with identity $1 \ne 0$.

(a) Define a **maximal ideal** and prove that $R$ contains at least one maximal ideal.

(b) Show that an element $r \in R$ is not invertible if and only if $r$ is contained in some maximal ideal of $R$.

(c) Let $M$ be an $R$-module. For any $m \in M$, the **annihilator** of $m$ is the ideal
$$
\operatorname{Ann}(m) = \{r \in R : r m = 0\}.
$$
Suppose that $I = \operatorname{Ann}(\mu)$ for some non-zero element $\mu \in M \setminus \{0\}$ is maximal among all proper annihilator ideals $\{\operatorname{Ann}(m) : m \in M, \, m \ne 0\}$. Prove that $I$ is a prime ideal of $R$.
:::

::: {.solution}
<1>1. A maximal ideal is a proper ideal maximal under inclusion, and every nonzero unital commutative ring possesses one.

::: {.proof}
Let $\mathcal P$ be the partially ordered set of proper ideals of $R$. It is nonempty because $(0)\in\mathcal P$. The union of any nonempty chain of proper ideals is an ideal; it remains proper because if $1$ belonged to the union, it would belong to one of its proper constituent ideals. The empty chain has the upper bound $(0)$. Zorn's lemma provides a maximal member of $\mathcal P$, which is a maximal ideal by definition.
:::

<1>2. An element of $R$ is a nonunit precisely when it belongs to a maximal ideal.

::: {.proof}
If $r$ is contained in a proper ideal, it cannot be a unit, since $r^{-1}r=1$ would belong to that ideal. Conversely, for a nonunit $r$ the principal ideal $(r)$ is proper. Apply Zorn's lemma to the set of proper ideals containing $(r)$, as in step <1>1, to obtain a maximal ideal containing $r$.
:::

<1>3. An annihilator $I=\operatorname{Ann}(\mu)$ maximal among annihilators of nonzero elements of $M$ is a prime ideal.

::: {.proof}
Since $\mu\neq0$, one has $1\notin I$, so $I$ is proper. Let $ab\in I$ and suppose $b\notin I$. Then $b\mu\neq0$. The ideal $J=\operatorname{Ann}(b\mu)$ contains $I$, because $r\mu=0$ implies $r(b\mu)=b(r\mu)=0$. By maximality, $J=I$. As $(ab)\mu=0$, one has $a(b\mu)=0$, hence $a\in J=I$. Therefore $ab\in I$ implies $a\in I$ or $b\in I$, the defining condition for a prime ideal.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>1, <1>2, and <1>3 prove parts (a), (b), and (c), respectively.
:::
:::
