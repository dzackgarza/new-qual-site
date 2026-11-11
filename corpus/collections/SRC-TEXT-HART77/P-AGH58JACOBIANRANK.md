---
schema: qual/card@1
id: P-AGH58JACOBIANRANK
kind: problem
title: Jacobian rank criterion for nonsingularity in $\PP^n$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Nonsingular Varieties
  - Projective Varieties
  - Jacobian Criterion
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement and all three hint components with the retained Hartshorne I.5.8 transcription. The proof checks coordinate scaling row-by-row, dehomogenizes on a standard affine chart, and uses Euler''s identity to show the omitted projective Jacobian column lies in the span of the affine columns in arbitrary characteristic.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read Block, Nonsingular Varieties (Columbia, 25 July 2017), Lemma 18 and
    Proposition 17 with its proof, printed p. 4, which proves the projective
    Jacobian criterion exactly as the card states it. Checked the card
    against it: row scaling by lambda^{d_i-1}, the affine Jacobian as the
    deleted-column submatrix, and Euler's identity at a point of Y writing
    the deleted column as a combination of the others in every
    characteristic. Confirmed that the card's chart D_+(x_l) is arbitrary
    where Block takes U_0, which changes nothing.
---

::: {.problem}
Let $Y \subseteq \PP^n$ be a projective variety of dimension $r$.
Let $f_1, \ldots, f_t \in S = k[x_0, \ldots, x_n]$ be homogeneous polynomials generating the ideal of $Y$.
Let $P \in Y$ be a point with homogeneous coordinates $P = (a_0, \ldots, a_n)$.
Show that $P$ is nonsingular on $Y$ if and only if the matrix
$$
\left[ \frac{\partial f_i}{\partial x_j}(a_0, \ldots, a_n) \right]
$$
has rank $n - r$.
:::

::: {.hint}
(a) Show that this rank is independent of the homogeneous coordinates chosen for $P$; (b) pass to an open affine $U_i \subseteq \PP^n$ containing $P$ and use the affine Jacobian matrix; (c) you will need Euler's lemma, which says that if $f$ is a homogeneous polynomial of degree $d$, then $\sum_i x_i \frac{\partial f}{\partial x_i} = d \cdot f$.
:::

::: {.solution}
Let $d_i=\deg f_i$ and write
$$
J(P)=
\left[
\frac{\partial f_i}{\partial x_j}(a_0,\ldots,a_n)
\right]_{\substack{1\le i\le t\\0\le j\le n}}.
$$

::: pf

