---
schema: qual/card@1
id: P-MMAQ-HXBFVZYTWW
kind: problem
title: a. Show that if $f$ is continuous with compact support on $\RR$, then
classification:
  areas:
  - real-analysis
  topics:
  - integrals
  - norms
relations: []
review: draft
solved: true
---

::: problem
a.  Show that if $f$ is continuous with compact support on $\RR$, then
    $$
    \lim _{y \rightarrow 0} \int_{\mathbb{R}}|f(x-y)-f(x)| d x=0
    $$

b.  Let $f\in L^1(\RR)$ and for each $h > 0$ let
    $$
    \mathcal{A}_{h} f(x):=\frac{1}{2 h} \int_{|y| \leq h} f(x-y) d y
    $$

c.  Prove that $\left\|\mathcal{A}_{h} f\right\|_{1} \leq\|f\|_{1}$ for all $h > 0$.

<!-- -->

ii. Prove that $\mathcal{A}_h f \to f$ in $L^1(\RR)$ as $h \to 0^+$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (a) Show continuity of translation in $L^1$ for continuous compactly supported $f$. (b) Define the averaging operator $\mathcal{A}_h$. (c) Show $\norm{\mathcal{A}_h f}_1 \leq \norm{f}_1$, and (ii) $\mathcal{A}_h f \to f$ in $L^1$ as $h \to 0^+$.

<1>1. Proof of (a): translation is continuous in $L^1$ for continuous compactly supported $f$.
    <2>1. A continuous function with compact support is uniformly continuous on $\RR$.
        Proof: $f$ is uniformly continuous on its compact support, and outside the support $f = 0$; taking $\delta$ smaller than the distance-scale works globally.
    <2>2. Fix $\eps > 0$. Let $\operatorname{supp}(f) \subseteq [-R, R]$, so that for $\abs{y} \leq 1$ both $f(\cdot)$ and $f(\cdot - y)$ are supported in $[-R-1, R+1]$, a set of measure $L \definedas 2R + 2$.
        Proof: $f$ has compact support contained in some $[-R, R]$; translating by $\abs{y} \leq 1$ shifts the support by at most $1$.
    <2>3. Uniform continuity (by <2>1) gives $\delta \in (0,1)$ with $\abs{f(x-y) - f(x)} < \frac{\eps}{2L}$ for all $x$ whenever $\abs{y} < \delta$.
        Proof: Definition of uniform continuity on $\RR$ with threshold $\eps/(2L)$; take $\delta < 1$ to fit <2>2.
    <2>4. Then $\int_\RR \abs{f(x-y) - f(x)} ~dx \leq L \cdot \frac{\eps}{2L} = \frac{\eps}{2}$ for $\abs{y} < \delta$.
        Proof: The integrand is $< \eps/(2L)$ everywhere (by <2>3) and vanishes outside the common support (by <2>2), whose measure is $L$.
    <2>5. Q.E.D.
        Proof: $\eps > 0$ was arbitrary; this proves the limit in (a) is $0$.

<1>2. $\norm{\mathcal{A}_h f}_1 \leq \norm{f}_1$ for every $h > 0$.
    <2>1. By Tonelli, $\int_\RR \abs{\mathcal{A}_h f(x)} ~dx \leq \frac{1}{2h} \int_{|y| \leq h} \int_\RR \abs{f(x-y)} ~dx ~dy$.
        Proof: $\abs{\mathcal{A}_h f(x)} \leq \frac{1}{2h}\int_{|y|\leq h}\abs{f(x-y)}~dy$; integrate over $x$ and apply Tonelli (nonnegative integrand).
    <2>2. $\int_\RR \abs{f(x-y)} ~dx = \norm{f}_1$ for every $y$, so the right side equals $\frac{1}{2h} \cdot (2h) \cdot \norm{f}_1 = \norm{f}_1$.
        Proof: Translation invariance of the $L^1$ norm, and $\int_{|y|\leq h} dy = 2h$.
    <2>3. Q.E.D.
        Proof: By <2>1 and <2>2.

<1>3. $\mathcal{A}_h f \to f$ in $L^1$ as $h \to 0^+$.
    <2>1. Write $\mathcal{A}_h f(x) - f(x) = \frac{1}{2h}\int_{|y| \leq h} (f(x-y) - f(x)) ~dy$.
        Proof: $\frac{1}{2h}\int_{|y|\leq h} f(x) ~dy = f(x)$, so subtract inside the integral.
    <2>2. Integrate over $x$: $\norm{\mathcal{A}_h f - f}_1 \leq \frac{1}{2h}\int_{|y| \leq h} \int_\RR \abs{f(x-y) - f(x)} ~dx ~dy$.
        Proof: Triangle inequality for integrals and Tonelli, as in <1>2.<2>1.
    <2>3. Let $g(y) \definedas \int_\RR \abs{f(x-y) - f(x)} ~dx$; then $g$ is bounded by $2\norm{f}_1$ and $g(y) \to 0$ as $y \to 0$.
        Proof: $g(y) \leq \norm{f(\cdot-y)}_1 + \norm{f}_1 = 2\norm{f}_1$; continuity of translation in $L^1$ for general $f \in L^1$ follows from (a) by density of compactly supported continuous functions in $L^1$ (the $3\eps$ argument).
    <2>4. Hence $\frac{1}{2h}\int_{|y|\leq h} g(y) ~dy \to 0$ as $h \to 0^+$.
        Proof: Fix $\eps$; for $\abs{y} < \delta$, $g(y) < \eps/2$; the average over $[-h,h]$ of $g$ splits into the $\delta$-neighborhood (small by <2>3) and a remaining arc whose length fraction $\to 0$ where $g \leq 2\norm{f}_1$; both parts are $< \eps/2$ for $h$ small.
    <2>5. Q.E.D.
        Proof: Combine <2>2 and <2>4: $\norm{\mathcal{A}_h f - f}_1 \leq \frac{1}{2h}\int_{|y|\leq h} g(y) ~dy \to 0$.

<1>4. Conclusion: (a), (c), and (ii) hold.
    Proof: (a) by <1>1, (c) by <1>2, (ii) by <1>3.
:::
