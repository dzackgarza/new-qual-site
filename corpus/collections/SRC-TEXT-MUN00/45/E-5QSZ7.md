---
schema: qual/card@1
id: E-5QSZ7
kind: exercise
title: Sources of equicontinuity
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $(Y, d)$ be a metric space; let $\mathcal{F}$ be a subset of $\mathcal{C}(X, Y)$.

(a) Show that if $\mathcal{F}$ is finite, then $\mathcal{F}$ is equicontinuous.

(b) Show that if $f_n$ is a sequence of elements of $\mathcal{C}(X, Y)$ that converges uniformly, then the collection $\ts{f_n}$ is equicontinuous.

(c) Suppose that $\mathcal{F}$ is a collection of differentiable functions $f: \mathbb{R} \to \mathbb{R}$ such that each $x \in \mathbb{R}$ lies in a neighborhood $U$ on which the derivatives of the functions in $\mathcal{F}$ are uniformly bounded.
[This means that there is an $M$ such that $\abs{f'(x)} \leq M$ for all $f$ in $\mathcal{F}$ and all $x \in U$.] Show that $\mathcal{F}$ is equicontinuous.
:::

::: solution
**Goal:** Prove equicontinuity for (a) finite families of continuous functions, (b) uniformly convergent sequences of continuous functions, and (c) families of differentiable functions with locally uniformly bounded derivatives.

<1>1. Part (a): Finite collections are equicontinuous.
    *Proof:*
    <2>1. Let $\mathcal{F} = \{f_1, \dots, f_k\}$ be finite, and let $x_0 \in X, \varepsilon > 0$.
    <2>2. For each $i \in \{1, \dots, k\}$, continuity of $f_i$ at $x_0$ guarantees an open neighborhood $U_i \subseteq X$ of $x_0$ such that $d(f_i(x), f_i(x_0)) < \varepsilon$ for all $x \in U_i$.
    <2>3. Define $U = \bigcap_{i=1}^k U_i$. As a finite intersection of open neighborhoods of $x_0$, $U$ is an open neighborhood of $x_0$.
    <2>4. For all $x \in U$ and all $f \in \mathcal{F}$, $d(f(x), f(x_0)) < \varepsilon$. Thus $\mathcal{F}$ is equicontinuous.

<1>2. Part (b): Uniformly convergent sequences $\{f_n\}$ are equicontinuous.
    *Proof:*
    <2>1. Let $f_n \to f$ uniformly on $X$, with $x_0 \in X$ and $\varepsilon > 0$. By the uniform limit theorem, $f: X \to Y$ is continuous.
    <2>2. Choose an integer $N \ge 1$ such that $d(f_n(x), f(x)) < \frac{\varepsilon}{3}$ for all $n \ge N$ and all $x \in X$.
    <2>3. By continuity of $f$ at $x_0$, choose an open neighborhood $U_0 \subseteq X$ of $x_0$ such that $d(f(x), f(x_0)) < \frac{\varepsilon}{3}$ for all $x \in U_0$.
    <2>4. For each $n \in \{1, \dots, N-1\}$, choose an open neighborhood $U_n$ of $x_0$ such that $d(f_n(x), f_n(x_0)) < \varepsilon$ for all $x \in U_n$.
    <2>5. Set $U = \bigcap_{n=0}^{N-1} U_n$, which is an open neighborhood of $x_0$.
    <2>6. For any $n < N$ and $x \in U$, $d(f_n(x), f_n(x_0)) < \varepsilon$ since $x \in U_n$.
    <2>7. For any $n \ge N$ and $x \in U$, the triangle inequality gives:
        $$d(f_n(x), f_n(x_0)) \le d(f_n(x), f(x)) + d(f(x), f(x_0)) + d(f(x_0), f_n(x_0)) < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$
    <2>8. Thus $\{f_n\}_{n=1}^\infty$ is equicontinuous at $x_0$, hence equicontinuous on $X$.

<1>3. Part (c): Locally uniformly bounded derivatives imply equicontinuity.
    *Proof:*
    <2>1. Let $x_0 \in \mathbb{R}$ and $\varepsilon > 0$.
    <2>2. By hypothesis, there exists an open neighborhood $U_0 \ni x_0$ and a constant $M > 0$ such that $|f'(t)| \le M$ for all $f \in \mathcal{F}$ and all $t \in U_0$.
    <2>3. Choose $\delta > 0$ such that the interval $U = (x_0 - \delta, x_0 + \delta) \subseteq U_0$ and $\delta < \frac{\varepsilon}{M}$.
    <2>4. For any $x \in U$ and any $f \in \mathcal{F}$, by the Mean Value Theorem, there exists a point $c$ strictly between $x$ and $x_0$ such that:
        $$|f(x) - f(x_0)| = |f'(c)| |x - x_0|.$$
    <2>5. Since $c \in U \subseteq U_0$, $|f'(c)| \le M$.
    <2>6. Consequently, $|f(x) - f(x_0)| \le M |x - x_0| < M \delta < \varepsilon$.
    <2>7. Thus $\mathcal{F}$ is equicontinuous at $x_0$, and therefore on $\mathbb{R}$. Q.E.D.
:::
