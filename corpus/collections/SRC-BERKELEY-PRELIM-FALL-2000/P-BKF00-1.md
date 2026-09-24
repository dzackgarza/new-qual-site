---
schema: qual/card@1
id: P-BKF00-1
kind: problem
title: Trace of an endomorphism equals the trace of its restriction to its image
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Used a basis of the image extended to a basis of V. In that basis the
    matrix of f has upper-left block equal to the matrix of the restriction
    to the image and zero lower block, so the two traces agree.
---

::: {.problem}
Let $V$ be finite-dimensional, let $f:V\to V$ be linear, and let
\[
W=\operatorname{im}f.
\]
Prove that the restriction $f|_W:W\to W$ has the same trace as $f:V\to V$.
:::

::: {.solution}
Let
$$
r=\dim W,
\qquad
n=\dim V.
$$

<1>1. The subspace $W$ is invariant under $f$.

::: {.proof}
If $w\in W$, then by definition of $W=\operatorname{im}f$ there is some
$v\in V$ such that
$$
w=f(v).
$$
Hence
$$
f(w)=f(f(v))\in\operatorname{im}f=W.
$$
Therefore $f(W)\subseteq W$, so the restriction $f|_W:W\to W$ is an
endomorphism.
:::

<1>2. Choose a basis
$$
w_1,\ldots,w_r
$$
of $W$ and extend it to a basis
$$
w_1,\ldots,w_r,u_{r+1},\ldots,u_n
$$
of $V$.

::: {.proof}
This is the basis-extension theorem for the finite-dimensional subspace
$W\subseteq V$.
:::

<1>3. Relative to the basis in step <1>2, the matrix of $f$ has the block
form
$$
[f]
=
\begin{pmatrix}
A&B\\
0&0
\end{pmatrix},
$$
where $A$ is the matrix of $f|_W$ in the basis
$w_1,\ldots,w_r$.

::: {.proof}
By step <1>1, each $f(w_i)$ belongs to $W$, so the first $r$ columns have
zero coordinates in the complementary basis vectors
$u_{r+1},\ldots,u_n$. Their first $r$ coordinates are exactly the columns
of the matrix $A$ of $f|_W$.

For every $j>r$, the vector $f(u_j)$ also belongs to
$\operatorname{im}f=W$ by the definition of $W$. Thus the remaining
columns likewise have zero coordinates in
$u_{r+1},\ldots,u_n$. Their coordinates in $W$ form the block $B$.
This gives the displayed matrix.
:::

<1>4. The two traces are equal:
$$
\boxed{
\operatorname{tr}(f|_W)=\operatorname{tr}(f).
}
$$

::: {.proof}
By step <1>3, the diagonal entries of $[f]$ consist of the diagonal entries
of $A$ followed by $n-r$ zeros. Therefore
$$
\operatorname{tr}(f)
=
\operatorname{tr}(A).
$$
Since $A$ is the matrix of $f|_W$, its trace is
$\operatorname{tr}(f|_W)$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required equality.
:::
:::
