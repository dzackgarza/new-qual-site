---
schema: qual/card@1
id: P-55AME
kind: problem
title: 'Let $f\in L^1([0, 1])$. Prove that Hint: Begin with the case that $f$ is...'
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - integrals
relations: []
review: draft
---

::: problem
Let $f\in L^1([0, 1])$.
Prove that
$$
\lim_{n \to \infty} \int_{0}^{1} f(x) \abs{\sin n x} ~d x= \frac{2}{\pi} \int_{0}^{1} f(x) ~d x
$$

> Hint: Begin with the case that $f$ is the characteristic function of an interval.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Note that the function $g(u) = |\sin u|$ is periodic with period $\pi$, and its mean value over a period is:
$$
\frac{1}{\pi} \int_0^\pi |\sin u| \, du = \frac{1}{\pi} [-\cos u]_0^\pi = \frac{2}{\pi}.
$$

**Step 1: Characteristic function of an interval $f = \mathbf{1}_{[a, b]} \subseteq [0, 1]$.** For $n \in \NN$, substitute $u = nx$:
$$
\int_0^1 \mathbf{1}_{[a, b]}(x) |\sin nx| \, dx = \int_a^b |\sin nx| \, dx = \frac{1}{n} \int_{na}^{nb} |\sin u| \, du.
$$
The interval $[na, nb]$ of length $n(b-a)$ can be partitioned into $k_n = \lfloor \frac{n(b-a)}{\pi} \rfloor$ full periods of length $\pi$, plus a remainder of length $< \pi$.
On each full period, the integral is $\int_0^\pi |\sin u| \, du = 2$.
Thus:
$$
\int_{na}^{nb} |\sin u| \, du = 2 k_n + O(1) = 2 \left(\frac{n(b-a)}{\pi}\right) + O(1).
$$
Multiplying by $\frac{1}{n}$ and taking $n \to \infty$:
$$
\lim_{n \to \infty} \int_a^b |\sin nx| \, dx = \frac{2}{\pi}(b - a) = \frac{2}{\pi} \int_0^1 \mathbf{1}_{[a, b]}(x) \, dx.
$$

**Step 2: Step functions.** By linearity, the result holds for all step functions $s(x) = \sum_{j=1}^m c_j \mathbf{1}_{[a_j, b_j]}(x)$.

**Step 3: General $f \in L^1([0, 1])$.** Step functions are dense in $L^1([0, 1])$.
Given $\varepsilon > 0$, choose a step function $s$ such that $\|f - s\|_{L^1} < \varepsilon$.
Then:
$$
\left| \int_0^1 f(x) |\sin nx| \, dx - \frac{2}{\pi} \int_0^1 f(x) \, dx \right|
$$
$$
\leq \int_0^1 |f(x) - s(x)| \cdot |\sin nx| \, dx + \left| \int_0^1 s(x) |\sin nx| \, dx - \frac{2}{\pi} \int_0^1 s(x) \, dx \right| + \frac{2}{\pi} \int_0^1 |s(x) - f(x)| \, dx
$$
$$
\leq 1 \cdot \|f - s\|_{L^1} + \left| \int_0^1 s(x) |\sin nx| \, dx - \frac{2}{\pi} \int_0^1 s(x) \, dx \right| + \frac{2}{\pi} \|f - s\|_{L^1}
$$
$$
< \left(1 + \frac{2}{\pi}\right) \varepsilon + \left| \int_0^1 s(x) |\sin nx| \, dx - \frac{2}{\pi} \int_0^1 s(x) \, dx \right|.
$$
Taking $\limsup_{n \to \infty}$, the middle term vanishes by Step 2:
$$
\limsup_{n \to \infty} \left| \int_0^1 f(x) |\sin nx| \, dx - \frac{2}{\pi} \int_0^1 f(x) \, dx \right| \leq \left(1 + \frac{2}{\pi}\right) \varepsilon.
$$
Since $\varepsilon > 0$ is arbitrary, the limit exists and equals $\frac{2}{\pi} \int_0^1 f(x) \, dx$.
:::
