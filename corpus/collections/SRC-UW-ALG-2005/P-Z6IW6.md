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

::: {.problem}
Let $G$ be a finite abelian group.
Let $f:\ZZ^m\rightarrow G$ be a surjection of abelian groups.
We may think of $f$ as a homomorphism of $\ZZ$-modules.
Let $K$ be the kernel of $f$.

- Prove that $K$ is isomorphic to $\ZZ^m$.

- We can therefore write the inclusion map $K\rightarrow\ZZ^m$ as $\ZZ^m\rightarrow\ZZ^m$ and represent it by an $m\times m$ integer matrix $A$.
  Prove that $|\det A|=|G|$.
:::

::: {.solution}

::: pf

::: pf-step
The subgroup $K\le \ZZ^m$ is a free abelian group of rank at most $m$.

::: pf-proof
Every subgroup of a finitely generated free abelian group is free abelian of rank at most the rank of the ambient group. Thus
\[
K\cong \ZZ^r
\]
for some $0\le r\le m$.
:::

:::

::: pf-step
In fact $r=m$.

::: pf-proof
The first isomorphism theorem gives
\[
\ZZ^m/K\cong G.
\]
Since $G$ is finite, tensoring the short exact sequence
\[
0\longrightarrow K\longrightarrow \ZZ^m\longrightarrow G\longrightarrow0
\]
with $\QQ$ gives
\[
K\otimes_{\ZZ}\QQ\cong \QQ^m,
\]
because $G\otimes_{\ZZ}\QQ=0$. If $K\cong\ZZ^r$, then
\[
K\otimes_{\ZZ}\QQ\cong\QQ^r.
\]
Therefore $r=m$.
:::

:::

::: pf-step
Hence
\[
K\cong\ZZ^m.
\]

:::

::: {.pf-step #s4}
After choosing a basis of $K$, let
\[
A:\ZZ^m\longrightarrow\ZZ^m
\]
be the integer matrix representing the inclusion $K\hookrightarrow\ZZ^m$. Then
\[
\ZZ^m/A\ZZ^m\cong G.
\]

::: pf-proof
Under the chosen identification $K\cong\ZZ^m$, the image of $A$ is precisely the subgroup $K$. Hence
\[
\ZZ^m/A\ZZ^m
\cong
\ZZ^m/K
\cong G.
\]
:::

:::

::: {.pf-step #s5}
Let
\[
UAV=\operatorname{diag}(d_1,\dots,d_m)
\]
be a Smith normal form of $A$, with $U,V\in\operatorname{GL}_m(\ZZ)$ and each $d_i>0$.
Then
\[
|G|=d_1\cdots d_m.
\]

::: pf-proof
The quotient in step [](#s4){.pf-ref} is finite, so $A$ has full rank and all Smith invariants $d_i$ are nonzero. Multiplication by the unimodular matrices $U$ and $V$ does not change the isomorphism type of the cokernel, so
\[
G\cong \ZZ^m/A\ZZ^m
\cong
\bigoplus_{i=1}^m \ZZ/d_i\ZZ.
\]
Therefore
\[
|G|=\prod_{i=1}^m d_i.
\]
:::

:::

::: pf-step
Finally,
\[
|\det A|=|G|.
\]

::: pf-proof
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
by step [](#s5){.pf-ref}.
:::

:::

:::

:::
