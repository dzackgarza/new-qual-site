---
schema: qual/card@1
id: P-UCTOP290-S12-6
kind: problem
title: "Vanishing cup products under a cover by n contractible sets; covering projective spaces"
classification:
  areas:
  - topology
  topics:
  - Cohomology Ring
  - Cup Product
relations: []
review: draft
---

::: {.problem}
Suppose $X$ is a space with a cover by contractible open sets $U_1, \ldots, U_n$.
Show that the cup product of any $n$ elements of $H^{>0}(X)$ is zero, and hence that projective $n$-spaces cannot be covered by fewer than $n + 1$ contractible open sets.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $a_i\in H^{d_i}(X;R)$ with $d_i>0$, for $i=1,\ldots,n$. Since $U_i$ is contractible, the restriction of $a_i$ to $U_i$ is zero.

::: pf-proof

A contractible space has no positive-degree reduced cohomology, so $H^{d_i}(U_i;R)=0$ for $d_i>0$.

:::

:::

::: pf-step

Each $a_i$ therefore lifts to a relative class
$$
\bar a_i\in H^{d_i}(X,U_i;R).
$$

::: pf-proof

The long exact sequence of the pair $(X,U_i)$ contains
$$
H^{d_i}(X,U_i)\longrightarrow H^{d_i}(X)\longrightarrow H^{d_i}(U_i).
$$
The last term receives $a_i$ as zero by step [](#s1){.pf-ref}, so exactness gives a relative lift.

:::

:::

::: {.pf-step #s3}

The relative cup product satisfies
$$
\bar a_1\smile\cdots\smile\bar a_n
\in H^{d_1+\cdots+d_n}(X,U_1\cup\cdots\cup U_n)=H^*(X,X)=0.
$$

::: pf-proof

Iterating the relative cup product
$$
H^p(X,A)\otimes H^q(X,B)\to H^{p+q}(X,A\cup B)
$$
gives the displayed class. Since the $U_i$ cover $X$, their union is $X$.

:::

:::

::: {.pf-step #s4}

Hence every product of $n$ positive-degree cohomology classes on $X$ is zero.

::: pf-proof

The forgetful map from relative to absolute cohomology sends the relative product in step [](#s3){.pf-ref} to $a_1\smile\cdots\smile a_n$. Since the relative product is zero, so is the absolute product.

:::

:::

::: pf-step

Consequently $\mathbb CP^n$ cannot be covered by fewer than $n+1$ contractible open sets.

::: pf-proof

In
$$
H^*(\mathbb CP^n;\mathbb Z)=\mathbb Z[\alpha]/(\alpha^{n+1}),\qquad |\alpha|=2,
$$
the $n$-fold product $\alpha^n$ is nonzero. If $\mathbb CP^n$ were covered by $n$ contractible open sets, step [](#s4){.pf-ref} would force $\alpha^n=0$.

:::

:::

::: pf-step

Likewise $\mathbb RP^n$ cannot be covered by fewer than $n+1$ contractible open sets.

::: pf-proof

Use mod-$2$ cohomology
$$
H^*(\mathbb RP^n;\mathbb F_2)=\mathbb F_2[\beta]/(\beta^{n+1}),\qquad |\beta|=1,
$$
for which $\beta^n\ne0$.

:::

:::

:::

:::
