---
schema: qual/card@1
id: P-CAF11B
kind: problem
title: "Construction of a metric from a sequence of metrics and convergence characterization"
classification:
  areas:
  - complex-analysis
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $X$ be a set and $\{\rho_n\}$ a sequence of metrics on $X$.
Define $\rho$ on $X \times X$ by $$\rho(x, y) := \sum_{n=1}^{\infty} \frac{1}{n^2} \cdot \frac{\rho_n(x, y)}{1 + \rho_n(x, y)}.$$

(a) Show that $\rho(x, y) < \infty$ for all $x, y \in X$ and prove that $\rho$ is a metric on $X$.

(b) Let $\{x_j\}$ be a sequence in $X$, and $x \in X$.
Prove that $\lim_{j \to \infty} \rho(x_j, x) = 0$ if and only if $\lim_{j \to \infty} \rho_n(x_j, x) = 0$ for all $n \geq 1$.
:::

::: {.solution}
<1>1. Part (a): Finiteness and metric verification for $\rho$:
<2>1. For all $n \ge 1$ and $x, y \in X$, since $\rho_n(x, y) \ge 0$:
\[
0 \le \frac{\rho_n(x, y)}{1 + \rho_n(x, y)} < 1 \implies 0 \le \rho(x, y) \le \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} < \infty.
\]
Thus $\rho(x, y)$ is finite and well-defined on $X \times X$.
::: {.proof}
comparison with the convergent $p$-series $\sum \frac{1}{n^2}$.
:::
<2>2. **Identity of indiscernibles:**
- If $x = y$, then $\rho_n(x, x) = 0$ for all $n$, so $\rho(x, x) = 0$.
- If $\rho(x, y) = 0$, every non-negative term in the series must vanish, so $\frac{\rho_n(x, y)}{1+\rho_n(x, y)} = 0 \implies \rho_n(x, y) = 0$ for all $n$.
  Since each $\rho_n$ is a metric, $\rho_1(x, y) = 0 \implies x = y$.
::: {.proof}
sum of non-negative terms is zero iff each term is zero.
:::
<2>3. **Symmetry:**
Since $\rho_n(x, y) = \rho_n(y, x)$ for all $n$, we have $\rho(x, y) = \rho(y, x)$.
::: {.proof}
symmetry of each $\rho_n$.
:::
<2>4. **Triangle inequality:**
The function $f(t) = \frac{t}{1+t} = 1 - \frac{1}{1+t}$ is non-decreasing and subadditive on $[0, \infty)$.
Using the triangle inequality for $\rho_n$:
\[
\frac{\rho_n(x, z)}{1 + \rho_n(x, z)} \le \frac{\rho_n(x, y) + \rho_n(y, z)}{1 + \rho_n(x, y) + \rho_n(y, z)}
\le \frac{\rho_n(x, y)}{1 + \rho_n(x, y)} + \frac{\rho_n(y, z)}{1 + \rho_n(y, z)}.
\]
Multiplying by $\frac{1}{n^2}$ and summing over $n \ge 1$ yields:
\[
\rho(x, z) \le \rho(x, y) + \rho(y, z).
\]
::: {.proof}
term-by-term subadditivity.
:::
<2>5. Therefore $\rho$ is a metric on $X$.
::: {.proof}
metric space axioms (<2>1 through <2>4).
:::

<1>2. Part (b): Equivalence of sequence convergence:
<2>1. **Forward direction ($\implies$):** Assume $\lim_{j \to \infty} \rho(x_j, x) = 0$.
For any fixed $n \ge 1$:
\[
\frac{1}{n^2} \cdot \frac{\rho_n(x_j, x)}{1 + \rho_n(x_j, x)} \le \rho(x_j, x) \to 0 \quad \text{as } j \to \infty.
\]
Multiplying by $n^2$ gives $\frac{\rho_n(x_j, x)}{1 + \rho_n(x_j, x)} \to 0$, which implies $\lim_{j \to \infty} \rho_n(x_j, x) = 0$.
::: {.proof}
single term is bounded by the series sum.
:::
<2>2. **Reverse direction ($\impliedby$):** Assume $\lim_{j \to \infty} \rho_n(x_j, x) = 0$ for all $n \ge 1$.
Let $\varepsilon > 0$.
Choose $N \in \mathbb{N}$ large enough such that $\sum_{n = N+1}^\infty \frac{1}{n^2} < \frac{\varepsilon}{2}$.
::: {.proof}
convergence of $\sum \frac{1}{n^2}$.
:::
<2>3. For the finite sum $\sum_{n=1}^N \frac{1}{n^2} \frac{\rho_n(x_j, x)}{1 + \rho_n(x_j, x)}$:
Since each of the finitely many terms tends to $0$ as $j \to \infty$, there exists $J \in \mathbb{N}$ such that for all $j \ge J$:
\[
\sum_{n=1}^N \frac{1}{n^2} \frac{\rho_n(x_j, x)}{1 + \rho_n(x_j, x)} < \frac{\varepsilon}{2}.
\]
::: {.proof}
finite sum of vanishing sequences.
:::
<2>4. For all $j \ge J$, split the series at $N$:
\[
\rho(x_j, x) = \sum_{n=1}^N \frac{1}{n^2} \frac{\rho_n(x_j, x)}{1 + \rho_n(x_j, x)} + \sum_{n=N+1}^\infty \frac{1}{n^2} \frac{\rho_n(x_j, x)}{1 + \rho_n(x_j, x)}
< \frac{\varepsilon}{2} + \sum_{n=N+1}^\infty \frac{1}{n^2} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.
\]
Thus $\lim_{j \to \infty} \rho(x_j, x) = 0$.
::: {.proof}
$\varepsilon/2$ tail estimate and <2>3.
:::

<1>3. Conclusion:
$\rho$ is a metric on $X$, and $\rho(x_j, x) \to 0 \iff \forall n \ge 1, \, \rho_n(x_j, x) \to 0$. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
