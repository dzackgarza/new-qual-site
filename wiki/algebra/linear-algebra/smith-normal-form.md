---
title: Smith normal form
order: 50
topics:
- Smith Normal Form
- Modules over PIDs
---

# Smith normal form

::: {.fact}
Let $R$ be a PID and $A\in \Mat(m\times n; R)$.
There are invertible matrices $P$ and $Q$ over $R$ such that $\SNF(A) = PAQ$ is diagonal with diagonal entries $a_1\divides a_2\divides\cdots\divides a_r$ followed by zeros, and the $a_i$ are unique up to units.

The diagonal entries are $a_i = d_i/d_{i-1}$, where $d_0=1$ and $d_i$ is a greatest common divisor of the $i\times i$ minors of $A$.

Two $m\times n$ matrices over $R$ are equivalent if and only if they have the same Smith normal form.
:::

::: {.remark}
The computation of $\SNF(A)$ by row and column operations is in [@DF04, p. 479].
:::

::: {.remark title="Classification of finitely generated modules"}
If $M\cong R^n/\im(A)$ for a matrix $A\in\Mat(n\times m;R)$, then
$$
M\cong R^{n-r}\oplus\bigoplus_{i=1}^r R/\gens{a_i},
$$
where $a_1,\ldots,a_r$ are the nonzero diagonal entries of $\SNF(A)$; the nonunit $a_i$ are the invariant factors of the torsion submodule of $M$.
This is the computation on [[algebra/modules/classify-this-module|Classify this module]]. For $R = \ZZ$ it classifies finitely generated abelian groups, and for $R=k[x]$ applied to $xI-A$ it gives the invariant factors of the [[algebra/linear-algebra/rational-canonical-form|rational canonical form]] of a square matrix $A$ over a field $k$.
:::
