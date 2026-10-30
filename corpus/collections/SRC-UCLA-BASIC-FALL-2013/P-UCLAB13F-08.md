---
schema: qual/card@1
id: P-UCLAB13F-08
kind: problem
title: Orthogonal projections with prescribed diagonal
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
An orthogonal projection on a finite-dimensional inner-product space $V$ is an endomorphism $P$ satisfying $P^2=P$ and $\operatorname{im}(P)=\ker(P)^\perp$.

Suppose $V=\RR^3$ and $P$ is an orthogonal projection with diagonal entries
$$
p_{11}=\frac23,\qquad p_{22}=\frac12,\qquad p_{33}=\frac56.
$$
Find all matrices that $P$ could be.

Hint: it is a very small finite set.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For an idempotent map $P$,
$$
V=\operatorname{im}P\oplus\ker P.
$$


::: pf-proof

For every $v\in V$,
$$
v
=
Pv+(v-Pv).
$$
The first term belongs to $\operatorname{im}P$, while
$$
P(v-Pv)
=
Pv-P^2v
=0,
$$
so the second term belongs to $\ker P$.

If
$$
w\in\operatorname{im}P\cap\ker P,
$$
then $w=Pu$ for some $u$, so
$$
Pw=P^2u=Pu=w,
$$
while $Pw=0$ because $w\in\ker P$.
Thus $w=0$.

:::

:::

::: {.pf-step #s1-2}

Under the orthogonality hypothesis
$$
\operatorname{im}P=(\ker P)^\perp,
$$
the map $P$ is the orthogonal projection onto $\operatorname{im}P$ and is represented by a symmetric matrix.


::: pf-proof

By step [](#s1-1){.pf-ref}, every $v$ decomposes uniquely as
$$
v=u+k,
\qquad
u\in\operatorname{im}P,
\quad
k\in\ker P.
$$
Since
$$
\operatorname{im}P=(\ker P)^\perp,
$$
the two summands are orthogonal.
Moreover
$$
Pv=u.
$$
Thus $P$ is the usual orthogonal projection onto $\operatorname{im}P$, hence self-adjoint.
In the standard orthonormal basis of $\RR^3$, its matrix is symmetric.

:::

:::

::: {.pf-step #s1-3}

The rank of $P$ is $2$.


::: pf-proof

Since
$$
P^2=P,
$$
the only eigenvalues of $P$ are $0$ and $1$.
Hence
$$
\operatorname{rank}P
=
\operatorname{trace}P.
$$
The prescribed diagonal entries give
$$
\operatorname{trace}P
=
\frac23+\frac12+\frac56
=
\frac{4+3+5}{6}
=2.
$$
Therefore
$$
\operatorname{rank}P=2.
$$

:::

:::

::: pf-step

The kernel of $P$ is one-dimensional.


::: pf-proof

By rank-nullity in $\RR^3$ and step [](#s1-3){.pf-ref},
$$
\dim\ker P
=
3-2
=1.
$$

:::

:::

::: {.pf-step #s1-5}

Let $u=(u_1,u_2,u_3)^t$ be a unit vector spanning $\ker P$.
Then
$$
\boxed{P=I-uu^t}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $P$ is the orthogonal projection onto
$$
(\ker P)^\perp=u^\perp.
$$
For any $v\in\RR^3$,
$$
v=(v-(u\cdot v)u)+(u\cdot v)u,
$$
with the first term in $u^\perp$ and the second in $\operatorname{span}\{u\}$.
Thus
$$
Pv=v-(u\cdot v)u
=(I-uu^t)v.
$$

:::

:::

::: {.pf-step #s1-6}

The diagonal conditions imply
$$
u_1^2=\frac13,
\qquad
u_2^2=\frac12,
\qquad
u_3^2=\frac16.
$$


::: pf-proof

By step [](#s1-5){.pf-ref},
$$
p_{ii}=1-u_i^2.
$$
Therefore
$$
u_1^2
=
1-\frac23
=
\frac13,
$$
$$
u_2^2
=
1-\frac12
=
\frac12,
$$
and
$$
u_3^2
=
1-\frac56
=
\frac16.
$$
Their sum is $1$, consistent with $\norm{u}=1$.

:::

:::

::: {.pf-step #s1-7}

Replacing $u$ by $-u$ does not change $P$, so every possible projection is obtained by taking
$$
u_{\varepsilon,\delta}
=
\begin{pmatrix}
\frac1{\sqrt3}\\[1mm]
\frac{\varepsilon}{\sqrt2}\\[1mm]
\frac{\delta}{\sqrt6}
\end{pmatrix},
\qquad
\varepsilon,\delta\in\{\pm1\}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} determines the absolute value of every coordinate of $u$.
There are $2^3$ sign choices, but
$$
uu^t=(-u)(-u)^t,
$$
so opposite vectors define the same projection.
Fixing the first sign to be positive leaves exactly four distinct possibilities, parameterized by $\varepsilon,\delta$.

:::

:::

::: {.pf-step #s1-8}

The four possible matrices are
$$
\boxed{
P_{\varepsilon,\delta}
=
\begin{pmatrix}
\frac23&
-\frac{\varepsilon}{\sqrt6}&
-\frac{\delta}{3\sqrt2}\\[2mm]
-\frac{\varepsilon}{\sqrt6}&
\frac12&
-\frac{\varepsilon\delta}{2\sqrt3}\\[2mm]
-\frac{\delta}{3\sqrt2}&
-\frac{\varepsilon\delta}{2\sqrt3}&
\frac56
\end{pmatrix},
\qquad
\varepsilon,\delta\in\{\pm1\}.
}
$$


::: pf-proof

Substitute the vector from step [](#s1-7){.pf-ref} into
$$
P=I-uu^t.
$$
The diagonal entries are the prescribed ones by step [](#s1-6){.pf-ref}.
The off-diagonal entries are
$$
-u_1u_2
=
-\frac{\varepsilon}{\sqrt6},
$$
$$
-u_1u_3
=
-\frac{\delta}{\sqrt{18}}
=
-\frac{\delta}{3\sqrt2},
$$
and
$$
-u_2u_3
=
-\frac{\varepsilon\delta}{\sqrt{12}}
=
-\frac{\varepsilon\delta}{2\sqrt3}.
$$

:::

:::

::: {.pf-step #s1-9}

These four matrices are all valid orthogonal projections.


::: pf-proof

For every choice of $\varepsilon,\delta$, the vector $u_{\varepsilon,\delta}$ has norm $1$.
Hence
$$
P_{\varepsilon,\delta}=I-u_{\varepsilon,\delta}u_{\varepsilon,\delta}^t
$$
is the orthogonal projection onto
$$
u_{\varepsilon,\delta}^\perp.
$$
Thus it satisfies
$$
P^2=P
$$
and
$$
\operatorname{im}P=(\ker P)^\perp.
$$

:::

:::

::: pf-qed

Steps [](#s1-7){.pf-ref} through [](#s1-9){.pf-ref} show that the displayed four matrices are exactly all possibilities.

:::

:::

:::
