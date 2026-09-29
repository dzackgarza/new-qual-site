---
schema: qual/card@1
id: P-AXFG7
kind: problem
title: Every $E\subseteq\RR$ has a Borel hull of equal outer measure; Carathéodory-measurable
  sets are Borel minus null
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 2 of the official UGA Spring 2020 Real Analysis qualifying examination DOCX.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Reviewed both finite- and infinite-outer-measure cases for the Borel hull and the Caratheodory-measurable-set decomposition; the proof correctly handles the infinite case by bounded pieces.
---

::: {.problem}
Let $m_*$ denote the Lebesgue outer measure on $\mathbb{R}$.

(a) Prove that for every $E \subseteq \mathbb{R}$, there exists a Borel set $B \subseteq \mathbb{R}$ containing $E$ ($E \subseteq B$) such that
$$
m_*(B) = m_*(E).
$$

(b) Prove that if $E \subseteq \mathbb{R}$ satisfies Carathéodory's measurability condition:
$$
m_*(A) = m_*(A \cap E) + m_*(A \cap E^c) \quad \text{for every } A \subseteq \mathbb{R},
$$
then there exists a Borel set $B \subseteq \mathbb{R}$ such that $E = B \setminus N$ with $m_*(N) = 0$.
Be sure to address the case when $m_*(E) = \infty$.
:::

::: {.hint}
For (a), intersect open covers of $E$ whose total lengths decrease to $m_*(E)$; the intersection is a $G_\delta$ set $B\supseteq E$ with $m_*(B)=m_*(E)$. For (b), apply Carathéodory's condition with test set $A=B$ to get $m_*(B\setminus E)=0$ when $m_*(E)<\infty$, and treat $E\cap[n,n+1)$ separately when $m_*(E)=\infty$.
:::

::: {.solution}

::: pf

