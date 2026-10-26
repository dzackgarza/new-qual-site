---
schema: qual/card@1
id: P-UCLAB05S-LA1
kind: problem
title: Trace-zero matrices and sums of commutators
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra Problem 1 of the official UCLA Basic Exam, May 2005 PDF; the retained PDF has the commutator sum indexed from $j=1$ to $m$.
---

::: {.problem}
For $n\geq1$, let
\[
\operatorname{tr}:M_n(\mathbb C)\longrightarrow\mathbb C,
\qquad
\operatorname{tr}(A)=\sum_{k=1}^n A_{k,k}.
\]

(a) Determine a basis for the kernel of $\operatorname{tr}$.

(b) For $X\in M_n(\mathbb C)$, show that $\operatorname{tr}(X)=0$ if and only if there are an integer $m$ and matrices
\[
A_1,\ldots,A_m,B_1,\ldots,B_m\in M_n(\mathbb C)
\]
such that
\[
X=\sum_{j=1}^m(A_jB_j-B_jA_j).
\]
:::

Let $E_{ij}$ denote the standard matrix unit.

::: pf

::: pf-step

For $n=1$, the kernel of $\operatorname{tr}$ is $\{0\}$, whose basis is the empty set. For $n\ge2$, a basis of $\ker(\operatorname{tr})$ is
$$
\boxed{
\{E_{ij}:i\ne j\}
\cup
\{E_{ii}-E_{nn}:1\le i\le n-1\}.}
$$


::: pf-proof

Every displayed matrix has trace $0$. There are
$$
n(n-1)+(n-1)=n^2-1
$$
such matrices. They are linearly independent: the coefficient of each off-diagonal entry determines the coefficient of $E_{ij}$, and then the first $n-1$ diagonal entries determine the coefficients of $E_{ii}-E_{nn}$.

Since $\operatorname{tr}$ is a nonzero linear map from the $n^2$-dimensional space $M_n(\CC)$ to the one-dimensional space $\CC$, its kernel has dimension $n^2-1$. Hence these $n^2-1$ independent trace-zero matrices form a basis.

:::

:::

::: pf-step

Every commutator has trace $0$.


::: pf-proof

For any $A,B\in M_n(\CC)$,
$$
\operatorname{tr}(AB)
=\sum_{i,j}A_{ij}B_{ji}
=\sum_{i,j}B_{ij}A_{ji}
=\operatorname{tr}(BA).
$$
Therefore
$$
\operatorname{tr}(AB-BA)=0.
$$
By linearity, every finite sum of commutators also has trace $0$.

:::

:::

::: pf-step

Every basis element from step <1>1 is a commutator.


::: pf-proof

If $i\ne j$, then
$$
[E_{ii},E_{ij}]
\coloneqq
E_{ii}E_{ij}-E_{ij}E_{ii}
=E_{ij}.
$$
For $1\le i\le n-1$,
$$
[E_{in},E_{ni}]
=E_{ii}-E_{nn}.
$$
Thus each basis vector of $\ker(\operatorname{tr})$ is a commutator.

:::

:::

::: pf-step

If $\operatorname{tr}(X)=0$, then $X$ is a finite sum of commutators.


::: pf-proof

If $n=1$, then $X=0=[0,0]$, so the assertion holds. Assume $n\ge2$.
By step <1>1, write $X$ as a linear combination of the displayed basis elements. By step <1>3, each basis element is a commutator. A scalar multiple of a commutator is again a commutator because
$$
c(AB-BA)=(cA)B-B(cA).
$$
Therefore $X$ is a finite sum of commutators.

:::

:::

::: pf-step

For $X\in M_n(\CC)$,
$$
\boxed{
\operatorname{tr}(X)=0
\iff
X=\sum_{j=1}^m(A_jB_j-B_jA_j)
}
$$
for some integer $m$ and matrices $A_j,B_j\in M_n(\CC)$.


::: pf-proof

The forward implication is step <1>4. The reverse implication is step <1>2.

:::

:::

::: pf-qed

Step <1>1 answers part (a), and step <1>5 proves part (b).

:::

:::
