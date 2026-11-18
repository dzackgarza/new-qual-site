---
schema: qual/card@1
id: E-C7KV4
kind: problem
title: The lower limit and K-topologies are not comparable
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §13 Exercise 6, printed p. 83, with the bases of
    R_l and R_K as defined in Examples 1 and 2 of §13 and Lemma 13.3 on printed p. 81; the
    stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise 13.6, printed pp.
    145-146. Both failures of Lemma 13.3 are his: at 0 in the lower-limit basis element
    [0,1) every K-basis element contains a point a/2 < 0, and at 0 in (-1,1) - K every
    lower-limit basis element contains some 1/n. (tmp/sources/munkres-solutions-
    whitman.pdf).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps and checked each step against Munkres §13 Exercise 6,
    printed p. 83, Examples 1-2 of §13, Lemma 13.3 and the unboundedness of $\ZZ_+$; the two
    failure points of Lemma 13.3 (0 in $[0,1)$ and 0 in $(-1,1)-K$) are Whitman's, Exercise
    13.6, printed pp. 145-146. The printed statement needed no repair.
---

::: {.exercise}

Show that the topologies of $\RR_\ell$ and $\RR_K$ are not comparable.
:::

::: {.solution}
The published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 13.6, printed pp. 145--146** (`tmp/sources/munkres-solutions-whitman.pdf`); both halves below are his.

Throughout, $\mathcal{B}_\ell=\{[a,b)\mid a<b\}$ and $\mathcal{B}_K=\{(a,b)\mid a<b\}\cup\{(a,b)-K\mid a<b\}$, with $K=\{1/n\mid n\in\ZZ_+\}$, are the bases for the lower limit topology and the $K$-topology given in Examples 1 and 2 of §13, and $\mathcal{T}_\ell$, $\mathcal{T}_K$ are the topologies they generate.

::: pf

::: {.pf-step #criterion}
If for some $x\in X$ and some $B\in\mathcal{B}_\ell$ containing $x$ no element of $\mathcal{B}_K$ containing $x$ is contained in $B$, then $\mathcal{T}_K$ is not finer than $\mathcal{T}_\ell$; and symmetrically with the two bases interchanged.

::: pf-proof
This is the contrapositive of condition (2) of Lemma 13.3: $\mathcal{T}_K$ finer than $\mathcal{T}_\ell$ means that for each $x$ and each $B\in\mathcal{B}_\ell$ containing $x$ there is $B'\in\mathcal{B}_K$ with $x\in B'\subset B$. If some pair $x$, $B$ fails this, the condition of Lemma 13.3 fails, so $\mathcal{T}_K$ is not finer than $\mathcal{T}_\ell$.
:::

:::

::: {.pf-step #not-finer-K}
$\mathcal{T}_K$ is not finer than $\mathcal{T}_\ell$.

:::: pf-proof

::: {.pf-step #k-point}
$B=[0,1)$ is a member of $\mathcal{B}_\ell$ and $0\in B$.

::: pf-proof
$B=[a,b)$ with $a=0<b=1$, so $B\in\mathcal{B}_\ell$ by definition, and $0\in[0,1)$.
:::

:::

::: {.pf-step #k-form}
Every $B_K\in\mathcal{B}_K$ containing $0$ is $(a,b)$ or $(a,b)-K$ for some reals $a<0<b$.

::: pf-proof
By definition each member of $\mathcal{B}_K$ is $(a,b)$ or $(a,b)-K$ with $a<b$. Such a set contains $0$ only if $a<0<b$: if $a\ge 0$ then no element of $(a,b)$, and hence none of $(a,b)-K$, is $\le 0$; if $b\le 0$ then every element of $(a,b)$ is negative, and again so is every element of $(a,b)-K$. Conversely $a<0<b$ puts $0$ in both $(a,b)$ and $(a,b)-K$, since $0\notin K$.
:::

:::

::: {.pf-step #k-half}
If $B_K=(a,b)$ or $B_K=(a,b)-K$ with $a<0<b$, then $a/2\in B_K$ but $a/2\notin B$.

::: pf-proof
Since $a<0$ we have $a<a/2<0<b$, so $a/2\in(a,b)$; and $a/2<0$, while every element of $K$ is positive, so $a/2\notin K$ and hence $a/2\in(a,b)-K$ as well. But $a/2<0$, so $a/2\notin[0,1)=B$.
:::

:::

::: {.pf-step}
No element of $\mathcal{B}_K$ containing $0$ is contained in $B$.

::: pf-proof
Let $B_K\in\mathcal{B}_K$ contain $0$. By step [](#k-form){.pf-ref} it is $(a,b)$ or $(a,b)-K$ with $a<0<b$, and then step [](#k-half){.pf-ref} produces $a/2\in B_K$ with $a/2\notin B$. So $B_K\not\subset B$.
:::

:::

::: {.pf-step}
$\mathcal{T}_K$ is not finer than $\mathcal{T}_\ell$.

::: pf-proof
Apply step [](#criterion){.pf-ref} with $x=0$ and $B=[0,1)$, a member of $\mathcal{B}_\ell$ containing $0$ by step [](#k-point){.pf-ref}: the preceding step shows that no basis element of $\mathcal{B}_K$ containing $0$ lies inside $B$.
:::

:::

:::

:::

::: {.pf-step #not-finer-l}
$\mathcal{T}_\ell$ is not finer than $\mathcal{T}_K$.

:::: pf-proof

::: {.pf-step #l-point}
$B_K=(-1,1)-K$ is a member of $\mathcal{B}_K$ and $0\in B_K$.

::: pf-proof
$(-1,1)-K$ is a member of $\mathcal{B}_K$ with $a=-1<b=1$, and $0\in(-1,1)$ while $0\notin K$ because every element of $K$ is positive.
:::

:::

::: {.pf-step #l-contains}
Every $B_\ell\in\mathcal{B}_\ell$ containing $0$ contains $1/n$ for some $n\in\ZZ_+$.

::: pf-proof
Write $B_\ell=[a,b)$ with $a<b$ and $0\in[a,b)$, so $a\le 0<b$. Since the positive integers are unbounded in $\RR$, choose $n\in\ZZ_+$ with $n>1/b$, that is $1/n<b$; and $1/n>0\ge a$. Hence $a\le 1/n<b$ and $1/n\in[a,b)=B_\ell$.
:::

:::

::: {.pf-step}
$\mathcal{T}_\ell$ is not finer than $\mathcal{T}_K$.

::: pf-proof
Apply step [](#criterion){.pf-ref} with $x=0$ and $B_K=(-1,1)-K$: by step [](#l-point){.pf-ref} this is a basis element of $\mathcal{B}_K$ containing $0$, and by step [](#l-contains){.pf-ref} every basis element of $\mathcal{B}_\ell$ containing $0$ contains a point $1/n$ of $K$, which is not in $(-1,1)-K$. So no basis element of $\mathcal{B}_\ell$ containing $0$ lies inside $B_K$.
:::

:::

:::

:::

::: {.pf-step}
The topologies of $\RR_\ell$ and $\RR_K$ are not comparable.

::: pf-proof
Steps [](#not-finer-K){.pf-ref} and [](#not-finer-l){.pf-ref} show that neither topology is finer than the other, which is what incomparability means.
:::

:::

:::
:::
