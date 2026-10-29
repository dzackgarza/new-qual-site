---
schema: qual/card@1
id: P-MNEPM
kind: problem
title: 'Linear functionals: definition, boundedness equivalent to continuity, and
  completeness of the dual'
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Functional Analysis
  - Norms
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $X$ be a normed vector space.

(a) Give the definition of what it means for a map $L:X\to \CC$ to be a *linear functional*.

(b) Define what it means for $L$ to be *bounded* and show $L$ is bounded $\iff L$ is continuous.

(c) Prove that $(\dualof{X}, \norm{\wait}_{\operatorname{op}})$ is a Banach space.
:::

::: {.solution}

Let $X^*$ be the space of bounded linear functionals on $X$, with $\norm{L}_{\operatorname{op}} \coloneqq \sup_{\norm{x} \le 1}\abs{L(x)}$.

::: pf

::: pf-step

(a) $L\colon X \to \CC$ is a \dfn{linear functional} if $L(x + y) = L(x) + L(y)$ and $L(\alpha x) = \alpha L(x)$ for all $x, y \in X$ and $\alpha \in \CC$.

::: pf-proof

This is the definition of a linear map into the scalar field $\CC$.

:::

:::

::: pf-step

(b) A linear functional $L$ is \dfn{bounded} if $\norm{L}_{\operatorname{op}} < \infty$, equivalently if $\abs{L(x)} \le C\norm{x}$ for some $C$ and all $x$; and $L$ is bounded if and only if it is continuous.

::: pf-proof

::: pf-step

If $L$ is bounded, then $L$ is continuous.

::: pf-proof

$\abs{L(x) - L(y)} = \abs{L(x - y)} \le \norm{L}_{\operatorname{op}}\norm{x - y}$, so $L$ is Lipschitz.

:::

:::

::: pf-step

If $L$ is continuous, then $L$ is bounded.

::: pf-proof

Suppose not.
Then there are $x_n$ with $\norm{x_n} = 1$ and $\abs{L(x_n)} \ge n$.
Then $y_n = x_n/n \to 0$ while $\abs{L(y_n)} \ge 1$, contradicting continuity at $0$, where $L(0) = 0$.

:::

:::

:::

:::

::: pf-step

(c) $(X^*, \norm{\wait}_{\operatorname{op}})$ is a Banach space.

::: pf-proof

::: pf-step

$\norm{\wait}_{\operatorname{op}}$ is a norm on $X^*$.

::: pf-proof

If $\norm{L}_{\operatorname{op}} = 0$ then $L(x) = 0$ for $\norm{x} \le 1$, hence for all $x$ by scaling.
$\norm{\alpha L}_{\operatorname{op}} = \abs{\alpha}\,\norm{L}_{\operatorname{op}}$, and $\abs{(L + M)(x)} \le \abs{L(x)} + \abs{M(x)}$ gives $\norm{L + M}_{\operatorname{op}} \le \norm{L}_{\operatorname{op}} + \norm{M}_{\operatorname{op}}$.

:::

:::

::: pf-step

Every Cauchy sequence $(L_n)$ in $X^*$ converges in $X^*$.

::: pf-proof

::: pf-step

For each $x \in X$, $L(x) \coloneqq \lim_n L_n(x)$ exists, and $L$ is linear.

::: pf-proof

$\abs{L_n(x) - L_m(x)} \le \norm{L_n - L_m}_{\operatorname{op}}\norm{x}$, so $(L_n(x))$ is Cauchy in the complete space $\CC$.
Linearity passes to the limit: $L(\alpha x + y) = \lim_n(\alpha L_n(x) + L_n(y)) = \alpha L(x) + L(y)$.

:::

:::

::: pf-qed

Given $\varepsilon > 0$, choose $N$ with $\norm{L_n - L_m}_{\operatorname{op}} < \varepsilon$ for $n, m \ge N$.
For $\norm{x} \le 1$ and $n \geq N$, $\abs{L(x) - L_n(x)} = \lim_m \abs{L_m(x) - L_n(x)} \le \varepsilon$, so $\norm{L - L_n}_{\operatorname{op}} \le \varepsilon$.
Then $\norm{L}_{\operatorname{op}} \le \norm{L_N}_{\operatorname{op}} + \varepsilon$, so $L \in X^*$, and $L_n \to L$ in $X^*$.

:::

:::

:::

:::

:::

:::

:::
