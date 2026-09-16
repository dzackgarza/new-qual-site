---
schema: qual/card@1
id: D-RHJMK
kind: definition
title: Projective modules
classification:
  areas:
  - algebra
  topics:
  - Projective Modules
  - Modules
  - Homological Algebra
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring.
An [[D-NQZUY|$R$-module]] $P$ is \dfn{projective} if for every surjective $R$-linear map $g\colon N \to M$ and every $R$-linear map $f\colon P\to M$ there exists an $R$-linear map $\tilde f\colon P\to N$ with $g\circ\tilde f = f$:

\begin{tikzcd}
	&& P \\
	\\
	N && M
	\arrow["g", two heads, from=3-1, to=3-3]
	\arrow["f", from=1-3, to=3-3]
	\arrow["{\exists \tilde f}"', dashed, from=1-3, to=3-1]
\end{tikzcd}
:::

::: {.proposition}
Let $R$ be a ring and $P$ an $R$-module.
The following are equivalent:

1. $P$ is projective;

2. $P$ is a direct summand of a [[D-LIEMF|free]] module: there are a free $R$-module $F$ and a submodule $T\leq F$ with $F = P \oplus T$, up to isomorphism;

3. every short exact sequence $0\to A\to B\xrightarrow{p} P\to 0$ of $R$-modules splits: there is an $R$-linear map $s\colon P\to B$ with $p\circ s = \id_P$;

4. the functor $\Hom_R(P, \wait)$ from $R$-modules to abelian groups is exact.
:::

::: {.proof}
(1)$\Rightarrow$(3): lift $\id_P$ along the surjection $p$.
(3)$\Rightarrow$(2): choose a free module $F$ with a surjection $p\colon F\to P$, for example on a generating set of $P$; a section $s$ of $p$ gives $F=s(P)\oplus\ker p$ with $s(P)\cong P$.
(2)$\Rightarrow$(1): a free module $F$ with basis $(e_i)$ is projective, since $\tilde f(e_i)$ may be chosen as any preimage under $g$ of $f(e_i)$; if $F=P\oplus T$ with inclusion $\iota\colon P\to F$ and projection $\pi\colon F\to P$, a lift $h$ of $f\circ\pi$ gives the lift $\tilde f=h\circ\iota$ of $f$.
(1)$\Leftrightarrow$(4): $\Hom_R(P,\wait)$ is always left exact, and it preserves surjections exactly when every $f\colon P\to M$ lifts along every surjection $g\colon N\to M$.
:::

::: {.remark}
In (3), the section $s$ gives $B = s(P) \oplus \ker p$, and $s(P)\cong P$.
:::
