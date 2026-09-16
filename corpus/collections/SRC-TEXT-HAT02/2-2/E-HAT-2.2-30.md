---
schema: qual/card@1
id: E-HAT-2.2-30
kind: problem
title: Homology of mapping tori via long exact sequence
classification:
  areas:
  - topology
  topics:
  - Homology
  - Mapping Torus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.2, Exercise 30; the stored statement matches the current Cornell text.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Complete Mayer--Vietoris/Wang-sequence calculation checked.
---

::: {.problem}
For the mapping torus $T_f$ of a map $f: X \to X$, we constructed in Example 2.48 a long exact sequence $\cdots \to H_n(X) \xrightarrow{1-f_*} H_n(X) \to H_n(T_f) \to H_{n-1}(X) \to \cdots$.
Use this to compute the homology of the mapping tori of the following maps:

(a) A reflection $S^2 \to S^2$.

(b) A map $S^2 \to S^2$ of degree 2.

(c) The map $S^1 \times S^1 \to S^1 \times S^1$ that is the identity on one factor and a reflection on the other.

(d) The map $S^1 \times S^1 \to S^1 \times S^1$ that is a reflection on each factor.

(e) The map $S^1 \times S^1 \to S^1 \times S^1$ that interchanges the two factors and then reflects one of the factors.
:::

::: {.solution}
For the mapping torus $T_f$, the Wang sequence yields short exact sequences
\[
0\to\operatorname{coker}(1-f_*:H_n(X)\to H_n(X))
\to H_n(T_f)
\to\ker(1-f_*:H_{n-1}(X)\to H_{n-1}(X))
\to0.
\]
In the cases below the kernel term is free, so each sequence splits as an abstract group.

<1>1. For a reflection $f:S^2\to S^2$,
\[
H_i(T_f)\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
\mathbb Z_2,&i=2,\\
0,&i\ge3.
\end{cases}
\]
::: {.proof}
On $H_2(S^2)=\mathbb Z$, a reflection acts by $-1$, so $1-f_*$ is multiplication by $2$. On $H_0$ it is zero. The displayed groups follow immediately from the short exact sequences.
:::

<1>2. If $f:S^2\to S^2$ has degree $2$, then
\[
H_i(T_f)\cong
\begin{cases}
\mathbb Z,&i=0,1,\\
0,&i\ge2.
\end{cases}
\]
::: {.proof}
On $H_2$, the map $1-f_*$ is multiplication by $-1$, hence an isomorphism. On $H_0$ it is zero. Thus there is no homology contribution in degrees $2$ or $3$, while the kernel in degree $0$ produces the usual $\mathbb Z$ in $H_1$.
:::

Let $T^2=S^1\times S^1$ and choose the standard basis of $H_1(T^2)=\mathbb Z^2$.

<1>3. If $f$ is the identity on the first factor and a reflection on the second, then
\[
H_i(T_f)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z^2\oplus\mathbb Z_2,&i=1,\\
\mathbb Z\oplus\mathbb Z_2,&i=2,\\
0,&i=3,\\
0,&i>3.
\end{cases}
\]
::: {.proof}
On $H_1$, $f_*=\operatorname{diag}(1,-1)$, so
\[
1-f_*=\operatorname{diag}(0,2).
\]
Its kernel is $\mathbb Z$ and its cokernel is $\mathbb Z\oplus\mathbb Z_2$. On $H_2(T^2)=\mathbb Z$, $f_*$ is multiplication by the determinant $-1$, so $1-f_*=2$. Hence
\[
H_2(T_f)\cong\mathbb Z_2\oplus\mathbb Z,
\]
while
\[
H_1(T_f)\cong(\mathbb Z\oplus\mathbb Z_2)\oplus\mathbb Z.
\]
There is no $H_3$ because multiplication by $2$ on $H_2$ has trivial kernel.
:::

<1>4. If $f$ reflects both factors, then
\[
H_i(T_f)\cong
\begin{cases}
\mathbb Z,&i=0,2,3,\\
\mathbb Z\oplus\mathbb Z_2\oplus\mathbb Z_2,&i=1,\\
0,&i>3.
\end{cases}
\]
::: {.proof}
On $H_1$, $f_*=-I$, so $1-f_*=2I$. Its kernel is zero and its cokernel is $(\mathbb Z_2)^2$. On $H_2$, $f_*$ is multiplication by $\det(-I)=+1$, so $1-f_*=0$. Thus $H_3\cong\mathbb Z$, $H_2\cong\mathbb Z$, and
\[
H_1\cong(\mathbb Z_2)^2\oplus\mathbb Z.
\]
:::

<1>5. If $f$ interchanges the two factors and then reflects one factor, then
\[
H_i(T_f)\cong
\begin{cases}
\mathbb Z,&i=0,2,3,\\
\mathbb Z\oplus\mathbb Z_2,&i=1,\\
0,&i>3.
\end{cases}
\]
::: {.proof}
Up to changing the basis, the induced map on $H_1$ has matrix
\[
A=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\]
Thus
\[
I-A=
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix}.
\]
This matrix has determinant $2$ and Smith normal form $\operatorname{diag}(1,2)$, so its kernel is zero and its cokernel is $\mathbb Z_2$. Since $\det A=1$, the induced map on $H_2$ is the identity, hence $1-f_*=0$ there. Therefore $H_3\cong\mathbb Z$, $H_2\cong\mathbb Z$, and
\[
H_1\cong\mathbb Z_2\oplus\mathbb Z.
\]
:::
:::
