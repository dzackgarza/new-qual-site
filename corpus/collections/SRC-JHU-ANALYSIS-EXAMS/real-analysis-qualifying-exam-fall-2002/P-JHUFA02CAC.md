---
schema: qual/card@1
id: P-JHUFA02CAC
kind: problem
title: "Equicontinuity and the Arzela-Ascoli theorem on a Sobolev family"
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Arzela-Ascoli Theorem
  - Uniform Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

3.i. Define equicontinuity and state the Arzela-Ascoli theorem.

ii.Let $\mathcal { F }$ be the family of real valued functions on [0,1] satisfying $f ( 0 ) = 0$ and $\begin{array} { r } { \int _ { 0 } ^ { 1 } f ^ { \prime } ( x ) ^ { 2 } \ d x \leq 1 } \end{array}$ Show that any sequence in $\mathcal { F }$ has a subsequence that converges uniformly.

::: solution
**Goal:** Define equicontinuity, state the Arzelà–Ascoli theorem, and prove that the family $\mathcal{F} = \{f \in AC([0,1]) : f(0)=0, \int_0^1 |f'(x)|^2\,dx \le 1\}$ is relatively compact in $C([0,1])$.

<1>1. Definition of equicontinuity:
    ::: {.proof}
    <2>1. A family of functions $\mathcal{F} \subset C([0,1])$ is equicontinuous at a point $x_0 \in [0,1]$ if for every $\varepsilon > 0$, there exists $\delta > 0$ such that for all $x \in [0,1]$ and all $f \in \mathcal{F}$:
    $$|x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon.$$
    <2>2. The family $\mathcal{F}$ is equicontinuous on $[0,1]$ if it is equicontinuous at every point $x_0 \in [0,1]$.
    <2>3. Because $[0,1]$ is compact, equicontinuity on $[0,1]$ is equivalent to uniform equicontinuity: for every $\varepsilon > 0$, there exists $\delta > 0$ such that $|x - y| < \delta \implies |f(x) - f(y)| < \varepsilon$ for all $x, y \in [0,1]$ and all $f \in \mathcal{F}$.

:::
<1>2. Statement of the Arzelà–Ascoli Theorem:
    ::: {.proof}
    <2>1. Let $K$ be a compact metric space and let $C(K)$ denote the Banach space of continuous real-valued functions on $K$ endowed with the supremum norm $\|f\|_\infty = \sup_{x \in K} |f(x)|$.
    <2>2. A subset $\mathcal{F} \subseteq C(K)$ is relatively compact (meaning its closure $\overline{\mathcal{F}}$ is compact in $(C(K), \|\cdot\|_\infty)$, so every sequence in $\mathcal{F}$ has a uniformly convergent subsequence) if and only if:
        1. $\mathcal{F}$ is pointwise bounded: for each $x \in K$, $\sup_{f \in \mathcal{F}} |f(x)| < \infty$.
        2. $\mathcal{F}$ is equicontinuous on $K$.

:::
<1>3. Pointwise and uniform boundedness of $\mathcal{F}$:
    ::: {.proof}
    <2>1. Let $f \in \mathcal{F}$. By the Fundamental Theorem of Calculus for absolutely continuous functions and the Cauchy–Schwarz inequality, for any $x \in [0,1]$:
    $$|f(x) - f(0)| = \left| \int_0^x f'(t)\,dt \right| \le \int_0^x 1 \cdot |f'(t)|\,dt \le \left( \int_0^x 1^2\,dt \right)^{1/2} \left( \int_0^x |f'(t)|^2\,dt \right)^{1/2}.$$
    <2>2. Since $f(0) = 0$ and $\int_0^1 |f'(t)|^2\,dt \le 1$:
    $$|f(x)| \le \sqrt{x} \left( \int_0^1 |f'(t)|^2\,dt \right)^{1/2} \le \sqrt{x} \le 1.$$
    <2>3. Hence $\sup_{f \in \mathcal{F}} \|f\|_\infty \le 1$, so $\mathcal{F}$ is uniformly bounded on $[0,1]$.

:::
<1>4. Equicontinuity of $\mathcal{F}$:
    ::: {.proof}
    <2>1. Let $f \in \mathcal{F}$ and let $x, y \in [0,1]$ with $y \le x$. By Cauchy–Schwarz:
    $$|f(x) - f(y)| = \left| \int_y^x f'(t)\,dt \right| \le \left( \int_y^x 1\,dt \right)^{1/2} \left( \int_y^x |f'(t)|^2\,dt \right)^{1/2} \le \sqrt{x - y} \cdot \|f'\|_{L^2} \le \sqrt{|x - y|}.$$
    <2>2. Thus every $f \in \mathcal{F}$ is Hölder continuous with exponent $1/2$ and constant 1.
    <2>3. Given any $\varepsilon > 0$, choose $\delta = \varepsilon^2 > 0$. Whenever $|x - y| < \delta$,
    $$|f(x) - f(y)| \le \sqrt{|x - y|} < \sqrt{\delta} = \varepsilon$$
    for all $f \in \mathcal{F}$, proving that $\mathcal{F}$ is equicontinuous on $[0,1]$.

:::
<1>5. Conclusion:
    ::: {.proof}
    By <1>3 and <1>4, the family $\mathcal{F}$ is bounded and equicontinuous in $C([0,1])$. By the Arzelà–Ascoli Theorem (<1>2), every sequence $(f_n)_{n=1}^\infty \subset \mathcal{F}$ contains a subsequence that converges uniformly on $[0,1]$.
:::
:::
