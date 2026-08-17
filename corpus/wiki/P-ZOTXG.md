---
schema: qual/card@1
id: P-ZOTXG
kind: problem
title: $L^1$ convolution with a bounded measurable function is bounded and uniformly continuous, and $(f*g)'=f*g'$ when $g'$ is bounded
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - uniform-continuity
  - differentiation
relations: []
review: draft
solved: true
---

::: problem
Let $f \in L^1(\RR)$ and $g$ be a bounded measurable function on $\RR$.

1. Show that the convolution $f\ast g$ is well-defined, bounded, and uniformly continuous on $\RR$.

2. Prove that one further assumes that $g \in C^1(\RR)$ with bounded derivative, then $f\ast g \in C^1(\RR)$ and
\[
\frac{d}{d x}(f * g)=f *\left(\frac{d}{d x} g\right)
\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. (Part 1) $f \ast g$ is well-defined and bounded.
    Proof: $g$ bounded, $|g| \le M$ a.e., and $f \in L^1$; by Tonelli/Fubini the convolution $(f\ast g)(x) = \int f(y)g(x-y)\,dy$ converges absolutely for every $x$ with
    \[
    |(f\ast g)(x)| \le \int |f(y)||g(x-y)|\,dy \le M \norm{f}_1 < \infty .
    \]
<1>2. $f \ast g$ is uniformly continuous.
    Proof: for $h \in \RR$,
    \[
    (f\ast g)(x+h) - (f\ast g)(x) = \int f(y)\big(g(x+h-y) - g(x-y)\big)\,dy = \int \big(f(y-h) - f(y)\big)g(x-y)\,dy ,
    \]
    so
    \[
    |(f\ast g)(x+h) - (f\ast g)(x)| \le M \int |f(y-h) - f(y)|\,dy = M \norm{\tau_h f - f}_1 ,
    \]
    and $\norm{\tau_h f - f}_1 \to 0$ as $h \to 0$ (strong continuity of translation in $L^1$). The bound is independent of $x$, so $f\ast g$ is uniformly continuous.
<1>3. (Part 2) $f \ast g$ is differentiable with derivative $f \ast g'$.
    Proof: fix $x$. For $h \ne 0$,
    \[
    \frac{(f\ast g)(x+h) - (f\ast g)(x)}{h} = \int f(y)\,\frac{g(x+h-y) - g(x-y)}{h}\,dy .
    \]
    As $h \to 0$: the difference quotient of $g$ converges pointwise to $g'(x-y)$ (since $g \in C^1$), and is bounded in absolute value by $\norm{g'}_\infty$ (mean value theorem). Since $|f| \in L^1$, the dominated convergence theorem gives
    \[
    \lim_{h\to 0}\frac{(f\ast g)(x+h) - (f\ast g)(x)}{h} = \int f(y)g'(x-y)\,dy = (f\ast g')(x) .
    \]
<1>4. $f \ast g'$ is continuous, so $f\ast g \in C^1(\RR)$.
    Proof: $g'$ is bounded (by hypothesis) and measurable, so by <1>2 applied to $(f, g')$, $f\ast g'$ is continuous; by <1>3 it is the derivative of $f\ast g$ everywhere.
<1>5. Q.E.D.
:::
