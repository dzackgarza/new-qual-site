---
schema: qual/card@1
id: P-APAS18G
kind: problem
title: Linear independence of standard monomials for a Gröbner basis
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
relations: []
review: draft
---

::: {.problem}
Let $k$ be a field and let $I\subseteq k[x_1,\ldots,x_n]$ be an ideal.
Fix a monomial order $<$ and let $G=\{g_1,\ldots,g_s\}$ be a Gröbner basis for $I$ with respect to $<$.

(a) Explain why the set of cosets
$$
\bigl\{m+I:\ m\text{ a monomial in }x_1,\ldots,x_n\text{ and }\operatorname{LM}(g_i)\nmid m\text{ for }1\leq i\leq s\bigr\}
$$
is linearly independent in the quotient $k[x_1,\ldots,x_n]/I$.

(b) Is the conclusion of (a) still true if $G$ is a basis for $I$ which is not necessarily Gröbner?
Prove or give a counterexample.
:::

::: {.solution}
Write $R\coloneqq k[x_1,\ldots,x_n]$ and let $\mathcal S$ be the set of monomials not divisible by any $\operatorname{LM}(g_i)$.

::: pf

::: pf-step

(a) The cosets $m+I$, $m\in\mathcal S$, are linearly independent in $R/I$.

::: pf-proof

Since $G$ is a Gröbner basis, $\operatorname{in}(I)=\langle\operatorname{LM}(g_1),\ldots,\operatorname{LM}(g_s)\rangle$, a monomial ideal, so a monomial lies in $\operatorname{in}(I)$ exactly when some $\operatorname{LM}(g_i)$ divides it. Suppose $f=\sum_{j=1}^r c_jm_j\in I$ with distinct $m_j\in\mathcal S$ and all $c_j\ne0$, $r\ge1$. The leading monomial of $f$ is the largest $m_j$, and it lies in $\operatorname{in}(I)$ because $f\in I$; so some $\operatorname{LM}(g_i)$ divides it, which contradicts $m_j\in\mathcal S$.

:::

:::

::: pf-step

(b) $\boxed{\text{No}}$: for $I=(x,y)\subseteq\QQ[x,y]$ with lex order $x>y$, the basis $G=\{x+y,\,x-y\}$ is a counterexample.

::: pf-proof

$G$ generates $I$, since $x=\frac12\bigl((x+y)+(x-y)\bigr)$ and $y=\frac12\bigl((x+y)-(x-y)\bigr)$. Both leading monomials are $x$, so $y\in\mathcal S$; but $y+I=0$ in $R/I$, and a set containing the zero vector is linearly dependent.

:::

:::

:::
:::
