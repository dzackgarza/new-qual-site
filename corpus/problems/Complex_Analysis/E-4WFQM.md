---
schema: qual/card@1
id: E-4WFQM
kind: problem
title: $\sum_{k\geq 1}\frac{1}{k^2+a^2}=\frac{\pi\coth(\pi a)}{2a}-\frac{1}{2a^2}$
  for $a>0$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
  - Hyperbolic Functions
  - Meromorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

:::{.exercise}
Show that
\[
\sum_{k\geq 1}{1\over k^2 + a^2} = {1\over 2}{\pi \coth(\pi a)\over a} - {1\over 2a^2} \qquad a>0
.\]

:::

::: solution
**Goal:** Prove the identity $\sum_{k=1}^\infty \frac{1}{k^2 + a^2} = \frac{\pi \coth(\pi a)}{2a} - \frac{1}{2a^2}$ for $a > 0$ using contour integration and residue calculus.

<1>1. Auxiliary function and contour setup:
    *Proof:*
    <2>1. Consider the meromorphic function:
        $$f(z) = \frac{\pi \cot(\pi z)}{z^2 + a^2}.$$
    <2>2. For an integer $N > a$, let $\Gamma_N$ be the positively oriented square contour with vertices $(N + \frac{1}{2})(\pm 1 \pm i)$.
    <2>3. On the contour $\Gamma_N$, $|\cot(\pi z)|$ is uniformly bounded by a constant $M$ independent of $N$.
    <2>4. For $z \in \Gamma_N$, $|z^2 + a^2| \ge |z|^2 - a^2 \ge (N + \frac{1}{2})^2 - a^2$.
    <2>5. By the ML-inequality, the contour integral satisfies:
        $$\left|\oint_{\Gamma_N} f(z) \, dz\right| \le \frac{\pi M}{(N + \frac{1}{2})^2 - a^2} \cdot 8\left(N + \frac{1}{2}\right) = O\left(\frac{1}{N}\right) \xrightarrow{N \to \infty} 0.$$

<1>2. Calculation of residues inside $\Gamma_N$:
    *Proof:*
    <2>1. **Poles at integers $z = k \in \{-N, \dots, N\}$:**
        $$\operatorname{Res}(f, k) = \lim_{z \to k} (z - k) \frac{\pi \cot(\pi z)}{z^2 + a^2} = \frac{1}{k^2 + a^2} \lim_{z \to k} \frac{\pi (z - k) \cos(\pi z)}{\sin(\pi z)} = \frac{1}{k^2 + a^2}.$$
    <2>2. **Poles at $z = \pm i a$:**
        - At $z = ia$:
          $$\operatorname{Res}(f, ia) = \lim_{z \to ia} (z - ia) \frac{\pi \cot(\pi z)}{(z - ia)(z + ia)} = \frac{\pi \cot(i \pi a)}{2ia}.$$
        - Using $\cot(ix) = \frac{\cos(ix)}{\sin(ix)} = \frac{\cosh x}{i \sinh x} = -i \coth x$:
          $$\operatorname{Res}(f, ia) = \frac{\pi (-i \coth(\pi a))}{2ia} = -\frac{\pi \coth(\pi a)}{2a}.$$
        - At $z = -ia$:
          $$\operatorname{Res}(f, -ia) = \frac{\pi \cot(-i \pi a)}{-2ia} = \frac{-\pi (-i \coth(\pi a))}{-2ia} = -\frac{\pi \coth(\pi a)}{2a}.$$

<1>3. Evaluation of the sum:
    *Proof:*
    <2>1. By the Cauchy Residue Theorem:
        $$\oint_{\Gamma_N} f(z) \, dz = 2\pi i \left[ \sum_{k=-N}^N \operatorname{Res}(f, k) + \operatorname{Res}(f, ia) + \operatorname{Res}(f, -ia) \right].$$
    <2>2. Taking the limit as $N \to \infty$ and applying <1>1 gives:
        $$0 = \sum_{k=-\infty}^\infty \frac{1}{k^2 + a^2} - 2\left(\frac{\pi \coth(\pi a)}{2a}\right) \implies \sum_{k=-\infty}^\infty \frac{1}{k^2 + a^2} = \frac{\pi \coth(\pi a)}{a}.$$
    <2>3. Splitting the full sum over $\mathbb{Z}$:
        $$\sum_{k=-\infty}^\infty \frac{1}{k^2 + a^2} = \frac{1}{a^2} + 2 \sum_{k=1}^\infty \frac{1}{k^2 + a^2}.$$
    <2>4. Solving for $\sum_{k=1}^\infty \frac{1}{k^2 + a^2}$:
        $$\sum_{k=1}^\infty \frac{1}{k^2 + a^2} = \frac{1}{2} \left[ \frac{\pi \coth(\pi a)}{a} - \frac{1}{a^2} \right] = \frac{\pi \coth(\pi a)}{2a} - \frac{1}{2a^2}.$$
    Q.E.D.
:::

