---
schema: qual/card@1
id: P-UCLAB16S-12
kind: problem
title: Orthogonality of combinations of eigenvectors of a symmetric matrix
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $A$ be a symmetric real $n\times n$ matrix, where $n\ge4$, and let $v_1,\ldots,v_4\in\mathbb R^n$ be nonzero vectors.
Suppose
\[
Av_k=(2k-1)v_k
\qquad (1\le k\le4).
\]
Prove that $v_1+2v_2$ is orthogonal to $3v_3+4v_4$.
:::

::: {.solution}
<1>1. If $i\ne j$, then
\[
\boxed{\langle v_i,v_j\rangle=0}.
\]

::: {.proof}
The matrix $A$ is real symmetric, so
\[
\langle Av_i,v_j\rangle
=
\langle v_i,Av_j\rangle.
\]
Using
\[
Av_i=(2i-1)v_i
\]
and
\[
Av_j=(2j-1)v_j,
\]
one obtains
\[
(2i-1)\langle v_i,v_j\rangle
=
(2j-1)\langle v_i,v_j\rangle.
\]
Thus
\[
2(i-j)\langle v_i,v_j\rangle
=0.
\]
Since
\[
i\ne j,
\]
it follows that
\[
\langle v_i,v_j\rangle=0.
\]
:::

<1>2. In particular,
\[
v_1\perp v_3,
\qquad
v_1\perp v_4,
\qquad
v_2\perp v_3,
\qquad
v_2\perp v_4.
\]

::: {.proof}
Apply step <1>1 to the four pairs
\[
(1,3),\ (1,4),\ (2,3),\ (2,4).
\]
:::

<1>3. One has
\[
\begin{aligned}
\langle v_1+2v_2,\,3v_3+4v_4\rangle
&=
3\langle v_1,v_3\rangle
+
4\langle v_1,v_4\rangle\\
&\quad+
6\langle v_2,v_3\rangle
+
8\langle v_2,v_4\rangle.
\end{aligned}
\]

::: {.proof}
Expand the inner product bilinearly.
:::

<1>4. Every term on the right-hand side of step <1>3 vanishes.

::: {.proof}
This is exactly step <1>2.
:::

<1>5. Therefore
\[
\boxed{
\langle v_1+2v_2,\,3v_3+4v_4\rangle
=
0.
}
\]

::: {.proof}
Combine steps <1>3--<1>4.
Thus
\[
v_1+2v_2
\]
is orthogonal to
\[
3v_3+4v_4.
\]
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
