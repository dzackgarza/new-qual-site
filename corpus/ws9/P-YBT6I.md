---
schema: qual/card@1
id: P-YBT6I
kind: problem
title: Convolution of two $L^2$ functions is bounded and continuous, and convolution by an $L^1$ function is a bounded operator on $L^1$
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - l2
  - l1
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $$f*g(x) := \int_{-\infty}^{+\infty} f(y)g(x-y)dy$$ denote the convolution of $f$ and $g$.

a. Let $f,g \in L^2(\mathbb{R})$ be two square-integrable functions on $\mathbb{R}$ (with the usual Lebesgue measure).
Show that the convolution $f*g$ is a bounded continuous function on $\mathbb{R}$.
b. Instead let $h \in L^1(\mathbb{R})$ be fixed.
Show that $A(f)=f*h$ is a bounded operator $L^1(\mathbb{R}) \to L^1(\mathbb{R})$.
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** (a) For $f, g \in L^2(\mathbb R)$: $f \ast g$ is bounded and continuous; (b) for $h \in L^1$: $A(f) = f \ast h$ is a bounded operator $L^1 \to L^1$.

<1>1. (a) $f \ast g$ is bounded.
Proof: by Cauchy–Schwarz, $|(f \ast g)(x)| = |\int f(y)g(x-y)dy| \le \|f\|_2\|g\|_2$ for every $x$ (since $y \mapsto g(x-y)$ has $L^2$ norm $\|g\|_2$ by translation invariance of Lebesgue measure).

<1>2. (a) $f \ast g$ is continuous.
<2>1. It suffices to show: $x_n \to x$ implies $(f \ast g)(x_n) \to (f \ast g)(x)$.
<2>2. $|(f\ast g)(x_n) - (f\ast g)(x)| = |\int f(y)[g(x_n - y) - g(x - y)]dy| \le \|f\|_2 \cdot \|g(\cdot + (x_n - x)) - g\|_2$.
Proof: Cauchy–Schwarz and the change of variables $y \mapsto y + (x_n - x)$.
<2>3. $\|g(\cdot + t_n) - g\|_2 \to 0$ as $t_n \to 0$ ($L^2$-continuity of translations).
Proof: standard: first for $g$ continuous with compact support (uniform continuity), then by density of such functions in $L^2$.
<2>4. Q.E.D. Proof: <2>2–<2>3 show $f \ast g$ is continuous.

<1>3. (b) $A(f) = f \ast h$ maps $L^1 \to L^1$ and is bounded with $\|A\| \le \|h\|_1$.
<2>1. For $f \in L^1$: $\|f \ast h\|_1 = \int |\int f(y)h(x-y)dy|dx \le \int\int |f(y)||h(x-y)|dy\,dx$.
<2>2. By Tonelli: $\int\int |f(y)||h(x-y)|dy\,dx = \int |f(y)|\left(\int |h(x-y)|dx\right)dy = \int |f(y)|\|h\|_1 dy = \|f\|_1\|h\|_1$.
Proof: the inner integral is $\|h\|_1$ by translation invariance.
<2>3. $\|f \ast h\|_1 \le \|f\|_1\|h\|_1$: $A$ is bounded with $\|A\| \le \|h\|_1$ (indeed $= \|h\|_1$). Proof: <2>1–<2>2; the operator norm is exactly $\|h\|_1$ (Young's inequality with $p = q = 1$, $r = 1$). <2>4. Q.E.D. Proof: <2>3 shows $A$ is a bounded linear operator $L^1 \to L^1$.
:::
