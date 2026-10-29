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
\operatorname{tr}:M_n(\CC)\longrightarrow\CC,
\qquad
\operatorname{tr}(A)=\sum_{k=1}^n A_{k,k}.
\]

(a) Determine a basis for the kernel of $\operatorname{tr}$.

(b) For $X\in M_n(\CC)$, show that $\operatorname{tr}(X)=0$ if and only if there are an integer $m$ and matrices
\[
A_1,\ldots,A_m,B_1,\ldots,B_m\in M_n(\CC)
\]
such that
\[
X=\sum_{j=1}^m(A_jB_j-B_jA_j).
\]
:::

::: {.solution}

Let $E_{ij}$ denote the standard matrix unit.

::: pf

::: {.pf-step #s1-1}

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

::: {.pf-step #s1-2}

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

::: {.pf-step #s1-3}

Every basis element from step [](#s1-1){.pf-ref} is a commutator.


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

::: {.pf-step #s1-4}

If $\operatorname{tr}(X)=0$, then $X$ is a finite sum of commutators.


::: pf-proof

If $n=1$, then $X=0=[0,0]$, so the assertion holds. Assume $n\ge2$.
By step [](#s1-1){.pf-ref}, write $X$ as a linear combination of the displayed basis elements. By step [](#s1-3){.pf-ref}, each basis element is a commutator. A scalar multiple of a commutator is again a commutator because
$$
c(AB-BA)=(cA)B-B(cA).
$$
Therefore $X$ is a finite sum of commutators.

:::

:::

::: {.pf-step #s1-5}

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

The forward implication is step [](#s1-4){.pf-ref}. The reverse implication is step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), and step [](#s1-5){.pf-ref} proves part (b).

:::

:::

:::
