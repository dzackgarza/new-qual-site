---
schema: qual/card@1
id: P-FHW1-07
kind: problem
title: Intermediate rings of an algebraic extension are fields
classification:
  areas: [algebra]
  topics: [Field Extensions, Rings]
relations: []
review: draft
audit:
- event: source-checked
  by: Claude Opus 5.5
  date: 2026-10-30
  note: Transcribed from the MinerU Flash extraction of assets/attachments/fields-homework-1.pdf and checked against the page image.
- event: solution-written
  by: claude
  date: 2026-10-31
---

::: {.problem}
Let $K\subset F$ be an algebraic extension and let $R$ be a subring of $F$ that contains $K$. Show that $R$ is a field.
:::

::: {.solution}
A subring $R\subseteq F$ containing $K$ is a $K$-subspace of $F$, and it contains $K$ and is closed under multiplication.

::: pf

::: {.pf-step #inverse}
Every nonzero $r\in R$ has its inverse in $R$.

::: pf-proof
Since $K\subseteq F$ is algebraic and $r\in F$, the element $r$ is algebraic over $K$; let $m_r(x)=x^n+c_{n-1}x^{n-1}+\cdots+c_0$ be its minimal polynomial over $K$, so $n\ge1$ and $c_0\ne0$ (otherwise $x$ would divide $m_r$ and $m_r(r)=0$ would give a factor of smaller degree).
From $r^n+c_{n-1}r^{n-1}+\cdots+c_0=0$ we get
$$
r\cdot\Bigl(-\frac{1}{c_0}\bigl(r^{n-1}+c_{n-1}r^{n-2}+\cdots+c_1\bigr)\Bigr)=1,
$$
and the factor in parentheses lies in $R$, because $r\in R$, the coefficients $c_i$ lie in $K\subseteq R$, and $R$ is a ring closed under addition and multiplication.
Hence $r^{-1}\in R$.
:::

:::

::: {.pf-step #field}
$R$ is a field.

::: pf-proof
The ring $R$ contains $1$ and is commutative, being a subring of the field $F$.
By step [](#inverse){.pf-ref} every nonzero element of $R$ is a unit of $R$, which is exactly the definition of a field.
:::

:::

:::

:::
