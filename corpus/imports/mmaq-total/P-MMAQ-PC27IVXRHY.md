---
schema: qual/card@1
id: P-MMAQ-PC27IVXRHY
kind: problem
title: "Let $f, g \\in L^2(\\RR)$. Prove that the formula $h(x):=\\int_{-\\infty}^{\\infty} f(t) g(x-t) d t$ defines a uniformly\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-continuity
  - integrals
  - l2
relations: []
review: draft
solved: true
---

::: problem
Let $f, g \in L^2(\RR)$.
Prove that the formula
$$
h(x):=\int_{-\infty}^{\infty} f(t) g(x-t) d t
$$
defines a uniformly continuous function $h$ on $\RR$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For $f, g \in L^2(\RR)$, show $h = f \ast g$ (defined a.e. by the integral) is uniformly continuous on $\RR$.

<1>1. $h$ is well-defined (a.e.) and bounded.
<2>1. For every $x$, $\int \abs{f(t)} \abs{g(x-t)} ~dt \leq \norm{f}_2 \norm{g}_2$.
Proof: Cauchy–Schwarz applied to $f(t)$ and $g(x-t)$: $\int \abs{f(t)}\abs{g(x-t)} ~dt \leq \left(\int \abs{f}^2\right)^{1/2} \left(\int \abs{g(x-t)}^2 ~dt\right)^{1/2} = \norm{f}_2 \norm{g}_2$, the second factor by the translation-invariance of the $L^2$ norm.
<2>2. Hence $h(x)$ exists for every $x$ and $\abs{h(x)} \leq \norm{f}_2 \norm{g}_2 < \infty$.
Proof: By <2>1, the defining integral converges absolutely.
<2>3. Q.E.D. Proof: $h$ is everywhere defined and bounded.

<1>2. Establish a continuity estimate for the difference.
<2>1. For any $x, y \in \RR$, $$\abs{h(x) - h(y)} = \abs{\int f(t) (g(x-t) - g(y-t)) ~dt} \leq \norm{f}_2 \cdot \left(\int \abs{g(x-t) - g(y-t)}^2 ~dt\right)^{1/2}.$$ Proof: Triangle inequality inside the integral, then Cauchy–Schwarz.
<2>2. By the change of variables $u = x - t$ (equivalently $t = x - u$), $\int \abs{g(x-t) - g(y-t)}^2 ~dt = \int \abs{g(u) - g(u - (y-x))}^2 ~du = \norm{g - \tau_{y-x} g}_2^2$, where $\tau_a g(u) \definedas g(u - a)$.
Proof: Substitute $u = x - t$; then $y - t = u - (y - x)$, so the integrand becomes $\abs{g(u) - g(u - (y-x))}^2$ and the Jacobian is $1$.
<2>3. Hence $\abs{h(x) - h(y)} \leq \norm{f}_2 \norm{g - \tau_{y-x} g}_2$.
Proof: Combine <2>1 and <2>2.

<1>3. Translation is strongly continuous on $L^2(\RR)$: $\norm{g - \tau_a g}_2 \to 0$ as $a \to 0$.
<2>1. The claim holds for $g \in C_c^0(\RR)$.
Proof: For continuous compactly supported $g$, $\abs{g(u) - g(u-a)} \to 0$ uniformly (uniform continuity) and is supported in a fixed compact set for $\abs{a} \leq 1$, so the $L^2$ norm tends to $0$ by dominated convergence.
<2>2. $C_c^0(\RR)$ is dense in $L^2(\RR)$.
Proof: Standard density theorem.
<2>3. Given $\eps > 0$, choose $q \in C_c^0$ with $\norm{g - q}_2 < \eps/3$; then $$\norm{g - \tau_a g}_2 \leq \norm{g - q}_2 + \norm{q - \tau_a q}_2 + \norm{\tau_a q - \tau_a g}_2 \leq \frac{\eps}{3} + \norm{q - \tau_a q}_2 + \frac{\eps}{3}.$$ Proof: Triangle inequality, inserting $\pm q$ and $\pm \tau_a q$; the last term uses translation-invariance of the $L^2$ norm.
<2>4. For $\abs{a}$ small, $\norm{q - \tau_a q}_2 < \eps/3$, so $\norm{g - \tau_a g}_2 < \eps$.
Proof: By <2>1 applied to $q$, then combine with <2>3. <2>5. Q.E.D. Proof: $\eps > 0$ was arbitrary.

<1>4. Conclusion: $h$ is uniformly continuous.
<2>1. $\abs{h(x) - h(y)} \leq \norm{f}_2 \norm{g - \tau_{y-x} g}_2 \to 0$ as $y - x \to 0$.
Proof: By <1>2<2>3 and <1>3 (strong continuity of translation with $\norm{f}_2$ fixed).
<2>2. The convergence is independent of the location of $x, y$, only of the difference $y - x$.
Proof: The bound of <1>2<2>3 depends on $y - x$ only (via $\tau_{y-x}$), not on $x$ or $y$ individually.
<2>3. Hence $h$ is uniformly continuous.
Proof: By <2>1 and <2>2, for every $\eps > 0$ there is $\delta > 0$ with $\abs{h(x) - h(y)} < \eps$ whenever $\abs{x - y} < \delta$, uniformly in $x, y$.
<2>4. Q.E.D. Proof: This proves the claim.
:::
