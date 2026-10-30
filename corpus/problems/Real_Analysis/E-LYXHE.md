---
schema: qual/card@1
id: E-LYXHE
kind: problem
title: Compact support and vanishing at infinity of convolutions
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
(a) If $f, g$ are compactly supported, is it necessarily the case that $f\ast g$ is compactly supported?

(b) Show that under any of the following assumptions, $f\ast g$ vanishes at infinity:

- $f, g\in L^1$ are both bounded.

- $f, g\in L^1$ with just $g$ bounded.

- $f, g$ smooth and compactly supported (and in fact $f\ast g$ is smooth)
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) If $f$ and $g$ are compactly supported, then $f \ast g$ is compactly supported.

::: pf-proof

::: {.pf-step #s1-1}

$\supp(f \ast g) \subseteq \supp f + \supp g$.

::: pf-proof

If $x \notin \supp f + \supp g$, then $(x - \supp g) \cap \supp f = \emptyset$, so $f(x-y) = 0$ for every $y \in \supp g$ and $f \ast g(x) = \int f(x-y)g(y)\,dy = 0$. Since $\supp f + \supp g$ is closed by step [](#s1-2){.pf-ref}, the support of $f\ast g$, the closure of $\theset{f\ast g \neq 0}$, is contained in it.

:::

:::

::: {.pf-step #s1-2}

$\supp f + \supp g$ is compact.

::: pf-proof

It is the image of the compact set $\supp f \times \supp g$ under the continuous map $(a,b) \mapsto a+b$.

:::

:::

::: pf-qed

A closed subset of a compact set is compact; apply steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.

:::

:::

:::

::: {.pf-step #s2}

(b) If $f, g \in L^1$ are both bounded, then $f \ast g$ vanishes at infinity.

::: pf-proof

::: {.pf-step #s2-1}

$\abs{\int_{\abs{y} \le \abs{x}/2} f(x-y)g(y)\,dy} \leq \norm{g}_\infty \int_{\abs{z} \ge \abs{x}/2} \abs{f(z)}\,dz$, which tends to $0$ as $\abs{x} \to \infty$.

::: pf-proof

On $\theset{\abs{y} \le \abs{x}/2}$, $\abs{x-y} \ge \abs{x}/2$. Substitute $z = x - y$ and use $\abs{g} \le \norm{g}_\infty$. The tail integral of $\abs{f} \in L^1$ tends to $0$ by dominated convergence.

:::

:::

::: {.pf-step #s2-2}

$\abs{\int_{\abs{y} > \abs{x}/2} f(x-y)g(y)\,dy} \leq \norm{f}_\infty \int_{\abs{y} > \abs{x}/2} \abs{g(y)}\,dy$, which tends to $0$ as $\abs{x} \to \infty$.

::: pf-proof

Use $\abs{f} \le \norm{f}_\infty$; the tail integral of $\abs{g} \in L^1$ tends to $0$.

:::

:::

::: pf-qed

$f\ast g(x)$ is the sum of the two integrals in steps [](#s2-1){.pf-ref} and [](#s2-2){.pf-ref}, and both tend to $0$ as $\abs{x} \to \infty$.

:::

:::

:::

::: pf-step

(b) If $f, g \in L^1$ with only $g$ bounded, then $f \ast g$ vanishes at infinity.

::: pf-proof

::: {.pf-step #s3-1}

For $M > 0$ write $f = f_M + r_M$ with $f_M = f \chi_{\theset{\abs{f} \le M}}$. Then $\abs{f_M} \le M$ and $\norm{r_M}_1 \to 0$ as $M \to \infty$.

::: pf-proof

$\int \abs{r_M} = \int_{\theset{\abs{f} > M}} \abs{f} \to 0$ by dominated convergence, since $\abs{f} \in L^1$ and $\chi_{\theset{\abs{f} > M}} \to 0$ a.e.

:::

:::

::: {.pf-step #s3-2}

$\norm{r_M \ast g}_\infty \le \norm{r_M}_1 \norm{g}_\infty$.

::: pf-proof

$\abs{r_M \ast g(x)} \le \int \abs{r_M(x-y)}\abs{g(y)}\,dy \le \norm{g}_\infty \norm{r_M}_1$.

:::

:::

::: {.pf-step #s3-3}

$f_M \ast g$ vanishes at infinity.

::: pf-proof

$f_M$ and $g$ are bounded and in $L^1$, so step [](#s2){.pf-ref} applies.

:::

:::

::: pf-qed

Given $\eps > 0$, choose $M$ with $\norm{r_M \ast g}_\infty < \eps/2$ by steps [](#s3-1){.pf-ref} and [](#s3-2){.pf-ref}, then $R$ with $\abs{f_M \ast g(x)} < \eps/2$ for $\abs{x} > R$ by step [](#s3-3){.pf-ref}. For $\abs{x} > R$, $\abs{f \ast g(x)} \le \abs{f_M \ast g(x)} + \abs{r_M \ast g(x)} < \eps$.

:::

:::

:::

::: pf-step

(b) If $f, g$ are smooth and compactly supported, then $f \ast g$ is smooth and vanishes at infinity.

::: pf-proof

::: pf-step

$f \ast g$ is $C^\infty$, with $D^\alpha(f \ast g) = (D^\alpha f) \ast g$ for every multi-index $\alpha$.

::: pf-proof

Each $D^\alpha f$ is continuous and compactly supported, hence bounded, and $g$ is integrable, so dominated convergence justifies differentiating under the integral in $f\ast g(x) = \int f(x-y)g(y)\,dy$. Each $(D^\alpha f) \ast g$ is continuous.

:::

:::

::: pf-step

$f \ast g$ vanishes at infinity.

::: pf-proof

By step [](#s1){.pf-ref}, $f \ast g$ is zero outside a compact set.

:::

:::

:::

:::

:::

:::
