---
schema: qual/card@1
id: P-BKF87-5
kind: problem
title: Powers $A^{100}$ and $A^{-7}$ of a unipotent $2\times2$ matrix
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let
\[
A=\begin{pmatrix}
3/2&1/2\\
-1/2&1/2
\end{pmatrix}.
\]
Calculate $A^{100}$ and $A^{-7}$.
:::

::: {.solution}
Set
$$
N=A-I
=
\frac12
\begin{pmatrix}
1&1\\
-1&-1
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1}

One has
$$
N^2=0.
$$

::: pf-proof

Direct multiplication gives
$$
\begin{pmatrix}
1&1\\
-1&-1
\end{pmatrix}^2
=
\begin{pmatrix}
0&0\\
0&0
\end{pmatrix}.
$$
Hence $N^2=0$.

:::

:::

::: {.pf-step #s2}

For every integer $m$,
$$
A^m=I+mN.
$$

::: pf-proof

For $m\geq0$, the binomial theorem and step [](#s1){.pf-ref} give
$$
(I+N)^m=I+mN.
$$

Also,
$$
(I+N)(I-N)=I-N^2=I,
$$
so
$$
A^{-1}=I-N.
$$
If $m=-k<0$, then
$$
A^m=(I-N)^k.
$$
Again using $N^2=0$,
$$
(I-N)^k=I-kN=I+mN.
$$
Thus the formula holds for every integer $m$.

:::

:::

::: {.pf-step #s3}

One has
$$
\boxed{
A^{100}
=
\begin{pmatrix}
51&50\\
-50&-49
\end{pmatrix}
}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\begin{aligned}
A^{100}
&=
I+100N\\
&=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
+
50
\begin{pmatrix}
1&1\\
-1&-1
\end{pmatrix}\\
&=
\begin{pmatrix}
51&50\\
-50&-49
\end{pmatrix}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s4}

One has
$$
\boxed{
A^{-7}
=
\begin{pmatrix}
-5/2&-7/2\\
7/2&9/2
\end{pmatrix}
}.
$$

::: pf-proof

By step [](#s2){.pf-ref},
$$
\begin{aligned}
A^{-7}
&=
I-7N\\
&=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
-
\frac72
\begin{pmatrix}
1&1\\
-1&-1
\end{pmatrix}\\
&=
\begin{pmatrix}
-5/2&-7/2\\
7/2&9/2
\end{pmatrix}.
\end{aligned}
$$

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} are the requested calculations.

:::

:::

:::
