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

Let $T\in M_n(\RR)$ be symmetric. The proof is by induction on $n$.

::: pf

::: {.pf-step #s1-1}

The matrix $T$ has a real eigenvalue and a nonzero real eigenvector.


::: pf-proof

Over $\CC$, the characteristic polynomial of $T$ has a root $\lambda$ by the fundamental theorem of algebra. Choose a nonzero vector $z\in\CC^n$ such that
$$
Tz=\lambda z.
$$
Because $T$ is real symmetric,
$$
\overline{z^*Tz}
=(Tz)^*z
=z^*T^tz
=z^*Tz,
$$
so $z^*Tz$ is real. On the other hand,
$$
z^*Tz=\lambda z^*z.
$$
Since $z^*z>0$, it follows that $\lambda\in\RR$.

Write $z=x+iy$ with $x,y\in\RR^n$. Since both $T$ and $\lambda$ are real,
$$
Tx=\lambda x,
\qquad
Ty=\lambda y.
$$
At least one of $x,y$ is nonzero, so $T$ has a nonzero real eigenvector.

:::

:::

::: {.pf-step #s1-2}

If $v$ is a real eigenvector of $T$, then the orthogonal complement
$$
v^\perp
$$
is invariant under $T$.


::: pf-proof

Suppose
$$
Tv=\lambda v
$$
and let $w\in v^\perp$. Since $T^t=T$,
$$
\langle Tw,v\rangle
=
\langle w,Tv\rangle
=
\lambda\langle w,v\rangle
=0.
$$
Thus $Tw\in v^\perp$.

:::

:::

::: {.pf-step #s1-3}

The restriction
$$
T|_{v^\perp}:v^\perp\to v^\perp
$$
is symmetric with respect to the Euclidean inner product.


::: pf-proof

By step [](#s1-2){.pf-ref} the restriction is well-defined. For $w_1,w_2\in v^\perp$,
$$
\langle T w_1,w_2\rangle
=
\langle w_1,T w_2\rangle
$$
because $T$ is symmetric on $\RR^n$. Hence the restriction is symmetric.

:::

:::

::: {.pf-step #s1-4}

For every $n\ge1$, every real symmetric $n\times n$ matrix has an orthonormal basis of real eigenvectors.


::: pf-proof

For $n=1$ the assertion is immediate.

Assume it holds in dimension $n-1$, and let $T\in M_n(\RR)$ be symmetric. By step [](#s1-1){.pf-ref}, choose a real eigenvector $v_1$ and normalize it so that $\|v_1\|=1$. Then $v_1^\perp$ has dimension $n-1$, and by steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} the restriction of $T$ to $v_1^\perp$ is symmetric. By the induction hypothesis, $v_1^\perp$ has an orthonormal basis
$$
v_2,\ldots,v_n
$$
consisting of eigenvectors of the restriction, hence of $T$. Therefore
$$
v_1,\ldots,v_n
$$
is an orthonormal basis of $\RR^n$ consisting of eigenvectors of $T$.

:::

:::

::: {.pf-step #s1-5}

The matrix $T$ is similar to a diagonal matrix.


::: pf-proof

Let $v_1,\ldots,v_n$ be the basis from step [](#s1-4){.pf-ref}, with
$$
Tv_i=\lambda_i v_i.
$$
Let $P$ be the matrix whose columns are $v_1,\ldots,v_n$. Then $P$ is orthogonal, hence invertible with
$$
P^{-1}=P^t.
$$
The matrix of $T$ in this eigenbasis is
$$
\boxed{P^{-1}TP=\operatorname{diag}(\lambda_1,\ldots,\lambda_n)}.
$$
Thus $T$ is similar to a diagonal matrix.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the required diagonalizability, and steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} establish it without invoking the Spectral Theorem.

:::

:::

:::
