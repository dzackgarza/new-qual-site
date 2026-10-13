---
schema: qual/card@1
id: P-UCLARA11S-03
kind: problem
title: A characteristic-function flatness condition forces a probability measure to be supported at zero
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
Let $\mu$ be a Borel probability measure on $\mathbb R$ and define
\[
f(t)=\int_{\mathbb R}e^{itx}\,d\mu(x).
\]
Suppose that
\[
\lim_{t\to0}\frac{f(0)-f(t)}{t^2}=0.
\]
Show that $\mu$ is supported at $\{0\}$.
:::

::: {.solution}
<1>1. One has
\[
f(0)=1
\]
and
\[
\operatorname{Re}(f(0)-f(t))
=
\int_{\mathbb R}(1-\cos(tx))\,d\mu(x).
\]

::: {.proof}
Since $\mu$ is a probability measure,
\[
f(0)
=
\int_{\mathbb R}1\,d\mu
=1.
\]
Also
\[
\operatorname{Re}f(t)
=
\int_{\mathbb R}\cos(tx)\,d\mu(x),
\]
so subtracting from $f(0)=1$ gives the identity.
:::

<1>2. The hypothesis implies
\[
\lim_{t\to0}
\int_{\mathbb R}
\frac{1-\cos(tx)}{t^2}
\,d\mu(x)
=
0.
\]

::: {.proof}
The assumed complex limit
\[
\frac{f(0)-f(t)}{t^2}\longrightarrow0
\]
implies convergence of its real part to $0$. Apply step <1>1.
:::

<1>3. One has
\[
\int_{\mathbb R}x^2\,d\mu(x)=0.
\]

::: {.proof}
For $t\ne0$ and every $x$,
\[
\frac{1-\cos(tx)}{t^2}\ge0.
\]
Moreover,
\[
\lim_{t\to0}
\frac{1-\cos(tx)}{t^2}
=
\frac{x^2}{2}.
\]
Choose any sequence $t_n\to0$ with $t_n\ne0$. Fatou's lemma and step <1>2 give
\[
\begin{aligned}
\frac12
\int_{\mathbb R}x^2\,d\mu(x)
&=
\int_{\mathbb R}
\liminf_{n\to\infty}
\frac{1-\cos(t_nx)}{t_n^2}
\,d\mu(x)\\
&\le
\liminf_{n\to\infty}
\int_{\mathbb R}
\frac{1-\cos(t_nx)}{t_n^2}
\,d\mu(x)\\
&=
0.
\end{aligned}
\]
The integral of $x^2$ is nonnegative, so it must vanish.
:::

<1>4. The measure $\mu$ is supported at $\{0\}$.

::: {.proof}
For every $\delta>0$,
\[
x^2\ge\delta^2
\qquad
\text{on }\{|x|\ge\delta\}.
\]
Hence step <1>3 gives
\[
0
=
\int x^2\,d\mu
\ge
\delta^2
\mu(\{|x|\ge\delta\}),
\]
so
\[
\mu(\{|x|\ge\delta\})=0.
\]
Taking
\[
\delta=1/m
\]
for $m\ge1$,
\[
\mathbb R\setminus\{0\}
=
\bigcup_{m=1}^{\infty}
\{|x|\ge1/m\},
\]
so
\[
\mu(\mathbb R\setminus\{0\})=0.
\]
Thus $\mu$ is supported at $0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the desired conclusion.
:::
:::
