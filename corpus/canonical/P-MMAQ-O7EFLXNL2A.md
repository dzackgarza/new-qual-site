---
schema: qual/card@1
id: P-MMAQ-O7EFLXNL2A
kind: problem
title: Layer-cake formula $\int f^p=\int_0^\infty p t^{p-1}\,m(\{f>t\})\,dt$
classification:
  areas:
  - real-analysis
  topics:
  - Integrals
  - Measure Theory
relations: []
review: draft
---

::: problem
If $f$ is a nonnegative measurable function on $\mathbb{R}$ and $p > 0$, show that $$\int f^p ~dx = \int_0^{\infty} p t^{p-1} \abs{\{x : f(x) > t\}} ~dt$$ where $\abs{\{x : f(x) > t\}}$ is the Lebesgue measure of the set $\{x : f(x) > t\}$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $f \geq 0$ measurable on $\RR$ and $p > 0$, prove $\int f^p ~dx = \int_0^\infty p t^{p-1} \abs{\{f > t\}} ~dt$, where $\abs{\cdot}$ is Lebesgue measure.
Both sides are allowed to be $+\infty$.

<1>1. Reduce to a product integral and apply Tonelli.
<2>1. Write $f(x)^p = \int_0^{f(x)} p t^{p-1} ~dt$.
Proof: For $a \geq 0$, $\int_0^a p t^{p-1} ~dt = \left[t^p\right]_0^a = a^p$, valid for every $p > 0$ (including $0 < p < 1$, where $t^{p-1}$ is integrable on $(0,a)$). <2>2. Hence $\int f(x)^p ~dx = \int_{\RR} \int_0^{f(x)} p t^{p-1} ~dt ~dx$.
Proof: Substitute <2>1. <2>3. The double integral $\int_\RR \int_0^\infty p t^{p-1} \chi_{\{t < f(x)\}} ~dt ~dx$ equals the iterated integral of <2>2. Proof: $\int_0^{f(x)} p t^{p-1} ~dt = \int_0^\infty p t^{p-1} \chi_{(0, f(x))}(t) ~dt = \int_0^\infty p t^{p-1} \chi_{\{t < f(x)\}}(t) ~dt$.
<2>4. The integrand $p t^{p-1} \chi_{\{t < f(x)\}}$ is nonnegative and jointly measurable in $(x, t)$.
Proof: $f$ is measurable, so $\{(x,t) : t < f(x)\} = f^{-1}((t, \infty))$ is a measurable subset of $\RR^2$; $t^{p-1}$ is measurable on $(0,\infty)$.
<2>5. Tonelli's theorem applies, so we may integrate in either order.
Proof: Tonelli's theorem: nonnegative measurable functions may be integrated in any order (possibly both $+\infty$). <2>6. Q.E.D. Proof: We have reduced the claim to identifying $\int_\RR \chi_{\{t < f(x)\}} ~dx$, done in <1>2.

<1>2. Identify the inner integral: $\int_\RR \chi_{\{t < f(x)\}} ~dx = \abs{\{x : f(x) > t\}}$ for each $t > 0$.
<2>1. $\int_\RR \chi_{\{t < f(x)\}} ~dx = \abs{\{x : f(x) > t\}}$.
Proof: The indicator $\chi_{\{t < f(x)\}}$ is $1$ exactly on the set $\{x : f(x) > t\}$, whose measure is by definition $\abs{\{x : f(x) > t\}}$.
<2>2. Q.E.D. Proof: Immediate from <2>1.

<1>3. Conclusion.
<2>1. $\int f^p ~dx = \int_0^\infty p t^{p-1} \left(\int_\RR \chi_{\{t < f(x)\}} ~dx\right) ~dt$.
Proof: By <1>1<2>5 (Tonelli, integrating over $x$ first), then <1>1<2>2, <1>1<2>3. <2>2. The inner integral equals $\abs{\{f > t\}}$, so $\int f^p ~dx = \int_0^\infty p t^{p-1} \abs{\{x : f(x) > t\}} ~dt$.
Proof: By <1>2. <2>3. Q.E.D. Proof: This is the claimed formula.
:::
