---
schema: qual/card@1
id: E-GNYRR
kind: problem
title: Cayley-Hamilton via invariant flags of an upper-triangular basis
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Eigenvalues and Eigenvectors
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

:::{.exercise}
Prove Cayley-Hamilton in the following way.
Let $V=\spanof\ts{\vector v_1,\ldots,\vector v_n}$ and define
\[
\Fil_iV=\spanof\ts{\vector v_1,\ldots,\vector v_i},
\qquad
\Fil_0V=\ts{0}.
\]
Suppose the matrix of $A$ in this basis is upper triangular, with diagonal entries $\lambda_1,\ldots,\lambda_n$.
Show that
\[
A(\Fil_iV)\subseteq\Fil_iV,
\qquad
(A-\lambda_iI)\Fil_iV\subseteq\Fil_{i-1}V.
\]
Deduce that
\[
(A-\lambda_1I)\cdots(A-\lambda_nI)V=0
\]
and hence $\chi_A(A)=0$. Finally, deduce Cayley-Hamilton for an arbitrary operator over an arbitrary field by extending scalars to an algebraic closure and triangularizing there.
:::

::: {.solution}
<1>1. For every $i$, the flag subspace $\Fil_iV$ is $A$-invariant.
::: {.proof}
Because the matrix of $A$ in the ordered basis $v_1,\ldots,v_n$ is upper triangular, for each $j$ one has
\[
Av_j\in\spanof\ts{v_1,\ldots,v_j}=\Fil_jV.
\]
Thus if $j\le i$, then $Av_j\in\Fil_iV$. Since $\Fil_iV$ is spanned by $v_1,\ldots,v_i$, it follows that
\[
A(\Fil_iV)\subseteq\Fil_iV.
\]
:::

<1>2. For every $i$, one has
\[
(A-\lambda_iI)\Fil_iV\subseteq\Fil_{i-1}V.
\]
::: {.proof}
For $j<i$, both $Av_j$ and $\lambda_i v_j$ lie in $\Fil_{i-1}V$, hence so does $(A-\lambda_iI)v_j$. For $j=i$, upper triangularity gives
\[
Av_i=\lambda_i v_i+w
\]
for some $w\in\Fil_{i-1}V$. Therefore
\[
(A-\lambda_iI)v_i=w\in\Fil_{i-1}V.
\]
Since $v_1,\ldots,v_i$ span $\Fil_iV$, the inclusion follows.
:::

<1>3. The product of the linear factors annihilates $V$:
\[
(A-\lambda_1I)\cdots(A-\lambda_nI)V=0.
\]
::: {.proof}
By <1>2,
\[
(A-\lambda_nI)\Fil_nV\subseteq\Fil_{n-1}V.
\]
Applying successively the factors with indices $n-1,n-2,\ldots,1$ gives
\[
(A-\lambda_1I)\cdots(A-\lambda_nI)\Fil_nV
\subseteq\Fil_0V=0.
\]
Since $\Fil_nV=V$, the displayed product is the zero operator.
:::

<1>4. For an upper-triangular matrix,
\[
\chi_A(t)=\prod_{i=1}^n(t-\lambda_i),
\]
so $\chi_A(A)=0$.
::: {.proof}
The determinant of $tI-A$ is the product of its diagonal entries, namely
\[
\det(tI-A)=\prod_{i=1}^n(t-\lambda_i).
\]
Evaluating this polynomial at $A$ yields exactly the product in <1>3. Hence $\chi_A(A)=0$.
:::

<1>5. Cayley-Hamilton holds for every endomorphism of a finite-dimensional vector space over an arbitrary field.
::: {.proof}
Let $A\in\End_k(V)$ and let $\overline{k}$ be an algebraic closure of $k$. Extend scalars:
\[
\overline{V}=V\otimes_k\overline{k},
\qquad
\overline{A}=A\otimes1.
\]
Over $\overline{k}$, the characteristic polynomial of $A$ splits, so $\overline{A}$ admits an upper-triangular matrix in some basis. By <1>4,
\[
\chi_{\overline{A}}(\overline{A})=0.
\]
Scalar extension does not change the characteristic polynomial coefficients, so
\[
\chi_{\overline{A}}(t)=\chi_A(t)
\]
viewed in $\overline{k}[t]$. Thus
\[
\chi_A(A)\otimes1=0
\]
in $\End_{\overline{k}}(\overline{V})$. The natural map
\[
\End_k(V)\longrightarrow\End_{\overline{k}}(V\otimes_k\overline{k}),
\qquad T\longmapsto T\otimes1,
\]
is injective because $k\to\overline{k}$ is a field extension. Therefore $\chi_A(A)=0$ already over $k$.
:::
:::
