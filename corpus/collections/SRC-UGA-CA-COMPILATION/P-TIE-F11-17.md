---
schema: qual/card@1
id: P-TIE-F11-17
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
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 17.
---

::: {.problem}
Let $a_{n}(z)$ be an analytic sequence in a domain $D$ such that $\sum_{n=0}^{\infty} \abs{a_{n}(z)}$ converges uniformly on bounded and closed sub-regions of $D$. Show that $\sum_{n=0}^{\infty} \abs{a_{n}'(z)}$ converges uniformly on bounded and closed sub-regions of $D$.
:::

::: {.solution}

Let $K\subset D$ be an arbitrary bounded closed subregion.

::: pf

::: {.pf-step #s1-1}

There exists $\delta>0$ such that
$$
K_\delta
\coloneqq
\{w\in\CC:\operatorname{dist}(w,K)\le\delta\}
$$
is a compact subset of $D$.


::: pf-proof

Since $K$ is compact and $D$ is open,
$$
d\coloneqq\operatorname{dist}(K,\CC\setminus D)>0.
$$
Choose $0<\delta<d$. Then every point whose distance from $K$ is at most $\delta$ still lies in $D$. The set $K_\delta$ is closed and bounded, hence compact.

:::

:::

::: {.pf-step #s1-2}

For every $z\in K$, every $n\ge0$, and the circle
$$
C_z\coloneqq\{z+\delta e^{it}:0\le t\le2\pi\},
$$
one has
$$
\abs{a_n'(z)}
\le
\frac1{2\pi\delta}
\int_0^{2\pi}
\abs{a_n(z+\delta e^{it})}\,dt.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, the closed disk $\abs{w-z}\le\delta$ lies in $D$. Cauchy's integral formula for derivatives gives
$$
a_n'(z)
=
\frac1{2\pi i}
\int_{C_z}
\frac{a_n(w)}{(w-z)^2}\,dw.
$$
Parametrize $C_z$ by $w=z+\delta e^{it}$. Then $\abs{dw}=\delta\,dt$ and $\abs{w-z}=\delta$, so taking absolute values gives the asserted estimate.

:::

:::

::: {.pf-step #s1-3}

For integers $M\ge N$ and every $z\in K$,
$$
\sum_{n=N}^M\abs{a_n'(z)}
\le
\frac1\delta
\sup_{w\in K_\delta}
\sum_{n=N}^M\abs{a_n(w)}.
$$


::: pf-proof

Summing the estimate from step [](#s1-2){.pf-ref} and using the finiteness of the sum,
$$
\begin{aligned}
\sum_{n=N}^M\abs{a_n'(z)}
&\le
\frac1{2\pi\delta}
\int_0^{2\pi}
\sum_{n=N}^M
\abs{a_n(z+\delta e^{it})}\,dt\\
&\le
\frac1\delta
\sup_{w\in K_\delta}
\sum_{n=N}^M\abs{a_n(w)}.
\end{aligned}
$$
The points $z+\delta e^{it}$ lie in $K_\delta$, which justifies the last inequality.

:::

:::

::: {.pf-step #s1-4}

The series
$$
\boxed{
\sum_{n=0}^\infty\abs{a_n'(z)}
}
$$
converges uniformly on $K$.


::: pf-proof

By hypothesis, the series
$$
\sum_{n=0}^\infty\abs{a_n(w)}
$$
converges uniformly on the compact set $K_\delta$. Hence its tails satisfy
$$
\sup_{w\in K_\delta}
\sum_{n=N}^M\abs{a_n(w)}
\longrightarrow0
$$
as $N,M\to\infty$ with $M\ge N$. Step [](#s1-3){.pf-ref} therefore implies
$$
\sup_{z\in K}
\sum_{n=N}^M\abs{a_n'(z)}
\longrightarrow0.
$$
Thus the partial sums of $\sum\abs{a_n'(z)}$ are uniformly Cauchy on $K$, and hence the series converges uniformly there.

:::

:::

::: pf-qed

The bounded closed subregion $K\subset D$ was arbitrary, so step [](#s1-4){.pf-ref} proves the assertion on every such subregion.

:::

:::

:::