::: {.pf-step #borel-hull-finite-case}
Part (a): Case $m_*(E) < \infty$.

::: pf-proof

::: pf-step
By definition of outer measure on $\mathbb{R}$, for any $E \subseteq \mathbb{R}$:
$$m_*(E) = \inf \left\{ \sum_{j=1}^\infty |I_j| \;\middle|\; E \subseteq \bigcup_{j=1}^\infty I_j, \, I_j \text{ open intervals} \right\}.$$

:::

::: pf-step
For each integer $k \ge 1$, by the definition of the infimum, there exists a countable collection of open intervals $\{I_{j, k}\}_{j=1}^\infty$ covering $E$ such that
$$\sum_{j=1}^\infty |I_{j, k}| < m_*(E) + \frac{1}{k}.$$

:::

::: pf-step
Define the open set $U_k = \bigcup_{j=1}^\infty I_{j, k}$.

:::

::: pf-step
Then $E \subseteq U_k$, and by countable subadditivity, $m_*(U_k) \le \sum_{j=1}^\infty |I_{j, k}| < m_*(E) + \frac{1}{k}$.

:::

::: pf-step
Define the $G_\delta$ set $B = \bigcap_{k=1}^\infty U_k$.

:::

::: pf-step
Since $B$ is a countable intersection of open sets, $B$ is a Borel set.

:::

::: pf-step
Since $E \subseteq U_k$ for every $k$, $E \subseteq B$.

:::

::: pf-step
By monotonicity of outer measure:
$$m_*(E) \le m_*(B) \le m_*(U_k) < m_*(E) + \frac{1}{k} \quad \text{for all } k \ge 1.$$

:::

::: pf-step
Taking $k \to \infty$ gives $m_*(B) = m_*(E)$.

:::

:::

:::

::: pf-step
Part (a): Case $m_*(E) = \infty$.

::: pf-proof

::: pf-step
Partition $\mathbb{R}$ into bounded, pairwise disjoint intervals $J_n = [n, n+1)$ for $n \in \mathbb{Z}$.

:::

::: pf-step
Define $E_n = E \cap J_n$ for each $n \in \mathbb{Z}$.

:::

::: pf-step
Since $E_n \subseteq J_n$, $m_*(E_n) \le m_*(J_n) = 1 < \infty$.

:::

::: pf-step
By step [](#borel-hull-finite-case){.pf-ref}, for each $n \in \mathbb{Z}$, there exists a Borel set $B_n \supseteq E_n$ such that $m_*(B_n) = m_*(E_n)$.

:::

::: pf-step
Define $B = \bigcup_{n \in \mathbb{Z}} B_n$.

:::

::: pf-step
As a countable union of Borel sets, $B$ is Borel, and $E = \bigcup_{n \in \mathbb{Z}} E_n \subseteq \bigcup_{n \in \mathbb{Z}} B_n = B$.

:::

::: pf-step
Since $E \subseteq B$, $m_*(E) \le m_*(B)$.

:::

::: pf-step
Since $m_*(E) = \infty$, $m_*(B) = \infty = m_*(E)$.

:::

:::

:::

::: {.pf-step #measurable-decomposition-finite-case}
Part (b): Case $m_*(E) < \infty$.

::: pf-proof

::: pf-step
By step [](#borel-hull-finite-case){.pf-ref}, choose a Borel set $B \supseteq E$ such that $m_*(B) = m_*(E) < \infty$.

:::

::: pf-step
Apply Carathéodory's condition to the test set $A = B$:
$$m_*(B) = m_*(B \cap E) + m_*(B \cap E^c).$$

:::

::: pf-step
Since $E \subseteq B$, $B \cap E = E$ and $B \cap E^c = B \setminus E$.

:::

::: pf-step
Thus:
$$m_*(B) = m_*(E) + m_*(B \setminus E).$$

:::

::: pf-step
Since $m_*(B) = m_*(E) < \infty$, subtract $m_*(E)$ from both sides:
$$m_*(B \setminus E) = m_*(B) - m_*(E) = 0.$$

:::

::: pf-step
Set $N = B \setminus E$. Then $m_*(N) = 0$ and $E = B \setminus N$.

:::

:::

:::

::: pf-step
Part (b): Case $m_*(E) = \infty$.

::: pf-proof

::: pf-step
Again partition $\mathbb{R}$ via $J_n = [n, n+1)$ for $n \in \mathbb{Z}$, and set $E_n = E \cap J_n$.

:::

::: pf-step
Since $E$ is Carathéodory-measurable and each interval $J_n$ is measurable, each $E_n = E \cap J_n$ is Carathéodory-measurable with $m_*(E_n) \le 1 < \infty$.

:::

::: pf-step
By step [](#measurable-decomposition-finite-case){.pf-ref}, for each $n \in \mathbb{Z}$, there exists a Borel set $B_n \supseteq E_n$ such that $N_n = B_n \setminus E_n$ has $m_*(N_n) = 0$.

:::

::: pf-step
Define $B = \bigcup_{n \in \mathbb{Z}} B_n$. Then $B$ is a Borel set containing $E$.

:::

::: pf-step
Define $N = B \setminus E = \left( \bigcup_{n \in \mathbb{Z}} B_n \right) \setminus \left( \bigcup_{n \in \mathbb{Z}} E_n \right) \subseteq \bigcup_{n \in \mathbb{Z}} (B_n \setminus E_n) = \bigcup_{n \in \mathbb{Z}} N_n$.

:::

::: pf-step
By countable subadditivity of outer measure:
$$m_*(N) \le \sum_{n \in \mathbb{Z}} m_*(N_n) = \sum_{n \in \mathbb{Z}} 0 = 0.$$

:::

::: pf-step
Thus $m_*(N) = 0$ and $E = B \setminus N$.

:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
Every set $E$ is contained in a Borel set of equal outer measure, and every Carathéodory-measurable set is of the form $E = B \setminus N$ where $B$ is Borel and $m_*(N) = 0$.
:::

:::

:::

:::
