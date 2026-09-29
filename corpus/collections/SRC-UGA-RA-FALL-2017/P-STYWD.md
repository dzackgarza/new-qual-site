---
schema: qual/card@1
id: P-STYWD
kind: problem
title: The series $\sum x^n/n!$ converges uniformly on bounded intervals but not on
  $\RR$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
---

::: {.problem}
Let
$$
f(x) = \sum_{n=0}^{\infty} \frac{x^{n}}{n!}.
$$
Determine all intervals $I \subseteq \mathbb{R}$ on which the series converges uniformly, and prove the characterization.
:::

::: {.solution}
**Goal:** Prove that the power series $\sum_{n=0}^\infty \frac{x^n}{n!}$ converges uniformly on an interval $I \subseteq \mathbb{R}$ if and only if $I$ is bounded.

::: pf

::: pf-step
Uniform convergence on bounded intervals (Weierstrass $M$-test):

::: pf-proof

::: pf-step
Let $I \subseteq \mathbb{R}$ be a bounded interval.

:::

::: pf-step
Since $I$ is bounded, there exists $M \in (0, \infty)$ such that $|x| \le M$ for all $x \in I$.

:::

::: pf-step
For each $n \ge 0$ and $x \in I$, the terms are bounded by
$$\left| \frac{x^n}{n!} \right| = \frac{|x|^n}{n!} \le \frac{M^n}{n!} =: M_n.$$

:::

::: pf-step
The numerical series $\sum_{n=0}^\infty M_n = \sum_{n=0}^\infty \frac{M^n}{n!} = e^M < \infty$ converges.

:::

::: pf-step
By the Weierstrass $M$-test, the series $\sum_{n=0}^\infty \frac{x^n}{n!}$ converges uniformly (and absolutely) on $I$.

:::

:::

:::

::: {.pf-step #s2}
Necessary condition for uniform convergence of series:

::: pf-proof

::: pf-step
If a series of functions $\sum_{n=0}^\infty u_n(x)$ converges uniformly on a set $E$, then its sequence of partial sums $S_N(x) = \sum_{n=0}^N u_n(x)$ is uniformly Cauchy on $E$.

:::

::: pf-step
In particular, the general term must converge uniformly to 0 on $E$:
$$\lim_{n \to \infty} \sup_{x \in E} |u_n(x)| = \lim_{n \to \infty} \sup_{x \in E} |S_n(x) - S_{n-1}(x)| = 0.$$

:::

:::

:::

::: pf-step
Failure of uniform convergence on unbounded intervals:

::: pf-proof

::: pf-step
Let $I \subseteq \mathbb{R}$ be an unbounded interval.

:::

::: pf-step
Case 1 ($I$ is unbounded from above):

- There exists a sequence $(x_k)_{k=1}^\infty \subset I$ such that $x_k \to +\infty$.
- For any fixed $n \ge 1$:
$$\sup_{x \in I} \left| \frac{x^n}{n!} \right| \ge \sup_{k \in \mathbb{N}} \frac{x_k^n}{n!} = \infty.$$
- Thus the terms $u_n(x) = \frac{x^n}{n!}$ do not tend to 0 uniformly on $I$.

:::

::: pf-step
Case 2 ($I$ is unbounded from below):

- There exists a sequence $(x_k)_{k=1}^\infty \subset I$ such that $x_k \to -\infty$.
- For any fixed $n \ge 1$:
$$\sup_{x \in I} \left| \frac{x^n}{n!} \right| \ge \sup_{k \in \mathbb{N}} \frac{|x_k|^n}{n!} = \infty.$$
- Again, $\sup_{x \in I} |u_n(x)| = \infty$ for each $n \ge 1$.

:::

::: pf-step
In either case, by the criterion in step [](#s2){.pf-ref}, the series does not converge uniformly on $I$.

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
The series converges uniformly on an interval $I$ if and only if $I$ is bounded.
:::

:::

:::

:::
