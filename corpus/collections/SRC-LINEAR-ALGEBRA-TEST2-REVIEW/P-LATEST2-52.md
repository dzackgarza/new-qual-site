---
schema: qual/card@1
id: P-LATEST2-52
kind: problem
title: Larger eigenvalue of a symmetric $2\times2$ matrix
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained PDF extraction for linear_algebra_from_test2.pdf; the source PDF has no usable text layer, so this audit is limited to the preserved extraction generated from that PDF.
---

::: {.problem}
Which of the following is the larger eigenvalue of
\[
\begin{pmatrix}5&1\\1&5\end{pmatrix}?
\]

(A) $4$  (B) $5$  (C) $6$  (D) $10$  (E) $12$
:::

::: {.solution}
Let
$$
A=\begin{pmatrix}5&1\\1&5\end{pmatrix}.
$$

<1>1. The vector
$$
v_+=\begin{pmatrix}1\\1\end{pmatrix}
$$
is an eigenvector with eigenvalue $6$.

::: {.proof}
Compute
$$
Av_+
=
\begin{pmatrix}5&1\\1&5\end{pmatrix}
\begin{pmatrix}1\\1\end{pmatrix}
=
\begin{pmatrix}6\\6\end{pmatrix}
=
6v_+.
$$
:::

<1>2. The vector
$$
v_-=\begin{pmatrix}1\\-1\end{pmatrix}
$$
is an eigenvector with eigenvalue $4$.

::: {.proof}
Compute
$$
Av_-
=
\begin{pmatrix}5&1\\1&5\end{pmatrix}
\begin{pmatrix}1\\-1\end{pmatrix}
=
\begin{pmatrix}4\\-4\end{pmatrix}
=
4v_-.
$$
:::

<1>3. The two eigenvalues of $A$ are $6$ and $4$.

::: {.proof}
The vectors $v_+$ and $v_-$ are linearly independent, so they form a basis of $\mathbb R^2$.
Hence the corresponding eigenvalues account for both eigenvalues of the $2\times2$ matrix $A$.
:::

<1>4. Therefore the larger eigenvalue is
$$
\boxed{6}.
$$

::: {.proof}
By step <1>3,
$$
6>4.
$$
Thus the correct choice is $\boxed{\text{(C)}}$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required answer.
:::
:::
