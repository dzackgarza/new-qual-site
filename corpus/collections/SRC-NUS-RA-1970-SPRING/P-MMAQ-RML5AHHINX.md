---
schema: qual/card@1
id: P-MMAQ-RML5AHHINX
kind: problem
title: Darboux's theorem for $f'$ attaining $2$, and $f'(0)=\lim_{x\to 0}f'(x)$ when
  $f$ is continuous and the limit exists
classification:
  areas:
  - real-analysis
  topics:
  - Mean Value Theorem
  - Sequences of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
(a) Let $f : \mathbb{R} \to \mathbb{R}$ be a differentiable function.
    If $f'(-1) < 2$ and $f'(1) > 2$, show that there exists $x_0 \in (i1, 1)$ such that $f'(x_0) = 2$.

    > Hint: consider the function $f(x) - 2x$ and recall the proof of Rolle's theorem.)

(b) Let $f : (-1, 1) \to \mathbb{R}$ be a differentiable function on $(-1, 0) \union (0, 1)$ such that $\lim_{x\to 0} f'(x) = L$.
    If $f$ is continuous on $(-1, 1)$, show that $f$ is indeed differentiable at $0$ and $f'(0) = L$.
:::

::: {.solution}
**Goal:** (a) If $f$ is differentiable on $\RR$ with $f'(-1) < 2 < f'(1)$, show $f'(x_0) = 2$ for some $x_0 \in (-1, 1)$. (b) If $f$ is continuous on $(-1,1)$, differentiable on $(-1,0) \union (0,1)$, and $\lim_{x \to 0} f'(x) = L$, show $f$ is differentiable at $0$ with $f'(0) = L$.

<1>1. Proof of (a).
    <2>1. Define $g(x) \definedas f(x) - 2x$; then $g'(-1) = f'(-1) - 2 < 0$ and $g'(1) = f'(1) - 2 > 0$.
        Proof: Differentiate $g$; the inequalities are the hypotheses.
    <2>2. Derivatives have the intermediate value property (Darboux's theorem): $g'$ takes every value between $g'(-1)$ and $g'(1)$ on $(-1, 1)$.
        Proof: Standard theorem: every derivative has the Darboux property on intervals. (Sketch of the classical proof: if $g'(a) < c < g'(b)$, the function $h(x) = g(x) - cx$ has $h'(a) < 0 < h'(b)$, and $h$ attains a minimum in $[a,b]$; a minimum in the interior forces $h' = 0$ there, while the endpoint case contradicts the sign of the one-sided derivatives; Rolle's-theorem style argument.)
    <2>3. Since $0$ lies strictly between $g'(-1) < 0$ and $g'(1) > 0$, there is $x_0 \in (-1, 1)$ with $g'(x_0) = 0$.
        Proof: By <2>2 with $c = 0$.
    <2>4. Hence $f'(x_0) = 2$.
        Proof: $g'(x_0) = f'(x_0) - 2 = 0$.
    <2>5. Q.E.D.
        Proof: This proves (a).

<1>2. Proof of (b).
    <2>1. Fix $x > 0$ (with $x$ small, $x \in (0, 1)$); the mean value theorem applies to $f$ on $[0, x]$: $f(x) - f(0) = f'(c_x) x$ for some $c_x \in (0, x)$.
        Proof: $f$ is continuous on $[0, x]$ (hypothesis) and differentiable on $(0, x)$ (since $(0, x) \subseteq (0, 1)$); MVT applies.
    <2>2. Similarly for $x < 0$: $f(x) - f(0) = f'(c_x) x$ for some $c_x \in (x, 0)$.
        Proof: MVT on $[x, 0]$, differentiable on $(x, 0)$.
    <2>3. As $x \to 0$ (either side), the point $c_x$ (which lies between $0$ and $x$) tends to $0$, so $f'(c_x) \to L$.
        Proof: $c_x \to 0$ by the squeeze theorem, and $\lim_{t \to 0} f'(t) = L$ by hypothesis.
    <2>4. Hence $\frac{f(x) - f(0)}{x} = f'(c_x) \to L$ as $x \to 0$.
        Proof: Divide <2>1/<2>2 by $x$ and use <2>3; the same limit $L$ is obtained from both sides.
    <2>5. Q.E.D.
        Proof: The two-sided limit $\lim_{x \to 0} (f(x) - f(0))/x$ exists and equals $L$, so $f$ is differentiable at $0$ with $f'(0) = L$.
:::
