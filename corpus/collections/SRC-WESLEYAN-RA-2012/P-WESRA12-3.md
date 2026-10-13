---
schema: qual/card@1
id: P-WESRA12-3
kind: problem
title: 'Norms, Banach spaces, uniform boundedness, and inverse continuity'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $V$ be a real vector space.

(a) Define a norm on $V$.

(b) Give the metric induced by a norm and prove that it is a metric.

(c) Define a Banach space.

(d) Give an example of a normed vector space that is not Banach.

(e) State the Uniform Boundedness Theorem with the correct hypotheses.

(f) If $X,Y$ are real Banach spaces and $T:X\to Y$ is a continuous bijective linear map, prove $T^{-1}$ is linear and determine whether $T^{-1}$ is continuous, giving a reason.
:::

::: {.solution}
<1>1. A **norm** on $V$ is a function
\[
\|\cdot\|:V\to[0,\infty)
\]
such that for all
\[
x,y\in V
\]
and
\[
a\in\mathbb R,
\]

1. \[
   \|x\|=0
   \quad\Longleftrightarrow\quad
   x=0;
   \]
2. \[
   \|ax\|
   =
   |a|\,\|x\|;
   \]
3. \[
   \|x+y\|
   \le
   \|x\|+\|y\|.
   \]

::: {.proof}
These are respectively positive definiteness, absolute homogeneity, and the
triangle inequality.
:::

<1>2. The metric induced by a norm is
\[
\boxed{
d(x,y)
\coloneqq
\|x-y\|.
}
\]

::: {.proof}
We verify the metric axioms in the next four steps.
:::

<1>3. One has
\[
d(x,y)\ge0.
\]

::: {.proof}
Norms take values in
\[
[0,\infty).
\]
:::

<1>4. One has
\[
d(x,y)=0
\quad\Longleftrightarrow\quad
x=y.
\]

::: {.proof}
By positive definiteness,
\[
d(x,y)=0
\Longleftrightarrow
\|x-y\|=0
\Longleftrightarrow
x-y=0
\Longleftrightarrow
x=y.
\]
:::

<1>5. The metric is symmetric:
\[
d(x,y)=d(y,x).
\]

::: {.proof}
Using absolute homogeneity,
\[
\begin{aligned}
d(y,x)
&=
\|y-x\|\\
&=
\|-(x-y)\|\\
&=
|-1|\,\|x-y\|\\
&=
d(x,y).
\end{aligned}
\]
:::

<1>6. The triangle inequality holds:
\[
d(x,z)
\le
d(x,y)+d(y,z).
\]

::: {.proof}
Since
\[
x-z
=
(x-y)+(y-z),
\]
the norm triangle inequality gives
\[
\begin{aligned}
d(x,z)
&=
\|x-z\|\\
&\le
\|x-y\|
+
\|y-z\|\\
&=
d(x,y)+d(y,z).
\end{aligned}
\]
:::

<1>7. Therefore
\[
d(x,y)=\|x-y\|
\]
is a metric.

::: {.proof}
Steps <1>3--<1>6 verify all metric axioms.
:::

<1>8. A **Banach space** is a normed vector space that is complete with
respect to the metric induced by its norm.

::: {.proof}
Equivalently, every Cauchy sequence in the norm converges in norm to a point
of the space.
:::

<1>9. Let
\[
c_{00}
\]
be the vector space of real sequences with finite support, equipped with the
norm
\[
\|x\|_2
=
\left(
\sum_{n=1}^{\infty}
|x_n|^2
\right)^{1/2}.
\]
Then
\[
c_{00}
\]
is a normed vector space that is not Banach.

::: {.proof}
The displayed formula is the usual
\[
\ell^2
\]
norm restricted to $c_{00}$.

Define
\[
x^{(m)}
=
\left(
1,
\frac12,
\frac13,
\dots,
\frac1m,
0,0,\dots
\right).
\]
Each
\[
x^{(m)}
\in
c_{00}.
\]

For
\[
n>m,
\]
\[
\|x^{(n)}-x^{(m)}\|_2^2
=
\sum_{k=m+1}^{n}
\frac1{k^2}.
\]
Since
\[
\sum_{k=1}^{\infty}\frac1{k^2}
\]
converges, the sequence
\[
(x^{(m)})
\]
is Cauchy in
\[
c_{00}.
\]

In
\[
\ell^2
\]
it converges to
\[
x
=
\left(
1,
\frac12,
\frac13,
\dots
\right),
\]
which belongs to
\[
\ell^2
\]
but not to
\[
c_{00}
\]
because it has infinite support.

If the sequence converged in $c_{00}$, uniqueness of limits in the ambient
metric space
\[
\ell^2
\]
would force its limit to be $x$, impossible.
Thus $c_{00}$ is incomplete.
:::

<1>10. **Uniform Boundedness Theorem.**

Let
\[
X
\]
be a Banach space,
\[
Y
\]
a normed vector space, and let
\[
\mathcal F
\subseteq
\mathcal L(X,Y)
\]
be a family of continuous linear maps.
Assume the family is pointwise bounded:
\[
\sup_{T\in\mathcal F}
\|Tx\|
<
\infty
\qquad
\text{for every }x\in X.
\]
Then
\[
\boxed{
\sup_{T\in\mathcal F}
\|T\|
<
\infty.
}
\]

::: {.proof}
This is the Banach--Steinhaus theorem.
The essential completeness hypothesis is on the domain $X$.
The codomain need only be normed.
:::

<1>11. Now let
\[
T:X\to Y
\]
be a bijective linear map.
Then
\[
T^{-1}:Y\to X
\]
is linear.

::: {.proof}
Let
\[
y_1,y_2\in Y
\]
and
\[
a,b\in\mathbb R.
\]
Set
\[
x_1=T^{-1}(y_1),
\qquad
x_2=T^{-1}(y_2).
\]
Then
\[
T(x_1)=y_1,
\qquad
T(x_2)=y_2.
\]
By linearity of $T$,
\[
T(ax_1+bx_2)
=
ay_1+by_2.
\]
Applying the inverse map gives
\[
T^{-1}(ay_1+by_2)
=
ax_1+bx_2
=
aT^{-1}(y_1)+bT^{-1}(y_2).
\]
Hence $T^{-1}$ is linear.
:::

<1>12. If, in addition,
\[
X
\quad\text{and}\quad
Y
\]
are Banach spaces and $T$ is continuous, then
\[
T^{-1}
\]
is continuous.

::: {.proof}
By the Open Mapping Theorem, every surjective continuous linear map between
Banach spaces is open.
Since $T$ is bijective, it is surjective, so
\[
T:X\to Y
\]
is an open map.

For an open set
\[
U\subseteq X,
\]
\[
(T^{-1})^{-1}(U)
=
T(U).
\]
Because $T$ is open,
\[
T(U)
\]
is open in $Y$.
Therefore
\[
T^{-1}:Y\to X
\]
is continuous.
:::

<1>13. Thus
\[
\boxed{
T^{-1}
\text{ is a continuous linear map}.
}
\]

::: {.proof}
Linearity is step <1>11 and continuity is step <1>12.
:::

<1>14. Q.E.D.

::: {.proof}
Steps <1>1--<1>7 answer parts (a)--(b), step <1>8 answers part (c),
step <1>9 answers part (d), step <1>10 answers part (e), and
steps <1>11--<1>13 answer part (f).
:::
:::
