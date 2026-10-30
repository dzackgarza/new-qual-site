---
schema: qual/card@1
id: P-7UIFE
kind: problem
title: 'Mollifiers $K_j=j\varphi(jx)$: $f*K_j$ is smooth and $f*K_j\to f$ in $L^1$'
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - L¹
relations: []
review: draft
---

::: {.problem}
Let $\varphi \in C_c^\infty(\RR)$ be a smooth, compactly supported function supported in $[-N, N]$ such that $\int_\RR \varphi(x) \, dx = 1$. For $f \in L^1(\RR)$ and $j \in \NN$, define the mollifier sequence
$$
K_j(x) = j \varphi(j x), \qquad (f * K_j)(x) = \int_\RR f(x - y) K_j(y) \, dy.
$$
Prove:

(a) Each $f * K_j$ is smooth ($C^\infty(\RR)$), and if $f$ is compactly supported, then $f * K_j \in C_c^\infty(\RR)$.

(b) $\lim_{j \to \infty} \norm{f * K_j - f}_{L^1(\RR)} = 0$. (You may use $\lim_{y\to0}\int_\RR\abs{f(x-y)-f(x)}\,dx=0$ without proof.)
:::

::: {.remark}
The exam asks that every $f*K_j$ vanish outside a compact interval. For a general $f\in L^1(\RR)$ this is false: if $f>0$ everywhere and $\varphi\ge0$, then $f*K_j>0$ everywhere. The compact-support conclusion holds when $f$ has compact support, which is the form stated in (a).
:::

::: {.solution}
**Goal:** Prove that convolution with a smooth compactly supported mollifier yields smooth functions in (a), and that $K_j$ acts as an approximate identity in $L^1(\RR)$ in (b).

::: pf

::: pf-step
Part (a): Smoothness and support of $f * K_j$.

::: pf-proof

::: pf-step
Change of variables in convolution:
For any $x \in \RR$, by substitution $y = x - t$:
$$(f * K_j)(x) = \int_\RR f(y) K_j(x - y) \, dy = \int_\RR f(y) j \varphi(j(x - y)) \, dy.$$

:::

::: pf-step
First derivative of $f * K_j$:
For $h \ne 0$, the difference quotient is
$$\frac{(f * K_j)(x + h) - (f * K_j)(x)}{h} = \int_\RR f(y) \left( \frac{K_j(x + h - y) - K_j(x - y)}{h} \right) dy.$$
By the Mean Value Theorem, for each $x, y, h$, there exists $\xi$ between $x - y$ and $x + h - y$ such that
$$\abs{ \frac{K_j(x + h - y) - K_j(x - y)}{h} } = \abs{K_j'(\xi)} = j^2 \abs{\varphi'(j \xi)} \le j^2 \norm{\varphi'}_\infty.$$
Since $\varphi \in C_c^\infty(\RR)$, $\norm{\varphi'}_\infty < \infty$, so the integrand is dominated by the integrable function $j^2 \norm{\varphi'}_\infty \abs{f(y)} \in L^1(\RR)$.
By the Dominated Convergence Theorem:
$$(f * K_j)'(x) = \int_\RR f(y) K_j'(x - y) \, dy = (f * K_j')(x).$$

:::

::: pf-step
Higher derivatives ($C^\infty$ property):
By induction, for every $m \in \NN$, the $m$-th derivative exists and satisfies
$$(f * K_j)^{(m)}(x) = (f * K_j^{(m)})(x) = \int_\RR f(y) j^{m+1} \varphi^{(m)}(j(x - y)) \, dy.$$
Since $\varphi^{(m)} \in C_c^\infty(\RR)$ is bounded and uniformly continuous, each $(f * K_j)^{(m)}$ is continuous on $\RR$. Thus $f * K_j \in C^\infty(\RR)$.

:::

::: pf-step
Compact support when $f$ is compactly supported:
If $\operatorname{supp}(f) \subseteq [-M, M]$, then since $\operatorname{supp}(K_j) \subseteq [-N/j, N/j]$, the convolution vanishes whenever $x - y \notin [-N/j, N/j]$ for all $y \in [-M, M]$.
Thus $\operatorname{supp}(f * K_j) \subseteq \operatorname{supp}(f) + \operatorname{supp}(K_j) \subseteq [-M - N/j, M + N/j]$, which is compact.

:::

:::

:::

::: pf-step
Part (b): $L^1$ convergence $\lim_{j \to \infty} \norm{f * K_j - f}_{L^1} = 0$.

::: pf-proof

::: pf-step
Normalization identity:
Using $\int_\RR K_j(y) \, dy = \int_\RR j \varphi(jy) \, dy = \int_\RR \varphi(u) \, du = 1$, we write
$$f(x) = f(x) \int_\RR K_j(y) \, dy = \int_\RR f(x) K_j(y) \, dy.$$

:::

::: pf-step
Integral representation of error:
$$(f * K_j)(x) - f(x) = \int_\RR (f(x - y) - f(x)) K_j(y) \, dy.$$

:::

::: pf-step
Fubini-Tonelli bound:
Taking the $L^1$ norm:
$$\norm{f * K_j - f}_{L^1} = \int_\RR \abs{ \int_\RR (f(x - y) - f(x)) K_j(y) \, dy } dx \le \int_\RR \int_\RR \abs{f(x - y) - f(x)} \abs{K_j(y)} \, dy \, dx.$$
Applying Tonelli's Theorem:
$$\norm{f * K_j - f}_{L^1} \le \int_\RR \abs{K_j(y)} \left( \int_\RR \abs{f(x - y) - f(x)} \, dx \right) dy = \int_\RR \abs{K_j(y)} \norm{\tau_y f - f}_{L^1} \, dy,$$
where $\tau_y f(x) = f(x - y)$.

:::

::: pf-step
Change of variables $u = j y$:
Since $K_j(y) = j \varphi(jy)$, substituting $u = j y$ ($dy = \frac{1}{j} du$) yields
$$\norm{f * K_j - f}_{L^1} \le \int_\RR \abs{\varphi(u)} \norm{\tau_{u/j} f - f}_{L^1} \, du = \int_{-N}^N \abs{\varphi(u)} \norm{\tau_{u/j} f - f}_{L^1} \, du.$$

:::

::: pf-step
Dominated Convergence Theorem:

- For each fixed $u \in [-N, N]$, as $j \to \infty$, $u/j \to 0$. By the $L^1$ continuity of translations, $\lim_{j \to \infty} \norm{\tau_{u/j} f - f}_{L^1} = 0$.
- The integrand is dominated on $[-N, N]$ by
$$\abs{\varphi(u)} \norm{\tau_{u/j} f - f}_{L^1} \le 2 \norm{f}_{L^1} \abs{\varphi(u)} \in L^1([-N, N]).$$
- By the Dominated Convergence Theorem:
$$\lim_{j \to \infty} \int_{-N}^N \abs{\varphi(u)} \norm{\tau_{u/j} f - f}_{L^1} \, du = \int_{-N}^N \abs{\varphi(u)} \cdot 0 \, du = 0.$$

:::

::: pf-step
Therefore $\lim_{j \to \infty} \norm{f * K_j - f}_{L^1(\RR)} = 0$.

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
$f * K_j \in C^\infty(\RR)$, with compact support if $f$ has compact support, and $f * K_j \to f$ in $L^1(\RR)$.
:::

:::

:::

:::

