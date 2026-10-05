---
schema: qual/card@1
id: P-UCLAB16F-02
kind: problem
title: Operator norm of $e^A$ for a $2\times2$ Jordan block
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 2 of the retained UCLA Basic Examination Fall 2016 PDF.
---

::: {.problem}
Suppose

$$
A = \left[ { \begin{array} { r r } { 2 } & { 1 } \\ { 0 } & { 2 } \end{array} } \right] .
$$

Find the smallest possible constant $C > 0$ so that

$$
\| e ^ { A } x \| \leq C \| x \|
$$

for all $x \in \mathbb { R } ^ { 2 }$ . Here $\| z \|$ denotes the usual (Pythagorean/Euclidean) length of the vector $z \in \mathbb { R } ^ { 2 }$ .
:::

::: {.solution}
Write
\[
A=2I+N,
\qquad
N=
\begin{pmatrix}
0&1\\
0&0
\end{pmatrix}.
\]

<1>1. One has
\[
\boxed{
e^A
=
e^2
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
}.
\]

::: {.proof}
Since $2I$ commutes with $N$,
\[
e^A=e^{2I}e^N.
\]
Also
\[
N^2=0,
\]
so
\[
e^N=I+N
=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]
Finally,
\[
e^{2I}=e^2I.
\]
:::

<1>2. Let
\[
M=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}.
\]
Then the optimal constant is
\[
C=e^2\|M\|_{\mathrm{op}}.
\]

::: {.proof}
By step <1>1,
\[
\|e^Ax\|
=
e^2\|Mx\|.
\]
The least constant $C$ satisfying
\[
\|e^Ax\|\le C\|x\|
\]
for every $x$ is therefore $e^2$ times the Euclidean operator norm of $M$.
:::

<1>3. One has
\[
M^TM
=
\begin{pmatrix}
1&1\\
1&2
\end{pmatrix}.
\]

::: {.proof}
Direct multiplication gives
\[
\begin{pmatrix}
1&0\\
1&1
\end{pmatrix}
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
=
\begin{pmatrix}
1&1\\
1&2
\end{pmatrix}.
\]
:::

<1>4. The eigenvalues of $M^TM$ are
\[
\lambda_\pm
=
\frac{3\pm\sqrt5}{2}.
\]

::: {.proof}
The characteristic polynomial is
\[
\det
\begin{pmatrix}
1-\lambda&1\\
1&2-\lambda
\end{pmatrix}
=
(1-\lambda)(2-\lambda)-1
=
\lambda^2-3\lambda+1.
\]
Its roots are
\[
\frac{3\pm\sqrt5}{2}.
\]
:::

<1>5. The Euclidean operator norm of $M$ is
\[
\boxed{
\|M\|_{\mathrm{op}}
=
\sqrt{\frac{3+\sqrt5}{2}}
=
\frac{1+\sqrt5}{2}
}.
\]

::: {.proof}
For any real matrix $M$,
\[
\|M\|_{\mathrm{op}}^2
\]
is the largest eigenvalue of the symmetric positive-semidefinite matrix
\[
M^TM.
\]
By step <1>4, that largest eigenvalue is
\[
\frac{3+\sqrt5}{2}.
\]
Thus
\[
\|M\|_{\mathrm{op}}
=
\sqrt{\frac{3+\sqrt5}{2}}.
\]
Since
\[
\left(\frac{1+\sqrt5}{2}\right)^2
=
\frac{3+\sqrt5}{2},
\]
the second expression follows.
:::

<1>6. Therefore the smallest possible constant is
\[
\boxed{
C
=
e^2\frac{1+\sqrt5}{2}
}.
\]

::: {.proof}
Combine steps <1>2 and <1>5.
The operator norm is attained on a unit eigenvector of $M^TM$ for its largest eigenvalue, so no smaller constant can work.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required optimal constant.
:::
:::
