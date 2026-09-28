---
schema: qual/card@1
id: P-BKF88-4
kind: problem
title: Jordan form of an explicit six-by-six matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 in the deterministic MinerU Flash extraction assets/attachments/Fall88_extracted.md.
---

::: {.problem}
Find the Jordan canonical form of
\[
\begin{pmatrix}
1&0&0&0&0&0\\
1&1&0&0&0&0\\
1&0&1&0&0&0\\
1&0&0&1&0&0\\
1&0&0&0&1&0\\
1&1&1&1&1&1
\end{pmatrix}.
\]
:::

::: {.solution}
Let
$$
A=
\begin{pmatrix}
1&0&0&0&0&0\\
1&1&0&0&0&0\\
1&0&1&0&0&0\\
1&0&0&1&0&0\\
1&0&0&0&1&0\\
1&1&1&1&1&1
\end{pmatrix},
\qquad
N=A-I.
$$

<1>1. The only eigenvalue of $A$ is $1$, with algebraic multiplicity $6$.

::: {.proof}
The matrix $A$ is lower triangular and every diagonal entry is $1$. Hence
$$
\chi_A(t)=(t-1)^6.
$$
:::

<1>2. The nilpotent matrix $N=A-I$ has rank $2$.

::: {.proof}
Its columns are
$$
\begin{aligned}
Ne_1&=(0,1,1,1,1,1)^{\mathsf T},\\
Ne_2&=Ne_3=Ne_4=Ne_5=e_6,\\
Ne_6&=0.
\end{aligned}
$$
Thus
$$
\operatorname{im}N
=
\operatorname{span}\left\{
(0,1,1,1,1,1)^{\mathsf T},e_6
\right\},
$$
and the displayed vectors are linearly independent. Therefore
$$
\operatorname{rank}N=2.
$$
:::

<1>3. One has
$$
N^2\neq0
\qquad\text{and}\qquad
N^3=0.
$$

::: {.proof}
From step <1>2,
$$
N(0,1,1,1,1,1)^{\mathsf T}
=
4e_6,
\qquad
N(e_6)=0.
$$
Hence
$$
N^2e_1=4e_6,
$$
while $N^2e_j=0$ for $j=2,\ldots,6$. Thus $N^2\neq0$, but applying $N$ once more gives $N^3=0$.
:::

<1>4. The Jordan form of $A$ has exactly four Jordan blocks, and its largest block has size $3$.

::: {.proof}
For the eigenvalue $1$, the number of Jordan blocks is
$$
\dim\ker(A-I)
=
6-\operatorname{rank}N
=
4
$$
by step <1>2. Step <1>3 shows that the nilpotency index of $N$ is $3$, so the largest Jordan block for $A$ has size $3$.
:::

<1>5. Therefore the Jordan canonical form is
$$
\boxed{
J_3(1)\oplus(1)\oplus(1)\oplus(1)
}
$$
or explicitly
$$
\boxed{
\begin{pmatrix}
1&1&0&0&0&0\\
0&1&1&0&0&0\\
0&0&1&0&0&0\\
0&0&0&1&0&0\\
0&0&0&0&1&0\\
0&0&0&0&0&1
\end{pmatrix}.
}
$$

::: {.proof}
By step <1>4 there are four Jordan blocks whose sizes sum to $6$, and one block has size $3$. The remaining three positive block sizes therefore sum to $3$, so each is $1$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the Jordan canonical form.
:::
:::
