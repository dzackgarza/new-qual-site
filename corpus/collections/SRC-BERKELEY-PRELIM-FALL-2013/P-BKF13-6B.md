---
schema: qual/card@1
id: P-BKF13-6B
kind: problem
title: A product of two real $2\times2$ involutions with eigenvalues $2$ and $1/2$
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
    Independently checked the retained Fall 2013 solution packet and verified
    an equivalent explicit pair of involutions directly.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked both involution identities and the two displayed eigenvectors of
    the product.
---

::: {.problem}
Is it possible to find two real $2\times2$ matrices $A,B$ such that $A^2=B^2=\operatorname{Id}$ (the identity matrix), but $AB$ has eigenvalues $2$ and $1/2$?
:::

::: {.solution}
Set
$$
A\coloneqq
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix},
\qquad
B\coloneqq
\begin{pmatrix}
\frac54&\frac34\\
-\frac34&-\frac54
\end{pmatrix}.
$$

<1>1. One has $A^2=I_2$ and $B^2=I_2$.

::: {.proof}
The identity $A^2=I_2$ is immediate. Also,
$$
B^2
=
\begin{pmatrix}
\frac{25}{16}-\frac9{16}
&
\frac{15}{16}-\frac{15}{16}\\
-\frac{15}{16}+\frac{15}{16}
&
-\frac9{16}+\frac{25}{16}
\end{pmatrix}
=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix}
=I_2.
$$
:::

<1>2. The product is
$$
AB=
\begin{pmatrix}
\frac54&\frac34\\
\frac34&\frac54
\end{pmatrix}.
$$

::: {.proof}
This follows by direct matrix multiplication.
:::

<1>3. The matrix $AB$ has eigenvalues $2$ and $1/2$.

::: {.proof}
By step <1>2,
$$
AB
\begin{pmatrix}
1\\
1
\end{pmatrix}
=
2
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
AB
\begin{pmatrix}
1\\
-1
\end{pmatrix}
=
\frac12
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
$$
Thus $2$ and $1/2$ are eigenvalues of $AB$.
:::

<1>4. Therefore such matrices exist.

::: {.proof}
Step <1>1 shows that the displayed $A$ and $B$ are involutions, and step
<1>3 shows that their product has the required eigenvalues.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 answers the existence question affirmatively.
:::
:::
