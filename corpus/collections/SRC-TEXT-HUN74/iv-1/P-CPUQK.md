---
schema: qual/card@1
id: P-CPUQK
kind: problem
title: Injective and surjective forms of the five lemma
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Homological Algebra
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Restored the omitted five-object commutative diagram from an independent reproduction of the source statement and checked the two requested assertions against the standard five-lemma diagram chase.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Let the following be a commutative diagram of $R$-modules and $R$-module homomorphisms with exact rows:

\[
\begin{array}{ccccccccc}
A_1&\xrightarrow{f_1}&A_2&\xrightarrow{f_2}&A_3&\xrightarrow{f_3}&A_4&\xrightarrow{f_4}&A_5\\
\downarrow\alpha_1&&\downarrow\alpha_2&&\downarrow\alpha_3&&\downarrow\alpha_4&&\downarrow\alpha_5\\
B_1&\xrightarrow{g_1}&B_2&\xrightarrow{g_2}&B_3&\xrightarrow{g_3}&B_4&\xrightarrow{g_4}&B_5.
\end{array}
\]

Prove the following:

1. If $\alpha_1$ is an epimorphism and $\alpha_2, \alpha_4$ are monomorphisms then $\alpha_3$ is a monomorphism.

2. If $\alpha_5$ is a monomorphism and $\alpha_2, \alpha_4$ are epimorphisms then $\alpha_3$ is an epimorphism.
:::

::: solution
<1>1. If $\alpha_1$ is surjective and $\alpha_2,\alpha_4$ are injective, then
$\alpha_3$ is injective.
::: proof
Let $x\in A_3$ satisfy $\alpha_3(x)=0$. Commutativity gives
\[
\alpha_4(f_3(x))=g_3(\alpha_3(x))=0.
\]
Since $\alpha_4$ is injective, $f_3(x)=0$. Exactness of the top row at $A_3$
therefore gives $y\in A_2$ such that
\[
f_2(y)=x.
\]

Now
\[
g_2(\alpha_2(y))
=\alpha_3(f_2(y))
=\alpha_3(x)
=0.
\]
By exactness of the bottom row at $B_2$, there is $b_1\in B_1$ with
\[
g_1(b_1)=\alpha_2(y).
\]
Since $\alpha_1$ is surjective, choose $a_1\in A_1$ such that
$\alpha_1(a_1)=b_1$. Commutativity then yields
\[
\alpha_2(f_1(a_1))
=g_1(\alpha_1(a_1))
=g_1(b_1)
=\alpha_2(y).
\]
Injectivity of $\alpha_2$ gives $f_1(a_1)=y$. Hence
\[
x=f_2(y)=f_2(f_1(a_1))=0
\]
by exactness of the top row. Thus $\ker\alpha_3=0$ and $\alpha_3$ is injective.
:::

<1>2. If $\alpha_5$ is injective and $\alpha_2,\alpha_4$ are surjective, then
$\alpha_3$ is surjective.
::: proof
Let $b_3\in B_3$. Since $\alpha_4$ is surjective, choose $a_4\in A_4$ such
that
\[
\alpha_4(a_4)=g_3(b_3).
\]
Then
\[
\alpha_5(f_4(a_4))
=g_4(\alpha_4(a_4))
=g_4(g_3(b_3))
=0.
\]
Because $\alpha_5$ is injective, $f_4(a_4)=0$. Exactness of the top row at
$A_4$ gives $a_3\in A_3$ with
\[
f_3(a_3)=a_4.
\]

Set
\[
\delta=\alpha_3(a_3)-b_3\in B_3.
\]
Then
\[
g_3(\delta)
=\alpha_4(f_3(a_3))-g_3(b_3)
=\alpha_4(a_4)-g_3(b_3)
=0.
\]
By exactness of the bottom row at $B_3$, choose $b_2\in B_2$ such that
\[
g_2(b_2)=\delta.
\]
Since $\alpha_2$ is surjective, choose $a_2\in A_2$ with
$\alpha_2(a_2)=b_2$. Therefore
\[
\alpha_3(a_3-f_2(a_2))
=\alpha_3(a_3)-g_2(\alpha_2(a_2))
=\alpha_3(a_3)-\delta
=b_3.
\]
Thus every $b_3\in B_3$ lies in the image of $\alpha_3$, so $\alpha_3$ is
surjective.
:::
:::
