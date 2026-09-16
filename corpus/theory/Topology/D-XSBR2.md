---
schema: qual/card@1
id: D-XSBR2
kind: definition
title: Direct product of modules
classification:
  areas:
  - topology
  topics:
  - Modules
  - Category Theory
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring and $(M_\alpha)_{\alpha\in A}$ a family of left $R$-modules.
The \dfn{direct product} of the family is the set
$$
\prod_{\alpha\in A} M_\alpha \coloneqq \ts{ (m_\alpha)_{\alpha\in A} \st m_\alpha \in M_\alpha \text{ for all } \alpha\in A }
$$
with componentwise addition and scalar multiplication, together with the projections $\pi_\beta\colon\prod_{\alpha\in A} M_\alpha\to M_\beta$, $(m_\alpha)_{\alpha\in A}\mapsto m_\beta$, for $\beta\in A$.
:::

::: {.proposition}
For every left $R$-module $N$ and every family of $R$-linear maps $f_\beta\colon N\to M_\beta$, $\beta\in A$, there is a unique $R$-linear map $f\colon N\to \prod_{\alpha\in A} M_\alpha$ with $\pi_\beta\circ f = f_\beta$ for all $\beta\in A$, namely $f(n) = (f_\alpha(n))_{\alpha\in A}$.
Thus $\prod_{\alpha\in A} M_\alpha$ is the categorical product of the family in the category of left $R$-modules.
:::

::: {.example}
In $\Top$, the categorical product of a family of spaces $(X_\alpha)_{\alpha\in A}$ is the set $\prod_{\alpha\in A} X_\alpha$ with the [[D-JKH35|product topology]], the coarsest topology for which every projection $\pi_\beta$ is continuous.
:::

::: {.concept}
[@DF04, §10.3]; [@Hat02, §4.H, p. 461].
:::
