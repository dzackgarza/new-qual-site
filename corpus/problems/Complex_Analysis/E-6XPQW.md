---
schema: qual/card@1
id: E-6XPQW
kind: exercise
title: $\sum_{k\in\mathbb{Z}}\frac{1}{(k-1/2)^2}=\pi^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
  - Trigonometry
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
\sum_{k\in \ZZ} {1\over \qty{ k - {1\over 2}}^2 } = \pi^2
.\]

:::

::: solution
**Goal:** Prove the summation identity $\sum_{k \in \mathbb{Z}} \frac{1}{(k - 1/2)^2} = \pi^2$ using contour integration and residue calculus.

<1>1. Auxiliary function and contour configuration:
    *Proof:*
    <2>1. Define the meromorphic function:
        $$f(z) = \frac{\pi \cot(\pi z)}{\left(z - \frac{1}{2}\right)^2}.$$
    <2>2. For an integer $N \ge 1$, let $\Gamma_N$ be the positively oriented square contour with vertices $(N + \frac{1}{4})(\pm 1 \pm i)$ (or $(N + \frac{1}{2})(\pm 1 \pm i)$ modified to enclose $z = 1/2$ and $z = -N, \dots, N$).
    <2>3. On $\Gamma_N$, $|\cot(\pi z)|$ is uniformly bounded by a constant $M$ independent of $N$.
    <2>4. On the boundary $\Gamma_N$, $|z - 1/2| \ge N$, so $|(z - 1/2)^2| \ge N^2$.
    <2>5. By the ML-inequality, the contour integral vanishes asymptotically:
        $$\left|\oint_{\Gamma_N} f(z) \, dz\right| \le \frac{\pi M}{N^2} \cdot O(N) = O\left(\frac{1}{N}\right) \xrightarrow{N \to \infty} 0.$$

<1>2. Calculation of residues inside $\Gamma_N$:
    *Proof:*
    <2>1. **Simple poles at integers $z = k \in \mathbb{Z}$:**
        For each $k \in \mathbb{Z}$, the pole of $\pi \cot(\pi z)$ is simple with residue $1$.
        $$\operatorname{Res}(f, k) = \lim_{z \to k} (z - k) \frac{\pi \cot(\pi z)}{\left(z - \frac{1}{2}\right)^2} = \frac{1}{\left(k - \frac{1}{2}\right)^2} \lim_{z \to k} \frac{\pi(z - k)\cos(\pi z)}{\sin(\pi z)} = \frac{1}{\left(k - \frac{1}{2}\right)^2}.$$
    <2>2. **Pole at $z = 1/2$:**
        Let $w = z - 1/2$. Using the trigonometric identity $\cot(\pi(w + 1/2)) = -\tan(\pi w)$:
        $$\pi \cot(\pi z) = -\pi \tan(\pi w) = -\pi \left( \pi w + \frac{\pi^3}{3} w^3 + O(w^5) \right) = -\pi^2 w - \frac{\pi^4}{3} w^3 + O(w^5).$$
        Substituting into $f(z)$:
        $$f(z) = \frac{-\pi^2 w - O(w^3)}{w^2} = -\frac{\pi^2}{w} + O(w).$$
        Hence the residue at the simple pole in $f$ at $z = 1/2$ is:
        $$\operatorname{Res}\left(f, \frac{1}{2}\right) = -\pi^2.$$

<1>3. Evaluation of the infinite sum:
    *Proof:*
    <2>1. By the Cauchy Residue Theorem:
        $$\frac{1}{2\pi i} \oint_{\Gamma_N} f(z) \, dz = \sum_{k=-N}^N \operatorname{Res}(f, k) + \operatorname{Res}\left(f, \frac{1}{2}\right) = \sum_{k=-N}^N \frac{1}{\left(k - \frac{1}{2}\right)^2} - \pi^2.$$
    <2>2. Taking the limit as $N \to \infty$, applying the vanishing integral bound from <1>1 gives:
        $$0 = \sum_{k=-\infty}^\infty \frac{1}{\left(k - \frac{1}{2}\right)^2} - \pi^2.$$
    <2>3. Therefore:
        $$\sum_{k \in \mathbb{Z}} \frac{1}{\left(k - \frac{1}{2}\right)^2} = \pi^2.$$
    Q.E.D.
:::

