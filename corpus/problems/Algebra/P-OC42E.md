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

::: {.problem}
State and prove the injective and surjective forms of the four lemma for commutative diagrams of modules with exact rows.
:::

::: {.solution}
Consider a commutative diagram of modules with exact rows
$$
\begin{array}{ccccccccc}
A_1&\xrightarrow{\alpha_1}&A_2&\xrightarrow{\alpha_2}&A_3&\xrightarrow{\alpha_3}&A_4&\xrightarrow{\alpha_4}&A_5\\
\downarrow f_1&&\downarrow f_2&&\downarrow f_3&&\downarrow f_4&&\downarrow f_5\\
B_1&\xrightarrow{\beta_1}&B_2&\xrightarrow{\beta_2}&B_3&\xrightarrow{\beta_3}&B_4&\xrightarrow{\beta_4}&B_5.
\end{array}
$$
The injective form uses only the first four columns and the surjective form only the last four.

::: pf

::: pf-step

Injective four lemma: if $f_1$ is surjective and $f_2,f_4$ are injective, then $f_3$ is injective.

::: pf-proof

Let $x\in A_3$ with $f_3(x)=0$. Then $f_4(\alpha_3(x))=\beta_3(f_3(x))=0$, and since $f_4$ is injective, $\alpha_3(x)=0$. Exactness at $A_3$ gives $y\in A_2$ with $\alpha_2(y)=x$.

Now $\beta_2(f_2(y))=f_3(\alpha_2(y))=f_3(x)=0$, so exactness at $B_2$ gives $b\in B_1$ with $\beta_1(b)=f_2(y)$. Since $f_1$ is surjective, choose $a\in A_1$ with $f_1(a)=b$. By commutativity,
$$
f_2\bigl(y-\alpha_1(a)\bigr)=f_2(y)-\beta_1(f_1(a))=0.
$$
Injectivity of $f_2$ gives $y=\alpha_1(a)$, hence $x=\alpha_2\alpha_1(a)=0$.

:::

:::

::: pf-step

Surjective four lemma: if $f_2,f_4$ are surjective and $f_5$ is injective, then $f_3$ is surjective.

::: pf-proof

Take $y\in B_3$. Choose $a_4\in A_4$ with $f_4(a_4)=\beta_3(y)$. Then $f_5(\alpha_4(a_4))=\beta_4\beta_3(y)=0$, and since $f_5$ is injective, $\alpha_4(a_4)=0$. Exactness at $A_4$ gives $a_3\in A_3$ with $\alpha_3(a_3)=a_4$.

Then $\beta_3\bigl(f_3(a_3)-y\bigr)=f_4(a_4)-\beta_3(y)=0$, so exactness at $B_3$ gives $b_2\in B_2$ with $\beta_2(b_2)=f_3(a_3)-y$. Choose $a_2\in A_2$ with $f_2(a_2)=b_2$. By commutativity,
$$
f_3(\alpha_2(a_2))=\beta_2(b_2)=f_3(a_3)-y,
$$
hence
$$
f_3\bigl(a_3-\alpha_2(a_2)\bigr)=y.
$$

:::

:::

:::

:::
