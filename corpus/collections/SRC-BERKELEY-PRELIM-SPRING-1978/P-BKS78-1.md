---
schema: qual/card@1
id: P-BKS78-1
kind: problem
title: Uniform convergence of $x^k/(x^2+n)$ on bounded and unbounded sets
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
---

::: {.problem}
Let $k\ge0$ be an integer and define
\[
f_n(x)=\frac{x^k}{x^2+n},\qquad x\in\mathbb R,\quad n=1,2,\ldots.
\]
For which values of $k$ does $(f_n)$ converge uniformly on $\mathbb R$? For which values does it converge uniformly on every bounded subset of $\mathbb R$?
:::

::: {.solution}
<1>1. For every integer $k\geq0$ and every fixed $x\in\mathbb R$,
$$
f_n(x)\longrightarrow0.
$$

::: {.proof}
For fixed $x$, the numerator $x^k$ is constant in $n$, while
$$
x^2+n\longrightarrow\infty.
$$
Hence
$$
\frac{x^k}{x^2+n}\longrightarrow0.
$$
:::

<1>2. For every $k\geq0$, the convergence $f_n\to0$ is uniform on every bounded subset of $\mathbb R$.

::: {.proof}
Let $S\subseteq\mathbb R$ be bounded. Choose $M\geq1$ such that
$$
|x|\leq M
$$
for every $x\in S$. Then
$$
|f_n(x)|
=
\frac{|x|^k}{x^2+n}
\leq
\frac{M^k}{n}
$$
for every $x\in S$. Therefore
$$
\sup_{x\in S}|f_n(x)|
\leq
\frac{M^k}{n}
\longrightarrow0.
$$
:::

<1>3. For $k=0$, the convergence is uniform on $\mathbb R$.

::: {.proof}
One has
$$
0<f_n(x)
=
\frac1{x^2+n}
\leq
\frac1n
$$
for every $x\in\mathbb R$. Hence
$$
\sup_{x\in\mathbb R}|f_n(x)|
=
\frac1n
\longrightarrow0.
$$
:::

<1>4. For $k=1$,
$$
\sup_{x\in\mathbb R}|f_n(x)|
=
\frac1{2\sqrt n},
$$
so the convergence is uniform on $\mathbb R$.

::: {.proof}
Because the expression is even after taking absolute values, set $t=|x|\geq0$ and consider
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

<1>5. For $k=2$, the convergence is not uniform on $\mathbb R$.

::: {.proof}
One has
$$
f_n(x)=\frac{x^2}{x^2+n}.
$$
For every fixed $n$,
$$
\lim_{|x|\to\infty}f_n(x)=1.
$$
Hence
$$
\sup_{x\in\mathbb R}|f_n(x)|=1
$$
for every $n$, so the suprema do not tend to $0$.
:::

<1>6. For every $k>2$, the convergence is not uniform on $\mathbb R$.

::: {.proof}
For fixed $n$,
$$
|f_n(x)|
=
\frac{|x|^k}{x^2+n}
\sim
|x|^{k-2}
$$
as $|x|\to\infty$. Since $k-2>0$,
$$
|f_n(x)|\longrightarrow\infty.
$$
Thus $f_n$ is unbounded on $\mathbb R$ for every $n$, and in particular
$$
\sup_{x\in\mathbb R}|f_n(x)|\neq\longrightarrow0.
$$
:::

<1>7. Therefore
$$
\boxed{
\text{$f_n\to0$ uniformly on $\mathbb R$ exactly for $k=0,1$}
}
$$
and
$$
\boxed{
\text{$f_n\to0$ uniformly on every bounded subset for every $k\geq0$.}
}
$$

::: {.proof}
Steps <1>3--<1>6 classify uniform convergence on $\mathbb R$, and step <1>2 handles every bounded subset.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 gives both requested classifications.
:::
:::
