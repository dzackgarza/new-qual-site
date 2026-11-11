---
schema: qual/card@1
id: E-8QHNV
kind: problem
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
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    Transcribed from the located published solution: "Tze Heng", *Munkres' Topology: Self-study Notes
    and Exercises Attempts*, "Chapter 7", "Exercises Attempts", item under "Exercise after §43" numbered
    2 (URL https://blog.ttheng.com/docs/mathematics/munkres-topology-self-study/chapt-7/exercises/, read
    2026-11-11; a web page has no printed page, so it is cited by URL and date read). Checked against
    Munkres, Topology (2000), §43 Exercise 2, printed p. 270, with the Sequence Lemma (Lemma 21.2), the
    definition of uniform continuity and the fact that a uniformly continuous map takes Cauchy sequences
    to Cauchy sequences. The blog's argument is the one on the card: the extension is defined by
    g(a) = lim f(a_n) along sequences a_n -> a in A, well defined because two such sequences have
    d_X(a_n, b_n) -> 0, completeness of Y supplies the limits, uniform continuity of g follows with the
    factor three bookkeeping on delta/3, and uniqueness because two continuous maps into a Hausdorff
    space that agree on a dense subspace agree. What was corrected: the blog closes the uniform
    continuity with "taking limits over n we have d_Y(g(x), g(y)) < eps", which needs the limit to be
    taken after the delta/3 comparison of d_X(x_n,y_n) is made for all large n; the card writes the
    three-term triangle inequalities explicitly in both X and Y. The card's earlier dangling step
    references, to labels that no step carried, are replaced by the prose sentence that closes the
    solution.
---

::: {.exercise}

Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces; let $Y$ be complete.
Let $A \subset X$.
Show that if $f: A \to Y$ is uniformly continuous, then $f$ can be uniquely extended to a continuous function $g: \overline{A} \to Y$, and $g$ is uniformly continuous.
:::

::: {.solution}

::: pf

::: pf-step

Definition and well-definedness of the extension $g$:
    *Proof:*

::: pf-proof

::: pf-step

Let $x \in \overline{A}$. There exists a sequence $(x_n)_{n=1}^\infty$ in $A$ such that $\lim_{n \to \infty} x_n = x$.

:::

::: pf-step

Since $(x_n)$ converges in $X$, it is a Cauchy sequence in $X$.

:::

::: pf-step

Because $f$ is uniformly continuous, it preserves Cauchy sequences: for any $\varepsilon > 0$, there exists $\delta > 0$ such that $d_X(a, b) < \delta \implies d_Y(f(a), f(b)) < \varepsilon$.

:::

::: pf-step

For large $n, m$, $d_X(x_n, x_m) < \delta$, so $d_Y(f(x_n), f(x_m)) < \varepsilon$. Thus $(f(x_n))_{n=1}^\infty$ is Cauchy in $Y$.

:::

::: pf-step

Completeness of $(Y, d_Y)$ ensures that $(f(x_n))$ converges to a unique limit $L \in Y$. Define $g(x) = \lim_{n \to \infty} f(x_n)$.

:::

::: pf-step

If $(x_n')$ is another sequence in $A$ converging to $x$, then $d_X(x_n, x_n') \to 0$, so $d_Y(f(x_n), f(x_n')) \to 0$ by uniform continuity. Hence $\lim f(x_n) = \lim f(x_n')$, making $g(x)$ well-defined.

:::

::: pf-step

For $x \in A$, taking $x_n = x$ gives $g(x) = f(x)$, so $g\restrict_A = f$.

:::

:::

:::

::: pf-step

Uniform continuity of the extension $g$:
    *Proof:*

::: pf-proof

::: pf-step

Given $\varepsilon > 0$, choose $\delta > 0$ such that for all $a, b \in A$, $d_X(a, b) < \delta \implies d_Y(f(a), f(b)) < \varepsilon/3$.

:::

::: pf-step

Let $x, y \in \overline{A}$ satisfy $d_X(x, y) < \delta/3$.

:::

::: pf-step

Choose sequences $(x_n), (y_n)$ in $A$ converging to $x, y$ respectively.

:::

::: pf-step

For all sufficiently large $n$, we have $d_X(x_n, x) < \delta/3$, $d_X(y_n, y) < \delta/3$, $d_Y(f(x_n), g(x)) < \varepsilon/3$, and $d_Y(f(y_n), g(y)) < \varepsilon/3$.

:::

::: pf-step

By the triangle inequality:
        $$d_X(x_n, y_n) \le d_X(x_n, x) + d_X(x, y) + d_X(y, y_n) < \frac{\delta}{3} + \frac{\delta}{3} + \frac{\delta}{3} = \delta.$$

:::

::: pf-step

Therefore $d_Y(f(x_n), f(y_n)) < \varepsilon/3$.

:::

::: pf-step

Applying the triangle inequality in $Y$:
        $$d_Y(g(x), g(y)) \le d_Y(g(x), f(x_n)) + d_Y(f(x_n), f(y_n)) + d_Y(f(y_n), g(y)) < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$

:::

::: pf-step

Thus $g$ is uniformly continuous on $\overline{A}$ (which also implies $g$ is continuous).

:::

:::

:::

::: pf-step

Uniqueness of the continuous extension:
    *Proof:*

::: pf-proof

::: pf-step

$A$ is dense in $\overline{A}$, and the metric codomain $Y$ is Hausdorff.

:::

::: pf-step

Any two continuous functions on $\overline{A}$ that agree on the dense subset $A$ are identically equal on all of $\overline{A}$.

:::

:::

:::

:::

Steps above give existence of the extension $g$, its uniform continuity, and its uniqueness among continuous extensions. For uniqueness: $Y$ is a metric space, hence Hausdorff, so the diagonal $\Delta$ is closed in $Y \times Y$ (Exercise 17.13); the set on which two continuous maps $g, h: \overline{A} \to Y$ agree is $(g \times h)^{-1}(\Delta)$, closed by the closed-set formulation of continuity (Theorem 18.1), and it contains the dense subset $A$, so it is all of $\overline{A}$.
:::
