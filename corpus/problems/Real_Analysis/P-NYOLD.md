---
schema: qual/card@1
id: P-NYOLD
kind: problem
title: $\sup_{y>0}|f*P_y|\le C\,Hf$ and $f*P_y\to f$ a.e. for the Poisson kernel
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - Approximations to the Identity
  - Convolution
  - Differentiation
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $f\in L^1(\RR)$ and let \( \mathcal{U}\definedas \theset{(x, y) \in \RR^2 \st y > 0}  \) denote the upper half plane.
For $(x, y) \in \mathcal{U}$ define 
\[
u(x, y) \definedas f \convolve P_y(x) && \text{where } P_y(x) \definedas {1\over \pi}\qty{y \over t^2 + y^2}
.\]

a. Prove that there exists a constant $C$ independent of $f$ such that for all $x\in \RR$, 
\[
\sup_{y > 0} \abs{ u(x, y) } \leq C\cdot Hf(x)
.\]

    *Hint: write the following and try to estimate each term:*
\[
u(x, y) = \int_{\abs t < y} f(x - t) P_y(t) \dt + \sum_{k=0}^{\infty } \int_{A_k} f(x-t) P_y(t)\dt && A_k \definedas \theset{2^ky \leq \abs t < 2^{k+1}y}
.\]

b. Following the proof of the Lebesgue differentiation theorem, show that for $f\in L^1(\RR)$ and for almost every $x\in \RR$,
\[
u(x, y) \converges{y\to 0} \to f(x)
.\]
:::
::: {.solution}
Here $P_y(t) = \frac{1}{\pi}\frac{y}{t^2 + y^2}$, $u(x,y) = \int f(x-t)P_y(t)\,dt$, and $Hf(x) = \sup_{r>0}\frac{1}{2r}\int_{x-r}^{x+r}|f(s)|\,ds$ is the Hardy--Littlewood maximal function.

::: pf

::: {.pf-step #s1}

$\int_\RR P_y = 1$, $P_y(t) \le \frac{1}{\pi y}$ for all $t$, and $P_y(t) \le \frac{1}{\pi 2^{2k}y}$ on $A_k = \theset{2^k y \le |t| < 2^{k+1}y}$.

::: pf-proof

The substitution $t = ys$ gives $\int P_y = \frac1\pi\int\frac{ds}{1+s^2} = 1$. The bounds follow from $t^2 + y^2 \ge y^2$ and, on $A_k$, $t^2 + y^2 \ge 2^{2k}y^2$.

:::

:::

::: {.pf-step #s2}

For $g \in L^1$, $x \in \RR$ and $y > 0$, $\int |g(x-t)|P_y(t)\,dt \le \frac{10}{\pi}\sup_{0 < r \le R}\frac{1}{2r}\int_{x-r}^{x+r}|g|$ whenever $g(x - t) = 0$ for $|t| \ge R$ and $R \geq y$; with $R = \infty$ the right side is $\frac{10}{\pi}Hg(x)$.

::: pf-proof

Let $\alpha$ denote the supremum on the right. By step [](#s1){.pf-ref}, $\int_{|t| < y}|g(x-t)|P_y(t)\,dt \le \frac{1}{\pi y}\cdot 2y\,\alpha$. For each $k$ with $2^ky < R$, the set $A_k$ lies in $\theset{|t| < 2^{k+1}y}$, so $\int_{A_k}|g(x-t)|P_y(t)\,dt \le \frac{1}{\pi 2^{2k} y}\int_{|t| < \min(2^{k+1}y, R)}|g(x-t)|\,dt \le \frac{1}{\pi 2^{2k}y}\cdot 2^{k+2}y\,\alpha = \frac{4}{\pi 2^k}\alpha$; terms with $2^ky \ge R$ vanish. Summing, the total is at most $\left(\frac2\pi + \frac4\pi\sum_{k \ge 0}2^{-k}\right)\alpha = \frac{10}{\pi}\alpha$.

:::

:::

::: pf-step

$\sup_{y>0}|u(x,y)| \le \frac{10}{\pi}Hf(x)$ for every $x$.

::: pf-proof

$|u(x,y)| \le \int|f(x-t)|P_y(t)\,dt$; apply step [](#s2){.pf-ref} with $g = f$ and $R = \infty$.

:::

:::

::: pf-step

$u(x,y) \to f(x)$ as $y \to 0$ at every Lebesgue point $x$ of $f$, hence for a.e. $x$.

::: pf-proof

Fix a Lebesgue point $x$ and $\eps > 0$, and choose $\delta > 0$ with $\frac{1}{2r}\int_{x-r}^{x+r}|f(s) - f(x)|\,ds < \eps$ for $0 < r \le \delta$. By step [](#s1){.pf-ref}, $u(x,y) - f(x) = \int (f(x-t) - f(x))P_y(t)\,dt$. Let $g(s) = (f(s) - f(x))\chi_{\theset{|s - x| < \delta}}$. For $y \le \delta$, step [](#s2){.pf-ref} with $R = \delta$ gives $\int_{|t| < \delta}|f(x-t) - f(x)|P_y(t)\,dt \le \frac{10}{\pi}\eps$. On $|t| \ge \delta$, $P_y(t) \le \frac{y}{\pi\delta^2}$, so
$$
\int_{|t| \ge \delta}|f(x-t) - f(x)|P_y(t)\,dt \le \frac{y}{\pi\delta^2}\|f\|_1 + |f(x)|\int_{|t|\ge\delta}P_y(t)\,dt,
$$
and $\int_{|t|\ge\delta}P_y = 1 - \frac2\pi\arctan(\delta/y) \to 0$ as $y \to 0$. So $\limsup_{y\to0}|u(x,y) - f(x)| \le \frac{10}{\pi}\eps$ for every $\eps > 0$. By the Lebesgue differentiation theorem a.e. $x$ is a Lebesgue point.

:::

:::

:::

:::

::: {.remark}
In the statement, the kernel is $P_y(t) = \frac1\pi\frac{y}{t^2+y^2}$ as a function of $t$, and $u(x,y) = \int f(x-t)P_y(t)\,dt$.
:::
