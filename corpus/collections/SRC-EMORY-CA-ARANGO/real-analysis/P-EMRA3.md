---
schema: qual/card@1
id: P-EMRA3
kind: problem
title: "Dominated convergence theorem and convergence in measure"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: problem
(a) State the Dominated Convergence Theorem for Lebesgue integrals.

(b) Let $\{f_n\}$ be a sequence of measurable functions on a Lebesgue measurable set $E$ which converges in measure to a function $f$ on $E$.
Suppose that for every $n$, $|f_n| \leq g$ with $g$ integrable on $E$.
Using the above theorem show that
$$
\int_E |f_n - f| \to 0.
$$
:::

::: {.solution}
**(a).**

<1>1. Let $\{f_n\}$ be a sequence of measurable functions on $E$ such that $f_n \to f$ a.e., and suppose there is an integrable $g$ with $|f_n| \le g$ a.e. for all $n$.
::: {.proof}
hypotheses of the theorem.
:::

<1>2. Then $f$ is integrable and $\int_E f_n \to \int_E f$.
::: {.proof}
conclusion of the Dominated Convergence Theorem.
:::

<1>3. Moreover $\int_E |f_n - f| \to 0$.
::: {.proof}
the same argument applied to $|f_n - f|$, which is dominated by $2g$ and converges to $0$ a.e.
:::

**(b).**

<1>1. Suppose for contradiction that $\int_E |f_n - f| \not\to 0$.
::: {.proof}
assume the conclusion fails.
:::

<1>2. Then there is $\varepsilon > 0$ and a subsequence $f_{n_k}$ with $\int_E |f_{n_k} - f| \ge \varepsilon$ for all $k$.
::: {.proof}
<1>1, negating convergence.
:::

<1>3. Since $f_{n_k} \to f$ in measure, there is a further subsequence $f_{n_{k_j}}$ converging to $f$ a.e.
::: {.proof}
convergence in measure implies a subsequence converges a.e.
:::

<1>4. $|f_{n_{k_j}} - f| \le 2g$ a.e., and $2g$ is integrable.
::: {.proof}
$|f_n| \le g$ and $|f| \le g$ (since $f$ is the a.e. limit), so $|f_{n_{k_j}} - f| \le |f_{n_{k_j}}| + |f| \le 2g$.
:::

<1>5. By the Dominated Convergence Theorem, $\int_E |f_{n_{k_j}} - f| \to 0$.
::: {.proof}
<1>3 and <1>4.
:::

<1>6. This contradicts <1>2, so $\int_E |f_n - f| \to 0$.
::: {.proof}
<1>5 contradicts the lower bound $\varepsilon$ in <1>2.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
