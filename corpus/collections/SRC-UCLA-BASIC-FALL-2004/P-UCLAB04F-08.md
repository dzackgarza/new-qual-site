---
schema: qual/card@1
id: P-UCLAB04F-08
kind: problem
title: A symmetric quadratic form and its minimum eigenvalue
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Exam Fall 2004 PDF. The source denotes the unit sphere in $\RR^n$ by $S^n$; the set itself is unambiguous and is denoted simply by $S$ here.
---

::: {.problem}
Let $A=(a_{ij})$ be a real symmetric $n\times n$ matrix, and define the associated quadratic form
\[
Q(v)=v\mathbin{\cdot}Av,
\qquad v\in\RR^n.
\]

(a) Show that
\[
\nabla Q(v)=2Av.
\]

(b) Let
\[
S=\{v\in\RR^n:\|v\|=1\},
\]
let $M$ be the minimum value of $Q$ on $S$, and choose $u\in S$ with $Q(u)=M$.
Use Lagrange multipliers to prove that $u$ is an eigenvector of $A$ with eigenvalue $M$.
:::

::: {.solution}

Write
\[
v=(v_1,\ldots,v_n)^t.
\]

::: pf

::: {.pf-step #s1-1}

For each $k\in\{1,\ldots,n\}$,
\[
\frac{\partial Q}{\partial v_k}(v)
=
2\sum_{j=1}^n a_{kj}v_j.
\]


::: pf-proof

Since
\[
Q(v)=\sum_{i,j=1}^n a_{ij}v_iv_j,
\]
differentiating with respect to $v_k$ gives
\[
\frac{\partial Q}{\partial v_k}
=
\sum_{j=1}^n a_{kj}v_j
+
\sum_{i=1}^n a_{ik}v_i.
\]
Because $A$ is symmetric,
\[
a_{ik}=a_{ki},
\]
so the two sums are equal. Hence
\[
\frac{\partial Q}{\partial v_k}
=
2\sum_{j=1}^n a_{kj}v_j.
\]

:::

:::

::: {.pf-step #s1-2}

One has
\[
\boxed{\nabla Q(v)=2Av}.
\]


::: pf-proof

The $k$th coordinate of $2Av$ is
\[
2\sum_{j=1}^n a_{kj}v_j,
\]
which equals the $k$th coordinate of $\nabla Q(v)$ by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Let
\[
h(v)=\|v\|^2.
\]
Then
\[
S=h^{-1}(1)
\]
and
\[
\nabla h(u)=2u\ne0.
\]


::: pf-proof

By definition,
\[
h(v)=v_1^2+\cdots+v_n^2,
\]
so
\[
\nabla h(v)=2v.
\]
Since $u\in S$, one has $\|u\|=1$, hence $u\ne0$ and therefore $\nabla h(u)\ne0$.

:::

:::

::: {.pf-step #s1-4}

There exists $\lambda\in\RR$ such that
\[
Au=\lambda u.
\]


::: pf-proof

The point $u$ minimizes $Q$ subject to the regular constraint
\[
h(v)=1.
\]
By the Lagrange multiplier theorem, there is $\lambda\in\RR$ such that
\[
\nabla Q(u)=\lambda\nabla h(u).
\]
Using steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
\[
2Au=2\lambda u.
\]
Dividing by $2$ gives
\[
Au=\lambda u.
\]
Since $u\ne0$, this shows that $u$ is an eigenvector of $A$.

:::

:::

::: {.pf-step #s1-5}

The eigenvalue in step [](#s1-4){.pf-ref} is
\[
\boxed{\lambda=M}.
\]


::: pf-proof

Taking the dot product of
\[
Au=\lambda u
\]
with $u$ gives
\[
Q(u)
=
u\mathbin{\cdot}Au
=
\lambda\|u\|^2
=
\lambda.
\]
By hypothesis,
\[
Q(u)=M.
\]
Hence $\lambda=M$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} prove part (b).

:::

:::

:::
