---
schema: qual/card@1
id: P-ZOYZH
kind: problem
title: Commutative unital simple rings are fields, and $M_n(k)$ is simple
classification:
  areas:
  - algebra
  topics:
  - Fields
  - Ideals
  - Semisimplicity
relations: []
review: draft
---
::: {.problem}
A ring $R$ is called *simple* if its only two-sided ideals are $\{0\}$ and $R$.

(a) Suppose $R$ is a commutative ring with identity $1 \ne 0$. Prove that $R$ is simple if and only if $R$ is a field.

(b) Let $k$ be a field and $n \ge 1$. Show that the ring $M_n(k)$ of $n \times n$ matrices with entries in $k$ is a simple ring.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If a commutative unital ring $R$ with $1\neq0$ is simple, then it is a field.

::: pf-proof

For any nonzero $x\in R$, the principal ideal $(x)$ is nonzero, so simplicity gives $(x)=R$. Consequently $1=yx$ for some $y\in R$. Commutativity gives $xy=1$ as well. Hence every nonzero element is invertible and $R$ is a field.

:::

:::

::: {.pf-step #s2}

Every field is a simple ring.

::: pf-proof

Let $I$ be a nonzero ideal of a field $R$. Choose $0\neq x\in I$. The inverse $x^{-1}\in R$ exists, and ideal closure yields $1=x^{-1}x\in I$. It follows that $r=r1\in I$ for every $r\in R$, hence $I=R$. Thus the only ideals are $0$ and $R$.

:::

:::

::: {.pf-step #s3}

The matrix algebra $M_n(k)$ is simple.

::: pf-proof

Let $I$ be a nonzero two-sided ideal of $M_n(k)$ and choose a nonzero matrix $A=(a_{ij})\in I$. Choose indices $r,c$ with $a_{rc}\neq0$. Let $E_{ij}$ be the standard matrix units. For arbitrary $i,j$ one has
$$
E_{ir}AE_{cj}=a_{rc}E_{ij}\in I.
$$
The scalar matrix $a_{rc}^{-1}I_n$ belongs to $M_n(k)$, so two-sided ideal closure gives $E_{ij}\in I$ for every $i,j$. In particular, $I_n=\sum_{i=1}^nE_{ii}\in I$. Every matrix $B$ satisfies $B=BI_n\in I$, proving $I=M_n(k)$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove the equivalence in part (a), and step [](#s3){.pf-ref} proves part (b).

:::

:::

:::
