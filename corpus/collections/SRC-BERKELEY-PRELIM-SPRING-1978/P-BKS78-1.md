---
schema: qual/card@1
id: P-BKS78-1
kind: problem
title: Uniform convergence of $x^k/(x^2+n)$ on bounded and unbounded sets
classification: {areas: [prelim], topics: [Real Analysis]}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let $k\ge0$ be an integer and define
$$
f_n(x)=\frac{x^k}{x^2+n},\qquad x\in\RR,\quad n=1,2,\ldots.
$$
For which values of $k$ does $(f_n)$ converge uniformly on $\RR$? For which values does it converge uniformly on every bounded subset of $\RR$?
:::

::: {.solution}
::: pf

::: pf-step
For every integer $k\geq0$ and every fixed $x\in\RR$,
$$
f_n(x)\longrightarrow0.
$$

::: pf-proof
For fixed $x$, the numerator $x^k$ is constant in $n$, while
$$
x^2+n\longrightarrow\infty.
$$
Hence
$$
\frac{x^k}{x^2+n}\longrightarrow0.
$$
:::

:::

::: {.pf-step #bounded-subsets}
For every $k\geq0$, the convergence $f_n\to0$ is uniform on every bounded subset of $\RR$.

::: pf-proof
Let $S\subseteq\RR$ be bounded. Choose $M\geq1$ such that
$$
\abs{x}\leq M
$$
for every $x\in S$. Then
$$
\abs{f_n(x)}
=
\frac{\abs{x}^k}{x^2+n}
\leq
\frac{M^k}{n}
$$
for every $x\in S$. Therefore
$$
\sup_{x\in S}\abs{f_n(x)}
\leq
\frac{M^k}{n}
\longrightarrow0.
$$
:::

:::

::: {.pf-step #case-zero}
For $k=0$, the convergence is uniform on $\RR$.

::: pf-proof
One has
$$
0<f_n(x)
=
\frac1{x^2+n}
\leq
\frac1n
$$
for every $x\in\RR$. Hence
$$
\sup_{x\in\RR}\abs{f_n(x)}
=
\frac1n
\longrightarrow0.
$$
:::

:::

::: {.pf-step #case-one}
For $k=1$,
$$
\sup_{x\in\RR}\abs{f_n(x)}
=
\frac1{2\sqrt n},
$$
so the convergence is uniform on $\RR$.

::: pf-proof
Because the expression is even after taking absolute values, set $t=\abs{x}\geq0$ and consider
$$
\phi_n(t)=\frac{t}{t^2+n}.
$$
Its derivative is
$$
\phi_n'(t)
=
\frac{n-t^2}{(t^2+n)^2}.
$$
Thus $\phi_n$ increases on $[0,\sqrt n]$ and decreases on $[\sqrt n,\infty)$, so its maximum occurs at $t=\sqrt n$. There
$$
\phi_n(\sqrt n)
=
\frac{\sqrt n}{2n}
=
\frac1{2\sqrt n}.
$$
This tends to $0$.
:::

:::

::: {.pf-step #case-two}
For $k=2$, the convergence is not uniform on $\RR$.

::: pf-proof
One has
$$
f_n(x)=\frac{x^2}{x^2+n}.
$$
For every fixed $n$,
$$
\lim_{\abs{x}\to\infty}f_n(x)=1.
$$
Hence
$$
\sup_{x\in\RR}\abs{f_n(x)}=1
$$
for every $n$, so the suprema do not tend to $0$.
:::

:::

::: {.pf-step #case-greater-than-two}
For every $k>2$, the convergence is not uniform on $\RR$.

::: pf-proof
For fixed $n$,
$$
\abs{f_n(x)}
=
\frac{\abs{x}^k}{x^2+n}
\sim
\abs{x}^{k-2}
$$
as $\abs{x}\to\infty$. Since $k-2>0$,
$$
\abs{f_n(x)}\longrightarrow\infty.
$$
Thus $f_n$ is unbounded on $\RR$ for every $n$, and in particular
$$
\sup_{x\in\RR}\abs{f_n(x)}\neq\longrightarrow0.
$$
:::

:::

::: pf-step
Therefore
$$
\boxed{
\text{$f_n\to0$ uniformly on $\RR$ exactly for $k=0,1$}
}
$$
and
$$
\boxed{
\text{$f_n\to0$ uniformly on every bounded subset for every $k\geq0$.}
}
$$

::: pf-proof
[](#case-zero){.pf-ref}, [](#case-one){.pf-ref}, [](#case-two){.pf-ref}, and [](#case-greater-than-two){.pf-ref} classify uniform convergence on $\RR$, and [](#bounded-subsets){.pf-ref} handles every bounded subset.
:::

:::

:::

:::
