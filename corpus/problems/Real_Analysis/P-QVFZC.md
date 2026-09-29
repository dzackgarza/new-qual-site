---
schema: qual/card@1
id: P-QVFZC
kind: problem
title: Countable subadditivity and outer regularity of Lebesgue outer measure
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $m_*(E)$ denote the Lebesgue outer measure of a set \( E \subseteq \RR^n \).

a. Prove using the definition of Lebesgue outer measure that
\[
m \qty{ \Union_{j=1}^{\infty } E_j  } \leq \sum_{j=1}^{\infty } m_*(E_j) 
.\]

b. Prove that for any \( E \subseteq \RR^n \) and any \( \epsilon> 0 \) there exists an open set $G$ with $E \subseteq G$ and
\[
m_*(E) \leq m_*(G) \leq m_*(E) + \epsilon
.\]
:::

::: {.solution}
Recall $m_*(E) = \inf\sum_k |Q_k|$, the infimum over countable covers of $E$ by closed boxes $Q_k$.

::: pf

::: pf-step

$m_*(\bigcup_{j\ge 1} E_j) \le \sum_{j\ge 1} m_*(E_j)$.

::: pf-proof

If $\sum_j m_*(E_j) = \infty$ there is nothing to prove. Otherwise fix $\eps > 0$ and, for each $j$, choose a cover $(Q_{j,k})_k$ of $E_j$ by boxes with $\sum_k |Q_{j,k}| \le m_*(E_j) + \eps 2^{-j}$. Then $(Q_{j,k})_{j,k}$ is a countable cover of $\bigcup_j E_j$, so $m_*(\bigcup_j E_j) \le \sum_{j,k} |Q_{j,k}| \le \sum_j m_*(E_j) + \eps$.

:::

:::

::: pf-step

For every $E \subseteq \RR^n$ and $\eps > 0$ there is an open $G \supseteq E$ with $m_*(E) \le m_*(G) \le m_*(E) + \eps$.

::: pf-proof

If $m_*(E) = \infty$ take $G = \RR^n$. Otherwise choose a cover $(Q_k)$ of $E$ by boxes with $\sum_k |Q_k| \le m_*(E) + \eps/2$, and open boxes $U_k \supseteq Q_k$ with $|U_k| \le |Q_k| + \eps 2^{-k-1}$. Then $G = \bigcup_k U_k$ is open and contains $E$, so $m_*(E) \le m_*(G)$ by monotonicity. The closures $\overline{U_k}$ cover $G$, so $m_*(G) \le \sum_k |U_k| \le m_*(E) + \eps$.

:::

:::

:::

:::
