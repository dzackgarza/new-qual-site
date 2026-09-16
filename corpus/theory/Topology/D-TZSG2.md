---
schema: qual/card@1
id: D-TZSG2
kind: definition
title: Direct sum of modules
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
Let $R$ be a ring and $(M_\alpha)_{\alpha\in A}$ a family of $R$-modules with [[D-XSBR2|direct product]] $\prod_{\alpha}M_\alpha$.
The \dfn{direct sum} of the family is the submodule
$$
\bigoplus_{\alpha\in A}M_\alpha\coloneqq\ts{(m_\alpha)_{\alpha\in A}\in\prod_{\alpha\in A}M_\alpha \st m_\alpha=0\text{ for all but finitely many }\alpha},
$$
with the inclusions $\iota_\beta\colon M_\beta\injects\bigoplus_\alpha M_\alpha$ sending $m$ to the family with $m$ in position $\beta$ and $0$ elsewhere [@DF04, sec. 10.3].
:::

::: {.proposition}
The direct sum is the [[D-COC6C|coproduct]] in the category of $R$-modules: for every $R$-module $N$ and every family of $R$-linear maps $\varphi_\alpha\colon M_\alpha\to N$ there is a unique $R$-linear map $\varphi\colon\bigoplus_\alpha M_\alpha\to N$ with $\varphi\circ\iota_\alpha=\varphi_\alpha$ for all $\alpha$ [@DF04, sec. 10.3].
If $A$ is finite, then $\bigoplus_\alpha M_\alpha=\prod_\alpha M_\alpha$.
:::
