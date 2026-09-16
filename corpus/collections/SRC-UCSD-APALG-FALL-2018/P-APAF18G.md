---
schema: qual/card@1
id: P-APAF18G
kind: problem
title: Linear independence of standard monomials for a Gröbner basis
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $k$ be a field and let $I\subseteq k[x_1,\ldots,x_n]$ be an ideal.
Fix a monomial order $<$ and let $G=\{g_1,\ldots,g_s\}$ be a Gröbner basis for $I$ with respect to $<$.

(a) Explain why the collection of cosets
\[
\bigl\{m+I:\ m\text{ a monomial in }x_1,\ldots,x_n\text{ and }\operatorname{LM}(g_i)\nmid m\text{ for }1\le i\le s\bigr\}
\]
is linearly independent in the quotient $k[x_1,\ldots,x_n]/I$.

(b) Is the conclusion of (a) still true if $G$ is a basis for $I$ which is not necessarily Gröbner?
Prove or give a counterexample.
:::

::: {.solution}
<1>1. The cosets of the monomials not divisible by any $\operatorname{LM}(g_i)$ are linearly independent in $k[x_1,\ldots,x_n]/I$.
::: {.proof}
Suppose, toward a contradiction, that there is a nontrivial finite linear relation
\[
\sum_{j=1}^r c_jm_j\in I,
\qquad c_j\in k,
\]
where the $m_j$ are distinct monomials and no $m_j$ is divisible by any $\operatorname{LM}(g_i)$.
Set
\[
f=\sum_{j=1}^r c_jm_j.
\]
After discarding zero coefficients, $f\ne0$. Its leading monomial $\operatorname{LM}(f)$ is one of the monomials $m_j$, so by hypothesis it is not divisible by any $\operatorname{LM}(g_i)$.

But $f\in I$ and $G$ is a Gröbner basis. Hence
\[
\operatorname{LM}(f)\in\langle\operatorname{LM}(g_1),\ldots,\operatorname{LM}(g_s)\rangle,
\]
so some $\operatorname{LM}(g_i)$ must divide $\operatorname{LM}(f)$. This is a contradiction.
Therefore no nontrivial linear relation among the displayed cosets exists.
:::

<1>2. The conclusion is false for an arbitrary generating set of $I$ that is not a Gröbner basis.
::: {.proof}
Take
\[
k[x,y]
\]
with lexicographic order $x>y$, and let
\[
I=(x,y).
\]
Consider the generating set
\[
G=\{x+y,\ x\}.
\]
It generates $I$, since
\[
y=(x+y)-x\in (G),
\]
while clearly both generators lie in $(x,y)$.

For both elements of $G$, the leading monomial is $x$. Thus the monomial $y$ is not divisible by the leading monomial of either generator, so $y+I$ belongs to the collection described in part (a) if one uses this non-Gröbner generating set.
However
\[
y\in I,
\]
so
\[
y+I=0
\]
in the quotient. A collection containing the zero vector is not linearly independent.

Indeed, this also shows directly that $G$ is not a Gröbner basis: the polynomial $y\in I$ has leading monomial $y$, which is not divisible by the leading monomial $x$ of either element of $G$.
:::
:::
