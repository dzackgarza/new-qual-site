---
schema: qual/card@1
id: D-MFPYG
kind: definition
title: Blaschke factors and finite Blaschke products
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Biholomorphisms
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.definition}
For $a\in\DD$, the \dfn{Blaschke factor}, or \dfn{hyperbolic translation}, at $a$ is
$$
\psi_a(z)\coloneqq\frac{a-z}{1-\bar a z},\qquad z\in\CC,\ \bar a z\neq1.
$$
For $n\ge1$, points $a_1,\ldots,a_n\in\DD$, and $\lambda\in\CC$ with $\abs{\lambda}=1$, the \dfn{finite Blaschke product} with zeros $a_1,\ldots,a_n$ is
$$
B(z)\coloneqq\lambda\prod_{k=1}^{n}\psi_{a_k}(z)=\lambda\prod_{k=1}^{n}\frac{a_k-z}{1-\bar a_k z}.
$$
:::

::: {.remark}
Some authors take the Blaschke factor to be $\phi_a(z)\coloneqq\frac{z-a}{1-\bar a z}=-\psi_a(z)$; the two conventions differ by the unimodular constant $-1$, which is absorbed into $\lambda$ in a Blaschke product.
:::

::: {.proposition}
Let $a\in\DD$.

(i) For $\abs{z}\le1$, $1-\abs{\psi_a(z)}^2=\frac{(1-\abs{a}^2)(1-\abs{z}^2)}{\abs{1-\bar a z}^2}$; hence $\psi_a(\DD)\subseteq\DD$ and $\psi_a(S^1)\subseteq S^1$.

(ii) $\psi_a\circ\psi_a=\operatorname{id}$ on $\overline{\DD}$, so $\psi_a$ is a biholomorphism $\DD\to\DD$ exchanging $0$ and $a$.

(iii) $\psi_a'(z)=\frac{\abs{a}^2-1}{(1-\bar a z)^2}$, and $\psi_a$ preserves the hyperbolic metric $\frac{\abs{dz}}{1-\abs{z}^2}$ on $\DD$: $\frac{\abs{\psi_a'(z)}}{1-\abs{\psi_a(z)}^2}=\frac{1}{1-\abs{z}^2}$ for $z\in\DD$.

(iv) Every finite Blaschke product $B$ is holomorphic on a neighborhood of $\overline{\DD}$, maps $\DD$ into $\DD$ and $S^1$ into $S^1$, and its zeros in $\DD$ are exactly $a_1,\ldots,a_n$.

(v) $\psi_a(\lambda z)=\lambda\,\psi_{\bar\lambda a}(z)$ for every $\lambda\in\CC$ with $\abs\lambda=1$.
:::
