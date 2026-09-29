---
schema: qual/card@1
id: P-BKS00-1
kind: problem
title: Similarity of two explicit real $4\times4$ matrices
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Exhibited a basis p_1=e_2, p_2=e_1+e_3, p_3=e_2+e_4, p_4=e_3
    on which B has exactly the displayed matrix A, equivalently BP=PA
    for the invertible change-of-basis matrix P.
---

::: {.problem}
Are the matrices
\[
A=\begin{pmatrix}
1&0&0&0\\
0&-1&0&0\\
0&0&0&1\\
0&0&0&0
\end{pmatrix},
\qquad
B=\begin{pmatrix}
-1&0&0&0\\
-1&1&1&-1\\
-1&0&0&0\\
-1&0&1&0
\end{pmatrix}
\]
similar over $\mathbb R$?
:::

::: {.solution}
Let $e_1,e_2,e_3,e_4$ denote the standard basis of $\RR^4$, and set
$$
p_1=e_2,
\qquad
p_2=e_1+e_3,
\qquad
p_3=e_2+e_4,
\qquad
p_4=e_3.
$$

::: pf

::: {.pf-step #s1}

The matrix
$$
P
=
\begin{pmatrix}
0&1&0&0\\
1&0&1&0\\
0&1&0&1\\
0&0&1&0
\end{pmatrix},
$$
whose columns are $p_1,p_2,p_3,p_4$, is invertible.

::: pf-proof

Expanding the determinant along the first row gives
$$
\det P
=
-
\det
\begin{pmatrix}
1&1&0\\
0&0&1\\
0&1&0
\end{pmatrix}
=1.
$$
Hence $P\in GL_4(\RR)$.

:::

:::

::: {.pf-step #s2}

The action of $B$ on these four columns is
$$
Bp_1=p_1,
\qquad
Bp_2=-p_2,
\qquad
Bp_3=0,
\qquad
Bp_4=p_3.
$$

::: pf-proof

Reading off the columns of $B$,
$$
Be_2=e_2,
$$
$$
B(e_1+e_3)
=
(-e_1-e_2-e_3-e_4)+(e_2+e_4)
=
-(e_1+e_3),
$$
$$
B(e_2+e_4)
=
e_2-e_2
=
0,
$$
and
$$
Be_3=e_2+e_4.
$$
These are exactly the four displayed identities.

:::

:::

::: {.pf-step #s3}

The matrices satisfy
$$
BP=PA.
$$

::: pf-proof

The columns of $PA$ are
$$
p_1,
\qquad
-p_2,
\qquad
0,
\qquad
p_3,
$$
because the four columns of $A$ are $e_1,-e_2,0,e_3$. By step [](#s2){.pf-ref},
these are also the four columns of $BP$.

:::

:::

::: {.pf-step #s4}

The answer is
$$
\boxed{\text{Yes}}.
$$

::: pf-proof

By step [](#s1){.pf-ref}, $P$ is invertible. Step [](#s3){.pf-ref} therefore gives
$$
B=PAP^{-1},
$$
so $A$ and $B$ are similar over $\RR$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves the requested similarity.

:::

:::

:::
