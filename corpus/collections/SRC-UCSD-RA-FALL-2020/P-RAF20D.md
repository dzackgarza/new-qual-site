---
schema: qual/card@1
id: P-RAF20D
kind: problem
title: "$\\int f^\\alpha\\,d\\mu\\to\\mu\\{f>0\\}$ as $\\alpha\\to0^+$ and $\\int\\abs{g}^{p+1}/\\int\\abs{g}^p\\to\\norm{g}_\\infty$ as $p\\to\\infty$"
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
  - Monotone Convergence
  - Essential Supremum
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Fall 2020 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Replaced a circular lower-bound argument in part (2) by concentration of the |g|^p-weight near the essential supremum; normalized legacy solution/proof blocks.
---

::: {.problem}
Let $(X, \mathcal{M}, \mu)$ be a finite measure space.
Prove the following:

(1) If $f \in L^1(\mu)$ and $f \geq 0$ on $X$, then $f^\alpha \in L^1(\mu)$ for any $\alpha \in (0, 1)$ and
$$
\lim_{\alpha \to 0^+} \int_X f^\alpha \, d\mu = \mu(\{x \in X : f(x) > 0\}).
$$

(2) If $g \in L^\infty(\mu)$ with $\norm{g}_\infty > 0$, then $g \in L^p(\mu)$ for any $p \in [1, \infty)$ and
$$
\lim_{p \to +\infty} \frac{\int_X \abs{g}^{p+1} \, d\mu}{\int_X \abs{g}^p \, d\mu} = \norm{g}_\infty.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(1) $f^\alpha \in L^1$ for $\alpha \in (0,1)$ and $\lim_{\alpha \to 0^+} \int f^\alpha\,d\mu = \mu\theset{f > 0}$.

::: pf-proof

::: {.pf-step #s1-1}

$f^\alpha \in L^1$.

::: pf-proof

On $\theset{f \le 1}$, $f^\alpha \le 1$; on $\theset{f > 1}$, $f^\alpha \le f$ because $\alpha < 1$. Hence $f^\alpha \le 1 + f$ for every $\alpha\in(0,1)$, and $1+f \in L^1$ because $\mu(X)<\infty$.

:::

:::

::: {.pf-step #s1-2}

$f^\alpha \to \mathbf 1_{\theset{f > 0}}$ pointwise as $\alpha \to 0^+$.

::: pf-proof

If $f(x) > 0$, then $f(x)^\alpha \to 1$; if $f(x) = 0$, then $f(x)^\alpha = 0$.

:::

:::

::: pf-step

$\lim_{\alpha \to 0^+} \int f^\alpha\,d\mu = \int \mathbf 1_{\theset{f>0}}\,d\mu = \mu\theset{f > 0}$.

::: pf-proof

Apply the dominated convergence theorem to the pointwise limit of step [](#s1-2){.pf-ref}, with the dominating function $1 + f$ of step [](#s1-1){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s2}

(2) $g \in L^p$ for $p \in [1,\infty)$ and $\lim_{p\to\infty} \frac{\int \abs{g}^{p+1}}{\int \abs{g}^p} = \norm{g}_\infty$.

::: pf-proof

::: pf-step

$g \in L^p$ for all $p \in [1,\infty)$.

::: pf-proof

Since $\abs{g} \le \norm{g}_\infty$ a.e., $\int \abs{g}^p \le \norm{g}_\infty^p \mu(X) < \infty$.

:::

:::

::: {.pf-step #s2-2}

$\frac{\int \abs{g}^{p+1}}{\int \abs{g}^p} \le \norm{g}_\infty$.

::: pf-proof

Since $\abs{g} \le \norm{g}_\infty$ a.e., $\int \abs{g}^{p+1} = \int \abs{g} \cdot \abs{g}^p \le \norm{g}_\infty \int \abs{g}^p$, and $\int\abs{g}^p>0$ because $\norm{g}_\infty>0$.

:::

:::

::: {.pf-step #s2-3}

$\liminf_{p\to\infty} \frac{\int \abs{g}^{p+1}}{\int \abs{g}^p} \ge \norm{g}_\infty$.

::: pf-proof

Write $M=\norm{g}_\infty>0$ and fix $\varepsilon\in(0,M)$. Let
$$
A=\{\abs{g}>M-\varepsilon/2\},
\qquad
B=\{\abs{g}\le M-\varepsilon\}.
$$
By the definition of essential supremum, $\mu(A)>0$. If
$$
Z_p=\int_X\abs{g}^p\,d\mu,
$$
then
$$
Z_p\ge (M-\varepsilon/2)^p\mu(A),
$$
whereas
$$
\int_B\abs{g}^p\,d\mu\le (M-\varepsilon)^p\mu(X).
$$
Therefore
$$
\frac{\int_B\abs{g}^p\,d\mu}{Z_p}
\le
\frac{\mu(X)}{\mu(A)}
\left(\frac{M-\varepsilon}{M-\varepsilon/2}\right)^p
\longrightarrow0.
$$
Now
$$
\frac{\int\abs{g}^{p+1}}{Z_p}
=\frac{\int \abs{g}\,\abs{g}^p}{Z_p}
\ge (M-\varepsilon)
\frac{\int_{X\setminus B}\abs{g}^p}{Z_p}.
$$
The last factor tends to $1$, so
$$
\liminf_{p\to\infty}\frac{\int\abs{g}^{p+1}}{\int\abs{g}^p}
\ge M-\varepsilon.
$$
Letting $\varepsilon\downarrow0$ proves the desired lower bound.

:::

:::

::: pf-step

Hence the limit is $\norm{g}_\infty$.

::: pf-proof

Steps [](#s2-2){.pf-ref} and [](#s2-3){.pf-ref} give matching upper and lower bounds.

:::

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove (1) and (2).

:::

:::

:::
