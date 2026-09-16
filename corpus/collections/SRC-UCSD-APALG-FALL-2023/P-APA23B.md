---
schema: qual/card@1
id: P-APA23B
kind: problem
title: Hermitian–skew Hermitian splitting and eigenvalue bounds for real and imaginary parts
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
relations: []
review: draft
---

::: {.problem}
Throughout, $M_n$ denotes the set of $n \times n$ matrices with complex entries, and $\operatorname{eig}(A)$ denotes the set of eigenvalues of $A$ counting multiplicities.

(a) Prove that every $A \in M_n$ may be written uniquely as $A = S + iT$, where $S$ and $T$ are Hermitian.

(b) For any $A \in M_n$, consider the unique expansion $A = S + iT$, where $S$ and $T$ are Hermitian.
Prove that for any $\lambda \in \operatorname{eig}(A)$, it holds that
\[
\lambda_n(S) \le \operatorname{Re}(\lambda) \le \lambda_1(S)
\quad\text{and}\quad
\lambda_n(T) \le \operatorname{Im}(\lambda) \le \lambda_1(T),
\]
where $\lambda_1(C)$ and $\lambda_n(C)$ denote the largest and smallest eigenvalues of a Hermitian matrix $C \in M_n$.
:::

::: {.solution}
<1>1. Every matrix $A\in M_n$ has a decomposition
\[
A=S+iT
\]
with $S,T$ Hermitian, namely
\[
S=\frac{A+A^H}{2},
\qquad
T=\frac{A-A^H}{2i}.
\]
::: {.proof}
One has
\[
S^H=\frac{A^H+A}{2}=S
\]
and
\[
T^H=\frac{A^H-A}{-2i}=T,
\]
so both matrices are Hermitian. Also
\[
S+iT
=\frac{A+A^H}{2}+\frac{A-A^H}{2}=A.
\]
:::

<1>2. The decomposition in <1>1 is unique.
::: {.proof}
Suppose
\[
A=S_1+iT_1=S_2+iT_2
\]
with all four matrices Hermitian. Taking Hermitian adjoints gives
\[
A^H=S_1-iT_1=S_2-iT_2.
\]
Adding and subtracting the two displayed equations yields
\[
S_1=S_2=\frac{A+A^H}{2},
\qquad
T_1=T_2=\frac{A-A^H}{2i}.
\]
This proves part (a).
:::

<1>3. Let $Av=\lambda v$ with $v\ne0$. Then
\[
\operatorname{Re}\lambda=\frac{v^HSv}{v^Hv},
\qquad
\operatorname{Im}\lambda=\frac{v^HTv}{v^Hv}.
\]
::: {.proof}
Since $A=S+iT$,
\[
\lambda v^Hv=v^HAv=v^HSv+i\,v^HTv.
\]
Because $S$ and $T$ are Hermitian, both $v^HSv$ and $v^HTv$ are real. Taking real and imaginary parts and dividing by the positive scalar $v^Hv$ gives the formulas.
:::

<1>4. If $C$ is Hermitian with smallest and largest eigenvalues $\lambda_n(C)$ and $\lambda_1(C)$, then for every nonzero $v$,
\[
\lambda_n(C)\le \frac{v^HCv}{v^Hv}\le\lambda_1(C).
\]
::: {.proof}
Choose an orthonormal eigenbasis $u_1,\ldots,u_n$ of $C$ and write
\[
v=\sum_j c_j u_j,
\qquad
Cu_j=\mu_j u_j.
\]
Then
\[
\frac{v^HCv}{v^Hv}
=\frac{\sum_j\mu_j|c_j|^2}{\sum_j|c_j|^2},
\]
which is a convex combination of the real eigenvalues $\mu_j$. Hence it lies between the smallest and largest eigenvalues.
:::

<1>5. Therefore every eigenvalue $\lambda$ of $A$ satisfies
\[
\boxed{
\lambda_n(S)\le\operatorname{Re}\lambda\le\lambda_1(S),
\qquad
\lambda_n(T)\le\operatorname{Im}\lambda\le\lambda_1(T).}
\]
::: {.proof}
Apply <1>4 first to $C=S$ and then to $C=T$, and use the identities in <1>3. This proves part (b).
:::
:::
