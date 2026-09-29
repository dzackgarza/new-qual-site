---
schema: qual/card@1
id: E-O0XAB
kind: problem
title: Completeness via nested closed sets of vanishing diameter
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.exercise}
Show that a metric space $(X, d)$ is **complete** if and only if for every nested sequence $A_1 \supset A_2 \supset A_3 \supset \cdots$ of non-empty closed subsets of $X$ such that $\lim_{n \to \infty} \operatorname{diam}(A_n) = 0$, the intersection $\bigcap_{n=1}^\infty A_n$ is **non-empty** (and in fact consists of a unique point).
:::

::: {.solution}

::: pf

::: pf-step

If $(X, d)$ is complete, then every nested sequence of nonempty closed sets with diameters tending to $0$ has intersection a single point.
    *Proof:*

::: pf-proof

::: pf-step

Let $A_1 \supset A_2 \supset A_3 \supset \cdots$ be a nested sequence of non-empty closed subsets of $X$ with $\lim_{n \to \infty} \operatorname{diam}(A_n) = 0$.

:::

::: pf-step

For each $n \ge 1$, since $A_n \ne \emptyset$, choose a point $x_n \in A_n$.

:::

::: pf-step

We claim that $\{x_n\}_{n \ge 1}$ is a Cauchy sequence in $(X, d)$:
        - Let $\varepsilon > 0$.
        - Since $\operatorname{diam}(A_n) \to 0$, choose $N$ such that $\operatorname{diam}(A_N) < \varepsilon$.
        - For any $n, m \ge N$, since the sequence of sets is nested ($A_n \subseteq A_N$ and $A_m \subseteq A_N$), we have $x_n \in A_N$ and $x_m \in A_N$.
        - By definition of diameter:
          $$d(x_n, x_m) \le \operatorname{diam}(A_N) < \varepsilon.$$
        - Thus $\{x_n\}$ is a Cauchy sequence.

:::

::: pf-step

Since $(X, d)$ is complete, there exists a limit point $x = \lim_{n \to \infty} x_n \in X$.

:::

::: pf-step

For any fixed $k \ge 1$, the tail sequence $\{x_n\}_{n \ge k}$ is entirely contained in $A_k$ (since $x_n \in A_n \subseteq A_k$ for all $n \ge k$).

:::

::: pf-step

Since $A_k$ is a closed set, the limit of the sequence lies in $A_k$:
        $$x = \lim_{n \to \infty} x_n \in A_k.$$

:::

::: pf-step

Since this holds for all $k \ge 1$, we have:
        $$x \in \bigcap_{n=1}^\infty A_n \ne \emptyset.$$

:::

::: pf-step

**Uniqueness:** If $x, y \in \bigcap_{n=1}^\infty A_n$, then $d(x, y) \le \operatorname{diam}(A_n)$ for all $n \ge 1$. Taking $n \to \infty$ gives $d(x, y) \le 0 \implies x = y$.

:::

:::

:::

::: pf-step

If every nested sequence of nonempty closed sets with diameters tending to $0$ has nonempty intersection, then $(X, d)$ is complete.
    *Proof:*

::: pf-proof

::: pf-step

Let $\{x_n\}_{n \ge 1}$ be any Cauchy sequence in $(X, d)$.

:::

::: pf-step

For each $n \ge 1$, define the tail set $T_n \coloneqq \{ x_k \mid k \ge n \}$.

:::

::: pf-step

Define $A_n \coloneqq \overline{T_n}$ to be the closure of the $n$-th tail.

:::

::: pf-step

Each $A_n$ is a closed nonempty subset of $X$, and $T_{n+1} \subseteq T_n$ gives $A_{n+1} \subseteq A_n$, so the sequence is nested.

:::

::: pf-step

We show that $\operatorname{diam}(A_n) \to 0$:
        - For any set $S \subseteq X$, its closure has the same diameter: $\operatorname{diam}(\overline{S}) = \operatorname{diam}(S)$.
        - Thus $\operatorname{diam}(A_n) = \operatorname{diam}(T_n) = \sup_{j, k \ge n} d(x_j, x_k)$.
        - Since $\{x_n\}$ is Cauchy, for any $\varepsilon > 0$ there exists $N$ such that $d(x_j, x_k) < \varepsilon$ for all $j, k \ge N$, so $\operatorname{diam}(A_N) \le \varepsilon$.
        - Therefore, $\lim_{n \to \infty} \operatorname{diam}(A_n) = 0$.

:::

::: pf-step

By the hypothesis, the intersection is non-empty:
        $$\bigcap_{n=1}^\infty A_n \ne \emptyset.$$

:::

::: pf-step

Let $x \in \bigcap_{n=1}^\infty A_n$.

:::

::: pf-step

We show that $x_n \to x$:
        - For any $\varepsilon > 0$, choose $N$ such that $\operatorname{diam}(A_N) < \varepsilon$.
        - Since $x \in A_N$ and for all $n \ge N$ we have $x_n \in T_N \subseteq A_N$:
          $$d(x_n, x) \le \operatorname{diam}(A_N) < \varepsilon \quad \text{for all } n \ge N.$$
        - Hence $\lim_{n \to \infty} x_n = x \in X$.

:::

::: pf-step

Thus every Cauchy sequence converges in $X$, which proves that $(X, d)$ is complete.

:::

:::

:::

:::

    Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give the two implications.
:::
