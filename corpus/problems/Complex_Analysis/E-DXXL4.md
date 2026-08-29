---
schema: qual/card@1
id: E-DXXL4
kind: exercise
title: Uniform limit theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Uniform Continuity
  - Continuity
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Prove the Heine–Cantor Theorem: let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces. If $X$ is compact and $f: X \to Y$ is continuous, then $f$ is uniformly continuous.
:::

::: solution
**Goal:** Prove the Heine–Cantor Theorem: any continuous map from a compact metric space into a metric space is uniformly continuous.

<1>1. Setting and Target:
    *Proof:*
    <2>1. Let $(X, d_X)$ be a compact metric space, $(Y, d_Y)$ a metric space, and $f: X \to Y$ a continuous function.
    <2>2. We must show that for every $\varepsilon > 0$, there exists $\delta > 0$ such that for all $x, x' \in X$:
        $$d_X(x, x') < \delta \implies d_Y(f(x), f(x')) < \varepsilon.$$

<1>2. Open cover construction using continuity:
    *Proof:*
    <2>1. Let $\varepsilon > 0$ be given.
    <2>2. For each point $p \in X$, the continuity of $f$ at $p$ implies that there exists $\delta_p > 0$ such that:
        $$d_X(x, p) < \delta_p \implies d_Y(f(x), f(p)) < \frac{\varepsilon}{2}.$$
    <2>3. Consider the open ball $B\left(p, \frac{\delta_p}{2}\right) = \left\{ x \in X \mid d_X(x, p) < \frac{\delta_p}{2} \right\}$.
    <2>4. The collection of open balls $\mathcal{U} = \left\{ B\left(p, \frac{\delta_p}{2}\right) \;\middle|\; p \in X \right\}$ forms an open cover of $X$:
        $$X = \bigcup_{p \in X} B\left(p, \frac{\delta_p}{2}\right).$$

<1>3. Finite subcover by compactness:
    *Proof:*
    <2>1. Since $X$ is compact, there exists a finite subcollection $\{p_1, p_2, \dots, p_n\} \subset X$ such that:
        $$X = \bigcup_{i=1}^n B\left(p_i, \frac{\delta_{p_i}}{2}\right).$$
    <2>2. Define $\delta = \min \left\{ \frac{\delta_{p_1}}{2}, \frac{\delta_{p_2}}{2}, \dots, \frac{\delta_{p_n}}{2} \right\}$.
    <2>3. Because this is the minimum of finitely many strictly positive numbers, $\delta > 0$.

<1>4. Verification of uniform continuity with parameter $\delta$:
    *Proof:*
    <2>1. Let $x, x' \in X$ be any two points with $d_X(x, x') < \delta$.
    <2>2. Since the finite balls cover $X$, $x \in B\left(p_k, \frac{\delta_{p_k}}{2}\right)$ for some $k \in \{1, \dots, n\}$, which means:
        $$d_X(x, p_k) < \frac{\delta_{p_k}}{2}.$$
    <2>3. By the triangle inequality:
        $$d_X(x', p_k) \le d_X(x', x) + d_X(x, p_k) < \delta + \frac{\delta_{p_k}}{2} \le \frac{\delta_{p_k}}{2} + \frac{\delta_{p_k}}{2} = \delta_{p_k}.$$
    <2>4. By definition of $\delta_{p_k}$:
        - $d_X(x, p_k) < \delta_{p_k} \implies d_Y(f(x), f(p_k)) < \frac{\varepsilon}{2}$.
        - $d_X(x', p_k) < \delta_{p_k} \implies d_Y(f(x'), f(p_k)) < \frac{\varepsilon}{2}$.
    <2>5. Applying the triangle inequality in $Y$:
        $$d_Y(f(x), f(x')) \le d_Y(f(x), f(p_k)) + d_Y(f(p_k), f(x')) < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$

<1>5. Conclusion:
    $f$ is uniformly continuous on $X$. Q.E.D.
:::
