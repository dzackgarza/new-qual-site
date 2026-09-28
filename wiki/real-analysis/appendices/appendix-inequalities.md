---
title: Common inequalities
order: 23
---

# Common inequalities

## Cauchy--Schwarz, Hölder, and Plancherel

[[PR-X5D4Z]]

::: {.remark title="Cauchy--Schwarz in coordinates and in $L^2$"}
For $a,b\in\RR^n$ and for $f,g\in L^2(\RR^n)$, the inequality reads
$$
\begin{aligned}
\left(\sum_{k=1}^{n} a_{k} b_{k}\right)^{2}
&\leq\left(\sum_{k=1}^{n} a_{k}^{2}\right)\left(\sum_{k=1}^{n} b_{k}^{2}\right), \\
\abs{\int_{\RR^{n}} f(x) \overline{g(x)} \dx}^{2}
&\leq \int_{\RR^{n}}\abs{f(x)}^{2} \dx \int_{\RR^{n}}\abs{g(x)}^{2} \dx.
\end{aligned}
$$

:::

[[PR-IJOPU]]

[[PR-7BGSE]]

::: {.proof title="Hölder's inequality"}
If $\norm f_p=0$ or $\norm g_q=0$, then $fg=0$ almost everywhere; if either norm is infinite there is nothing to prove.
Otherwise, replacing $f$ and $g$ by $f/\norm f_p$ and $g/\norm g_q$, it suffices to treat $\norm{f}_p = \norm{g}_q = 1$.
For $1<p<\infty$, Young's product inequality $AB \leq \frac 1 p A^p + \frac 1 q B^q$ for $A,B\geq0$ gives
$$
\int\abs{f}\abs{g} \leq \int \qty{\frac{\abs{f}^{p}}{p} + \frac{\abs{g}^{q}}{q}}=\frac{1}{p}+\frac{1}{q}=1.
$$
For $p=1$, $q=\infty$, $\int\abs{fg}\leq\norm g_\infty\int\abs f$.

:::

::: {.proposition title="Inclusions of $L^p$ spaces"}
If $\mu(X)<\infty$ and $1 \leq p < q \leq \infty$, then $L^q(\mu) \subseteq L^p(\mu)$ and $\norm f_p\leq\mu(X)^{\frac1p-\frac1q}\norm f_q$.
For sequences, $\ell^p \subseteq \ell^q$.

:::

::: {.proof}
For $q=\infty$, $\int\abs f^p\leq\mu(X)\norm f_\infty^p$.
For $q<\infty$, let $r \coloneqq q/p>1$ and $s \coloneqq r/(r-1)$, so $\frac1r+\frac1s = 1$, and let $h \coloneqq \abs{f}^p$.
By Hölder's inequality,
$$
\norm{f}_p^p
= \norm{h\cdot 1}_1 \leq \norm{h}_r\norm{1}_s
= \norm{f}_q^{p}\,\mu(X)^{\frac 1 s},
$$
and $\frac{1}{ps} = \frac1p\qty{1-\frac pq} = \frac 1 p - \frac 1 q$.

For sequences, if $x\in\ell^p$ then $x_n\to0$, so $\abs{x_n}\leq1$ for $n\geq N$, and then $\abs{x_n}^q \leq \abs{x_n}^p$ for $n\geq N$; hence $x\in\ell^q$.

:::

[[PR-RYVI7]]

[[PR-ZI7M3]]

::: {.remark title="Parseval's identity for Fourier series"}
For $f\in L^2(-\pi,\pi)$ and the orthonormal basis $\theset{e^{ikx}/\sqrt{2\pi}}_{k\in\ZZ}$, Parseval's identity reads
$$
{1\over 2\pi} \int_{(-\pi, \pi)} \abs{f}^2 = \sum_{k\in \ZZ} \abs{c_k}^2, \qquad c_k \coloneqq {1\over 2\pi } \int_{(-\pi, \pi)} f(x) e^{-ikx} \dx.
$$

:::

[[PR-JCZKL]]

## Chebyshev, Minkowski, and Young

[[PR-YO7MV]]

[[FD-3BK6U]]

[[PR-XUVZY]]

::: {.remark}
For $p=\infty$, $\abs{f+g}\leq\norm f_\infty+\norm g_\infty$ almost everywhere, so $\norm{f+g}_\infty\leq\norm f_\infty+\norm g_\infty$.
Together with the case $1\leq p<\infty$, Minkowski's inequality is the triangle inequality for $\norm{\wait}_p$, so $L^p$ is a normed space for $1\leq p\leq\infty$.

:::

::: {.proof title="Minkowski's inequality"}
For $p=1$ the inequality follows by integrating $\abs{f+g}\leq\abs f+\abs g$.
Let $1<p<\infty$ with conjugate exponent $q = \frac{p}{p-1}$, so that $(p-1)q = p$.
Since $\abs{f+g}^p\leq 2^{p-1}\qty{\abs f^p+\abs g^p}$, $\norm{f+g}_p<\infty$; assume $\norm{f+g}_p>0$.
Since $\abs{f+g}^p \leq \qty{\abs{f} + \abs{g}} \abs{f+g}^{p-1}$, Hölder's inequality gives
$$
\begin{aligned}
\norm{f+g}_p^p
&\leq \int \abs{f} \abs{f+g}^{p-1} + \int \abs{g} \abs{f+g}^{p-1} \\
&\leq \qty{\norm{f}_p + \norm{g}_p} \norm{\abs{f+g}^{p-1}}_q \\
&= \qty{\norm{f}_p + \norm{g}_p} \qty{\int \abs{f+g}^{p}}^{1 - \frac 1 p} \\
&= \qty{\norm{f}_p + \norm{g}_p} \norm{f+g}_p^{p-1}.
\end{aligned}
$$
Dividing by $\norm{f+g}_p^{p-1}$ gives $\norm{f+g}_p \leq \norm{f}_p + \norm{g}_p$.

:::

[[PR-2C3SZ]]

::: {.remark title="Special cases of Young's convolution inequality"}
For conjugate exponents $p,q$ and $1\leq p\leq\infty$,
$$
\begin{aligned}
\norm{f\ast g}_1      & \leq \norm{f}_1 \norm{g}_1, \\
\norm{f\ast g}_p      & \leq \norm{f}_1 \norm{g}_p, \\
\norm{f\ast g}_\infty & \leq \norm{f}_p \norm{g}_q, \\
\norm{f\ast g}_\infty & \leq \norm{f}_2 \norm{g}_2.
\end{aligned}
$$

:::

## Elementary inequalities

[[PR-IQYTA]]

[[PR-W4ICW]]

[[PR-BPOH2]]

[[PR-7KTA6]]

[[FF-Z3E3C]]

[[PR-CHY3F]]

::: {.proof}
Let $g(t)\coloneqq e^t-1-t$.
Then $g(0)=0$ and $g'(t) = e^t-1$ is negative for $t<0$ and positive for $t>0$, so $g$ attains its minimum $0$ at $t=0$ and $g\geq0$ on $\RR$.

:::

::: {.fact}
For $x,y\geq0$, $\sqrt{x + y} \leq \sqrt{x} + \sqrt{y}$, since $\qty{\sqrt x+\sqrt y}^2 = x+y+2\sqrt{xy}\geq x+y$.

:::
