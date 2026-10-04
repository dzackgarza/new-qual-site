---
schema: qual/card@1
id: P-TIE-F09-15
kind: problem
title: Termwise differentiation of locally uniformly absolutely convergent series of analytic functions
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2009, question 15.
---

::: {.problem}
Let $a _ { n } ( z )$ be an analytic sequence in a domain D such that $\sum _ { n = 0 } ^ { \infty } | a _ { n } ( z ) |$ converges uniformly on bounded and closed sub-regions of D. Show that $\sum _ { n = 0 } ^ { \infty } \left| a _ { n } ^ { \prime } ( z ) \right|$ converges uniformly on bounded and closed sub-regions of $D .$
:::

::: {.solution}
Let $K$ be an arbitrary bounded closed subregion compactly contained in $D$.

<1>1. There exists $\rho>0$ such that
$$
K_\rho
=
\{w\in\CC:\operatorname{dist}(w,K)\le\rho\}
$$
is a bounded closed subset of $D$.

::: {.proof}
Since $K$ is compact and $\CC\setminus D$ is closed and disjoint from $K$,
$$
d=\operatorname{dist}(K,\CC\setminus D)>0.
$$
Choose $0<\rho<d$. Then every point at distance at most $\rho$ from $K$ still lies in $D$,
and $K_\rho$ is compact.
:::

<1>2. For every $\varepsilon>0$, there is $N$ such that for all $M\ge N$ and all
$w\in K_\rho$,
$$
\sum_{n=N}^{M}|a_n(w)|<\rho\varepsilon.
$$

::: {.proof}
The compact set $K_\rho$ is covered by finitely many closed disks whose slightly larger closed
disks still lie in $D$. By hypothesis the series
$$
\sum_{n=0}^{\infty}|a_n(w)|
$$
converges uniformly on each of those bounded closed subregions. Taking the maximum of the
finitely many resulting Cauchy thresholds gives one $N$ for which every finite tail beginning
at $N$ has the displayed bound throughout $K_\rho$.
:::

<1>3. Fix $z\in K$ and integers $M\ge N$. There exist complex numbers
$\lambda_N,\ldots,\lambda_M$ with $|\lambda_n|=1$ such that
$$
\sum_{n=N}^{M}|a_n'(z)|
=
\left|
\sum_{n=N}^{M}\lambda_na_n'(z)
\right|.
$$

::: {.proof}
For each $n$, if $a_n'(z)\ne0$, choose
$$
\lambda_n=\frac{\overline{a_n'(z)}}{|a_n'(z)|},
$$
so that $\lambda_na_n'(z)=|a_n'(z)|$. If $a_n'(z)=0$, choose any $\lambda_n$ of modulus
$1$. Summing gives the equality.
:::

<1>4. For every $z\in K$ and every $M\ge N$,
$$
\sum_{n=N}^{M}|a_n'(z)|<\varepsilon.
$$

::: {.proof}
For the phases chosen in step <1>3, put
$$
A(\zeta)=\sum_{n=N}^{M}\lambda_na_n(\zeta).
$$
This is analytic on $D$, and
$$
A'(z)=\sum_{n=N}^{M}\lambda_na_n'(z).
$$
The circle $|\zeta-z|=\rho$ lies in $K_\rho$. Cauchy's derivative formula and step <1>3 give
$$
\begin{aligned}
\sum_{n=N}^{M}|a_n'(z)|
&=
|A'(z)|\\
&\le
\frac1\rho
\max_{|\zeta-z|=\rho}|A(\zeta)|\\
&\le
\frac1\rho
\max_{|\zeta-z|=\rho}
\sum_{n=N}^{M}|a_n(\zeta)|.
\end{aligned}
$$
Step <1>2 makes the last quantity strictly less than $\varepsilon$.
:::

<1>5. The series
$$
\boxed{
\sum_{n=0}^{\infty}|a_n'(z)|
}
$$
converges uniformly on $K$.

::: {.proof}
Step <1>4 shows that for every $\varepsilon>0$ there exists $N$ such that every finite tail
from $N$ onward is bounded by $\varepsilon$, uniformly for $z\in K$. This is the uniform
Cauchy criterion for the series of nonnegative functions $|a_n'|$.
:::

<1>6. Q.E.D.

::: {.proof}
The bounded closed subregion $K\Subset D$ was arbitrary, so step <1>5 proves the asserted
local uniform absolute convergence throughout $D$.
:::
:::
