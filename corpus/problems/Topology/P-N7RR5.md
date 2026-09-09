---
schema: qual/card@1
id: P-N7RR5
kind: problem
title: Interior of a product versus product of interiors
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Product Topology
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
Is it true that the interior of a product is the product of the interiors? Specifically, for topological spaces $X$ and $Y$ and subsets $A \subseteq X$ and $B \subseteq Y$, is $\operatorname{int}(A \times B) = \operatorname{int}(A) \times \operatorname{int}(B)$? What about infinite products?
:::

::: solution
<1>1. For two factors,
\[
\operatorname{int}_{X\times Y}(A\times B)
=\operatorname{int}_X(A)\times\operatorname{int}_Y(B).
\]
<2>1. The right-hand side is open in $X\times Y$ and contained in $A\times B$, so it is contained in the left-hand side.
<2>2. Conversely, if $(x,y)\in\operatorname{int}(A\times B)$, then some basic open set $U\times V$ satisfies
\[
(x,y)\in U\times V\subseteq A\times B.
\]
Hence $U\subseteq A$ and $V\subseteq B$, so $x\in\operatorname{int}(A)$ and $y\in\operatorname{int}(B)$.

<1>2. The same argument gives the finite-product identity
\[
\operatorname{int}\!\left(\prod_{i=1}^n A_i\right)
=\prod_{i=1}^n\operatorname{int}(A_i).
\]

<1>3. Let now $\prod_{i\in I}X_i$ have the product topology and put $A=\prod_{i\in I}A_i$.
<2>1. If $A$ has nonempty interior, choose a basic open set
\[
\prod_{i\in I}U_i\subseteq A,
\]
where $U_i=X_i$ for all but finitely many $i$.
<2>2. For every index with $U_i=X_i$, the inclusion $U_i\subseteq A_i$ forces $A_i=X_i$. Thus $A_i=X_i$ for all but finitely many $i$.
<2>3. Conversely, if $A_i=X_i$ for all but finitely many $i$, then
\[
\operatorname{int}(A)=\prod_{i\in I}\operatorname{int}(A_i),
\]
because the right-hand side is then a basic open product (possibly empty), and the finite-coordinate argument from <1>1 proves maximality.
<2>4. Therefore
\[
\operatorname{int}\!\left(\prod_{i\in I}A_i\right)=
\begin{cases}
\prod_{i\in I}\operatorname{int}(A_i),&A_i=X_i\text{ for all but finitely many }i,\\
\varnothing,&\text{otherwise}.
\end{cases}
\]

<1>4. Hence the finite-product identity always holds, whereas for infinite products it can fail. For example,
\[
\operatorname{int}_{\mathbb R^{\mathbb N}}([0,1]^{\mathbb N})=\varnothing
\quad\text{but}\quad
\prod_{n\ge1}\operatorname{int}[0,1]=(0,1)^{\mathbb N}\ne\varnothing.
\]
:::
