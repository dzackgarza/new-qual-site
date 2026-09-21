---
schema: qual/card@1
id: P-BERK79S-09
kind: problem
title: One- and two-dimensional invariant subspaces of a real three-dimensional operator
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
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    A real cubic characteristic polynomial has a real root, so T has a real
    eigenvector and hence an invariant line. Applying the same argument to
    T^T gives a real eigenvector w of the transpose; then w^perp is
    two-dimensional and T-invariant because
    <Tv,w>=<v,T^T w>=lambda<v,w>.
---

::: {.problem}
Prove that every linear transformation $T:\mathbb R^3\to\mathbb R^3$ has

1. a one-dimensional invariant subspace; and

2. a two-dimensional invariant subspace.
:::

::: {.solution}
<1>1. The characteristic polynomial of $T$ has a real root.

::: {.proof}
The characteristic polynomial
$$
p(\lambda)=\det(\lambda I-T)
$$
is a real polynomial of degree $3$. Its leading term is $\lambda^3$, so
$$
p(\lambda)\longrightarrow\infty
$$
as $\lambda\to\infty$ and
$$
p(\lambda)\longrightarrow-\infty
$$
as $\lambda\to-\infty$.
By the intermediate value theorem, $p$ has a real zero.
:::

<1>2. There is a nonzero vector $v\in\RR^3$ and a real number $\lambda$
such that
$$
Tv=\lambda v.
$$

::: {.proof}
Let $\lambda$ be a real root from step <1>1. Then
$$
\det(\lambda I-T)=0,
$$
so $\lambda I-T$ is singular. Hence its kernel contains a nonzero vector
$v$, and
$$
(\lambda I-T)v=0
$$
is equivalent to the displayed eigenvector equation.
:::

<1>3. The line
$$
\boxed{
\RR v
}
$$
is a one-dimensional $T$-invariant subspace.

::: {.proof}
For every scalar $a\in\RR$,
$$
T(av)
=
aTv
=
a\lambda v
\in
\RR v.
$$
Thus $\RR v$ is invariant, and it is one-dimensional because $v\neq0$.
:::

<1>4. The transpose $T^T$ has a real eigenvector: there are
$$
0\neq w\in\RR^3
$$
and $\mu\in\RR$ such that
$$
T^Tw=\mu w.
$$

::: {.proof}
The operator $T^T$ is again a real linear transformation of $\RR^3$.
Applying steps <1>1--<1>2 to $T^T$ gives the stated eigenvector and
eigenvalue.
:::

<1>5. The plane
$$
w^\perp
=
\{x\in\RR^3:\langle x,w\rangle=0\}
$$
is $T$-invariant.

::: {.proof}
Let $x\in w^\perp$. Then
$$
\langle x,w\rangle=0.
$$
Using step <1>4,
$$
\begin{aligned}
\langle Tx,w\rangle
&=
\langle x,T^Tw\rangle\\
&=
\langle x,\mu w\rangle\\
&=
\mu\langle x,w\rangle\\
&=
0.
\end{aligned}
$$
Hence $Tx\in w^\perp$.
:::

<1>6. The subspace
$$
\boxed{
w^\perp
}
$$
is two-dimensional.

::: {.proof}
The vector $w$ is nonzero, so its orthogonal complement in the
three-dimensional Euclidean space $\RR^3$ has codimension $1$. Therefore
$$
\dim w^\perp=2.
$$
Step <1>5 shows that it is $T$-invariant.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>3 proves part (1), and steps <1>5--<1>6 prove part (2).
:::
:::
