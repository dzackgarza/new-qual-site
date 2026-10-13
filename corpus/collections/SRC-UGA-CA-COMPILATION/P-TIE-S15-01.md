---
schema: qual/card@1
id: P-TIE-S15-01
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 1.
---

::: {.problem}
Let $a _ { n } ( z )$ be an analytic sequence in a domain D such that $\sum _ { n = 0 } ^ { \infty } | a _ { n } ( z ) |$ converges uniformly on bounded and closed sub-regions of D. Show that $\sum _ { n = 0 } ^ { \infty } \left| a _ { n } ^ { \prime } ( z ) \right|$ converges uniformly on bounded and closed sub-regions of D.
:::

::: {.solution}
Let $K\subset D$ be an arbitrary bounded closed subregion.

<1>1. There exists $\delta>0$ such that
$$
K_\delta
\coloneqq
\{w\in\CC:\operatorname{dist}(w,K)\le\delta\}
$$
is a compact subset of $D$.

::: {.proof}
Since $K$ is compact and $D$ is open,
$$
d\coloneqq\operatorname{dist}(K,\CC\setminus D)>0.
$$
Choose $0<\delta<d$. Then every point at distance at most $\delta$ from $K$ still lies in $D$. The set $K_\delta$ is closed and bounded, hence compact.
:::

<1>2. For every $z\in K$ and every $n\ge0$,
$$
\abs{a_n'(z)}
\le
\frac1{2\pi\delta}
\int_0^{2\pi}
\abs{a_n(z+\delta e^{it})}\,dt.
$$

::: {.proof}
The closed disk $\abs{w-z}\le\delta$ lies in $D$ by step <1>1. Cauchy's integral formula for derivatives gives
$$
a_n'(z)
=
\frac1{2\pi i}
\int_{\abs{w-z}=\delta}
\frac{a_n(w)}{(w-z)^2}\,dw.
$$
Parametrize the circle by $w=z+\delta e^{it}$. Taking absolute values yields the stated inequality.
:::

<1>3. For integers $M\ge N$ and every $z\in K$,
$$
\sum_{n=N}^{M}\abs{a_n'(z)}
\le
\frac1\delta
\sup_{w\in K_\delta}
\sum_{n=N}^{M}\abs{a_n(w)}.
$$

::: {.proof}
Sum the estimate in step <1>2 over $n=N,\ldots,M$:
$$
\begin{aligned}
\sum_{n=N}^{M}\abs{a_n'(z)}
&\le
\frac1{2\pi\delta}
\int_0^{2\pi}
\sum_{n=N}^{M}
\abs{a_n(z+\delta e^{it})}\,dt\\
&\le
\frac1\delta
\sup_{w\in K_\delta}
\sum_{n=N}^{M}\abs{a_n(w)}.
\end{aligned}
$$
:::

<1>4. The series
$$
\boxed{
\sum_{n=0}^{\infty}\abs{a_n'(z)}
}
$$
converges uniformly on $K$.

::: {.proof}
By hypothesis,
$$
\sum_{n=0}^{\infty}\abs{a_n(w)}
$$
converges uniformly on the bounded closed set $K_\delta$. Hence its tails satisfy
$$
\sup_{w\in K_\delta}
\sum_{n=N}^{M}\abs{a_n(w)}
\longrightarrow0
$$
as $N,M\to\infty$ with $M\ge N$. Step <1>3 therefore gives
$$
\sup_{z\in K}
\sum_{n=N}^{M}\abs{a_n'(z)}
\longrightarrow0.
$$
Thus the derivative series is uniformly Cauchy on $K$, and hence converges uniformly there.
:::

<1>5. Q.E.D.

::: {.proof}
The bounded closed subregion $K$ was arbitrary, so step <1>4 proves the assertion on every such subregion of $D$.
:::
:::
