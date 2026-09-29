---
schema: qual/card@1
id: P-RASP08B
kind: problem
title: "Convergence of level sets under monotone a.e. convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.problem}
Let $(X, \mu)$ be a measure space and $f, f_n : X \to \mathbb{R}$ measurable functions such that $f_1 \leq f_2 \leq \cdots \leq f_n \leq \cdots$ a.e. and $\lim_{n \to \infty} f_n = f$ a.e.

(a) For every $a \in \mathbb{R}$, show that $\lim_{n \to \infty} \mu(\{x : f_n(x) > a\})$ exists and
$$
\lim_{n \to \infty} \mu(\{x : f_n(x) > a\}) = \mu(\{x : f(x) > a\}).
$$

(b) Assume that $\mu(X) < \infty$.
Show that $\lim_{n \to \infty} \mu(\{x : f_n(x) < a\})$ exists for every $a \in \mathbb{R}$ and
$$
\mu(\{x : f(x) < a\}) \leq \lim_{n \to \infty} \mu(\{x : f_n(x) < a\}) \leq \mu(\{x : f(x) < a\}) + \mu(\{x : f(x) = a\}).
$$
Give an example where
$$
\mu(\{x : f(x) < a\}) < \lim_{n \to \infty} \mu(\{x : f_n(x) < a\})
$$
for some $a \in \mathbb{R}$.
:::

::: {.solution}
**Goal:** Prove the continuity of measures for level sets under monotone a.e. convergence and provide a strict inequality counterexample.

::: pf

::: pf-step
Null set reduction:
Let $N \subset X$ be a measurable null set ($\mu(N) = 0$) such that for all $x \in X \setminus N$:
$$f_1(x) \le f_2(x) \le \cdots \le f_n(x) \le \cdots \quad \text{and} \quad \lim_{n\to\infty} f_n(x) = f(x) = \sup_{n\ge 1} f_n(x).$$

::: pf-proof
Monotonicity holds outside a countable union of null sets $N_k$ where $f_k(x) > f_{k+1}(x)$, and pointwise convergence holds outside a null set $N_0$. The union $N = N_0 \cup \bigcup_{k=1}^\infty N_k$ satisfies $\mu(N) = 0$.
:::

:::

::: pf-step
Part (a): $\lim_{n\to\infty} \mu(\{x : f_n(x) > a\}) = \mu(\{x : f(x) > a\})$.

::: pf-proof

::: pf-step
Define $E_n = \{x \in X \setminus N : f_n(x) > a\}$ and $E = \{x \in X \setminus N : f(x) > a\}$.
:::

::: pf-step
Since $f_n(x) \le f_{n+1}(x)$ on $X \setminus N$, $f_n(x) > a \implies f_{n+1}(x) > a$, so $E_n \subseteq E_{n+1}$.
:::

::: pf-step
If $x \in \bigcup_{n=1}^\infty E_n$, then $f_n(x) > a$ for some $n$, so $f(x) \ge f_n(x) > a$, meaning $x \in E$.
:::

::: pf-step
If $x \in E$, then $f(x) > a$. Since $\lim_{n\to\infty} f_n(x) = f(x)$, there exists $n_0$ such that $f_n(x) > a$ for all $n \ge n_0$, so $x \in E_{n_0} \subseteq \bigcup_{n=1}^\infty E_n$.
:::

::: pf-step
Thus $\{E_n\}$ is an increasing sequence of measurable sets with $\bigcup_{n=1}^\infty E_n = E$.
:::

::: pf-step
By continuity of measure from below:
$$\lim_{n\to\infty} \mu(\{x : f_n(x) > a\}) = \lim_{n\to\infty} \mu(E_n) = \mu(E) = \mu(\{x : f(x) > a\}).$$
:::

:::

:::

::: pf-step
Part (b): Bounds on $\lim_{n\to\infty} \mu(\{x : f_n(x) < a\})$ when $\mu(X) < \infty$.

::: pf-proof

::: pf-step
Define $A_n = \{x \in X \setminus N : f_n(x) < a\}$.
:::

::: pf-step
If $f_{n+1}(x) < a$, then $f_n(x) \le f_{n+1}(x) < a$, so $A_{n+1} \subseteq A_n$.
:::

::: pf-step
Since $\mu(X) < \infty$, $\mu(A_1) \le \mu(X) < \infty$. By continuity of measure from above:
$$\lim_{n\to\infty} \mu(\{x : f_n(x) < a\}) = \lim_{n\to\infty} \mu(A_n) = \mu\left(\bigcap_{n=1}^\infty A_n\right).$$
:::

::: pf-step
For $x \in X \setminus N$: $x \in \bigcap_{n=1}^\infty A_n \iff \forall n, f_n(x) < a \iff \sup_{n\ge 1} f_n(x) \le a \iff f(x) \le a$.
:::

::: pf-step
If $f(x) < a$, then for all $n$, $f_n(x) \le f(x) < a$, so $\{x \in X \setminus N : f(x) < a\} \subseteq \bigcap_{n=1}^\infty A_n$.
:::

::: pf-step
Thus $\{x \in X \setminus N : f(x) < a\} \subseteq \bigcap_{n=1}^\infty A_n \subseteq \{x \in X \setminus N : f(x) \le a\}$.
:::

::: pf-step
Taking measures:
$$\mu(\{f < a\}) \le \mu\left(\bigcap_{n=1}^\infty A_n\right) \le \mu(\{f \le a\}) = \mu(\{f < a\}) + \mu(\{f = a\}).$$
:::

:::

:::

::: pf-step
Counterexample with strict inequality:

::: pf-proof

::: pf-step
Let $X = [0, 1]$ equipped with Lebesgue measure $m$, so $m(X) = 1 < \infty$.
:::

::: pf-step
Choose $a = 0$.
:::

::: pf-step
For each $n \ge 1$, define $f_n(x) = -\frac{1}{n}$ for all $x \in [0, 1]$, and $f(x) = 0$.
:::

::: pf-step
Then $f_1 \le f_2 \le \cdots$ everywhere and $f_n(x) \to f(x) = 0$.
:::

::: pf-step
For each $n$, $\{x \in [0, 1] : f_n(x) < 0\} = [0, 1]$, so $m(\{x : f_n(x) < 0\}) = 1$.
:::

::: pf-step
Hence $\lim_{n\to\infty} m(\{x : f_n(x) < 0\}) = 1$.
:::

::: pf-step
However, $\{x \in [0, 1] : f(x) < 0\} = \emptyset$, so $m(\{x : f(x) < 0\}) = 0$.
:::

::: pf-step
Thus $0 = m(\{f < 0\}) < \lim_{n\to\infty} m(\{f_n < 0\}) = 1$.
:::

:::

:::

:::
:::
