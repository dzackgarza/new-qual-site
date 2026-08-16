---
schema: qual/card@1
id: P-ZGEFJ
kind: problem
title: "$IS$ is a submodule of $A$"
classification:
  areas:
  - algebra
  topics:
  - modules
  - ideals
relations: []
review: draft
---

::: problem
Here $I$ is a left ideal of $R$, $S$ is a nonempty subset of the $R\dash$module $A$, and
\[
IS \definedas \theset{ \sum_{i=1}^n r_i a_i \suchthat n\geq 1,\ r_i \in I,\ a_i \in S }
.\]

$A$ carries no internal multiplication, so being a submodule is closure under addition and under the action of $R$, not closure under multiplication by elements of $A$.
So we show
$$
x, y \in IS,~ r\in R \implies x + y \in IS \text{ and } rx \in IS.
$$

Closure under addition is immediate: concatenating the two sums
$$
x = \sum_{i=1}^n r_i a_i, \qquad y = \sum_{j=1}^m r_j' a_j'
$$
exhibits $x+y$ as another finite sum of the same shape, with all coefficients in $I$ and all module elements in $S$.

For the action of $R$, let $r\in R$. Then
\[
\begin{align*}
rx &= r\left( \sum_{i=1}^n r_i a_i \right) \\
&= \sum_{i=1}^n (r r_i) a_i
,\end{align*}
\]

and $r r_i \in I$ for each $i$, because $I$ is a *left* ideal and is therefore closed under left multiplication by $R$.
This exhibits $rx$ as an element of $IS$.

Finally $IS \neq \emptyset$ since $S\neq\emptyset$, so $IS$ is a submodule of $A$.
:::
