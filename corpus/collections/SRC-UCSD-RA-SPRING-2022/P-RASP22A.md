---
schema: qual/card@1
id: P-RASP22A
kind: problem
title: 'True or false on integral inequalities, $L^2$ convergence, and Radon measures'
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
  note: Checked against Problem 1 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: chatgpt
  date: 2026-10-31
  note: >-
    Statement 3 is false without a countability hypothesis on X. The former
    proof used inner regularity on every Borel set and omitted outer
    regularity of the restricted measure. An uncountable disjoint union
    of convergent sequences gives a Radon measure whose restriction to
    the open set of isolated points is not outer regular.
---

::: {.problem}
Determine if each of the following statements is true or false.

1. If $f, g : \RR \to \RR$ belong to $L^1(\RR)$ and satisfy $\int_{-\infty}^{x} f(t)\,dt \leq \int_{-\infty}^{x} g(t)\,dt$ for all $x \in \RR$, then $f \leq g$ almost everywhere.

2. Let $(X, \mathcal{M}, \mu)$ be a finite measure space, and let $f_n \in L^2(X)$ be a sequence.
   If $\sup_{n \in \NN} \norm{f_n}_2 < \infty$ and $f_n \to f$ almost everywhere, then $\int_X f_n\,d\mu \to \int_X f\,d\mu$.

3. Let $\mu$ be a Radon measure on an LCH space $X$ and let $A$ be an open subset of $X$.
   Define $\mu_A(E) = \mu(A \cap E)$.
   Then $\mu_A$ is a Radon measure.
:::

::: {.solution}

::: pf

::: pf-step

Statement 1 is false.

::: pf-proof

Take $g=0$ and
$$
f=-\mathbf1_{(0,1)}+\mathbf1_{(1,2)}.
$$
Then $f,g\in L^1(\RR)$. Its cumulative integral is
$$
\int_{-\infty}^x f(t)\,dt
=
\begin{cases}
0,&x\le0,\\
-x,&0<x\le1,\\
x-2,&1<x\le2,\\
0,&x>2,
\end{cases}
$$
which is always $\le0=\int_{-\infty}^xg$. But $f=1>0=g$ on $(1,2)$. Thus the asserted pointwise a.e. order does not follow.

:::

:::

::: pf-step

Statement 2 is true.

::: pf-proof

Let
$$
M:=\sup_n\norm{f_n}_2<\infty.
$$
By Fatou,
$$
\norm{f}_2^2\le\liminf_n\norm{f_n}_2^2\le M^2,
$$
so $f\in L^2(X)$. Since $\mu(X)<\infty$, for every measurable $E$,
$$
\int_E\abs{f_n}\,d\mu
\le \norm{f_n}_2\mu(E)^{1/2}
\le M\mu(E)^{1/2}.
$$
Thus $(f_n)$ is uniformly integrable in $L^1$. Since $f_n\to f$ almost everywhere, it also converges to $f$ in measure. Vitali's theorem therefore gives
$$
\norm{f_n-f}_1\to0.
$$
Hence
$$
\abs{\int_Xf_n\,d\mu-\int_Xf\,d\mu}
\le\norm{f_n-f}_1\to0.
$$

:::

:::

::: pf-step

Statement 3 is false.

::: pf-proof

Let $I$ be uncountable. For each $i\in I$, take a copy
$$
X_i=\{0\}\cup\{1/n:n\ge1\}
$$
of the convergent sequence, and let $X$ be their topological disjoint
union. It is locally compact and Hausdorff. Give $0$ mass $1$ and $1/n$
mass $2^{-n}$ in each component. The resulting atomic Borel measure
$\mu$ is finite on compact sets: a compact subset of $X$ meets only
finitely many components, each of total mass $2$.

Every open set is inner regular, since its measure is the supremum of
the masses of its finite subsets. The measure is also outer regular.
If a Borel set $B$ has infinite mass, this is immediate. If $\mu(B)$ is
finite, $B$ contains at most countably many points because every point
has positive mass. The points $1/n$ are isolated. At each point $0$
in $B$, choose a neighborhood whose additional tail mass is as small
as desired. Doing this for the countably many such points, with
summable error bounds, gives for every $\varepsilon>0$ an open
$U\supseteq B$ with $\mu(U)\le\mu(B)+\varepsilon$. Thus $\mu$ is Radon.

Let $A$ be the set of all isolated points $1/n$ in all components, and
let $E=X\setminus A$ be the set of all limit points $0$. Then $A$ is
open and $\mu_A(E)=0$. Every open neighborhood $U$ of $E$ contains a
tail of isolated points in each of the uncountably many components.
Each such tail has positive $\mu_A$-mass, so $\mu_A(U)=\infty$. Hence
$$
\inf_{U\supseteq E,\ U\text{ open}}\mu_A(U)=\infty
>\mu_A(E)=0.
$$
The restriction is not outer regular and therefore is not Radon.

:::

:::

:::

:::
