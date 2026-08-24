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
---

::: problem
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
> **AI-Generated Solution**

<1>1. (Countable subadditivity.) $m_*(\cup_{j\ge 1} E_j) \le \sum_{j\ge 1} m_*(E_j)$.
    Proof: if $\sum_j m_*(E_j) = \infty$ there is nothing to prove. Otherwise, fix $\eps > 0$. By definition of $m_*$ as an infimum over countable coverings by boxes, for each $j$ choose a cover $\{Q_{j,k}\}_k$ of $E_j$ by boxes with
    \[
    \sum_k |Q_{j,k}| \le m_*(E_j) + \frac{\eps}{2^j}.
    \]
    Then $\{Q_{j,k}\}_{j,k}$ is a countable cover of $\cup_j E_j$, so
    \[
    m_*\Big(\bigcup_j E_j\Big) \le \sum_{j,k} |Q_{j,k}| \le \sum_j m_*(E_j) + \eps .
    \]
    Since $\eps > 0$ is arbitrary, the claim follows.
<1>2. (Outer regularity.) For every $E \subseteq \RR^n$ and $\eps > 0$ there is an open $G \supseteq E$ with $m_*(E) \le m_*(G) \le m_*(E) + \eps$.
    Proof: by definition of $m_*$ there is a countable cover $\{Q_k\}_k$ of $E$ by boxes with $\sum_k |Q_k| \le m_*(E) + \eps$. Enlarge each box to an open box $U_k \supseteq Q_k$ with $|U_k| \le |Q_k| + \eps/2^k$ and set $G = \cup_k U_k$, which is open. Then $E \subseteq G$, so $m_*(E) \le m_*(G)$ (monotonicity), and by <1>1
    \[
    m_*(G) \le \sum_k |U_k| \le \sum_k |Q_k| + \eps \le m_*(E) + 2\eps .
    \]
    Replacing $\eps$ by $\eps/2$ throughout gives the stated bound.
<1>3. Q.E.D.
:::
