---
schema: qual/card@1
id: P-BERK95S-02
kind: problem
title: Real $a$ for which $a^nA^n$ converges to a nonzero matrix
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
  note: The retained PDF page confirms that A is a 3-by-3 matrix; the extraction garbled the size.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let
\[
A=\begin{pmatrix}
1&-1&0\\
-1&2&-1\\
0&-1&1
\end{pmatrix}.
\]
Determine all real numbers $a$ for which
\[
\lim_{n\to\infty}a^nA^n
\]
exists and is nonzero as a matrix.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The matrix $A$ has eigenvalues $0,1,3$, with respective
eigenvectors
$$
u_0=(1,1,1)^{\mathsf T},
\qquad
u_1=(1,0,-1)^{\mathsf T},
\qquad
u_3=(1,-2,1)^{\mathsf T}.
$$

::: pf-proof

Direct multiplication gives
$$
Au_0=0,
\qquad
Au_1=u_1,
\qquad
Au_3=3u_3.
$$
The three vectors are nonzero and mutually orthogonal, so they form a
basis of $\RR^3$.

:::

:::

::: pf-step

If $a^nA^n$ converges as a matrix, then both scalar sequences
$a^n$ and $(3a)^n$ converge.

::: pf-proof

By step [](#s1){.pf-ref},
$$
a^nA^n u_1=a^n u_1,
\qquad
a^nA^n u_3=(3a)^n u_3.
$$
Convergence of the matrices implies convergence of their values on
each fixed vector, hence of the two scalar sequences.

:::

:::

::: {.pf-step #s3}

If $a^nA^n$ converges to a nonzero matrix, then
$$
a=\frac13.
$$

::: pf-proof

For a real number $c$, the sequence $c^n$ has a nonzero finite limit
only when $c=1$. If both $a^n$ and $(3a)^n$ converged to zero, then
step [](#s1){.pf-ref} would imply $a^nA^n\to0$ on a basis, hence as a matrix.
Therefore a nonzero matrix limit requires either
$$
a=1
\qquad\text{or}\qquad
3a=1.
$$
The first possibility is impossible because then
$(3a)^n=3^n$ does not converge. Hence $a=1/3$.

:::

:::

::: {.pf-step #s4}

For $a=1/3$, the sequence $a^nA^n$ converges to a nonzero
matrix.

::: pf-proof

On the basis from step [](#s1){.pf-ref},
$$
\left(\frac A3\right)^n u_0=0,
\qquad
\left(\frac A3\right)^n u_1=3^{-n}u_1\longrightarrow0,
\qquad
\left(\frac A3\right)^n u_3=u_3.
$$
Thus $(A/3)^n$ converges to the projection onto
$\RR u_3$ along $\RR u_0\oplus\RR u_1$. This projection is nonzero.

:::

:::

::: {.pf-step #s5}

The unique answer is
$$
\boxed{a=\frac13}.
$$

::: pf-proof

Step [](#s3){.pf-ref} proves necessity, and step [](#s4){.pf-ref} proves sufficiency.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} gives the complete classification.

:::

:::

:::
