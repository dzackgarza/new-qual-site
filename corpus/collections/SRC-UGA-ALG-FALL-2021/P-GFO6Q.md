---
schema: qual/card@1
id: P-GFO6Q
kind: problem
title: Maximal ideals of finite-dimensional $\CC$-algebras have codimension $1$, and
  classification in dimension $2$
classification:
  areas:
  - algebra
  topics:
  - Algebras
  - Maximal Ideals
  - Classification
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source posed the problem for a finite-dimensional unital C-algebra, where part (a) fails for M_2(C). The statement now assumes R is commutative.
---
::: {.problem}
Let $R$ be a finite-dimensional commutative unital algebra over $\CC$. The codimension of a $\CC$-subspace $I \subseteq R$ is defined by
$$
\operatorname{codim}_R I = \dim_{\CC} R - \dim_{\CC} I.
$$

(a) Show that every maximal ideal $\mathfrak{m} \subset R$ has codimension $1$.

(b) Suppose that $\dim_{\CC} R = 2$. Show that there exists a surjective homomorphism of $\CC$-algebras from the polynomial ring $\CC[t]$ to $R$.

(c) Classify all unital $\CC$-algebras $R$ with $\dim_{\CC} R = 2$ up to isomorphism, and list their maximal ideals.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every maximal ideal $\mathfrak m\subset R$ has codimension $1$.

::: pf-proof

Since $R$ is commutative and $\mathfrak m$ is maximal, $K=R/\mathfrak m$ is a field. It contains $\CC$ through the unit map, and $\dim_{\CC}K\le\dim_{\CC}R<\infty$, so every $\alpha\in K$ is algebraic over $\CC$. As $\CC$ is algebraically closed, the minimal polynomial of $\alpha$ is linear, so $\alpha\in\CC$. Thus $K=\CC$ and $\operatorname{codim}_R\mathfrak m=\dim_{\CC}R/\mathfrak m=1$.

:::

:::

::: {.pf-step #s2}

If $\dim_{\CC}R=2$, then a surjective $\CC$-algebra homomorphism $\CC[t]\to R$ exists.

::: pf-proof

Choose $u\in R$ outside $\CC1_R$. The two elements $1_R,u$ form a vector-space basis of $R$. Since every element is a linear combination of $1_R$ and $u$, the unital homomorphism $\CC[t]\to R$ sending $t\mapsto u$ is surjective.
:::

:::

::: {.pf-step #s3}

Up to isomorphism, the two-dimensional unital complex algebras are
\[
\boxed{\CC\times\CC\quad\text{and}\quad
\CC[\varepsilon]/(\varepsilon^2)}.
\]
The first has maximal ideals $\CC\times0$ and $0\times\CC$; the second has the unique maximal ideal $(\varepsilon)$.

::: pf-proof

By step [](#s2){.pf-ref}, $R\cong\CC[t]/(f)$ for an ideal $(f)$ of $\CC[t]$. Since $\dim_{\CC}R=2$, the monic generator $f$ has degree two. Over $\CC$, it factors as $(t-a)(t-b)$. If $a\neq b$, the Chinese remainder theorem gives $R\cong\CC\times\CC$, whose maximal ideals are the kernels of the two projections. If $a=b$, translation of $t$ gives $R\cong\CC[\varepsilon]/(\varepsilon^2)$; every element $c+d\varepsilon$ with $c\neq0$ is a unit, and its nonunits form the unique maximal ideal $(\varepsilon)$. These rings are not isomorphic because the second has a nonzero nilpotent element while the first is reduced.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove parts (a), (b) and (c).

:::

:::

:::
