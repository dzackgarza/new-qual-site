---
schema: qual/card@1
id: P-3GQBI
kind: problem
title: $\QQ(i)$ and $\QQ(\sqrt2)$ as vector spaces and fields
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Vector Spaces
  - Fields
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent modern-algebra qualifying exam reproducing the same two assertions.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that in $\mathbb{C}$, the fields $\mathbb{Q}(i) \cong \mathbb{Q}(\sqrt 2)$ as vector spaces, but not as fields.
:::

::: solution
Both fields are regarded as vector spaces over $\QQ$.

<1>1. The sets
\[
\{1,i\}
\qquad\text{and}\qquad
\{1,\sqrt2\}
\]
are $\QQ$-bases of $\QQ(i)$ and $\QQ(\sqrt2)$, respectively.
::: proof
The element $i$ has minimal polynomial $X^2+1$ over $\QQ$, while $\sqrt2$ has
minimal polynomial $X^2-2$. Both polynomials are irreducible over $\QQ$, so both
simple extensions have degree $2$. The standard power bases are therefore the
displayed pairs.
:::

<1>2. The map
\[
T:\QQ(i)\longrightarrow\QQ(\sqrt2),
\qquad
T(a+bi)=a+b\sqrt2
\]
is a $\QQ$-vector-space isomorphism.
::: proof
The map sends the basis $\{1,i\}$ from <1>1 bijectively to the basis
$\{1,\sqrt2\}$. Hence it is a $\QQ$-linear isomorphism.
:::

<1>3. There is no field isomorphism
\[
\QQ(i)\longrightarrow\QQ(\sqrt2).
\]
::: proof
Suppose $\varphi$ were such an isomorphism. Every field homomorphism fixes the
prime field, so $\varphi(-1)=-1$. Since $i^2=-1$,
\[
\varphi(i)^2=\varphi(i^2)=\varphi(-1)=-1.
\]
But $\QQ(\sqrt2)\subseteq\RR$, and no real number has square $-1$. This is a
contradiction.
:::

<1>4. Thus $\QQ(i)$ and $\QQ(\sqrt2)$ are isomorphic as $\QQ$-vector spaces
but not as fields.
::: proof
Combine <1>2 and <1>3.
:::
:::
