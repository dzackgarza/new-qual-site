---
schema: qual/card@1
id: P-MMAQ-L3IVZR2LI6
kind: problem
title: Let $f \in C_c^0(\RR^n)$, and show
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - integrals
  - convergence-of-integrals
  - l1
  - uniform-continuity
relations: []
review: draft
solved: true
---

::: problem
1. Let $f \in C_c^0(\RR^n)$, and show
   $$
   \lim _{t \rightarrow 0} \int_{\mathbb{R}^{n}}|f(x+t)-f(x)| d x=0.
   $$

2. Extend the above result to $f\in L^1(\RR^n)$ and show that
   $$
   f\in L^1(\RR^n),~ g\in L^\infty(\RR^n) \implies f \ast g \text{ is bounded and uniformly continuous. }
   $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (1) Prove $\int_{\RR^n} \abs{f(x+t) - f(x)} ~dx \to 0$ as $t \to 0$ for $f \in C_c^0(\RR^n)$.
(2) Extend to $f \in L^1(\RR^n)$, and show $f \in L^1, g \in L^\infty \implies f \ast g$ is bounded and uniformly continuous.

<1>1. Proof of (1) for $f \in C_c^0(\RR^n)$.
<2>1. $f$ is uniformly continuous on $\RR^n$.
Proof: $f$ is continuous and vanishes outside a compact set $K$; on $K$ it is uniformly continuous, and outside $K$ it is $0$ (equal to $f$ on $\partial K$ by continuity), so the two pieces paste to a uniformly continuous function.
<2>2. For every $x \in \RR^n$, $\abs{f(x+t) - f(x)} \to 0$ as $t \to 0$.
Proof: Continuity of $f$ at $x$.
<2>3. The integrands are dominated by an integrable function: for $\abs{t} \leq 1$, $\abs{f(x+t) - f(x)} \leq 2\norm{f}_\infty \chi_{K + \overline{B_1}} (x)$, where $K$ is the support of $f$.
Proof: Both $x$ and $x + t$ must lie in the compact set $K + \overline{B_1}$ for the difference to be nonzero, and $f$ is bounded by $\norm{f}_\infty$; $\chi_{K + \overline{B_1}} \in L^1$ since $K + \overline{B_1}$ has finite measure.
<2>4. Hence $\int_{\RR^n} \abs{f(x+t) - f(x)} ~dx \to 0$ as $t \to 0$.
Proof: It suffices to check convergence along any sequence $t_k \to 0$.
By <2>2 the integrands converge pointwise to $0$, and by <2>3 they are dominated by the fixed integrable function $2\norm{f}_\infty \chi_{K+\overline{B_1}}$ (once $\abs{t_k} \leq 1$). The dominated convergence theorem yields the limit $0$.
<2>5. Q.E.D. Proof: This proves (1).

<1>2. The translation map is strongly continuous on $L^1$: for every $f \in L^1(\RR^n)$, $\int \abs{f(x+t) - f(x)} ~dx \to 0$ as $t \to 0$.
<2>1. The claim holds for $f \in C_c^0(\RR^n)$.
Proof: This is exactly part (1). <2>2. $C_c^0(\RR^n)$ is dense in $L^1(\RR^n)$.
Proof: Standard density theorem: continuous functions of compact support are dense in $L^1$.
<2>3. Fix $\eps > 0$ and choose $h \in C_c^0(\RR^n)$ with $\norm{f - h}_1 < \eps/3$; then $$\int \abs{f(x+t) - f(x)} ~dx \leq \int \abs{f(x+t) - h(x+t)} ~dx + \int \abs{h(x+t) - h(x)} ~dx + \int \abs{h(x) - f(x)} ~dx.$$ Proof: Insert $\pm h(x+t)$ and $\pm h(x)$, then apply the triangle inequality to the three pairs.
<2>4. $\int \abs{f(x+t) - h(x+t)} ~dx = \norm{f - h}_1$ for every $t$.
Proof: Change of variables $u = x + t$ (Jacobian $1$) in the integral.
<2>5. For $\abs{t}$ sufficiently small, $\int \abs{h(x+t) - h(x)} ~dx < \eps/3$.
Proof: By <2>1 applied to $h$, since $h \in C_c^0$.
<2>6. Hence $\int \abs{f(x+t) - f(x)} ~dx < \eps$ for all $\abs{t}$ sufficiently small.
Proof: Combine <2>3, <2>4, <2>5: the first and third terms are $< \eps/3$ and the middle is $< \eps/3$.
<2>7. Q.E.D. Proof: $\eps > 0$ was arbitrary.

