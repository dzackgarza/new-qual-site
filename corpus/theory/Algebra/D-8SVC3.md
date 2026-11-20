---
schema: qual/card@1
id: D-8SVC3
kind: definition
title: Norm of an element of a finite field extension
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Number Fields
relations: []
review: draft
---

::: {.definition}
Let $L/K$ be a finite extension of fields and let $u\in L$.
Multiplication by $u$ is the $K$-linear endomorphism
$$
\begin{aligned}
m_u\colon L &\to L \\
x &\mapsto ux,
\end{aligned}
$$
and the \dfn{norm of $u$} is $N_{L/K}(u)\coloneqq \det(m_u)$, an element of $K$ [@Hun74, chapter VII, §1, exercise 9(b)].
:::

::: {.remark}
Write $[L:K]_i$ for the inseparable degree and let $\sigma_1,\ldots,\sigma_r$ be the distinct $K$-monomorphisms of $L$ into an algebraic closure of $K$; then
$$
N_{L/K}(u) = \bigl(\sigma_1(u)\cdots\sigma_r(u)\bigr)^{[L:K]_i},
$$
which is the definition in [@Hun74, chapter V, §7, definition 7.1], and the two agree by the exercise cited above.
:::

::: {.proposition}
Let $L/K$ be a finite extension of fields and $u,v\in L$. Then $N_{L/K}(uv) = N_{L/K}(u)\,N_{L/K}(v)$, and $N_{L/K}(u)\neq0$ when $u\neq0$.
:::

::: {.proof}
$m_{uv} = m_u\circ m_v$, so $\det(m_{uv}) = \det(m_u)\det(m_v)$ by multiplicativity of the determinant; and $m_u$ is invertible with inverse $m_{u^{-1}}$ when $u\neq0$, so its determinant is nonzero.
:::
