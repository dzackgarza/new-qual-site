---
schema: qual/card@1
id: P-BKS05-8A
kind: problem
title: Eigenvalues of a product of positive definite Hermitian matrices are positive
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked the retained quadratic-form proof: for CDx=lambda x,
    positivity of C at Dx gives a positive real number equal to
    lambda times the positive real number x^*Dx.
---

::: {.problem}
Let $C$ and $D$ be two $n\times n$ positive definite Hermitian matrices over $\CC$ and let $A=CD$. Prove that all eigenvalues of $A$ are positive real numbers.
:::

::: {.solution}
<1>1. Let $\lambda$ be an eigenvalue of $A=CD$, and choose a nonzero
eigenvector $x$ such that
$$
CDx=\lambda x.
$$
Then $Dx\neq0$.

::: {.proof}
Since $D$ is positive definite, its kernel is zero: if $Dv=0$, then
$$
v^*Dv=0,
$$
which is impossible for nonzero $v$. Thus $D$ is invertible. Since
$x\neq0$, one has $Dx\neq0$.
:::

<1>2. One has
$$
(Dx)^*C(Dx)
=
\lambda x^*Dx.
$$

::: {.proof}
Using $CDx=\lambda x$ and the fact that $D$ is Hermitian,
$$
\begin{aligned}
(Dx)^*C(Dx)
&=(Dx)^*(CDx)\\
&=(Dx)^*(\lambda x)\\
&=\lambda x^*D^*x\\
&=\lambda x^*Dx.
\end{aligned}
$$
:::

<1>3. The eigenvalue $\lambda$ is a positive real number.

::: {.proof}
By step <1>1 and positive definiteness of $C$,
$$
(Dx)^*C(Dx)>0.
$$
Positive definiteness of $D$ also gives
$$
x^*Dx>0.
$$
Both quantities are positive real numbers. Hence step <1>2 yields
$$
\lambda
=
\frac{(Dx)^*C(Dx)}{x^*Dx}
>0.
$$
Thus $\lambda\in\RR_{>0}$.
:::

<1>4. Every eigenvalue of $A$ is positive real.

::: {.proof}
The choice of eigenvalue $\lambda$ in step <1>1 was arbitrary, so
step <1>3 applies to every eigenvalue.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
