---
schema: qual/card@1
id: P-5EVB3
kind: problem
title: Hölder, completeness, a.e. uniform convergence, and density of simple functions
  in $L^\infty$
classification:
  areas:
  - real-analysis
  topics:
  - L∞
  - Norms
  - Density
  - Lp Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a measure space and prove the following properties of $L^ \infty (X, \mathcal{M}, \mu)$:

- If $f, g$ are measurable on $X$ then 
\[
\norm{fg}_1 \leq \norm{f}_1 \norm{g}_{\infty }
.\]

- $\norm{\wait}_{\infty }$ is a norm on $L^{\infty }$ making it a Banach space.

- $\norm{f_n - f}_{\infty } \converges{n\to \infty }\to 0 \iff$ there exists an $E\in \mathcal{M}$ such that $\mu(X\sm E) = 0$ and $f_n \to f$ uniformly on $E$. 

- Simple functions are dense in $L^{\infty }$.
:::

::: {.solution}
Recall $\|f\|_\infty = \inf\theset{M \geq 0 : |f| \le M \text{ a.e.}}$, and the infimum is attained: $|f| \le \|f\|_\infty$ a.e., because $\theset{|f| > \|f\|_\infty} = \bigcup_k \theset{|f| > \|f\|_\infty + 1/k}$ is a countable union of null sets.

::: pf

::: pf-step

$\|fg\|_1 \le \|f\|_1\|g\|_\infty$ for measurable $f, g$.

::: pf-proof

$|fg| \le |f|\,\|g\|_\infty$ a.e., so $\int|fg| \le \|g\|_\infty\int|f|$.

:::

:::

::: pf-step

$\|\cdot\|_\infty$ is a norm on $L^\infty$, the space of a.e.-equivalence classes of essentially bounded functions, and $L^\infty$ is complete.

::: pf-proof

::: {.pf-step #s2-1}

$\|\cdot\|_\infty$ is a norm.

::: pf-proof

$\|f\|_\infty = 0$ if and only if $f = 0$ a.e., and $\|\alpha f\|_\infty = |\alpha|\,\|f\|_\infty$. Since $|f + g| \le |f| + |g| \le \|f\|_\infty + \|g\|_\infty$ a.e., $\|f + g\|_\infty \le \|f\|_\infty + \|g\|_\infty$.

:::

:::

::: {.pf-step #s2-2}

Every Cauchy sequence $(f_n)$ in $L^\infty$ converges in $L^\infty$.

::: pf-proof

For $n, m$ let $Z_{n,m}$ be a null set off which $|f_n - f_m| \le \|f_n - f_m\|_\infty$, and let $Z = \bigcup_{n,m} Z_{n,m}$, a null set. On $X \setminus Z$, $\sup|f_n - f_m| \le \|f_n - f_m\|_\infty$, so $(f_n)$ is uniformly Cauchy there and converges uniformly to a bounded measurable $f$; put $f = 0$ on $Z$. Given $\eps > 0$ choose $N$ with $\|f_n - f_m\|_\infty < \eps$ for $n, m \ge N$; letting $m \to \infty$ gives $|f_n - f| \le \eps$ on $X \setminus Z$, so $\|f_n - f\|_\infty \le \eps$ for $n \geq N$.

:::

:::

::: pf-qed

Steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref}.

:::

:::

:::

::: pf-step

$\|f_n - f\|_\infty \to 0$ if and only if there is $E \in \mathcal M$ with $\mu(X \setminus E) = 0$ and $f_n \to f$ uniformly on $E$.

::: pf-proof

If $f_n \to f$ uniformly on such an $E$, then $\|f_n - f\|_\infty \le \sup_{E}|f_n - f| \to 0$. Conversely, let $Z_n$ be a null set off which $|f_n - f| \le \|f_n - f\|_\infty$, and put $E = X \setminus \bigcup_n Z_n$. Then $\sup_E|f_n - f| \le \|f_n - f\|_\infty \to 0$.

:::

:::

::: pf-step

Simple functions are dense in $L^\infty$.

::: pf-proof

Let $f \in L^\infty$ be real-valued, $M = \|f\|_\infty$, and $Z = \theset{|f| > M}$, a null set. For $k \ge 1$ let
$$
s_k = \sum_{j} \frac{j}{2^k}\,\chi_{\theset{x \notin Z\,:\, j2^{-k} \le f(x) < (j+1)2^{-k}}},
$$
the sum over the finitely many integers $j$ with $|j| \le M2^k + 1$. Then $s_k$ is simple and $|f - s_k| < 2^{-k}$ on $X \setminus Z$, so $\|f - s_k\|_\infty \le 2^{-k}$. For complex $f$ apply this to the real and imaginary parts.

:::

:::

:::

:::