::: {.pf-step #rank-independent-of-representative}
The rank of $J(P)$ is independent of the chosen nonzero homogeneous-coordinate representative of $P$.

::: pf-proof
Replace
$$
(a_0,\ldots,a_n)
$$
by
$$
(\lambda a_0,\ldots,\lambda a_n),
\qquad \lambda\in k^\times.
$$
Because $f_i$ is homogeneous of degree $d_i$, each first partial derivative is homogeneous of degree $d_i-1$.
Thus every entry in row $i$ is multiplied by the same nonzero scalar
$$
\lambda^{d_i-1}.
$$
Multiplying individual rows by nonzero scalars does not change matrix rank.
Hence the rank depends only on the projective point $P$.
:::

:::

::: {.pf-step #affine-chart-equations}
Choose an index $\ell$ with $a_\ell\ne0$ and normalize the coordinates so that $a_\ell=1$.
On the standard affine chart $U_\ell=D_+(x_\ell)\cong\AA^n$, the affine equations of $Y\cap U_\ell$ are
$$
g_i(u_0,\ldots,\widehat{u_\ell},\ldots,u_n)
=
f_i(u_0,\ldots,u_{\ell-1},1,u_{\ell+1},\ldots,u_n).
$$

::: pf-proof
This is the standard dehomogenization of homogeneous equations on the chart $x_\ell\ne0$.
The point $P$ corresponds to the affine point
$$
p=(a_0,\ldots,\widehat{a_\ell},\ldots,a_n).
$$
Since localization and dehomogenization preserve the vanishing ideal on the chart, these $g_i$ generate the ideal of $Y\cap U_\ell$ there.
The open subvariety $Y\cap U_\ell$ has the same dimension $r$ as $Y$, because it is a nonempty open subset of the irreducible variety $Y$.
:::

:::

::: {.pf-step #affine-jacobian-is-submatrix}
The affine Jacobian matrix of the $g_i$ at $p$ is obtained from $J(P)$ by deleting column $\ell$.

::: pf-proof
For $j\ne\ell$, differentiating the dehomogenized polynomial gives
$$
\frac{\partial g_i}{\partial u_j}(p)
=
\frac{\partial f_i}{\partial x_j}(a_0,\ldots,a_n).
$$
Thus the $t\times n$ affine Jacobian consists exactly of the columns of $J(P)$ indexed by $j\ne\ell$.
:::

:::

::: {.pf-step #deleted-column-in-span}
The deleted column $\ell$ lies in the span of the remaining columns, so the projective and affine Jacobian matrices have the same rank.

::: pf-proof
Euler's identity for the homogeneous polynomial $f_i$ is
$$
\sum_{j=0}^n x_j\frac{\partial f_i}{\partial x_j}=d_i f_i.
$$
Evaluate it at the representative $a=(a_0,\ldots,a_n)$ of the point $P$.
Since $P\in Y$, one has $f_i(a)=0$, hence
$$
\sum_{j=0}^n a_j\frac{\partial f_i}{\partial x_j}(a)=0.
$$
This holds for every row $i$, even when the characteristic divides $d_i$.
Because $a_\ell=1$, it can be rewritten simultaneously for all rows as the column relation
$$
C_\ell=-\sum_{j\ne\ell}a_j C_j,
$$
where $C_j$ denotes column $j$ of $J(P)$.
Thus adjoining column $\ell$ to the affine Jacobian does not increase its rank.
By step [](#affine-jacobian-is-submatrix){.pf-ref}, the two ranks are equal.
:::

:::

::: {.pf-step #jacobian-criterion-equivalence}
One has
$$
\boxed{P\text{ nonsingular on }Y
\quad\Longleftrightarrow\quad
\operatorname{rank}J(P)=n-r.}
$$

::: pf-proof
The affine variety $Y\cap U_\ell\subseteq\AA^n$ has dimension $r$ by step [](#affine-chart-equations){.pf-ref}.
The affine Jacobian criterion says that $P$ is nonsingular on this affine open exactly when its affine Jacobian has rank
$$
n-r
$$
[@Har77, Chapter I, §5].
Nonsingularity is local, so this is equivalent to $P$ being nonsingular on $Y$.
Step [](#deleted-column-in-span){.pf-ref} identifies the affine Jacobian rank with $\operatorname{rank}J(P)$.
The displayed equivalence follows.
:::

:::

::: pf-qed
Step [](#rank-independent-of-representative){.pf-ref} verifies that the stated rank is intrinsic to the projective point.
Steps [](#affine-chart-equations){.pf-ref}, [](#affine-jacobian-is-submatrix){.pf-ref} and [](#deleted-column-in-span){.pf-ref} compare it with the affine Jacobian rank, and step [](#jacobian-criterion-equivalence){.pf-ref} applies the affine criterion to prove the result.
:::

:::
:::

::: {.remark title="Published solution"}
The complete published argument is Adam B. Block, *Nonsingular Varieties* (Columbia, 25 July 2017), Proposition 17 with Lemma 18 and the proof following it, printed p. 4. Lemma 18 is Euler's identity $\sum_{i=0}^n x_i\,\partial f/\partial x_i=df$ proved on monomials. Proposition 17 states the criterion in the same form as the card, "Then $Y$ is nonsingular at $P$ if and only if $\operatorname{rk}J_P=n-r$", and its proof is the card's three steps: the rows of $J_{P'}$ are the rows of $J_P$ scaled by the constants $\lambda^{d_i-1}$ for $P'=\lambda P$; the affine Jacobian on $U_0$ is the submatrix of $J_P$ with the column $\partial f_i/\partial x_0$ deleted; and Euler's identity, evaluated where $f_i(P)=0$, writes that column as $-\sum_{j\ge1}y_j\,\partial f_i/\partial y_j$ with $y_j=x_j/x_0$, so the rank is unchanged. Block restricts to the chart $U_0$, which the card replaces by an arbitrary chart $D_+(x_\ell)$; the argument is the same.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), gives no solution to 5.8.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), gives no solution to 5.8.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.5.8, PDF p. 47: "The hint is the answer", with no argument.
No retained set proves this exercise; the argument of Block's Proposition 17 is the published one, and it is the printed hint: row scalings by $\lambda^{d_i-1}$ show the rank is independent of the representative, dehomogenizing on $D_+(x_\ell)$ gives the affine Jacobian as the columns other than $\ell$, and Euler's identity evaluated at a point of $Y$ writes column $\ell$ as $-\sum_{j\ne\ell}a_jC_j$, so nothing is lost by deleting it.
:::
