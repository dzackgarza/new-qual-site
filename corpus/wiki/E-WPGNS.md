---
schema: qual/card@1
id: E-WPGNS
kind: exercise
title: "Let $f$ be entire and suppose that"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $f$ be entire and suppose that
$\lim_{z \rightarrow \infty} f(z) = \infty$. Show that $f$ is a polynomial.
:::

:::{.solution}
Note that $f$ has finitely many zeros: since $f$ is unbounded, there is some $R$ such that $f(\DD_R^c) \subseteq \DD^c$, so in particular $f$ is nonvanishing on $\DD_R^c$.
So $Z_f$ is a closed subset of a compact set, so is either finite or has an accumulation point.
In the latter case, $f\equiv 0$ by the identity principle, so suppose not.

Write $Z_f = \ts{z_k}_{k\leq n}$ for the $n$ many zeros of $f$, included with multiplicity, and set 
\[
\Phi(z) \da \prod_{k\leq n} (z-z_k), \qquad F(z) \da {\Phi(z) \over f(z) }
.\]
Now $F$ is a nonvanishing entire function.

:::{.claim}
$F$ is bounded on $\CC$.
:::

:::{.proof title="of claim"}
Choose $R\gg 1$ so that all of $z_k$ are in $\DD_R$, so $\abs{\xi - z_k} < R$ for all $\xi \in \DD_R$ and all $k$.
By Cauchy's integral formula,
\[
\abs{F(z)} 
&\leq {1\over 2\pi} \oint_{\abs{\xi} = R} \abs{F(\xi) \over \xi} \dxi \\
&={1\over 2\pi} \oint_{\abs{\xi} = R} \abs{\Psi(\xi) \over f(\xi) \cdot \xi} \dxi \\
&\leq {1\over 2\pi} \oint_{\abs{\xi} = R} {R^m \over \abs{ f(\xi) } R } \dxi \\
&\leq {1\over 2\pi} \oint_{\abs{\xi} = R} R^{m-1} \dxi \\
&= R^m
,\]
where $R$ is increased if necessary to ensure $\abs{1\over f(z)} < 1$, which can be done since $\abs{f(z)}\to \infty$ as $R\to \infty$.
So $\abs{F(z)} \leq C\abs{z}^m$ in $\bar{\DD_R}^c$ for $R$ large enough, making $F$ a polynomial of degree at most $m$.
Since $F$ is continuous in $\bar{\DD_R}$ which is compact, $F$ is bounded in here as well, making $F$ bounded on all of $\CC$.
:::

Given this, $F$ is entire and bounded and thus constant by Liouville.
So $F(z) = c$, and as a result $f(z) = c\Phi(z)$ which is a polynomial of degree $n$.
:::
