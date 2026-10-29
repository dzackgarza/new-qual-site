---
schema: qual/card@1
id: P-HM21B18-FIN-07
kind: problem
title: Eigenstructure and dynamics of the Arnold cat map
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Part (e) asks the student to choose among source images of a transformed Garfield picture; those candidate images are not recovered in the extraction.
---

::: {.problem}
For the Arnold cat map $T(v)=Av$ with
$$
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},
$$

(a) find the characteristic polynomial;

(b) find the eigenvalues and eigenvectors;

(c) decide whether the discrete dynamical system is asymptotically stable;

(d) find an orthogonal matrix $S$ and diagonal matrix $B$ with $B=S^{-1}AS$;

(e) choose which source picture A--D is the image of the displayed upright
Garfield figure under $T$. In the source, candidate A is flattened
horizontally, candidate B is strongly elongated along a line of positive
slope, candidate C is elongated along the opposite diagonal direction, and
candidate D has a broader opposite shear.
:::

::: {.solution}

Set
$$
\lambda_\pm=\frac{3\pm\sqrt5}{2},
\qquad
\alpha=\frac{\sqrt5-1}{2},
\qquad
\beta=\frac{\sqrt5+1}{2}.
$$

::: pf

::: {.pf-step #s1-1}

The characteristic polynomial is
$$
\chi_A(\lambda)=\lambda^2-3\lambda+1.
$$


::: pf-proof

One has
$$
\det(\lambda I-A)
=
\det
\begin{pmatrix}
\lambda-2&-1\\
-1&\lambda-1
\end{pmatrix}
=(\lambda-2)(\lambda-1)-1
=\lambda^2-3\lambda+1.
$$

:::

:::

::: {.pf-step #s1-2}

The eigenvalues are $\lambda_+$ and $\lambda_-$, with respective
eigenvectors
$$
u_+=\begin{pmatrix}1\\\alpha\end{pmatrix},
\qquad
u_-=\begin{pmatrix}-1\\\beta\end{pmatrix}.
$$


::: pf-proof

Solving the quadratic in step [](#s1-1){.pf-ref} gives
$\lambda_\pm=(3\pm\sqrt5)/2$. Directly,
$$
Au_+
=
\begin{pmatrix}2+\alpha\\1+\alpha\end{pmatrix}
=\lambda_+
\begin{pmatrix}1\\\alpha\end{pmatrix},
$$
because $2+\alpha=\lambda_+$ and $1+\alpha=\lambda_+\alpha$. Likewise,
$$
Au_-
=
\begin{pmatrix}-2+\beta\\-1+\beta\end{pmatrix}
=\lambda_-
\begin{pmatrix}-1\\\beta\end{pmatrix}.
$$
Thus the displayed vectors are eigenvectors for the stated eigenvalues.

:::

:::

::: {.pf-step #s1-3}

The discrete system $x(t+1)=Ax(t)$ is not asymptotically stable.


::: pf-proof

Since
$$
\lambda_+=\frac{3+\sqrt5}{2}>1,
$$
the trajectory starting at $u_+$ is
$$
x(t)=A^tu_+=\lambda_+^t u_+,
$$
which does not tend to $0$. Hence the origin is not asymptotically
stable.

:::

:::

::: {.pf-step #s1-4}

The eigenvectors $u_+$ and $u_-$ are orthogonal.


::: pf-proof

Their dot product is
$$
u_+\cdot u_-
=-1+\alpha\beta
=-1+\frac{(\sqrt5-1)(\sqrt5+1)}4
=0.
$$

:::

:::

::: {.pf-step #s1-5}

Define
$$
n_+=\sqrt{\frac{5-\sqrt5}{2}},
\qquad
n_-=\sqrt{\frac{5+\sqrt5}{2}},
$$
and
$$
S=
\begin{pmatrix}
1/n_+&-1/n_-\\
\alpha/n_+&\beta/n_-
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
\lambda_+&0\\
0&\lambda_-
\end{pmatrix}.
$$
Then $S$ is orthogonal and $B=S^{-1}AS$.


::: pf-proof

One computes
$$
\|u_+\|^2=1+\alpha^2=\frac{5-\sqrt5}{2}=n_+^2,
\qquad
\|u_-\|^2=1+\beta^2=\frac{5+\sqrt5}{2}=n_-^2.
$$
By step [](#s1-4){.pf-ref}, the columns of $S$ form an orthonormal basis, so
$S^{-1}=S^T$. Step [](#s1-2){.pf-ref} says that these columns are eigenvectors with
eigenvalues $\lambda_+,\lambda_-$, hence
$$
AS=SB.
$$
Multiplying on the left by $S^{-1}$ gives $S^{-1}AS=B$.

:::

:::

::: {.pf-step #s1-6}

In part (e), the transformed picture is candidate B.


::: pf-proof

The eigendirection $u_+=(1,\alpha)^T$ has positive slope
$\alpha>0$ and is expanded by the factor $\lambda_+>1$. The perpendicular
eigendirection $u_-$ is contracted by
$0<\lambda_-<1$. Therefore the image of a generic figure is strongly
elongated along the positive-slope direction $u_+$. Among the source
candidates, this is precisely picture B.

:::

:::

::: {.pf-step #s1-7}

The requested answers are
$$
\boxed{
\begin{gathered}
\chi_A(\lambda)=\lambda^2-3\lambda+1,\qquad
\lambda_\pm=\frac{3\pm\sqrt5}{2},\\
u_+=(1,\alpha)^T,\quad u_-=(-1,\beta)^T,\qquad
\text{the system is not asymptotically stable},\\
B=S^{-1}AS\text{ for the }S,B\text{ of step [](#s1-5){.pf-ref}},\qquad
\text{picture B in part (e).}
\end{gathered}}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-6){.pf-ref} establish parts (a)--(e), respectively, with step [](#s1-5){.pf-ref}
providing the requested orthogonal diagonalization.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} records all requested outputs.

:::

:::

:::
