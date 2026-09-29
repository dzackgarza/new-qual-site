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

a. Give the definition of what it means for a map $L:X\to \CC$ to be a *linear functional*.

b. Define what it means for $L$ to be *bounded* and show $L$ is bounded $\iff L$ is continuous.

c. Prove that $(\dualof{X}, \norm{\wait}_{\operatorname{op}})$ is a Banach space.
:::
::: {.solution}
(a) $L\colon X \to \CC$ is a \dfn{linear functional} if $L(x + y) = L(x) + L(y)$ and $L(\alpha x) = \alpha L(x)$ for all $x, y \in X$ and $\alpha \in \CC$.

(b) A linear functional $L$ is \dfn{bounded} if $\|L\|_{\operatorname{op}} \coloneqq \sup_{\|x\| \le 1}|L(x)| < \infty$, equivalently if $|L(x)| \le C\|x\|$ for some $C$ and all $x$.

::: pf

::: pf-step
A linear functional $L$ is bounded if and only if it is continuous.

::: pf-proof

::: {.pf-step #s1-1}
If $L$ is bounded, then $L$ is continuous.

::: pf-proof
$|L(x) - L(y)| = |L(x - y)| \le \|L\|_{\operatorname{op}}\|x - y\|$.
:::

:::

::: {.pf-step #s1-2}
If $L$ is continuous, then $L$ is bounded.

::: pf-proof
Suppose not.
Then there are $x_n$ with $\|x_n\| = 1$ and $|L(x_n)| \ge n$.
Then $y_n = x_n/n \to 0$ while $|L(y_n)| \ge 1$, contradicting continuity at $0$, where $L(0) = 0$.
:::

:::

::: pf-qed
Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}.
:::

:::

:::

:::

(c) Let $X^*$ be the space of bounded linear functionals on $X$.

::: pf

::: {.pf-step #s2}
$\|\cdot\|_{\operatorname{op}}$ is a norm on $X^*$.

::: pf-proof
If $\|L\|_{\operatorname{op}} = 0$ then $L(x) = 0$ for $\|x\| \le 1$, hence for all $x$ by scaling.
$\|\alpha L\|_{\operatorname{op}} = |\alpha|\,\|L\|_{\operatorname{op}}$, and $|(L + M)(x)| \le |L(x)| + |M(x)|$ gives $\|L + M\|_{\operatorname{op}} \le \|L\|_{\operatorname{op}} + \|M\|_{\operatorname{op}}$.
:::

:::

::: {.pf-step #s3}
Every Cauchy sequence $(L_n)$ in $X^*$ converges in $X^*$.

::: pf-proof

::: pf-step
For each $x \in X$, $L(x) \coloneqq \lim_n L_n(x)$ exists, and $L$ is linear.

::: pf-proof
$|L_n(x) - L_m(x)| \le \|L_n - L_m\|_{\operatorname{op}}\|x\|$, so $(L_n(x))$ is Cauchy in the complete space $\CC$.
Linearity passes to the limit: $L(\alpha x + y) = \lim_n(\alpha L_n(x) + L_n(y)) = \alpha L(x) + L(y)$.
:::

:::

::: pf-qed
Given $\eps > 0$, choose $N$ with $\|L_n - L_m\|_{\operatorname{op}} < \eps$ for $n, m \ge N$.
For $\|x\| \le 1$ and $n \geq N$, $|L(x) - L_n(x)| = \lim_m |L_m(x) - L_n(x)| \le \eps$, so $\|L - L_n\|_{\operatorname{op}} \le \eps$.
Then $\|L\|_{\operatorname{op}} \le \|L_N\|_{\operatorname{op}} + \eps$, so $L \in X^*$, and $L_n \to L$ in $X^*$.
:::

:::

:::

::: pf-qed
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} show that $X^*$ is a Banach space.
:::

:::

:::
