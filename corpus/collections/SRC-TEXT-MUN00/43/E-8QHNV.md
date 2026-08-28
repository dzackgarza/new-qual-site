---
schema: qual/card@1
id: E-8QHNV
kind: exercise
title: Uniformly continuous maps extend to the closure
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces; let $Y$ be complete.
Let $A \subset X$.
Show that if $f: A \to Y$ is uniformly continuous, then $f$ can be uniquely extended to a continuous function $g: \overline{A} \to Y$, and $g$ is uniformly continuous.
:::

::: solution
**Goal:** Prove that a uniformly continuous map $f: A \to Y$ into a complete metric space $Y$ extends uniquely to a uniformly continuous map $g: \overline{A} \to Y$.

<1>1. Definition and well-definedness of the extension $g$:
    *Proof:*
    <2>1. Let $x \in \overline{A}$. There exists a sequence $(x_n)_{n=1}^\infty$ in $A$ such that $\lim_{n \to \infty} x_n = x$.
    <2>2. Since $(x_n)$ converges in $X$, it is a Cauchy sequence in $X$.
    <2>3. Because $f$ is uniformly continuous, it preserves Cauchy sequences: for any $\varepsilon > 0$, there exists $\delta > 0$ such that $d_X(a, b) < \delta \implies d_Y(f(a), f(b)) < \varepsilon$.
    <2>4. For large $n, m$, $d_X(x_n, x_m) < \delta$, so $d_Y(f(x_n), f(x_m)) < \varepsilon$. Thus $(f(x_n))_{n=1}^\infty$ is Cauchy in $Y$.
    <2>5. Completeness of $(Y, d_Y)$ ensures that $(f(x_n))$ converges to a unique limit $L \in Y$. Define $g(x) = \lim_{n \to \infty} f(x_n)$.
    <2>6. If $(x_n')$ is another sequence in $A$ converging to $x$, then $d_X(x_n, x_n') \to 0$, so $d_Y(f(x_n), f(x_n')) \to 0$ by uniform continuity. Hence $\lim f(x_n) = \lim f(x_n')$, making $g(x)$ well-defined.
    <2>7. For $x \in A$, taking $x_n = x$ gives $g(x) = f(x)$, so $g|_A = f$.

<1>2. Uniform continuity of the extension $g$:
    *Proof:*
    <2>1. Given $\varepsilon > 0$, choose $\delta > 0$ such that for all $a, b \in A$, $d_X(a, b) < \delta \implies d_Y(f(a), f(b)) < \varepsilon/3$.
    <2>2. Let $x, y \in \overline{A}$ satisfy $d_X(x, y) < \delta/3$.
    <2>3. Choose sequences $(x_n), (y_n)$ in $A$ converging to $x, y$ respectively.
    <2>4. For all sufficiently large $n$, we have $d_X(x_n, x) < \delta/3$, $d_X(y_n, y) < \delta/3$, $d_Y(f(x_n), g(x)) < \varepsilon/3$, and $d_Y(f(y_n), g(y)) < \varepsilon/3$.
    <2>5. By the triangle inequality:
        $$d_X(x_n, y_n) \le d_X(x_n, x) + d_X(x, y) + d_X(y, y_n) < \frac{\delta}{3} + \frac{\delta}{3} + \frac{\delta}{3} = \delta.$$
    <2>6. Therefore $d_Y(f(x_n), f(y_n)) < \varepsilon/3$.
    <2>7. Applying the triangle inequality in $Y$:
        $$d_Y(g(x), g(y)) \le d_Y(g(x), f(x_n)) + d_Y(f(x_n), f(y_n)) + d_Y(f(y_n), g(y)) < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$
    <2>8. Thus $g$ is uniformly continuous on $\overline{A}$ (which also implies $g$ is continuous).

<1>3. Uniqueness of the continuous extension:
    *Proof:*
    <2>1. $A$ is dense in $\overline{A}$, and the metric codomain $Y$ is Hausdorff.
    <2>2. Any two continuous functions on $\overline{A}$ that agree on the dense subset $A$ are identically equal on all of $\overline{A}$.

<1>4. Conclusion:
    $f$ extends uniquely to a uniformly continuous function $g: \overline{A} \to Y$. Q.E.D.
:::
