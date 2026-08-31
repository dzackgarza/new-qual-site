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

::: problem
Let
$$
f(x) = \sum_{n=0}^{\infty} \frac{x^{n}}{n!}.
$$
Determine all intervals $I \subseteq \mathbb{R}$ on which the series converges uniformly, and prove the characterization.
:::

::: solution
**Goal:** Prove that the power series $\sum_{n=0}^\infty \frac{x^n}{n!}$ converges uniformly on an interval $I \subseteq \mathbb{R}$ if and only if $I$ is bounded.

<1>1. Uniform convergence on bounded intervals (Weierstrass $M$-test):
::: {.proof}
    <2>1. Let $I \subseteq \mathbb{R}$ be a bounded interval.
    <2>2. Since $I$ is bounded, there exists $M \in (0, \infty)$ such that $|x| \le M$ for all $x \in I$.
    <2>3. For each $n \ge 0$ and $x \in I$, the terms are bounded by
    $$\left| \frac{x^n}{n!} \right| = \frac{|x|^n}{n!} \le \frac{M^n}{n!} =: M_n.$$
    <2>4. The numerical series $\sum_{n=0}^\infty M_n = \sum_{n=0}^\infty \frac{M^n}{n!} = e^M < \infty$ converges.
    <2>5. By the Weierstrass $M$-test, the series $\sum_{n=0}^\infty \frac{x^n}{n!}$ converges uniformly (and absolutely) on $I$.

:::

<1>2. Necessary condition for uniform convergence of series:
::: {.proof}
    <2>1. If a series of functions $\sum_{n=0}^\infty u_n(x)$ converges uniformly on a set $E$, then its sequence of partial sums $S_N(x) = \sum_{n=0}^N u_n(x)$ is uniformly Cauchy on $E$.
    <2>2. In particular, the general term must converge uniformly to 0 on $E$:
    $$\lim_{n \to \infty} \sup_{x \in E} |u_n(x)| = \lim_{n \to \infty} \sup_{x \in E} |S_n(x) - S_{n-1}(x)| = 0.$$

:::

<1>3. Failure of uniform convergence on unbounded intervals:
::: {.proof}
    <2>1. Let $I \subseteq \mathbb{R}$ be an unbounded interval.
    <2>2. Case 1 ($I$ is unbounded from above):
        - There exists a sequence $(x_k)_{k=1}^\infty \subset I$ such that $x_k \to +\infty$.
        - For any fixed $n \ge 1$:
        $$\sup_{x \in I} \left| \frac{x^n}{n!} \right| \ge \sup_{k \in \mathbb{N}} \frac{x_k^n}{n!} = \infty.$$
        - Thus the terms $u_n(x) = \frac{x^n}{n!}$ do not tend to 0 uniformly on $I$.
    <2>3. Case 2 ($I$ is unbounded from below):
        - There exists a sequence $(x_k)_{k=1}^\infty \subset I$ such that $x_k \to -\infty$.
        - For any fixed $n \ge 1$:
        $$\sup_{x \in I} \left| \frac{x^n}{n!} \right| \ge \sup_{k \in \mathbb{N}} \frac{|x_k|^n}{n!} = \infty.$$
        - Again, $\sup_{x \in I} |u_n(x)| = \infty$ for each $n \ge 1$.
    <2>4. In either case, by the criterion in <1>2, the series does not converge uniformly on $I$.

:::

<1>4. Conclusion:
::: {.proof}
    The series converges uniformly on an interval $I$ if and only if $I$ is bounded.
:::
:::
