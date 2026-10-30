---
schema: qual/card@1
id: P-CHAVAN-CA-1-1
kind: problem
title: Maximum modulus for polynomials via a unitary dilation
classification: {areas: [complex-analysis], topics: [Maximum Modulus Principle]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
    note: Checked against Problem 1.1 in the deterministic MinerU Flash extraction; the standard-basis dimension is corrected to match the displayed (n+1)-by-(n+1) matrix.
---

::: {.problem}
Let
$$
p(z)=a_0+a_1z+\cdots+a_nz^n,
\qquad
s=\sqrt{1-\abs{z}^2},
\qquad \abs{z}\le1,
$$
and let $e_1,\ldots,e_{n+1}$ be the standard basis of $\CC^{n+1}$.

(a) Let $U$ be the $(n+1)\times(n+1)$ matrix whose columns, in order, are
$$
ze_1+se_2,\ e_3,\ldots,e_{n+1},\ se_1-\overline z e_2.
$$
Show that $U$ is unitary, hence its eigenvalues $\lambda_1,\ldots,\lambda_{n+1}$ have modulus $1$.

(b) For $0\le k\le n$, show that $z^k=e_1^TU^ke_1$, and hence $p(z)=e_1^Tp(U)e_1$.

(c) Choose $z$ so that $\abs{p(z)}=\max_{\abs{w}\le1}\abs{p(w)}$, and let $U$ be the matrix from part (a) for this $z$. Deduce
$$
\max_{\abs{w}\le1}\abs{p(w)}\le\norm{p(U)}.
$$

(d) If $D=\operatorname{diag}(\lambda_1,\ldots,\lambda_{n+1})$, show
$$
\norm{p(U)}=\norm{p(D)}=\max_i\abs{p(\lambda_i)}.
$$

Conclude that
$$
\max_{\abs{z}\le1}\abs{p(z)}=\max_{\abs{z}=1}\abs{p(z)}.
$$
:::

::: {.solution}

For $\abs{z}\le1$, write $s=\sqrt{1-\abs{z}^2}$ and denote the matrix in part (a) by $U_z$.
Let $\norm{\cdot}$ denote the operator norm induced by the Euclidean norm on $\CC^{n+1}$.

::: pf

::: {.pf-step #s1-1}

The matrix $U_z$ is unitary, and every eigenvalue of $U_z$ has modulus $1$.


::: pf-proof

The first and last columns of $U_z$ are
$$
c_1=ze_1+se_2,
\qquad
c_{n+1}=se_1-\overline z e_2.
$$
Since $s$ is real and $s^2=1-\abs{z}^2$,
$$
\norm{c_1}^2=\abs{z}^2+s^2=1,
\qquad
\norm{c_{n+1}}^2=s^2+\abs{z}^2=1,
$$
and
$$
\langle c_1,c_{n+1}\rangle
=\overline z\,s-s\overline z
=0.
$$
The remaining columns are $e_3,\ldots,e_{n+1}$, which are mutually
orthonormal and orthogonal to both $c_1$ and $c_{n+1}$. Thus the
columns of $U_z$ form an orthonormal basis of $\CC^{n+1}$, so
$U_z$ is unitary.

If $U_zv=\lambda v$ with $v\ne0$, then unitarity gives
$$
\norm{v}=\norm{U_zv}=\abs{\lambda}\,\norm{v},
$$
and hence $\abs{\lambda}=1$.

:::

:::

::: {.pf-step #s1-2}

For every integer $k$ with $0\le k\le n$,
$$
e_1^TU_z^ke_1=z^k.
$$


::: pf-proof

For $k=0$ the equality is $e_1^Te_1=1$. For $1\le k\le n$, the stronger identity
$$
U_z^ke_1
=z^ke_1+s\bigl(z^{k-1}e_2+z^{k-2}e_3+\cdots+ze_k+e_{k+1}\bigr)
$$
holds. It is true for $k=1$ because the first column of $U_z$ is
$ze_1+se_2$. If it holds for some $1\le k<n$, then
$U_ze_j=e_{j+1}$ for $2\le j\le n$, and therefore
$$
\begin{aligned}
U_z^{k+1}e_1
&=z^k(ze_1+se_2)
  +s\bigl(z^{k-1}e_3+z^{k-2}e_4+\cdots+ze_{k+1}+e_{k+2}\bigr)\\
&=z^{k+1}e_1
  +s\bigl(z^ke_2+z^{k-1}e_3+\cdots+ze_{k+1}+e_{k+2}\bigr).
\end{aligned}
$$
Thus the identity follows by induction. Taking the first coordinate
gives $e_1^TU_z^ke_1=z^k$.

:::

:::

::: {.pf-step #s1-3}

For every $\abs{z}\le1$,
$$
p(z)=e_1^Tp(U_z)e_1.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
\begin{aligned}
e_1^Tp(U_z)e_1
&=\sum_{k=0}^n a_k e_1^TU_z^ke_1\\
&=\sum_{k=0}^n a_k z^k\\
&=p(z).
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-4}

Let $z_0$ satisfy
$$
\abs{p(z_0)}=\max_{\abs{z}\le1}\abs{p(z)},
$$
and put $U=U_{z_0}$. Then
$$
\max_{\abs{z}\le1}\abs{p(z)}\le\norm{p(U)}.
$$


::: pf-proof

Such a point $z_0$ exists because $p$ is continuous on the compact
closed unit disk. Since the standard basis vector $e_1$ has real
coordinates, $e_1^T=e_1^*$, and step [](#s1-3){.pf-ref} gives
$$
\begin{aligned}
\max_{\abs{z}\le1}\abs{p(z)}
&=\abs{p(z_0)}\\
&=\abs{e_1^*p(U)e_1}\\
&\le \norm{e_1}\,\norm{p(U)e_1}\\
&\le \norm{p(U)}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

If $\lambda_1,\ldots,\lambda_{n+1}$ are the eigenvalues of $U$ and
$D=\operatorname{diag}(\lambda_1,\ldots,\lambda_{n+1})$, then
$$
\norm{p(U)}=\norm{p(D)}=\max_{1\le i\le n+1}\abs{p(\lambda_i)}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $U$ is unitary. The spectral theorem for unitary matrices
therefore gives a unitary matrix $V$ such that
$$
U=VDV^*.
$$
Polynomial functional calculus yields
$$
p(U)=Vp(D)V^*.
$$
The operator norm is invariant under multiplication by unitary
matrices, so $\norm{p(U)}=\norm{p(D)}$. Moreover,
$$
p(D)=\operatorname{diag}\bigl(p(\lambda_1),\ldots,p(\lambda_{n+1})\bigr).
$$
For a diagonal matrix, the Euclidean operator norm is the largest
absolute value of a diagonal entry: indeed, if
$M=\max_i\abs{p(\lambda_i)}$, then
$$
\norm{p(D)x}^2
=\sum_i\abs{p(\lambda_i)}^2\abs{x_i}^2
\le M^2\norm{x}^2,
$$
with equality for a standard basis vector corresponding to an index
where the maximum is attained. Hence
$$
\norm{p(D)}=\max_i\abs{p(\lambda_i)}.
$$

:::

:::

::: {.pf-step #s1-6}

The maximum modulus of $p$ on the closed unit disk is attained on the unit circle:
$$
\boxed{\max_{\abs{z}\le1}\abs{p(z)}=\max_{\abs{z}=1}\abs{p(z)}}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, every eigenvalue $\lambda_i$ of $U$ satisfies
$\abs{\lambda_i}=1$. Hence steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} give
$$
\max_{\abs{z}\le1}\abs{p(z)}
\le \max_i\abs{p(\lambda_i)}
\le \max_{\abs{z}=1}\abs{p(z)}.
$$
The reverse inequality is immediate because the unit circle is a
subset of the closed unit disk. Therefore the two maxima are equal.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} establish the four requested intermediate claims,
and step [](#s1-6){.pf-ref} gives the required conclusion.

:::

:::

:::
