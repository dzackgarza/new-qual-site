---
schema: qual/card@1
id: P-UCLAB17S-02
kind: problem
title: Jordan blocks in a four-parameter family of $4\times4$ matrices
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2017, `assets/attachments/basic-17S.pdf`.
---

::: {.problem}
Let
\[
M=\begin{pmatrix}1&0&a&b\\0&1&0&0\\0&c&3&-2\\0&d&2&-1\end{pmatrix},\qquad a,b,c,d\in\mathbb R.
\]
(a) Determine conditions on $a,b,c,d$ such that the Jordan form of $M$ has only one Jordan block for each eigenvalue.

(b) Find the Jordan form when $a=c=d=2$ and $b=-2$.
:::

::: {.solution}
Set
\[
N=M-I.
\]
Then
\[
N=
\begin{pmatrix}
0&0&a&b\\
0&0&0&0\\
0&c&2&-2\\
0&d&2&-2
\end{pmatrix}.
\]

<1>1. One has
\[
N^2=
\begin{pmatrix}
0&ac+bd&2(a+b)&-2(a+b)\\
0&0&0&0\\
0&2(c-d)&0&0\\
0&2(c-d)&0&0
\end{pmatrix}.
\]

::: {.proof}
Multiply the displayed matrix $N$ by itself.
The second row and first column remain zero.
The only nonzero contributions are the entries shown.
:::

<1>2. One has
\[
\boxed{
N^3=
\begin{pmatrix}
0&2(a+b)(c-d)&0&0\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix}.
}
\]

::: {.proof}
Multiply $N$ by the matrix in step <1>1.
Only the first-row entries in columns $3,4$ of $N$ can combine with the nonzero second-column entries in rows $3,4$ of $N^2$:
\[
2a(c-d)+2b(c-d)
=
2(a+b)(c-d).
\]
All other entries vanish.
:::

<1>3. One has
\[
\boxed{N^4=0}.
\]

::: {.proof}
By step <1>2, the only possibly nonzero entry of $N^3$ lies in column $2$.
But the second row of $N$ is zero.
Therefore
\[
N^4=N^3N=0.
\]
:::

<1>4. Hence every eigenvalue of $M$ is equal to $1$.

::: {.proof}
Step <1>3 gives
\[
(M-I)^4=0.
\]
Thus the minimal polynomial of $M$ divides
\[
(t-1)^4.
\]
Every eigenvalue must therefore be a root of
\[
(t-1)^4,
\]
so the only eigenvalue is $1$.
Since $M$ is $4\times4$, its algebraic multiplicity is $4$.
:::

<1>5. The Jordan form of $M$ consists of a single Jordan block if and only if
\[
N^3\ne0.
\]

::: {.proof}
By step <1>4, every Jordan block has eigenvalue $1$.
For a nilpotent operator $N=M-I$ on a $4$-dimensional space, the size of the largest Jordan block is the nilpotency index of $N$.

There is a single Jordan block exactly when the unique block has size $4$, which is equivalent to
\[
N^4=0
\quad\text{and}\quad
N^3\ne0.
\]
Step <1>3 gives the first condition automatically.
:::

<1>6. Therefore the condition in part (a) is
\[
\boxed{
(a+b)(c-d)\ne0.
}
\]

::: {.proof}
By step <1>2,
\[
N^3\ne0
\]
exactly when
\[
2(a+b)(c-d)\ne0.
\]
Apply step <1>5.
:::

<1>7. Under the specialization
\[
a=c=d=2,
\qquad
b=-2,
\]
one has
\[
\boxed{N^2=0}.
\]

::: {.proof}
In step <1>1,
\[
a+b=0
\]
and
\[
c-d=0.
\]
Also
\[
ac+bd
=
4-4
=0.
\]
Thus every entry of $N^2$ vanishes.
:::

<1>8. Under the same specialization,
\[
\operatorname{rank}N=2.
\]

::: {.proof}
The matrix becomes
\[
N=
\begin{pmatrix}
0&0&2&-2\\
0&0&0&0\\
0&2&2&-2\\
0&2&2&-2
\end{pmatrix}.
\]
The first and third rows are linearly independent, the fourth row equals the third, and the second row is zero.
Hence the row rank, and therefore the rank, is $2$.
:::

<1>9. The Jordan form in part (b) is
\[
\boxed{
J_2(1)\oplus J_2(1).
}
\]

::: {.proof}
By step <1>7, every Jordan block for $N$ has size at most $2$.
For a nilpotent matrix with square zero, each size-$2$ Jordan block contributes rank $1$, while each size-$1$ zero block contributes rank $0$.
Step <1>8 gives
\[
\operatorname{rank}N=2.
\]
Therefore there are exactly two size-$2$ nilpotent Jordan blocks and no size-$1$ blocks.
Adding the identity shifts both eigenvalues from $0$ to $1$, giving
\[
J_2(1)\oplus J_2(1).
\]
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>6 answers part (a), and step <1>9 answers part (b).
:::
:::
