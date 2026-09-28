---
schema: qual/card@1
id: P-BKF11-8B
kind: problem
title: The power $A^{100}$ of a $2\times2$ matrix with a repeated eigenvalue
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 8B of the retained Berkeley Fall 2011 preliminary-exam solution packet f11solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the decomposition A=I+N, the nilpotence N^2=0, and the resulting
    truncated binomial expansion for A^100.
---

::: {.problem}
Compute $A^{100}$, where
$$
A=\begin{pmatrix}
\frac32&\frac12\\
-\frac12&\frac12
\end{pmatrix}.
$$
:::

::: {.solution}
<1>1. One has
$$
A=I+N,
\qquad
N=
\begin{pmatrix}
\frac12&\frac12\\
-\frac12&-\frac12
\end{pmatrix},
$$
and $N^2=0$.

::: {.proof}
Subtracting the identity matrix from $A$ gives the displayed $N$.
Direct multiplication gives
$$
N^2=
\begin{pmatrix}
\frac14-\frac14&\frac14-\frac14\\
-\frac14+\frac14&-\frac14+\frac14
\end{pmatrix}
=0.
$$
:::

<1>2. For every integer $m\ge0$,
$$
A^m=I+mN.
$$

::: {.proof}
Since $I$ and $N$ commute, the binomial theorem gives
$$
(I+N)^m
=\sum_{k=0}^m\binom{m}{k}N^k.
$$
By step <1>1, every term with $k\ge2$ vanishes. Hence
$$
A^m=(I+N)^m=I+mN.
$$
:::

<1>3. Therefore
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

::: {.proof}
Step <1>2 gives
$$
A^{100}
=I+100N
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
+
\begin{pmatrix}
50&50\\
-50&-50
\end{pmatrix},
$$
which is the displayed matrix.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested power.
:::
:::
