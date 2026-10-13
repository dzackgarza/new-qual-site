---
schema: qual/card@1
id: P-UCLAB06S-08
kind: problem
title: Orthogonal maps of $\mathbb R^{2n+1}$ have an eigenvalue $\pm1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 8 of the retained UCLA Basic Examination Spring 2006 PDF.
---

::: {.problem}
A linear transformation T is called orthogonal if it is nonsingular and ${ } ^ { t } T = T ^ { - 1 }$ . Prove that if $T : { \mathbf { R } } ^ { 2 n + 1 } \to { \mathbf { R } } ^ { 2 n + 1 }$ is orthogonal, then there exists a vector $\boldsymbol { v } \in \mathbf { R } ^ { 2 n + 1 }$ such that $T v = \pm v$
:::

::: {.solution}
<1>1. The characteristic polynomial
\[
\chi_T(\lambda)=\det(\lambda I-T)
\]
has a real root.

::: {.proof}
The matrix $T$ has size $(2n+1)\times(2n+1)$, so $\chi_T$ is a real polynomial of odd degree $2n+1$ with leading coefficient $1$.
Hence $\chi_T(\lambda)\to+\infty$ as $\lambda\to+\infty$ and $\chi_T(\lambda)\to-\infty$ as $\lambda\to-\infty$.
By the intermediate value theorem, there exists $\lambda_0\in\mathbb R$ such that
\[
\chi_T(\lambda_0)=0.
\]
:::

<1>2. There exists a nonzero real vector $v$ such that
\[
Tv=\lambda_0v.
\]

::: {.proof}
Since
\[
\det(\lambda_0I-T)=0,
\]
the real matrix $\lambda_0I-T$ is singular.
Therefore its kernel contains a nonzero real vector $v$.
For such a vector,
\[
(\lambda_0I-T)v=0,
\]
so
\[
Tv=\lambda_0v.
\]
:::

<1>3. The orthogonality relation implies
\[
\|Tx\|_2=\|x\|_2
\]
for every $x\in\mathbb R^{2n+1}$.

::: {.proof}
From
\[
T^t=T^{-1},
\]
one gets
\[
T^tT=I.
\]
Hence
\[
\|Tx\|_2^2
=(Tx)^t(Tx)
=
x^tT^tTx
=
x^tx
=
\|x\|_2^2.
\]
Taking square roots gives the claim.
:::

<1>4. The real eigenvalue $\lambda_0$ satisfies
\[
|\lambda_0|=1.
\]

::: {.proof}
By step <1>2,
\[
Tv=\lambda_0v
\]
for some nonzero $v$.
Using step <1>3,
\[
\|v\|_2
=
\|Tv\|_2
=
\|\lambda_0v\|_2
=
|\lambda_0|\|v\|_2.
\]
Since $\|v\|_2>0$, division gives $|\lambda_0|=1$.
:::

<1>5. Since $\lambda_0$ is real,
\[
\lambda_0=\pm1.
\]

::: {.proof}
The only real numbers with absolute value $1$ are $1$ and $-1$.
:::

<1>6. Therefore there exists a nonzero vector
\[
v\in\mathbb R^{2n+1}
\]
such that
\[
\boxed{Tv=\pm v}.
\]

::: {.proof}
Combine steps <1>2 and <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
