---
schema: qual/card@1
id: P-MMAQ-WOUTK5GNAD
kind: problem
title: $\int_{\{f>\alpha\}}f^2\to 0$ as $\alpha\to\infty$ when $\int f^3<\infty$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Lp Spaces
  - Integrals
relations: []
review: draft
solved: true
---

::: problem
If $f$ is a nonnegative measurable function on $[0, \pi]$ and $\int_0^\pi f(x)^3~dx < \infty$, show that `\begin{align*} \lim_{\alpha\to\infty} \int_{ \theset{x :f(x) > \alpha} } f(x)^2 ~dx=0 .\end{align*}`{=tex}
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For nonnegative measurable $f$ on $[0, \pi]$ with $\int_0^\pi f^3 < \infty$, prove that $\lim_{\alpha \to \infty} \int_{\theset{x : f(x) > \alpha}} f^2 = 0$.

<1>1. On the set $\theset{x : f(x) > \alpha}$, the pointwise bound $f^2 \leq \frac{1}{\alpha} f^3$ holds.
Proof: where $f > \alpha$ we have $\frac{f^2}{f^3} = \frac{1}{f} < \frac{1}{\alpha}$, so $f^2 < \frac{f^3}{\alpha}$.

<1>2. $\int_{\theset{f > \alpha}} f^2 \leq \frac{1}{\alpha} \int_{\theset{f > \alpha}} f^3 \leq \frac{1}{\alpha} \int_0^\pi f^3$.
Proof: integrate the bound of <1>1 over $\theset{f > \alpha}$; then use $\theset{f > \alpha} \subseteq [0, \pi]$ and $f^3 \geq 0$ to bound the restricted integral by the full one.

<1>3. The upper bound in <1>2 tends to $0$ as $\alpha \to \infty$.
Proof: $\int_0^\pi f^3$ is a fixed finite constant, and $\frac{1}{\alpha} \to 0$.

<1>4. Q.E.D. Proof: the integrals in question are nonnegative (f^2 \geq 0) and squeezed between $0$ and a quantity tending to $0$, so the limit is $0$.
:::
