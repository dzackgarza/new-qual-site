---
schema: qual/card@1
id: P-UCLAB12W-11
kind: problem
title: A quadratic annihilating polynomial for a $2\times2$ matrix
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked directly against Problem 11 of the retained UCLA Basic Examination, Winter 2012; the extraction garbled the displayed matrix, which the PDF gives as [[1,3],[4,2]].
---

::: {.problem}
(a) Find a polynomial $P(x)$ of degree $2$ such that $P(A)=0$ for
\[
A=\begin{pmatrix}1&3\\4&2\end{pmatrix}.
\]

(b) Prove that such a polynomial $P(x)$ is unique up to multiplication by a constant.
:::

::: {.solution}
<1>1. The characteristic polynomial of
$$
A=\begin{pmatrix}1&3\\4&2\end{pmatrix}
$$
is
$$
P(x)=x^2-3x-10.
$$

::: {.proof}
Directly,
$$
\begin{aligned}
\det(xI-A)
&=
\det\begin{pmatrix}x-1&-3\\-4&x-2\end{pmatrix}\\
&=(x-1)(x-2)-12\\
&=x^2-3x-10.
\end{aligned}
$$
:::

<1>2. The polynomial from step <1>1 annihilates $A$:
$$
\boxed{P(A)=A^2-3A-10I=0}.
$$

::: {.proof}
Compute
$$
A^2
=
\begin{pmatrix}1&3\\4&2\end{pmatrix}
\begin{pmatrix}1&3\\4&2\end{pmatrix}
=
\begin{pmatrix}13&9\\12&16\end{pmatrix}.
$$
Also
$$
3A+10I
=
\begin{pmatrix}3&9\\12&6\end{pmatrix}
+
\begin{pmatrix}10&0\\0&10\end{pmatrix}
=
\begin{pmatrix}13&9\\12&16\end{pmatrix}.
$$
Hence $A^2=3A+10I$, which is equivalent to $P(A)=0$.
:::

<1>3. No nonzero polynomial of degree at most $1$ annihilates $A$.

::: {.proof}
Suppose
$$
R(x)=rx+s
$$
satisfies $R(A)=0$. Then
$$
rA+sI=0.
$$
If $r\ne0$, this would give
$$
A=-\frac sr I,
$$
so $A$ would be a scalar matrix. But $A$ has nonzero off-diagonal entries $3$ and $4$, a contradiction. Thus $r=0$, and then $sI=0$ forces $s=0$. Therefore $R=0$.
:::

<1>4. Every degree-$2$ polynomial $Q$ satisfying $Q(A)=0$ is a nonzero scalar multiple of $P$.

::: {.proof}
Let
$$
Q(x)=cx^2+dx+e,
\qquad c\ne0,
$$
and suppose $Q(A)=0$. Since $P$ is monic of degree $2$, the polynomial
$$
R(x)=Q(x)-cP(x)
$$
has degree at most $1$. By step <1>2,
$$
R(A)=Q(A)-cP(A)=0.
$$
Step <1>3 therefore gives $R=0$. Hence
$$
Q=cP.
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>2 answers part (a), and step <1>4 proves the uniqueness up to multiplication by a nonzero constant required in part (b).
:::
:::
