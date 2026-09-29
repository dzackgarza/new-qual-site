---
schema: qual/card@1
id: P-BKF14-6B
kind: problem
title: Approximating a singular $4\times4$ matrix by matrices with distinct real eigenvalues of both signs
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2014 solution packet: the stated
    diagonal perturbation has characteristic polynomial equal to the product
    of its four shifted diagonal factors.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked entrywise convergence and the four distinct eigenvalues
    1/n, 2/n, -1/n, and -2/n.
---

::: {.problem}
Show that there is a sequence of $4 \times 4$ matrices $A ( n )$ with real entries, which converges to

$$
A = { \left( \begin{array} { l l l l } { 0 } & { 0 } & { 0 } & { 0 } \\ { 0 } & { 0 } & { 0 } & { 1 } \\ { 0 } & { 1 } & { 0 } & { 0 } \\ { 1 } & { 0 } & { 0 } & { 0 } \end{array} \right) }
$$

and such that $A ( n )$ has 4 distinct real eigenvalues, two of which are positive and two negative.
:::

::: {.solution}
For $n\ge1$, set
$$
D_n\coloneqq
\begin{pmatrix}
\frac1n&0&0&0\\
0&\frac2n&0&0\\
0&0&-\frac1n&0\\
0&0&0&-\frac2n
\end{pmatrix}
$$
and define
$$
A_n\coloneqq A+D_n.
$$

::: pf

::: {.pf-step #s1}

One has
$$
A_n\longrightarrow A
$$
as $n\to\infty$.

::: pf-proof

Every entry of $D_n$ tends to $0$, so $D_n\to0$. Hence
$$
A_n-A=D_n\longrightarrow0.
$$
Thus $A_n\to A$ entrywise, equivalently in any norm on the
finite-dimensional space of $4\times4$ real matrices.

:::

:::

::: {.pf-step #s2}

For arbitrary real numbers $a,b,c,d$, the matrix
$$
A+\operatorname{diag}(a,b,c,d)
$$
has characteristic polynomial
$$
(\lambda-a)(\lambda-b)(\lambda-c)(\lambda-d).
$$

::: pf-proof

One has
$$
\lambda I-
\bigl(A+\operatorname{diag}(a,b,c,d)\bigr)
=
\begin{pmatrix}
\lambda-a&0&0&0\\
0&\lambda-b&0&-1\\
0&-1&\lambda-c&0\\
-1&0&0&\lambda-d
\end{pmatrix}.
$$
Expanding first along the first row and then along the last row of the
resulting $3\times3$ minor gives
$$
\begin{aligned}
\det\!\left(
\lambda I-
\bigl(A+\operatorname{diag}(a,b,c,d)\bigr)
\right)
&=
(\lambda-a)(\lambda-d)
\det
\begin{pmatrix}
\lambda-b&0\\
-1&\lambda-c
\end{pmatrix}\\
&=
(\lambda-a)(\lambda-b)(\lambda-c)(\lambda-d).
\end{aligned}
$$

:::

:::

::: {.pf-step #s3}

The eigenvalues of $A_n$ are
$$
\frac1n,\qquad
\frac2n,\qquad
-\frac1n,\qquad
-\frac2n.
$$

::: pf-proof

Apply step [](#s2){.pf-ref} with
$$
(a,b,c,d)
=
\left(
\frac1n,\frac2n,-\frac1n,-\frac2n
\right).
$$
The four roots of the resulting characteristic polynomial are exactly
the displayed numbers.

:::

:::

::: {.pf-step #s4}

For every $n\ge1$, the matrix $A_n$ has four distinct real
eigenvalues, exactly two positive and two negative.

::: pf-proof

The four numbers in step [](#s3){.pf-ref} are real and pairwise distinct. The
first two are positive and the last two are negative.

:::

:::

::: {.pf-step #s5}

The sequence $(A_n)$ has all the required properties.

::: pf-proof

Step [](#s1){.pf-ref} gives convergence to $A$, and step [](#s4){.pf-ref} gives the required
eigenvalue condition for every $n$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} completes the construction.

:::

:::

:::
