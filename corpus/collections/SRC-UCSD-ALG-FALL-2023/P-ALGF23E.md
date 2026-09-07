---
schema: qual/card@1
id: P-ALGF23E
kind: problem
title: "Jordan form of a matrix with minimal polynomial t^p - 1 over C and F_p"
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 5 of the official UCSD Algebra Qualifying Exam, Fall 2023 source; the minimal-polynomial hypothesis and both field cases agree with the source.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Replaced the old list-format solution with the degree argument over C and the single-block argument from t^p - 1 = (t - 1)^p over F_p.
---

::: problem
Suppose $p$ is a prime number and the minimal polynomial of $a \in M_p(F)$ is $t^p - 1$.

(a) Find the Jordan form of $a$ if $F = \mathbb{C}$.
Justify your answer.

(b) Find the Jordan form of $a$ if $F = \mathbb{F}_p$.
Justify your answer.
:::

::: {.solution}
<1>1. Over $\mathbb C$, the polynomial $t^p-1$ has $p$ distinct roots.
::: {.proof}
Let
\[
\zeta_p=e^{2\pi i/p}.
\]
Then
\[
t^p-1=\prod_{k=0}^{p-1}(t-\zeta_p^k).
\]
The roots are distinct because the derivative
\[
pt^{p-1}
\]
does not vanish at any $p$-th root of unity in characteristic zero.
:::

<1>2. If $F=\mathbb C$, the characteristic polynomial of $a$ equals its minimal polynomial:
\[
\chi_a(t)=t^p-1.
\]
::: {.proof}
The minimal polynomial divides the characteristic polynomial.
By hypothesis its degree is $p$, while $a$ is a $p\times p$ matrix, so $\chi_a$ also has degree $p$.
Both polynomials are monic.
Therefore they are equal.
:::

<1>3. If $F=\mathbb C$, the Jordan form of $a$ is
\[
\operatorname{diag}(1,\zeta_p,\zeta_p^2,\ldots,\zeta_p^{p-1}),
\]
up to permutation of the diagonal entries.
::: {.proof}
By <1>1 and <1>2, the characteristic polynomial has the $p$ distinct eigenvalues
\[
1,\zeta_p,\ldots,\zeta_p^{p-1},
\]
each with algebraic multiplicity one.
Hence every Jordan block has size one, and each eigenvalue occurs exactly once.
This proves part (a).
:::

<1>4. Over $\mathbb F_p$ one has
\[
t^p-1=(t-1)^p.
\]
::: {.proof}
In characteristic $p$, all intermediate binomial coefficients
\[
\binom pk
\qquad(0<k<p)
\]
vanish.
Thus the binomial theorem gives
\[
(t-1)^p=t^p-1.
\]
:::

<1>5. If $F=\mathbb F_p$, the largest Jordan block of $a$ for the eigenvalue $1$ has size $p$.
::: {.proof}
By <1>4, the minimal polynomial is
\[
m_a(t)=(t-1)^p.
\]
For a matrix whose only eigenvalue is $1$, the exponent of $(t-1)$ in the minimal polynomial is the size of the largest Jordan block for that eigenvalue.
Hence a Jordan block of size $p$ occurs.
:::

<1>6. If $F=\mathbb F_p$, the Jordan form of $a$ is the single block
\[
J_p(1).
\]
::: {.proof}
The matrix $a$ acts on a vector space of dimension $p$.
By <1>5, one Jordan block already has size $p$, so it exhausts the entire dimension and no other block can occur.
Thus the Jordan form is
\[
J_p(1)=
\begin{pmatrix}
1&1&0&\cdots&0\\
0&1&1&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&1&1\\
0&\cdots&\cdots&0&1
\end{pmatrix}.
\]
This proves part (b).
:::
:::
