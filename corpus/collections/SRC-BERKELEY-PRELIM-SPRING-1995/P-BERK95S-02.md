---
schema: qual/card@1
id: P-BERK95S-02
kind: problem
title: Determine when $a^nA^n$ converges to a nonzero matrix
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
<1>1. The matrix $A$ has eigenvalues $0,1,3$, with respective
eigenvectors
$$
u_0=(1,1,1)^{\mathsf T},
\qquad
u_1=(1,0,-1)^{\mathsf T},
\qquad
u_3=(1,-2,1)^{\mathsf T}.
$$

::: {.proof}
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

<1>2. If $a^nA^n$ converges as a matrix, then both scalar sequences
$a^n$ and $(3a)^n$ converge.

::: {.proof}
By step <1>1,
$$
a^nA^n u_1=a^n u_1,
\qquad
a^nA^n u_3=(3a)^n u_3.
$$
Convergence of the matrices implies convergence of their values on
each fixed vector, hence of the two scalar sequences.
:::

<1>3. If $a^nA^n$ converges to a nonzero matrix, then
$$
a=\frac13.
$$

::: {.proof}
For a real number $c$, the sequence $c^n$ has a nonzero finite limit
only when $c=1$. If both $a^n$ and $(3a)^n$ converged to zero, then
step <1>1 would imply $a^nA^n\to0$ on a basis, hence as a matrix.
Therefore a nonzero matrix limit requires either
$$
a=1
\qquad\text{or}\qquad
3a=1.
$$
The first possibility is impossible because then
$(3a)^n=3^n$ does not converge. Hence $a=1/3$.
:::

<1>4. For $a=1/3$, the sequence $a^nA^n$ converges to a nonzero
matrix.

::: {.proof}
On the basis from step <1>1,
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

<1>5. The unique answer is
$$
\boxed{a=\frac13}.
$$

::: {.proof}
Step <1>3 proves necessity, and step <1>4 proves sufficiency.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the complete classification.
:::
:::
