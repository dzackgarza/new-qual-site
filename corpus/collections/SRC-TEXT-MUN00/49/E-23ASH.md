---
schema: qual/card@1
id: E-23ASH
kind: exercise
title: Small functions in the nowhere-differentiability open sets
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Given $n$ and $\epsilon$, define a continuous function $f: I \to \mathbb{R}$ such that $f \in U_n$ and $\abs{f(x)} \leq \epsilon$ for all $x$.
:::

::: solution
**Goal:** Construct a continuous function $f: [0, 1] \to [-\varepsilon, \varepsilon]$ in the nowhere-differentiability open set $U_n = \{f \in \mathcal{C}(I, \mathbb{R}) : \forall x \in I, \exists t \in I, 0 < |x - t| < \frac{1}{n} \text{ and } |\frac{f(x) - f(t)}{x - t}| > n\}$.

<1>1. Parameter selection:
    Given $n \in \mathbb{Z}_+$ and $\varepsilon > 0$, choose an integer $k \in \mathbb{Z}_+$ sufficiently large such that:
    $$k > 2n \quad \text{and} \quad k > \frac{2n}{\varepsilon}.$$
    Let $h = \frac{1}{2k}$. Then $h < \frac{1}{4n} < \frac{1}{n}$ and $\frac{\varepsilon}{h} = 2k\varepsilon > 4n > n$.

<1>2. Construction of the sawtooth function $f$:
    Partition $[0, 1]$ into $2k$ subintervals of equal length $h = \frac{1}{2k}$ by the division points $t_j = jh$ for $j = 0, 1, \dots, 2k$.
    Define $f: [0, 1] \to \mathbb{R}$ to be the continuous piecewise linear function with values at the vertices:
    $$f(t_j) = \begin{cases} \varepsilon & \text{if } j \text{ is odd}, \\ 0 & \text{if } j \text{ is even}, \end{cases}$$
    and linearly interpolated on each subinterval $[t_{j-1}, t_j]$.

<1>3. Uniform bound on $f$:
    For all $x \in [0, 1]$, $0 \le f(x) \le \varepsilon$, so $|f(x)| \le \varepsilon$.
    *Proof:* On each subinterval $[t_{j-1}, t_j]$, $f$ is linear with endpoint values in $\{0, \varepsilon\}$. By convexity, $0 \le f(x) \le \varepsilon$.

<1>4. Secant slope property ($f \in U_n$):
    For every $x \in [0, 1]$, there exists $t \in [0, 1]$ such that $0 < |x - t| < \frac{1}{n}$ and $\left|\frac{f(x) - f(t)}{x - t}\right| > n$.
    *Proof:*
    <2>1. For any $x \in [0, 1]$, $x$ belongs to some subinterval $[t_{j-1}, t_j]$ of length $h$.
    <2>2. The function $f$ is strictly linear on $[t_{j-1}, t_j]$ with constant slope magnitude:
        $$\left|\frac{f(t_j) - f(t_{j-1})}{t_j - t_{j-1}}\right| = \frac{\varepsilon}{h} = 2k\varepsilon > 4n > n.$$
    <2>3. If $x \neq t_j$, choose $t = t_j$. Then $0 < |t - x| \le h < \frac{1}{n}$, and by linearity on $[t_{j-1}, t_j]$, $\left|\frac{f(x) - f(t)}{x - t}\right| = \frac{\varepsilon}{h} > n$.
    <2>4. If $x = t_j$, choose $t = t_{j-1}$ (or $t_{j+1}$ if $j = 0$). Then $0 < |t - x| = h < \frac{1}{n}$, and the secant slope is $\frac{\varepsilon}{h} > n$.
    <2>5. Hence $f \in U_n$.

<1>5. Conclusion:
    The constructed continuous function $f$ satisfies $f \in U_n$ and $|f(x)| \le \varepsilon$ for all $x \in [0, 1]$. Q.E.D.
:::
