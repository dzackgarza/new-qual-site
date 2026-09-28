---
schema: qual/card@1
id: P-BKF78-8
kind: problem
title: Characteristic polynomial and Jordan form of the all-ones matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the deterministic MinerU Flash extraction of the Berkeley Fall 1978 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Writing u=(1,...,1)^T, Mv=(sum_i v_i)u and M^2=nM. The sum-zero
    hyperplane has dimension n-1, giving characteristic polynomial
    t^{n-1}(t-n). If n is nonzero in F, F^n=ker(M) direct-sum Fu and M
    is diagonalizable with diagonal (n,0,...,0). If char(F) divides n,
    M is nonzero rank-one square-zero, so its Jordan form is J_2(0)
    plus n-2 zero blocks.
---

::: {.problem}
Let $M$ be the $n\times n$ matrix over a field $F$ all of whose entries are $1$.

1. Find the characteristic polynomial of $M$.

2. Is $M$ diagonalizable?

3. Find the Jordan canonical form of $M$, and discuss the extent to which the Jordan form depends on the characteristic of $F$.
:::

::: {.solution}
Let
$$
u=
\begin{pmatrix}
1\\
\vdots\\
1
\end{pmatrix}
\in F^n,
$$
and write
$$
\overline{n}=n\cdot1_F\in F.
$$

<1>1. For every $v=(v_1,\ldots,v_n)^T\in F^n$,
$$
Mv=(v_1+\cdots+v_n)u.
$$
Consequently,
$$
\operatorname{rank}M=1
$$
and
$$
M^2=\overline{n}M.
$$

::: {.proof}
Every row of $M$ consists entirely of $1$'s, so each coordinate of
$Mv$ is $v_1+\cdots+v_n$, giving the first formula. The image is
therefore the line $Fu$, and $u\neq0$, so the rank is $1$.

Also
$$
Mu=\overline{n}u.
$$
Applying $M$ to the first formula gives
$$
M^2v
=(v_1+\cdots+v_n)Mu
=
\overline{n}Mv.
$$
:::

<1>2. The kernel of $M$ is the hyperplane
$$
H
=
\left\{
v\in F^n:
v_1+\cdots+v_n=0
\right\},
$$
which has dimension $n-1$.

::: {.proof}
By step <1>1, $Mv=0$ exactly when
$v_1+\cdots+v_n=0$. The defining linear functional is nonzero, so
its kernel has codimension $1$.
:::

<1>3. The characteristic polynomial of $M$ is
$$
\boxed{
\chi_M(t)=t^{n-1}(t-\overline{n})
}.
$$

::: {.proof}
Choose a basis $h_1,\ldots,h_{n-1}$ of $H$ and append a vector
$w\notin H$. Step <1>2 shows that $M$ vanishes on all $h_i$, so in
this basis the first $n-1$ columns have only zeros.

Modulo $H$, the action of $M$ is multiplication by $\overline{n}$.
Indeed, if $s(v)=v_1+\cdots+v_n$, then
$$
s(Mv)=\overline{n}s(v).
$$
Thus the matrix of $M$ in this basis is upper triangular with
diagonal entries
$$
0,\ldots,0,\overline{n}.
$$
Its characteristic polynomial is therefore the displayed one.
:::

<1>4. If $\overline{n}\neq0$, then $M$ is diagonalizable and its
Jordan form is
$$
\boxed{
\operatorname{diag}
(\overline{n},0,\ldots,0)
}.
$$

::: {.proof}
By step <1>2, $M$ vanishes on the $(n-1)$-dimensional space $H$.
Step <1>1 gives
$$
Mu=\overline{n}u.
$$
Since $\overline{n}\neq0$,
$$
u\notin H,
$$
because the sum of the coordinates of $u$ is $\overline{n}$.
Therefore
$$
F^n=H\oplus Fu.
$$
Relative to a basis of $H$ followed by $u$, the matrix is diagonal
with eigenvalues $0,\ldots,0,\overline{n}$.
:::

<1>5. If $\overline{n}=0$, then $M$ is not diagonalizable.

::: {.proof}
Step <1>1 gives
$$
M^2=0,
$$
while $M\neq0$ because all of its entries are $1$. Thus $M$ is a
nonzero nilpotent matrix. A diagonalizable nilpotent matrix must be
the zero matrix, so $M$ is not diagonalizable.
:::

<1>6. If $\overline{n}=0$, the Jordan form of $M$ is
$$
\boxed{
J_2(0)\oplus
0\oplus\cdots\oplus0
},
$$
with one block of size $2$ and $n-2$ blocks of size $1$.

::: {.proof}
In this case step <1>5 gives $M^2=0$, so every nilpotent Jordan block
has size at most $2$. Step <1>1 gives
$$
\operatorname{rank}M=1.
$$
Each size-$2$ nilpotent Jordan block contributes rank $1$, while each
size-$1$ zero block contributes rank $0$. Hence there is exactly one
size-$2$ block. The remaining $n-2$ dimensions are size-$1$ zero
blocks.
:::

<1>7. The dependence on the characteristic is exactly whether
$\overline{n}$ vanishes:
$$
\boxed{
\overline{n}=0
\quad\Longleftrightarrow\quad
\operatorname{char}F=p>0\text{ for some prime }p\mid n
}.
$$

::: {.proof}
The scalar $\overline{n}$ vanishes precisely when $F$ has positive
characteristic $p$ dividing the integer $n$. If it does not vanish,
step <1>4 gives the diagonal Jordan form. If it vanishes, steps
<1>5 and <1>6 give the nontrivial nilpotent Jordan form.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>3 answers part 1, steps <1>4 and <1>5 answer part 2, and
steps <1>4, <1>6, and <1>7 answer part 3.
:::
:::
