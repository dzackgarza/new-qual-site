---
schema: qual/card@1
id: P-RASP23D
kind: problem
title: "Radon measure on a non-standard metric space"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2023 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Define the distance function between $(x_1, y_1)$ and $(x_2, y_2)$ in the plane to be
$$
d = \begin{cases} |y_1 - y_2| & \text{if } x_1 = x_2, \\ 1 + |y_1 - y_2| & \text{if } x_1 \neq x_2. \end{cases}
$$

(i) Prove that this is indeed a metric.

(ii) The corresponding metric space $(X, d)$ is locally compact.

(iii) For any $f \in C_c(X)$, let $F$ be the set of $x$ such that there exists $y$ with $f(x,y) \neq 0$.
Prove that $F$ is a finite set $\{x_1, x_2, \ldots, x_n\}$.

(iv) For $f$ in (iii) define $I(f) = \sum_{i=1}^{n} \int_{-\infty}^{\infty} f(x_i, y)\,dy$.
Then $I(f)$ induces a Radon measure $\mu$ on $X$.
Is $\mu$ inner regular for all Borel sets?
If yes, prove it.
If no, find a Borel set which is not inner regular.
:::


::: solution
<1>1. Verify the metric axioms.
::: proof
Write a point as $(x,y)$. Then the proposed distance is
\[
d((x_1,y_1),(x_2,y_2))
=d_{\mathrm{disc}}(x_1,x_2)+|y_1-y_2|,
\]
where
\[
d_{\mathrm{disc}}(x_1,x_2)=
\begin{cases}
0,&x_1=x_2,\\
1,&x_1\ne x_2.
\end{cases}
\]
The discrete distance and the Euclidean distance are metrics, and the sum of two metrics is a metric. Thus positivity, symmetry, definiteness, and the triangle inequality all hold.
:::

<1>2. Prove local compactness.
::: proof
Fix $(x_0,y_0)\in X$ and choose $0<r<1$. If
\[
d((x,y),(x_0,y_0))\le r,
\]
then necessarily $x=x_0$, because distinct $x$-coordinates already contribute $1$ to the distance. Hence
\[
\overline B((x_0,y_0),r)
=\{x_0\}\times[y_0-r,y_0+r].
\]
With the induced metric this is isometric to the compact interval $[y_0-r,y_0+r]$. Thus every point has a neighborhood with compact closure, so $X$ is locally compact.
:::

<1>3. Show that a compactly supported continuous function uses only finitely many vertical lines.
::: proof
Let $K=\operatorname{supp}f$, which is compact. The balls
\[
B((x,y),1/3),\qquad (x,y)\in K,
\]
form an open cover of $K$. Each such ball lies entirely in one vertical line $\{x\}\times\mathbb R$. By compactness, finitely many of these balls cover $K$. Therefore $K$, and hence the set
\[
F=\{x:\exists y,\ f(x,y)\ne0\},
\]
meets only finitely many vertical lines. Thus
\[
F=\{x_1,\dots,x_n\}.
\]
:::

<1>4. Identify the measure induced by $I$.
::: proof
For each $x\in\mathbb R$, let $\lambda_x$ be one-dimensional Lebesgue measure on the open-and-closed vertical line $\{x\}\times\mathbb R$. Define, for Borel $E\subseteq X$,
\[
\nu(E):=\sum_{x\in\mathbb R}m(E_x),
\qquad
E_x:=\{y:(x,y)\in E\},
\]
where an uncountable sum of nonnegative numbers means the supremum of the finite partial sums.

This is a Borel measure: it is the sum of the family $(\lambda_x)_{x\in\mathbb R}$. If $f\in C_c(X)$, Step 3 shows that only finitely many vertical lines meet its support, so
\[
\int_X f\,d\nu
=\sum_{i=1}^n\int_{\mathbb R}f(x_i,y)\,dy
=I(f).
\]
Hence the Radon measure induced by the positive functional $I$ is precisely $\mu=\nu$.
:::

<1>5. Prove inner regularity on every Borel set.
::: proof
Let $E\subseteq X$ be Borel. We show
\[
\mu(E)=\sup\{\mu(K):K\subseteq E,\ K\text{ compact}\}.
\]

Suppose first that $\mu(E)<\infty$. Then at most countably many sections $E_x$ have positive Lebesgue measure, and
\[
\mu(E)=\sum_xm(E_x).
\]
Given $\varepsilon>0$, choose finitely many $x_1,\dots,x_N$ such that
\[
\sum_{i=1}^N m(E_{x_i})>\mu(E)-\frac\varepsilon2.
\]
By inner regularity of Lebesgue measure, choose compact sets
\[
K_i\subseteq E_{x_i}
\]
so that
\[
\sum_{i=1}^N m(K_i)
>\sum_{i=1}^N m(E_{x_i})-\frac\varepsilon2.
\]
Then
\[
K:=\bigcup_{i=1}^N\bigl(\{x_i\}\times K_i\bigr)
\]
is a finite union of compact sets, hence compact in $X$, and $K\subseteq E$. Moreover,
\[
\mu(K)>\mu(E)-\varepsilon.
\]

If $\mu(E)=\infty$, then for every $M>0$ the definition of the uncountable sum provides finitely many $x_1,\dots,x_N$ with
\[
\sum_{i=1}^N m(E_{x_i})>M+1.
\]
Approximating those finitely many sections from inside by compact sets as above produces a compact $K\subseteq E$ with $\mu(K)>M$. Hence the supremum over compact subsets is infinite.

Thus $\mu$ is inner regular on every Borel set. In particular, the answer to the final question is **yes**.
:::
:::
