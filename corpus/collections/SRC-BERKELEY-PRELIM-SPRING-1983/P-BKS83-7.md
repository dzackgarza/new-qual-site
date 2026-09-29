---
schema: qual/card@1
id: P-BKS83-7
kind: problem
title: No automorphism of $(\mathbb Z/p\mathbb Z)^n$ has order $p^2$ when $n\le p$
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
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the identification with GL_n(F_p), the nilpotency-index bound, and the characteristic-p binomial calculation.
---

::: {.problem}
Let $p$ be prime and let
\[
G=(\mathbb Z/p\mathbb Z)^n,
\qquad 1\le n\le p.
\]
Prove that $G$ has no automorphism of order $p^2$.
:::

::: {.solution}
Write
$$
V\coloneqq\FF_p^n,
$$
viewed as an additive group.

::: pf

::: {.pf-step #automorphisms-are-gln}
Every automorphism of $G$ is an element of
$\operatorname{GL}_n(\FF_p)$.

::: pf-proof
The additive groups $G$ and $V$ are naturally the same. If
$\varphi:G\to G$ is a group homomorphism, then for every
$a\in\FF_p$ and $v\in V$,
$$
\varphi(av)=a\varphi(v),
$$
because scalar multiplication by $a$ is repeated addition. Thus every group
homomorphism is $\FF_p$-linear, and the automorphisms are exactly the
invertible linear maps.
:::

:::

::: {.pf-step #nilpotency-bound}
If $A\in\operatorname{GL}_n(\FF_p)$ has order $p^2$ and
$N\coloneqq A-I$, then $N^p=0$.

::: pf-proof
Since $A^{p^2}=I$ and the characteristic is $p$,
$$
N^{p^2}
=(A-I)^{p^2}
=A^{p^2}-I
=0.
$$
Hence $N$ is nilpotent.

Let $m$ be its nilpotency index, so $N^m=0$ and, if $N\ne0$,
$N^{m-1}\ne0$. Choose $v$ with $N^{m-1}v\ne0$. Then
$$
v,Nv,\ldots,N^{m-1}v
$$
are linearly independent: if
$$
c_0v+c_1Nv+\cdots+c_{m-1}N^{m-1}v=0
$$
and $j$ is the least index with $c_j\ne0$, applying $N^{m-1-j}$
leaves
$$
c_jN^{m-1}v=0,
$$
a contradiction. Therefore $m\le n$. Since $n\le p$, one has
$N^p=0$. The same conclusion is immediate when $N=0$.
:::

:::

::: {.pf-step #order-not-p-squared}
No such $A$ can have order $p^2$.

::: pf-proof
Because $I$ and $N$ commute, the binomial theorem in characteristic $p$
gives
$$
A^p
=(I+N)^p
=I+N^p.
$$
Step [](#nilpotency-bound){.pf-ref} gives $N^p=0$, so $A^p=I$. Hence the order of $A$ divides $p$,
contradicting the assumption that its order is $p^2$.
:::

:::

::: pf-qed
By step [](#automorphisms-are-gln){.pf-ref} every automorphism of $G$ is represented by such a matrix,
and step [](#order-not-p-squared){.pf-ref} excludes order $p^2$.
:::

:::
:::
