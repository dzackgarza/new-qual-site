---
schema: qual/card@1
id: P-UCLAB09F-12
kind: problem
title: Spectrum and diagonalizability of a cyclic basis shift
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
Let $V$ be an $n$-dimensional complex vector space, $n\ge2$, with basis $e_1,\ldots,e_n$.
Let $T\colon V\to V$ satisfy
\[
T(e_1)=e_2,\quad \ldots,\quad T(e_{n-1})=e_n,\quad T(e_n)=e_1.
\]

<1>1. Show that $1$ is an eigenvalue of $T$, write down an eigenvector with eigenvalue $1$, and prove that it is unique up to scaling.

<1>2. Is $T$ diagonalizable?
Hint: compute its characteristic polynomial.
:::

::: {.solution}
<1>1. The vector
\[
v_1=e_1+\cdots+e_n
\]
is an eigenvector of $T$ with eigenvalue $1$.

::: {.proof}
Using the cyclic-shift definition of $T$,
\[
\begin{aligned}
T(v_1)
&=
T(e_1)+\cdots+T(e_n)\\
&=
e_2+\cdots+e_n+e_1\\
&=
v_1.
\end{aligned}
\]
Since $v_1\ne0$, it is an eigenvector with eigenvalue $1$.
:::

<1>2. The eigenspace for eigenvalue $1$ is one-dimensional:
\[
\boxed{E_1=\operatorname{span}\{e_1+\cdots+e_n\}}.
\]

::: {.proof}
Let
\[
v=c_1e_1+\cdots+c_ne_n
\]
satisfy
\[
Tv=v.
\]
Then
\[
Tv
=
c_ne_1+c_1e_2+\cdots+c_{n-1}e_n.
\]
Comparing coefficients with
\[
v=c_1e_1+\cdots+c_ne_n
\]
gives
\[
c_n=c_1,\quad
c_1=c_2,\quad
\ldots,\quad
c_{n-1}=c_n.
\]
Hence
\[
c_1=\cdots=c_n,
\]
so $v$ is a scalar multiple of $e_1+\cdots+e_n$.
:::

<1>3. Let $\lambda\in\mathbb C$ satisfy
\[
\lambda^n=1.
\]
Then
\[
v_\lambda
=
e_1+\lambda^{-1}e_2+\lambda^{-2}e_3+\cdots+\lambda^{-(n-1)}e_n
\]
is a nonzero eigenvector of $T$ with eigenvalue $\lambda$.

::: {.proof}
Applying $T$ gives
\[
\begin{aligned}
Tv_\lambda
&=
\lambda^{-(n-1)}e_1
+
e_2
+
\lambda^{-1}e_3
+
\cdots
+
\lambda^{-(n-2)}e_n.
\end{aligned}
\]
Since $\lambda^n=1$,
\[
\lambda^{-(n-1)}=\lambda.
\]
Therefore
\[
\begin{aligned}
Tv_\lambda
&=
\lambda e_1
+
e_2
+
\lambda^{-1}e_3
+
\cdots
+
\lambda^{-(n-2)}e_n\\
&=
\lambda
\left(
e_1+\lambda^{-1}e_2+\cdots+\lambda^{-(n-1)}e_n
\right)\\
&=
\lambda v_\lambda.
\end{aligned}
\]
The coefficient of $e_1$ is $1$, so $v_\lambda\ne0$.
:::

<1>4. The characteristic polynomial of $T$ is
\[
\boxed{\chi_T(t)=t^n-1}.
\]

::: {.proof}
Over $\mathbb C$, the polynomial
\[
t^n-1
\]
has exactly $n$ distinct roots
\[
\lambda_1,\ldots,\lambda_n,
\]
because its derivative is
\[
nt^{n-1},
\]
which has no common root with $t^n-1$.

By step <1>3, every $\lambda_j$ is an eigenvalue of $T$, hence a root of the characteristic polynomial $\chi_T$. The characteristic polynomial is monic of degree $n$. Therefore it is the unique monic degree-$n$ polynomial with these $n$ roots:
\[
\chi_T(t)
=
\prod_{j=1}^n(t-\lambda_j)
=
t^n-1.
\]
:::

<1>5. The operator $T$ is diagonalizable over $\mathbb C$.

::: {.proof}
By step <1>4, $T$ has the $n$ distinct eigenvalues given by the $n$th roots of unity. Eigenvectors belonging to distinct eigenvalues are linearly independent. Hence the corresponding vectors
\[
v_{\lambda_1},\ldots,v_{\lambda_n}
\]
from step <1>3 are $n$ linearly independent vectors in the $n$-dimensional space $V$. They form a basis consisting of eigenvectors of $T$. Thus
\[
\boxed{T\text{ is diagonalizable}}.
\]
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove part <1>1, while steps <1>3--<1>5 compute the characteristic polynomial and prove diagonalizability in part <1>2.
:::
:::
