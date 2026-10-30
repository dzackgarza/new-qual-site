---
schema: qual/card@1
id: P-MMAQ-CAKXSUJ3LN
kind: problem
title: Rational irreps of $C_p$ of dimensions $1$ and $p-1$, and abelian groups whose
  rational representations are absolutely irreducible
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $C_p$ denote the cyclic group of prime order $p$.

(a) Show that $C_p$ has two irreducible representations over $\QQ$ (up to isomorphism), one of dimension $1$ and one of dimension $p-1$.

(b) Let $G$ be a finite group, and let $\rho:G\rightarrow\GL_n(\QQ)$ be a representation of $G$ over $\QQ$.
Let $\rho_{\CC}:G\rightarrow\GL_n(\CC)$ denote $\rho$ followed by the inclusion $\GL_n(\QQ)\rightarrow\GL_n(\CC)$.
Thus $\rho_{\CC}$ is a representation of $G$ over $\CC$, called the *complexification* of $\rho$.
We say that an irreducible representation $\rho$ of $G$ is *absolutely irreducible* if its complexification remains irreducible over $\CC$.

Now suppose $G$ is abelian and that every representation of $G$ over $\QQ$ is absolutely irreducible.
Show that $G\cong(C_2)^k$ for some $k$ (i.e., is a product of cyclic groups of order 2).
:::

::: {.solution}

::: pf

::: pf-step

As a $\QQ$-algebra,
$$
\QQ[C_p]\cong \QQ[x]/(x^p-1)
\cong \QQ[x]/(x-1)\times \QQ[x]/(\Phi_p(x)).
$$

::: pf-proof

If $g$ generates $C_p$, the map $\QQ[x]\to\QQ[C_p]$ sending $x\mapsto g$ has kernel $(x^p-1)$. Since
$$
x^p-1=(x-1)\Phi_p(x)
$$
and the two factors are coprime over $\QQ$, the Chinese remainder theorem gives the product decomposition. The cyclotomic polynomial $\Phi_p$ is irreducible over $\QQ$, so
$$
\QQ[x]/(\Phi_p(x))\cong\QQ(\zeta_p).
$$

:::

:::

::: pf-step

Hence $C_p$ has exactly two irreducible rational representations up to isomorphism: the trivial representation of dimension $1$, and one representation of dimension $p-1$.

::: pf-proof

The simple modules over a finite product of fields are exactly the simple modules coming from one factor. Thus the two simple $\QQ[C_p]$-modules are
$$
\QQ
\quad\text{and}\quad
\QQ(\zeta_p).
$$
Their dimensions over $\QQ$ are $1$ and
$$
[\QQ(\zeta_p):\QQ]=\varphi(p)=p-1.
$$

:::

:::

::: {.pf-step #s3}

If $p>2$, the $(p-1)$-dimensional rational irreducible representation of $C_p$ is not absolutely irreducible.

::: pf-proof

After extending scalars to $\CC$,
$$
\QQ(\zeta_p)\otimes_{\QQ}\CC
\cong
\bigoplus_{j=1}^{p-1}\CC_{\chi_j},
$$
where $\chi_j(g)=\zeta_p^j$. Thus its complexification is a direct sum of $p-1>1$ one-dimensional characters.

:::

:::

::: {.pf-step #s4}

The nontrivial two-dimensional rational irreducible representation of $C_4$ is not absolutely irreducible.

::: pf-proof

We have
$$
\QQ[C_4]\cong
\QQ[x]/(x^4-1),
$$
and the factor $x^2+1$ gives the simple module
$$
\QQ(i),
$$
of dimension $2$. After complexification,
$$
\QQ(i)\otimes_{\QQ}\CC
\cong\CC\oplus\CC,
$$
corresponding to the two characters sending a generator of $C_4$ to $i$ and $-i$. Hence this rational irreducible is not absolutely irreducible.

:::

:::

::: {.pf-step #s5}

Under the hypothesis in the problem, every element of the finite abelian group $G$ has order dividing $2$.

::: pf-proof

Suppose instead that $G$ has an element of order greater than $2$. By the structure theorem for finite abelian groups, one of the following holds:

- some odd prime $p$ divides the order of an element of $G$, in which case $G$ has a quotient isomorphic to $C_p$; or
- the exponent of $G$ is divisible by $4$, in which case $G$ has a quotient isomorphic to $C_4$.

Let $q:G\twoheadrightarrow H$ be such a quotient. Inflate along $q$ the rational irreducible representation of $H$ from step [](#s3){.pf-ref} or step [](#s4){.pf-ref}. Inflation preserves irreducibility because a subspace is $G$-stable exactly when it is $H$-stable, and its complexification remains reducible because the action still factors through $H$. This contradicts the hypothesis that every irreducible rational representation of $G$ is absolutely irreducible.

:::

:::

::: pf-step

Therefore
$$
G\cong(C_2)^k
$$
for some $k\ge0$.

::: pf-proof

By step [](#s5){.pf-ref}, every nonidentity element of the finite abelian group $G$ has order $2$. Thus $G$ is naturally a vector space over $\FF_2$. Since it is finite, it has finite dimension $k$, so as an abelian group
$$
G\cong (C_2)^k.
$$

:::

:::

:::

:::

::: {.remark}
The printed hypothesis in (b) says that every representation of $G$ over $\QQ$ is absolutely irreducible; a reducible representation is never absolutely irreducible, so the intended hypothesis is that every irreducible representation of $G$ over $\QQ$ is absolutely irreducible, which the solution uses.
:::
