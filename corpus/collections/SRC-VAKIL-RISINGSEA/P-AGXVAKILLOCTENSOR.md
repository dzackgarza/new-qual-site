---
schema: qual/card@1
id: P-AGXVAKILLOCTENSOR
kind: problem
title: Localization of a module as a tensor product with $S^{-1}A$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Localization
  - Tensor Products
  - Universal Properties
relations: []
review: draft
---

::: {.problem}
If $S\subseteq A$ is multiplicative and $M\in \mods{A}$, describe a natural isomorphism
\[
\eta: (S^{-1}A)\tensor_A M \to S^{-1}M
\]
of both $S^{-1}A\dash$modules and $A\dash$modules.
:::

::: {.solution}
Recall the definition
\[
S^{-1}A &\da \ts{ {a\over s} \st a\in A,\, s\in S} / \sim \\
{a_1 \over s_1} &\sim {a_2 \over s_2} \iff \exists s\in S \text{ such that } s\qty{ s_2 a_1 - s_1 a_2 } = 0_A
,\]
and similarly $S^{-1}M = \ts{{m\over s}}/\sim$.

The universal property: in $\mods{A}$, $M\to S^{-1}M$ is initial among all morphisms $\alpha: M\to N$ such that $\alpha(S) \subseteq N\units$:

\begin{tikzcd}
	& S^{-1}M \ar[d, dotted, "{\exists ! \tilde\alpha}"] \\
	M\ar[ru, "S^{-1}\cdot"]\ar[r, "\alpha"] & N
\end{tikzcd}

> Strategy: define a map $M\to S^{-1}A \tensor_A M$ such that $S$ is invertible in the image, to obtain a map.
> Show they satisfy the same universal property.

- Since $M \in \mods{A}$, we have an action $a\cdot m$, so define
\[
\eta: (S^{-1}A)\cross M &\to S^{-1}M \\
\qty{ {a\over s}, m } &\mapsto {a\cdot m \over s }
.\]

- The tensor product $S^{-1}A \tensor_A M$ makes sense:
  - $S^{-1}A$ is a right $A\dash$module by $a_0 \mapsto \qty{ {a\over s} \mapsto {a_0 a \over s}}$.
  - $M$ is a left $A\dash$module by $a_0 \mapsto (m \mapsto a_0 \cdot m)$.

- The map makes sense as an $A\dash$module morphism:
  - $S^{-1}A \tensor_A M$ is a left $A\dash$module by $a_0 \mapsto \qty{{a\over s}\tensor m \mapsto {a_0 a \over s} \tensor m}$.
  - $S^{-1}M$ is a left $A\dash$module by $a_0 \mapsto \qty{ {m\over s } \mapsto {a_0 \cdot m \over s}}$, using the $A\dash$module structure on $M$.

- The map makes sense as an $S^{-1}A\dash$module morphism:
  - $S^{-1}A \tensor_A M$ is a left $S^{-1}A\dash$module by ${a_0\over s_0} \mapsto \qty{ {a\over s}\tensor m \mapsto {a_0 a \over s_0 s} \tensor m }$.
  - $S^{-1}M$ is a left $S^{-1}A\dash$module by ${a_0\over s_0} \mapsto \qty{{m \over s} \mapsto {a_0 \cdot m \over s_0 s} }$, by the $A\dash$module structure on $M$.

- Well-defined: ?

- $A\dash$bilinear: let $r\in A$, then
\[
\eta\qty{r \cdot {a\over s}, m}
&\da \eta\qty{{r\cdot a\over s}, m}  \\
&\da {\psi(r\cdot a)(m) \over s} \\
&= {r\cdot \psi(a)(m) \over s} \quad\text{since $\psi$ is a ring morphism} \\
&= {\psi(a)(r\cdot m) \over s} \quad\text{since $\psi(a)$ is a ring morphism} \\
&\da \eta\qty{ {a\over s}, r\cdot m}
.\]
So this lifts to a map out of the tensor product.

- $S^{-1}A\dash$bilinear: ?
:::

::: {.remark}
Erratum: the argument above is unfinished and uses undefined notation.

- A module has no units. The universal property of $M \to S^{-1}M$ is initial among $A$-module maps $\alpha: M\to N$ into modules $N$ on which multiplication by every $s \in S$ is bijective.
- The map $\psi$ in the bilinearity computation is never defined, and "$\psi(a)$ is a ring morphism" has no meaning here. The $A$-balance of $\eta$ is $\eta\qty{\frac{ra}{s}, m} = \frac{ram}{s} = \eta\qty{\frac{a}{s}, rm}$ by the module axioms.
- Well-definedness, left as "?", holds because $t(s'a - sa') = 0$ implies $t(s'am - sa'm) = 0$, so $\frac{am}{s} = \frac{a'm}{s'}$.
- The solution never shows that $\eta$ is an isomorphism. The map $\frac{m}{s} \mapsto \frac{1}{s}\tensor m$ is a well-defined inverse, and $S^{-1}A$-linearity, also left as "?", is checked on elementary tensors.
:::
