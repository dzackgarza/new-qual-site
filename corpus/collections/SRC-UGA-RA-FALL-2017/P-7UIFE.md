---
schema: qual/card@1
id: P-7UIFE
kind: problem
title: 'Approximate identity $K_j=j\varphi(jx)$: $f*K_j$ is smooth of compact support
  and converges in $L^1$'
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

::: problem
Let $\varphi \in C_c^\infty(\mathbb{R})$ be a smooth, compactly supported function supported in $[-N, N]$ such that $\int_\mathbb{R} \varphi(x) \, dx = 1$. For $f \in L^1(\mathbb{R})$ and $j \in \mathbb{N}$, define the mollifier sequence
$$
K_j(x) = j \varphi(j x), \qquad (f * K_j)(x) = \int_\mathbb{R} f(x - y) K_j(y) \, dy.
$$
Prove:

(a) Each $f * K_j$ is smooth ($C^\infty(\mathbb{R})$), and if $f$ is compactly supported, then $f * K_j \in C_c^\infty(\mathbb{R})$.

(b) $\lim_{j \to \infty} \|f * K_j - f\|_{L^1(\mathbb{R})} = 0$.
:::

::: solution
**Goal:** Prove that convolution with a smooth compactly supported mollifier yields smooth functions in (a), and that $K_j$ acts as an approximate identity in $L^1(\mathbb{R})$ in (b).

<1>1. Part (a): Smoothness and support of $f * K_j$.
    *Proof:*
    <2>1. Change of variables in convolution:
        For any $x \in \mathbb{R}$, by substitution $y = x - t$:
        $$(f * K_j)(x) = \int_\mathbb{R} f(y) K_j(x - y) \, dy = \int_\mathbb{R} f(y) j \varphi(j(x - y)) \, dy.$$
    <2>2. First derivative of $f * K_j$:
        For $h \ne 0$, the difference quotient is
        $$\frac{(f * K_j)(x + h) - (f * K_j)(x)}{h} = \int_\mathbb{R} f(y) \left( \frac{K_j(x + h - y) - K_j(x - y)}{h} \right) dy.$$
        By the Mean Value Theorem, for each $x, y, h$, there exists $\xi$ between $x - y$ and $x + h - y$ such that
        $$\left| \frac{K_j(x + h - y) - K_j(x - y)}{h} \right| = |K_j'(\xi)| = j^2 |\varphi'(j \xi)| \le j^2 \|\varphi'\|_\infty.$$
        Since $\varphi \in C_c^\infty(\mathbb{R})$, $\|\varphi'\|_\infty < \infty$, so the integrand is dominated by the integrable function $j^2 \|\varphi'\|_\infty |f(y)| \in L^1(\mathbb{R})$.
        By the Dominated Convergence Theorem:
        $$(f * K_j)'(x) = \int_\mathbb{R} f(y) K_j'(x - y) \, dy = (f * K_j')(x).$$
    <2>3. Higher derivatives ($C^\infty$ property):
        By induction, for every $m \in \mathbb{N}$, the $m$-th derivative exists and satisfies
        $$(f * K_j)^{(m)}(x) = (f * K_j^{(m)})(x) = \int_\mathbb{R} f(y) j^{m+1} \varphi^{(m)}(j(x - y)) \, dy.$$
        Since $\varphi^{(m)} \in C_c^\infty(\mathbb{R})$ is bounded and uniformly continuous, each $(f * K_j)^{(m)}$ is continuous on $\mathbb{R}$. Thus $f * K_j \in C^\infty(\mathbb{R})$.
    <2>4. Compact support when $f$ is compactly supported:
        If $\operatorname{supp}(f) \subseteq [-M, M]$, then since $\operatorname{supp}(K_j) \subseteq [-N/j, N/j]$, the convolution vanishes whenever $x - y \notin [-N/j, N/j]$ for all $y \in [-M, M]$.
        Thus $\operatorname{supp}(f * K_j) \subseteq \operatorname{supp}(f) + \operatorname{supp}(K_j) \subseteq [-M - N/j, M + N/j]$, which is compact.

<1>2. Part (b): $L^1$ convergence $\lim_{j \to \infty} \|f * K_j - f\|_{L^1} = 0$.
    *Proof:*
    <2>1. Normalization identity:
        Using $\int_\mathbb{R} K_j(y) \, dy = \int_\mathbb{R} j \varphi(jy) \, dy = \int_\mathbb{R} \varphi(u) \, du = 1$, we write
        $$f(x) = f(x) \int_\mathbb{R} K_j(y) \, dy = \int_\mathbb{R} f(x) K_j(y) \, dy.$$
    <2>2. Integral representation of error:
        $$(f * K_j)(x) - f(x) = \int_\mathbb{R} (f(x - y) - f(x)) K_j(y) \, dy.$$
    <2>3. Fubini-Tonelli bound:
        Taking the $L^1$ norm:
        $$\|f * K_j - f\|_{L^1} = \int_\mathbb{R} \left| \int_\mathbb{R} (f(x - y) - f(x)) K_j(y) \, dy \right| dx \le \int_\mathbb{R} \int_\mathbb{R} |f(x - y) - f(x)| |K_j(y)| \, dy \, dx.$$
        Applying Tonelli's Theorem:
        $$\|f * K_j - f\|_{L^1} \le \int_\mathbb{R} |K_j(y)| \left( \int_\mathbb{R} |f(x - y) - f(x)| \, dx \right) dy = \int_\mathbb{R} |K_j(y)| \|\tau_y f - f\|_{L^1} \, dy,$$
        where $\tau_y f(x) = f(x - y)$.
    <2>4. Change of variables $u = j y$:
        Since $K_j(y) = j \varphi(jy)$, substituting $u = j y$ ($dy = \frac{1}{j} du$) yields
        $$\|f * K_j - f\|_{L^1} \le \int_\mathbb{R} |\varphi(u)| \|\tau_{u/j} f - f\|_{L^1} \, du = \int_{-N}^N |\varphi(u)| \|\tau_{u/j} f - f\|_{L^1} \, du.$$
    <2>5. Dominated Convergence Theorem:
        - For each fixed $u \in [-N, N]$, as $j \to \infty$, $u/j \to 0$. By the $L^1$ continuity of translations, $\lim_{j \to \infty} \|\tau_{u/j} f - f\|_{L^1} = 0$.
        - The integrand is dominated on $[-N, N]$ by
        $$|\varphi(u)| \|\tau_{u/j} f - f\|_{L^1} \le 2 \|f\|_{L^1} |\varphi(u)| \in L^1([-N, N]).$$
        - By the Dominated Convergence Theorem:
        $$\lim_{j \to \infty} \int_{-N}^N |\varphi(u)| \|\tau_{u/j} f - f\|_{L^1} \, du = \int_{-N}^N |\varphi(u)| \cdot 0 \, du = 0.$$
    <2>6. Therefore $\lim_{j \to \infty} \|f * K_j - f\|_{L^1(\mathbb{R})} = 0$.

<1>3. Conclusion:
    *Proof:*
    $f * K_j \in C^\infty(\mathbb{R})$, with compact support if $f$ has compact support, and $f * K_j \to f$ in $L^1(\mathbb{R})$.
:::

