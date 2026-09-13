---
schema: qual/card@1
id: P-Z6IW6
kind: problem
title: The kernel of a surjection $\ZZ^m\to G$ onto a finite abelian group is isomorphic
  to $\ZZ^m$, with $|\det A|=|G|$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Matrices
  - Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $G$ be a finite abelian group.
Let $f:\mathbb Z^m\rightarrow G$ be a surjection of abelian groups.
We may think of $f$ as a homomorphism of $\mathbb Z$-modules.
Let $K$ be the kernel of $f$.

- Prove that $K$ is isomorphic to $\mathbb Z^m$.

- We can therefore write the inclusion map $K\rightarrow\mathbb Z^m$ as $\mathbb Z^m\rightarrow\mathbb Z^m$ and represent it by an $m\times m$ integer matrix $A$.
  Prove that $|\det A|=|G|$.
:::

::: solution
<1>1. The subgroup $K\le \mathbb Z^m$ is a free abelian group of rank at most $m$.
::: {.proof}
Every subgroup of a finitely generated free abelian group is free abelian of rank at most the rank of the ambient group. Thus
\[
K\cong \mathbb Z^r
\]
for some $0\le r\le m$.
:::

<1>2. In fact $r=m$.
::: {.proof}
The first isomorphism theorem gives
\[
\mathbb Z^m/K\cong G.
\]
Since $G$ is finite, tensoring the short exact sequence
\[
0\longrightarrow K\longrightarrow \mathbb Z^m\longrightarrow G\longrightarrow0
\]
with $\mathbb Q$ gives
\[
K\otimes_{\mathbb Z}\mathbb Q\cong \mathbb Q^m,
\]
because $G\otimes_{\mathbb Z}\mathbb Q=0$. If $K\cong\mathbb Z^r$, then
\[
K\otimes_{\mathbb Z}\mathbb Q\cong\mathbb Q^r.
\]
Therefore $r=m$.
:::

<1>3. Hence
\[
K\cong\mathbb Z^m.
\]
:::

<1>4. After choosing a basis of $K$, let
\[
A:\mathbb Z^m\longrightarrow\mathbb Z^m
\]
be the integer matrix representing the inclusion $K\hookrightarrow\mathbb Z^m$. Then
\[
\mathbb Z^m/A\mathbb Z^m\cong G.
\]
::: {.proof}
Under the chosen identification $K\cong\mathbb Z^m$, the image of $A$ is precisely the subgroup $K$. Hence
\[
\mathbb Z^m/A\mathbb Z^m
\cong
\mathbb Z^m/K
\cong G.
\]
:::

<1>5. Let
\[
UAV=\operatorname{diag}(d_1,\dots,d_m)
\]
be a Smith normal form of $A$, with $U,V\in\operatorname{GL}_m(\mathbb Z)$ and each $d_i>0$.
Then
\[
|G|=d_1\cdots d_m.
\]
::: {.proof}
The quotient in <1>4 is finite, so $A$ has full rank and all Smith invariants $d_i$ are nonzero. Multiplication by the unimodular matrices $U$ and $V$ does not change the isomorphism type of the cokernel, so
\[
G\cong \mathbb Z^m/A\mathbb Z^m
\cong
\bigoplus_{i=1}^m \mathbb Z/d_i\mathbb Z.
\]
Therefore
\[
|G|=\prod_{i=1}^m d_i.
\]
:::

<1>6. Finally,
\[
|\det A|=|G|.
\]
::: {.proof}
Since $U$ and $V$ are unimodular,
\[
|\det U|=|\det V|=1.
\]
Thus
\[
|\det A|
=|\det(UAV)|
=\prod_{i=1}^m d_i
=|G|
\]
by <1>5.
:::
