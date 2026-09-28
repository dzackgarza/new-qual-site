---
schema: qual/card@1
id: FD-6XJ7D
kind: definition
title: Projective module
prompts:
- What is a projective module, and how does it sit inside a free module?
classification:
  areas:
  - algebra
  topics:
  - Projective Modules
  - Free Modules
  - Modules
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
An $R$-module $P$ is \dfn{projective} if for every surjective $R$-linear map $g\colon M\to N$ and every $R$-linear map $f\colon P\to N$ there exists an $R$-linear map $\phi\colon P\to M$ with $g\circ\phi=f$:

\begin{tikzcd}
	&& P \\
	\\
	M && N
	\arrow["{\exists\phi}"', dashed, from=1-3, to=3-1]
	\arrow["f", from=1-3, to=3-3]
	\arrow["g"', two heads, from=3-1, to=3-3]
\end{tikzcd}
:::

::: {.proposition}
An $R$-module $P$ is projective if and only if there are an $R$-module $Q$ and a [[D-LIEMF|free]] $R$-module $F$ with $F\cong P\oplus Q$.
:::

::: {.proof}
Suppose $P$ is projective.
Let $F$ be the free $R$-module on the set $P$ and $\pi\colon F\to P$ the surjection sending each basis element to the corresponding element of $P$.
Applying the definition to $g=\pi$ and $f=\id_P$ gives $s\colon P\to F$ with $\pi\circ s=\id_P$, and then $F\cong P\oplus\ker\pi$ via $x\mapsto(\pi(x),x-s\pi(x))$.

Conversely, a free module $F$ with basis $(e_i)_{i\in I}$ is projective: given $g\colon M\to N$ surjective and $f\colon F\to N$, choose $m_i\in M$ with $g(m_i)=f(e_i)$ and let $\phi$ be the $R$-linear map with $\phi(e_i)=m_i$.
If $F=P\oplus Q$ is free and $f\colon P\to N$ is given, lift $f\oplus 0\colon F\to N$ to $\psi\colon F\to M$; the restriction $\phi=\psi|_P$ satisfies $g\circ\phi=f$.
:::
