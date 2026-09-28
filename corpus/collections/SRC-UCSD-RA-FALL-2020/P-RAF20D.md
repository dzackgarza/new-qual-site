---
schema: qual/card@1
id: P-RAF20D
kind: problem
title: "$\\int f^\\alpha\\,d\\mu\\to\\mu\\{f>0\\}$ as $\\alpha\\to0^+$ and $\\int|g|^{p+1}/\\int|g|^p\\to\\|g\\|_\\infty$ as $p\\to\\infty$"
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

(2) If $g \in L^\infty(\mu)$ with $\|g\|_\infty > 0$, then $g \in L^p(\mu)$ for any $p \in [1, \infty)$ and
$$
\lim_{p \to +\infty} \int_X \frac{|g|^{p+1} \, d\mu}{\int_X |g|^p \, d\mu} = \|g\|_\infty.
$$
:::

::: {.solution}
<1>1. (1) $f^\alpha \in L^1$ for $\alpha \in (0,1)$ and $\lim_{\alpha \to 0^+} \int f^\alpha\,d\mu = \mu\theset{f > 0}$.
<2>1. $f^\alpha \in L^1$.
::: {.proof}
On $\theset{f \le 1}$, $f^\alpha \le 1$; on $\theset{f > 1}$, $f^\alpha \le f$ because $\alpha < 1$. Hence $f^\alpha \le 1 + f$ for every $\alpha\in(0,1)$, and $1+f \in L^1$ because $\mu(X)<\infty$.
:::
<2>2. $f^\alpha \to \mathbf 1_{\theset{f > 0}}$ pointwise as $\alpha \to 0^+$.
::: {.proof}
If $f(x) > 0$, then $f(x)^\alpha \to 1$; if $f(x) = 0$, then $f(x)^\alpha = 0$.
:::
<2>3. $\lim_{\alpha \to 0^+} \int f^\alpha\,d\mu = \int \mathbf 1_{\theset{f>0}}\,d\mu = \mu\theset{f > 0}$.
::: {.proof}
Apply the dominated convergence theorem to the pointwise limit of step <2>2, with the dominating function $1 + f$ of step <2>1.
:::

<1>2. (2) $g \in L^p$ for $p \in [1,\infty)$ and $\lim_{p\to\infty} \frac{\int |g|^{p+1}}{\int |g|^p} = \|g\|_\infty$.
<2>1. $g \in L^p$ for all $p \in [1,\infty)$.
::: {.proof}
Since $|g| \le \|g\|_\infty$ a.e., $\int |g|^p \le \|g\|_\infty^p \mu(X) < \infty$.
:::
<2>2. $\frac{\int |g|^{p+1}}{\int |g|^p} \le \|g\|_\infty$.
::: {.proof}
Since $|g| \le \|g\|_\infty$ a.e., $\int |g|^{p+1} = \int |g| \cdot |g|^p \le \|g\|_\infty \int |g|^p$, and $\int|g|^p>0$ because $\|g\|_\infty>0$.
:::
<2>3. $\liminf_{p\to\infty} \frac{\int |g|^{p+1}}{\int |g|^p} \ge \|g\|_\infty$.
::: {.proof}
Write $M=\|g\|_\infty>0$ and fix $\varepsilon\in(0,M)$. Let
\[
A=\{|g|>M-\varepsilon/2\},
\qquad
B=\{|g|\le M-\varepsilon\}.
\]
By the definition of essential supremum, $\mu(A)>0$. If
\[
Z_p=\int_X|g|^p\,d\mu,
\]
then
\[
Z_p\ge (M-\varepsilon/2)^p\mu(A),
\]
whereas
\[
\int_B|g|^p\,d\mu\le (M-\varepsilon)^p\mu(X).
\]
Therefore
\[
\frac{\int_B|g|^p\,d\mu}{Z_p}
\le
\frac{\mu(X)}{\mu(A)}
\left(\frac{M-\varepsilon}{M-\varepsilon/2}\right)^p
\longrightarrow0.
\]
Now
\[
\frac{\int|g|^{p+1}}{Z_p}
=\frac{\int |g|\,|g|^p}{Z_p}
\ge (M-\varepsilon)
\frac{\int_{X\setminus B}|g|^p}{Z_p}.
\]
The last factor tends to $1$, so
\[
\liminf_{p\to\infty}\frac{\int|g|^{p+1}}{\int|g|^p}
\ge M-\varepsilon.
\]
Letting $\varepsilon\downarrow0$ proves the desired lower bound.
:::
<2>4. Hence the limit is $\|g\|_\infty$.
::: {.proof}
Steps <2>2 and <2>3 give matching upper and lower bounds.
:::

<1>3. Q.E.D.
::: {.proof}
Steps <1>1 and <1>2 prove (1) and (2).
:::
:::
