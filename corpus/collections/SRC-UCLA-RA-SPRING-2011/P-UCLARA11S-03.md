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
Let $\mu$ be a Borel probability measure on $\RR$ and define
$$
f(t)=\int_{\RR}e^{itx}\,d\mu(x).
$$
Suppose that
$$
\lim_{t\to0}\frac{f(0)-f(t)}{t^2}=0.
$$
Show that $\mu$ is supported at $\{0\}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
$$
f(0)=1
$$
and
$$
\operatorname{Re}(f(0)-f(t))
=
\int_{\RR}(1-\cos(tx))\,d\mu(x).
$$


::: pf-proof

Since $\mu$ is a probability measure,
$$
f(0)
=
\int_{\RR}1\,d\mu
=1.
$$
Also
$$
\operatorname{Re}f(t)
=
\int_{\RR}\cos(tx)\,d\mu(x),
$$
so subtracting from $f(0)=1$ gives the identity.

:::

:::

::: {.pf-step #s1-2}

The hypothesis implies
$$
\lim_{t\to0}
\int_{\RR}
\frac{1-\cos(tx)}{t^2}
\,d\mu(x)
=
0.
$$


::: pf-proof

The assumed complex limit
$$
\frac{f(0)-f(t)}{t^2}\longrightarrow0
$$
implies convergence of its real part to $0$. Apply step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\int_{\RR}x^2\,d\mu(x)=0.
$$


::: pf-proof

For $t\ne0$ and every $x$,
$$
\frac{1-\cos(tx)}{t^2}\ge0.
$$
Moreover,
$$
\lim_{t\to0}
\frac{1-\cos(tx)}{t^2}
=
\frac{x^2}{2}.
$$
Choose any sequence $t_n\to0$ with $t_n\ne0$. Fatou's lemma and step [](#s1-2){.pf-ref} give
$$
\begin{aligned}
\frac12
\int_{\RR}x^2\,d\mu(x)
&=
\int_{\RR}
\liminf_{n\to\infty}
\frac{1-\cos(t_nx)}{t_n^2}
\,d\mu(x)\\
&\le
\liminf_{n\to\infty}
\int_{\RR}
\frac{1-\cos(t_nx)}{t_n^2}
\,d\mu(x)\\
&=
0.
\end{aligned}
$$
The integral of $x^2$ is nonnegative, so it must vanish.

:::

:::

::: {.pf-step #s1-4}

The measure $\mu$ is supported at $\{0\}$.


::: pf-proof

For every $\delta>0$,
$$
x^2\ge\delta^2
\qquad
\text{on }\{|x|\ge\delta\}.
$$
Hence step [](#s1-3){.pf-ref} gives
$$
0
=
\int x^2\,d\mu
\ge
\delta^2
\mu(\{|x|\ge\delta\}),
$$
so
$$
\mu(\{|x|\ge\delta\})=0.
$$
Taking
$$
\delta=1/m
$$
for $m\ge1$,
$$
\RR\setminus\{0\}
=
\bigcup_{m=1}^{\infty}
\{|x|\ge1/m\},
$$
so
$$
\mu(\RR\setminus\{0\})=0.
$$
Thus $\mu$ is supported at $0$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the desired conclusion.

:::

:::

:::
