---
schema: qual/card@1
id: P-UCLAB04S-10
kind: problem
title: Diagonalizability of a real symmetric matrix without the spectral theorem
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 10 of the official UCLA Basic Exam Spring 2004 PDF.
---

::: {.problem}
Let $T$ be a real symmetric matrix.
Show that $T$ is similar to a diagonal matrix.

You may not use the Spectral Theorem.
:::

::: {.solution}
Let $T\in M_n(\mathbb R)$ be symmetric. The proof is by induction on $n$.

<1>1. The matrix $T$ has a real eigenvalue and a nonzero real eigenvector.

::: {.proof}
Over $\mathbb C$, the characteristic polynomial of $T$ has a root $\lambda$ by the fundamental theorem of algebra. Choose a nonzero vector $z\in\mathbb C^n$ such that
\[
Tz=\lambda z.
\]
Because $T$ is real symmetric,
\[
\overline{z^*Tz}
=(Tz)^*z
=z^*T^tz
=z^*Tz,
\]
so $z^*Tz$ is real. On the other hand,
\[
z^*Tz=\lambda z^*z.
\]
Since $z^*z>0$, it follows that $\lambda\in\mathbb R$.

Write $z=x+iy$ with $x,y\in\mathbb R^n$. Since both $T$ and $\lambda$ are real,
\[
Tx=\lambda x,
\qquad
Ty=\lambda y.
\]
At least one of $x,y$ is nonzero, so $T$ has a nonzero real eigenvector.
:::

<1>2. If $v$ is a real eigenvector of $T$, then the orthogonal complement
\[
v^\perp
\]
is invariant under $T$.

::: {.proof}
Suppose
\[
Tv=\lambda v
\]
and let $w\in v^\perp$. Since $T^t=T$,
\[
\langle Tw,v\rangle
=
\langle w,Tv\rangle
=
\lambda\langle w,v\rangle
=0.
\]
Thus $Tw\in v^\perp$.
:::

<1>3. The restriction
\[
T|_{v^\perp}:v^\perp\to v^\perp
\]
is symmetric with respect to the Euclidean inner product.

::: {.proof}
By step <1>2 the restriction is well-defined. For $w_1,w_2\in v^\perp$,
\[
\langle T w_1,w_2\rangle
=
\langle w_1,T w_2\rangle
\]
because $T$ is symmetric on $\mathbb R^n$. Hence the restriction is symmetric.
:::

<1>4. For every $n\ge1$, every real symmetric $n\times n$ matrix has an orthonormal basis of real eigenvectors.

::: {.proof}
For $n=1$ the assertion is immediate.

Assume it holds in dimension $n-1$, and let $T\in M_n(\mathbb R)$ be symmetric. By step <1>1, choose a real eigenvector $v_1$ and normalize it so that $\|v_1\|=1$. Then $v_1^\perp$ has dimension $n-1$, and by steps <1>2--<1>3 the restriction of $T$ to $v_1^\perp$ is symmetric. By the induction hypothesis, $v_1^\perp$ has an orthonormal basis
\[
v_2,\ldots,v_n
\]
consisting of eigenvectors of the restriction, hence of $T$. Therefore
\[
v_1,\ldots,v_n
\]
is an orthonormal basis of $\mathbb R^n$ consisting of eigenvectors of $T$.
:::

<1>5. The matrix $T$ is similar to a diagonal matrix.

::: {.proof}
Let $v_1,\ldots,v_n$ be the basis from step <1>4, with
\[
Tv_i=\lambda_i v_i.
\]
Let $P$ be the matrix whose columns are $v_1,\ldots,v_n$. Then $P$ is orthogonal, hence invertible with
\[
P^{-1}=P^t.
\]
The matrix of $T$ in this eigenbasis is
\[
\boxed{P^{-1}TP=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)}.
\]
Thus $T$ is similar to a diagonal matrix.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 proves the required diagonalizability, and steps <1>1--<1>4 establish it without invoking the Spectral Theorem.
:::
:::
