---
schema: qual/card@1
id: P-OC42E
kind: problem
title: The four lemma
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: problem
State and prove the injective and surjective forms of the four lemma for commutative diagrams of modules with exact rows.
:::

::: {.solution}
Consider a commutative diagram with exact rows
\[
\begin{array}{ccccccccc}
A_1&\to&A_2&\to&A_3&\to&A_4\\
\downarrow f_1&&\downarrow f_2&&\downarrow f_3&&\downarrow f_4\\
B_1&\to&B_2&\to&B_3&\to&B_4.
\end{array}
\]

<1>1. Injective four lemma: if $f_1$ is surjective and $f_2,f_4$ are injective, then $f_3$ is injective.
::: {.proof}
Let $x\in A_3$ with $f_3(x)=0$. Its image in $A_4$ maps under $f_4$ to zero by commutativity. Since $f_4$ is injective, the image of $x$ in $A_4$ is zero. Exactness gives $y\in A_2$ mapping to $x$.

The element $f_2(y)$ maps to $f_3(x)=0$, so exactness in the bottom row gives $b\in B_1$ mapping to $f_2(y)$. Since $f_1$ is surjective, choose $a\in A_1$ with $f_1(a)=b$. By commutativity,
\[
f_2\bigl(y-\operatorname{im}(a)\bigr)=0.
\]
Injectivity of $f_2$ implies $y=\operatorname{im}(a)$, hence $x=0$. Therefore $f_3$ is injective.
:::

For the surjective form, consider exact rows
\[
\begin{array}{ccccccccc}
A_2&\to&A_3&\to&A_4&\to&A_5\\
\downarrow f_2&&\downarrow f_3&&\downarrow f_4&&\downarrow f_5\\
B_2&\to&B_3&\to&B_4&\to&B_5.
\end{array}
\]

<1>2. Surjective four lemma: if $f_2,f_4$ are surjective and $f_5$ is injective, then $f_3$ is surjective.
::: {.proof}
Take $y\in B_3$ and let $y_4$ be its image in $B_4$. Choose $a_4\in A_4$ with $f_4(a_4)=y_4$. The image of $a_4$ in $A_5$ maps under $f_5$ to zero, because $y_4$ maps to zero by exactness. Since $f_5$ is injective, $a_4$ maps to zero. Exactness gives $a_3\in A_3$ mapping to $a_4$.

Then $f_3(a_3)-y$ maps to zero in $B_4$, so exactness gives $b_2\in B_2$ mapping to $f_3(a_3)-y$. Choose $a_2\in A_2$ with $f_2(a_2)=b_2$, and let $a_3'$ be the image of $a_2$ in $A_3$. By commutativity,
\[
f_3(a_3')=f_3(a_3)-y.
\]
Hence
\[
f_3(a_3-a_3')=y.
\]
Thus $f_3$ is surjective.
:::
:::
