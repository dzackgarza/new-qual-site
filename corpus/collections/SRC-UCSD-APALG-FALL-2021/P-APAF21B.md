---
schema: qual/card@1
id: P-APAF21B
kind: problem
title: Rayleigh quotient minimum; unique Hermitian splitting and eigenvalue real/imaginary bounds
classification:
  areas:
  - applied-algebra
  topics:
  - Hermitian Matrices
  - Norms
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
Assume that the eigenvalues of a Hermitian matrix $A\in M_n$ are arranged in the order
\[
\lambda_n(A)\le\cdots\le\lambda_2(A)\le\lambda_1(A).
\]

(a) Let $A\in M_n$ be Hermitian.
Prove that
\[
\lambda_n=\min_{x\neq 0}\frac{x^HAx}{x^Hx}.
\]

(b) Prove that every $A\in M_n$ may be written uniquely as $A=S+iT$, where $S$ and $T$ are Hermitian.

(c) For any $A\in M_n$, consider the unique expansion $A=S+iT$, where $S$ and $T$ are Hermitian.
Prove that for any $\lambda\in\operatorname{eig}(A)$, it holds that
\[
\lambda_n(S)\le\operatorname{Re}(\lambda)\le\lambda_1(S)
\quad\text{and}\quad
\lambda_n(T)\le\operatorname{Im}(\lambda)\le\lambda_1(T).
\]
:::

::: {.solution}
<1>1. If $A$ is Hermitian with eigenvalues
\[
\lambda_n\le\cdots\le\lambda_1,
\]
then for every nonzero $x$,
\[
\lambda_n\le \frac{x^HAx}{x^Hx}\le\lambda_1.
\]
::: {.proof}
By the spectral theorem there is an orthonormal eigenbasis $u_1,\ldots,u_n$ with
\[
Au_j=\lambda_j u_j.
\]
Write
\[
x=\sum_{j=1}^n c_j u_j.
\]
Then
\[
x^HAx=\sum_{j=1}^n \lambda_j|c_j|^2,
\qquad
x^Hx=\sum_{j=1}^n|c_j|^2.
\]
Hence the Rayleigh quotient is
\[
\frac{x^HAx}{x^Hx}
=\sum_{j=1}^n
\lambda_j\frac{|c_j|^2}{\sum_k|c_k|^2},
\]
a convex combination of the eigenvalues. It therefore lies between the smallest and largest eigenvalues.
:::

<1>2. The minimum of the Rayleigh quotient is
\[
\boxed{\lambda_n=\min_{x\ne0}\frac{x^HAx}{x^Hx}}.
\]
::: {.proof}
By <1>1 every Rayleigh quotient is at least $\lambda_n$. Taking $x=u_n$, an eigenvector for $\lambda_n$, gives
\[
\frac{u_n^HAu_n}{u_n^Hu_n}=\lambda_n.
\]
Thus the lower bound is attained and is the minimum.
:::

<1>3. Every matrix $A\in M_n$ has a decomposition
\[
A=S+iT
\]
with $S,T$ Hermitian, namely
\[
\boxed{S=\frac{A+A^H}{2},\qquad
T=\frac{A-A^H}{2i}}.
\]
::: {.proof}
One has
\[
S^H=\frac{A^H+A}{2}=S.
\]
Also
\[
T^H
=\left(\frac{A-A^H}{2i}\right)^H
=\frac{A^H-A}{-2i}
=T.
\]
Finally,
\[
S+iT
=\frac{A+A^H}{2}+\frac{A-A^H}{2}
=A.
\]
:::

<1>4. The decomposition in <1>3 is unique.
::: {.proof}
Suppose
\[
A=S_1+iT_1=S_2+iT_2
\]
with all $S_i,T_i$ Hermitian. Taking Hermitian adjoints gives
\[
A^H=S_1-iT_1=S_2-iT_2.
\]
Adding the two equations yields
\[
2S_1=A+A^H=2S_2,
\]
so $S_1=S_2$. Subtracting them yields
\[
2iT_1=A-A^H=2iT_2,
\]
so $T_1=T_2$.
:::

<1>5. Let $Av=\lambda v$ with $v\ne0$. If $A=S+iT$ is the decomposition from <1>3, then
\[
\operatorname{Re}\lambda
=\frac{v^HSv}{v^Hv},
\qquad
\operatorname{Im}\lambda
=\frac{v^HTv}{v^Hv}.
\]
::: {.proof}
From $Av=\lambda v$,
\[
\lambda
=\frac{v^HAv}{v^Hv}
=\frac{v^HSv}{v^Hv}
+i\frac{v^HTv}{v^Hv}.
\]
Because $S$ and $T$ are Hermitian, the two Rayleigh quotients on the right are real. Comparing real and imaginary parts gives the formulas.
:::

<1>6. Therefore every eigenvalue $\lambda$ of $A$ satisfies
\[
\boxed{\lambda_n(S)\le\operatorname{Re}\lambda\le\lambda_1(S)}
\]
and
\[
\boxed{\lambda_n(T)\le\operatorname{Im}\lambda\le\lambda_1(T)}.
\]
::: {.proof}
Apply the two-sided Rayleigh quotient bound from <1>1 first to the Hermitian matrix $S$ and the vector $v$, then to $T$ and $v$. Substitute the identities from <1>5.
:::
:::
