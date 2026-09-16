---
schema: qual/card@1
id: D-LIEMF
kind: definition
title: Free module
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Modules
  - Bases
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
An [[D-NQZUY|$R$-module]] $M$ is \dfn{free} if it has a [[D-I7D56|basis]]: a family $(\beta_i)_{i\in I}$ in $M$ such that every $m\in M$ can be written as $m=\sum_{i\in I} r_i\beta_i$ with $r_i\in R$, all but finitely many zero, and $\sum_{i\in I} r_i\beta_i = 0$ implies $r_i = 0$ for all $i$.
:::

::: {.proposition}
Let $R$ be a ring and $M$ an $R$-module.
The following are equivalent:

1. $M$ is free, with basis $(\beta_i)_{i\in I}$;

2. there are a set $\mathcal{B}$ and a map of sets $\iota\colon\mathcal{B}\to M$ such that for every $R$-module $N$ and every map of sets $f\colon\mathcal{B}\to N$ there is a unique $R$-linear map $\tilde f\colon M\to N$ with $\tilde f\circ\iota = f$:

\begin{tikzcd}
	M \\
	\\
	{\mathcal{B}} && N
	\arrow["f", from=3-1, to=3-3]
	\arrow["{\tilde f}"', dashed, from=1-1, to=3-3]
	\arrow["\iota", hook, from=3-1, to=1-1]
\end{tikzcd}

3. there is a family $(\beta_i)_{i\in I}$ in $M$ such that $M = \bigoplus_{i\in I} R\beta_i$ is the internal direct sum of the cyclic submodules $R\beta_i$, and $r\mapsto r\beta_i$ is injective for each $i$, so that $R\beta_i\cong R$.
:::

::: {.proof}
Given a basis $(\beta_i)_{i\in I}$, take $\mathcal B=I$ and $\iota(i)=\beta_i$; the unique extension of $f$ is $\tilde f(\sum_i r_i\beta_i)=\sum_i r_if(i)$, which is well defined because the coefficients $r_i$ are unique.
Conversely, if $(\mathcal B,\iota)$ has the universal property, compare $M$ with the module $R^{(\mathcal B)}$ of finitely supported functions $\mathcal B\to R$ and its standard basis $(e_b)_{b\in\mathcal B}$: the linear maps $M\to R^{(\mathcal B)}$ extending $b\mapsto e_b$ and $R^{(\mathcal B)}\to M$ extending $e_b\mapsto\iota(b)$ compose in both orders to maps that restrict to the identity on the generators, so by uniqueness they are inverse isomorphisms, and $(\iota(b))_{b\in\mathcal B}$ is a basis of $M$.
Finally, the spanning condition says that $M=\sum_i R\beta_i$, and linear independence says exactly that this sum is direct and each $r\mapsto r\beta_i$ is injective.
:::
