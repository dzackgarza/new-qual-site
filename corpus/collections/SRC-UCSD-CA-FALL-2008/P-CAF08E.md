---
schema: qual/card@1
id: P-CAF08E
kind: problem
title: "Periodic entire function with subexponential growth must vanish"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Suppose that $f(z)$ is an entire function satisfying $f(z) = f(z + 1)$ for all $z$.
If there exists a real number $c$, with $c \neq 2\pi k$, $k \in \ZZ$, such that $\abs{f(z)} \leq e^{c\,\operatorname{Im} z}$ for all $z \in \CC$, prove that $f \equiv 0$.
:::

::: {.solution}

The argument is the card's own, by the Fourier expansion of a periodic entire function; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $f$ be entire with $f(z+1)=f(z)$ for all $z$ and $\abs{f(z)}\le e^{c\operatorname{Im}z}$ for some real $c$ with $c\ne2\pi k$ for every $k\in\ZZ$.

::: pf

::: {.pf-step #descent}
There is a holomorphic $F$ on $\CC^{*}=\CC\setminus\{0\}$ with $F(e^{2\pi iz})=f(z)$, and $f(z)=\sum_{n\in\ZZ}a_{n}e^{2\pi inz}$ with $F(w)=\sum_{n}a_{n}w^{n}$ its Laurent expansion at $0$.

::: pf-proof
The exponential $w=e^{2\pi iz}$ is surjective onto $\CC^{*}$ and any two of its values at points $z,z'$ with equal image differ by an integer, so $F(w):=f(z)$ for any $z$ with $e^{2\pi iz}=w$ is well defined by the $1$-periodicity of $f$; it is holomorphic because locally $z\mapsto\log w/(2\pi i)$ is a holomorphic branch of the inverse. The Laurent expansion $F(w)=\sum_{n\in\ZZ}a_{n}w^{n}$ converges on $\CC^{*}$, and substituting $w=e^{2\pi iz}$ gives the displayed Fourier series, convergent for every $z$.
:::

:::

::: {.pf-step #bound}
$\abs{a_{n}}\le e^{(c+2\pi n)y}$ for every $n\in\ZZ$ and every $y\in\RR$.

::: pf-proof
Write $z=x+iy$ with $x,y$ real. For each $n$, the function $x\mapsto f(x+iy)e^{-2\pi inx}$ is $1$-periodic and continuous, so its $n$-th Fourier coefficient on one period is
$$
\int_{0}^{1}f(x+iy)e^{-2\pi inx}\,dx=\int_{0}^{1}\sum_{m}a_{m}e^{2\pi im(x+iy)}e^{-2\pi inx}\,dx=a_{n}e^{-2\pi ny},
$$
the interchange of sum and integral being justified by uniform convergence of the series in $x$ for fixed $y$ (its terms are bounded by $\abs{a_{m}}e^{-2\pi my}$, summable over $m$). Estimating the integral by the sup norm and using the growth hypothesis,
$$
\abs{a_{n}}e^{-2\pi ny}\le\int_{0}^{1}\abs{f(x+iy)}\,dx\le e^{cy},
$$
which gives the bound.
:::

:::

::: {.pf-step #vanish}
$a_{n}=0$ for every $n\in\ZZ$.

::: pf-proof
Fix $n$. If $c+2\pi n>0$, the bound $\abs{a_{n}}\le e^{(c+2\pi n)y}$ with $y\to-\infty$ forces $a_{n}=0$. If $c+2\pi n<0$, the same bound with $y\to+\infty$ forces $a_{n}=0$. The remaining case is $c+2\pi n=0$, that is $c=-2\pi n=2\pi(-n)$, which the hypothesis $c\ne2\pi k$ for all $k\in\ZZ$ excludes. So $a_{n}=0$.
:::

:::

::: {.pf-step #zero}
$f\equiv0$.

::: pf-proof
By step [](#vanish){.pf-ref} every Laurent coefficient of $F$ vanishes, so $F\equiv0$ on $\CC^{*}$ and hence $f(z)=F(e^{2\pi iz})=0$ for every $z\in\CC$.
:::

:::

:::
:::
