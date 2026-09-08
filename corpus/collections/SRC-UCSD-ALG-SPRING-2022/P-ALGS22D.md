---
schema: qual/card@1
id: P-ALGS22D
kind: problem
title: 'Diagonalizability of $2\times2$ matrices satisfying $A^m=I$'
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-08
- event: solution-written
  by: OpenAI
  date: 2026-09-08
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-08
---

::: problem
Let $F$ be an algebraically closed field.
For which $m \geq 1$ is it true that every matrix $A \in M_2(F)$ such that $A^m = I$ is diagonalizable?
(The answer may depend on the characteristic of $F$.)
:::


::: {.solution}
<1>1. If \(\operatorname{char}F=0\), or more generally if \(\operatorname{char}F=p>0\) with \(p\nmid m\), then every \(A\in M_2(F)\) satisfying \(A^m=I\) is diagonalizable.
::: {.proof}
The minimal polynomial \(\mu_A(t)\) divides \(t^m-1\). Its derivative is \(mt^{m-1}\), which is nonzero under the stated hypothesis, and
\[
\gcd(t^m-1,mt^{m-1})=1.
\]
Thus \(t^m-1\) has no repeated roots. Since \(F\) is algebraically closed, \(\mu_A\) splits into distinct linear factors, so \(A\) is diagonalizable.
:::

<1>2. Suppose \(\operatorname{char}F=p>0\) and \(p\mid m\). Then the assertion fails.
::: {.proof}
Let
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad A=I+N.
\]
Then \(N^2=0\), so the binomial theorem gives
\[
A^m=(I+N)^m=I+mN=I
\]
because \(m=0\) in characteristic \(p\). But \(A\) is not diagonalizable: its only eigenvalue is \(1\), while \(A\neq I\), equivalently its minimal polynomial is \((t-1)^2\).
:::

<1>3. Therefore every \(2\times2\) matrix \(A\) with \(A^m=I\) is diagonalizable exactly when the characteristic of \(F\) does not divide \(m\).
::: {.proof}
Combine <1>1 and <1>2. In characteristic zero, no positive integer \(m\) is divisible by the characteristic, so every \(m\ge1\) works.
:::
:::