<1>3. If $f \in L^1(\RR^n)$ and $g \in L^\infty(\RR^n)$, then $f \ast g$ is bounded.
<2>1. For each $x$, $\int \abs{f(t)} \abs{g(x-t)} ~dt \leq \norm{g}_\infty \norm{f}_1 < \infty$.
Proof: $\abs{g(x-t)} \leq \norm{g}_\infty$ for almost every $t$, so the integrand is dominated by $\norm{g}_\infty \abs{f(t)} \in L^1$.
<2>2. Hence $f \ast g$ is defined (a.e.) and $\abs{(f \ast g)(x)} \leq \norm{g}_\infty \norm{f}_1$ for all $x$ where it is defined.
Proof: By <2>1 and the triangle inequality.
<2>3. Q.E.D. Proof: The bound of <2>2 is independent of $x$.

<1>4. $f \ast g$ is uniformly continuous.
<2>1. For any $x, h$, $(f \ast g)(x+h) - (f \ast g)(x) = \int f(t) \left(g(x+h-t) - g(x-t)\right) ~dt$.
Proof: Linearity of the integral: the difference of the two convolutions is the integral of $f(t)$ times the difference of the two $g$-factors.
<2>2. It suffices to prove the claim for $f \in C_c^0(\RR^n)$.
Proof: Given $f \in L^1$ and $\eps > 0$, choose $h \in C_c^0$ with $\norm{f - h}_1 < \eps/(4\norm{g}_\infty + 1)$ (density, <1>2<2>2). Then $$\abs{(f \ast g)(x+h_0) - (f \ast g)(x)} \leq \abs{((f-h) \ast g)(x+h_0) - ((f-h) \ast g)(x)} + \abs{(h \ast g)(x+h_0) - (h \ast g)(x)},$$ and the first term is $\leq 2\norm{g}_\infty \norm{f-h}_1 < \eps/2$ by <1>3. If $h \ast g$ is uniformly continuous, the second term is $< \eps/2$ for $\abs{h_0}$ small, uniformly in $x$.
<2>3. For $f \in C_c^0(\RR^n)$, $f \ast g$ is uniformly continuous.
Proof: Write $(f \ast g)(x) = \int f(x - u) g(u) ~du$ (change of variables $u = x - t$). Fix $h_0$ and set $K = \operatorname{supp}(f)$; the difference $$(f \ast g)(x+h_0) - (f \ast g)(x) = \int \left(f(x+h_0 - u) - f(x - u)\right) g(u) ~du$$ has integrand supported on the set $\{u : x + h_0 - u \in K \text{ or } x - u \in K\}$, which has measure $\leq 2 m(K)$ independently of $x$, and bounded by $2 \norm{f}_\infty \norm{g}_\infty$ pointwise.
Since $f$ is uniformly continuous (<2>1 of <1>1), $f(x + h_0 - u) - f(x - u) \to 0$ uniformly in $(x, u)$ as $h_0 \to 0$.
The dominated convergence theorem (with the fixed bound $2\norm{f}_\infty\norm{g}_\infty$ on a set of measure $\leq 2m(K)$) gives $\sup_x \abs{(f \ast g)(x+h_0) - (f \ast g)(x)} \to 0$ as $h_0 \to 0$, which is uniform continuity.
<2>4. Q.E.D. Proof: By <2>2, the general case reduces to <2>3.

<1>5. Conclusion.
Proof: (1) is <1>1. The $L^1$ extension is <1>2. Boundedness and uniform continuity of $f \ast g$ are <1>3 and <1>4.
:::
