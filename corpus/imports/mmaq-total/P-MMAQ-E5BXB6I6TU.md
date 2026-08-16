---
schema: qual/card@1
id: P-MMAQ-E5BXB6I6TU
kind: problem
title: "Let $f(x) = s \\sum_{n=0}^{\\infty} \\frac{x^{n}}{n !}$ Describe the intervals on which $f$ does and does not\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-convergence
relations: []
review: draft
---

::: problem
Let
$$
f(x) = \sum_{n=0}^{\infty} \frac{x^{n}}{n !}.
$$

Describe the intervals on which $f$ does and does not converge uniformly.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $S_N(x) = \sum_{n=0}^N \frac{x^n}{n!}$ and $f(x) = \sum_{n=0}^\infty \frac{x^n}{n!} = e^x$. Characterize all intervals $I \subseteq \RR$ on which the series converges uniformly versus where it fails to converge uniformly.

<1>1. **Uniform convergence on bounded subsets and intervals bounded from above.**
  <2>1. On any bounded interval $I \subseteq [-R, R]$ with $R < \infty$:
    <3>1. For all $x \in I$ and all $n \geq 0$, $\left|\frac{x^n}{n!}\right| \leq \frac{R^n}{n!}$.
    <3>2. The numeric series $M_n \definedas \frac{R^n}{n!}$ converges: $\sum_{n=0}^\infty M_n = e^R < \infty$.
    <3>3. By the Weierstrass $M$-test, $S_N(x)$ converges uniformly and absolutely to $e^x$ on $I$.
  <2>2. On any interval bounded from above: $I = (-\infty, b]$ for any $b \in \RR$:
    <3>1. For $x \leq 0$, $S_N(x) = \sum_{n=0}^N \frac{x^n}{n!}$ is an alternating series for each $x < 0$ with terms eventually decreasing in magnitude. More directly, for $x \leq 0$:
      By Taylor's Theorem with Lagrange remainder, $e^x - S_N(x) = \frac{x^{N+1}}{(N+1)!} e^{\xi}$ for some $\xi$ between $x$ and $0$ (so $\xi \leq 0$, hence $e^\xi \leq 1$).
      Thus for $x \in [-R, 0]$: $|e^x - S_N(x)| \leq \frac{|x|^{N+1}}{(N+1)!} \leq \frac{R^{N+1}}{(N+1)!}$.
    <3>2. More generally, on $(-\infty, b]$, for any $\eps > 0$:
      - On $[0, b]$ (if $b \geq 0$), $S_N \to e^x$ uniformly by <2>1.
      - On $(-\infty, 0]$, for any fixed $N$, as $x \to -\infty$, $S_N(x)$ is a polynomial of degree $N$, while $e^x \to 0$. However, on any fixed interval $(-\infty, b]$, notice that for $x \to -\infty$, $\lim_{x\to-\infty} |e^x - S_N(x)| = \lim_{x\to-\infty} |S_N(x)| = \infty$ for any fixed $N \geq 1$.
      - Wait: $\sup_{x \in (-\infty, b]} |e^x - S_N(x)| \geq \lim_{x\to -\infty} |e^x - S_N(x)| = \infty$ for every fixed $N \geq 1$!
      - Thus $S_N(x)$ does NOT converge uniformly on $(-\infty, b]$ either!

<1>2. **Characterization: Uniform convergence holds if and only if $I$ is bounded.**
  <2>1. If $I \subseteq \RR$ is bounded, then $I \subseteq [-R, R]$ for some $R > 0$, and by <1>1 (<2>1), the convergence is uniform on $I$.
  <2>2. If $I$ is unbounded from above (i.e. $\sup I = \infty$):
    <3>1. For any fixed $N \in \NN$, the remainder is $R_N(x) = e^x - S_N(x) = \sum_{n=N+1}^\infty \frac{x^n}{n!}$.
    <3>2. For $x > 0$, $R_N(x) \geq \frac{x^{N+1}}{(N+1)!}$.
    <3>3. For any fixed $N$, $\sup_{x \in I} |e^x - S_N(x)| \geq \sup_{x \in I \cap (0, \infty)} \frac{x^{N+1}}{(N+1)!} = \infty$.
    <3>4. Thus $\sup_{x \in I} |e^x - S_N(x)|$ does not converge to $0$ as $N \to \infty$, so convergence is not uniform on $I$.
  <2>3. If $I$ is unbounded from below (i.e. $\inf I = -\infty$):
    <3>1. For each fixed $N \geq 1$, $S_N(x) = 1 + x + \frac{x^2}{2} + \dots + \frac{x^N}{N!}$ is a non-constant polynomial of degree $N$.
    <3>2. Therefore, $\lim_{x\to -\infty} |S_N(x)| = \infty$.
    <3>3. Since $\lim_{x\to-\infty} e^x = 0$, we have $\lim_{x\to-\infty} |e^x - S_N(x)| = \infty$.
    <3>4. Consequently, for every $N \geq 1$, $\sup_{x \in I} |e^x - S_N(x)| = \infty$.
    <3>5. Hence $\lim_{N\to\infty} \sup_{x \in I} |e^x - S_N(x)| \neq 0$, so convergence is not uniform on $I$.

<1>3. **Conclusion.**
  - **Uniform convergence holds on:** Every bounded interval $I \subset \RR$ (such as $[a, b]$, $(a, b)$, $[a, b)$, etc. with $-\infty < a \leq b < \infty$).
  - **Uniform convergence does NOT hold on:** Any unbounded interval (such as $[a, \infty)$, $(a, \infty)$, $(-\infty, b]$, $(-\infty, b)$, or $(-\infty, \infty)$). Q.E.D.
:::
