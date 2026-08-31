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
---

Let $m_*$ denote the Lebesgue outer measure on \( \RR \).

::: problem
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

::: solution
**Goal:** Construct a Borel $G_\delta$ hull $B \supseteq E$ with $m(B) = m_*(E)$ in (a), and apply Carathéodory's criterion with test set $A = B$ in (b) to show $E$ differs from $B$ by a null set.

<1>1. Part (a): Case $m_*(E) < \infty$.
::: {.proof}
    <2>1. By definition of outer measure on $\mathbb{R}$, for any $E \subseteq \mathbb{R}$:
    $$m_*(E) = \inf \left\{ \sum_{j=1}^\infty |I_j| \;\middle|\; E \subseteq \bigcup_{j=1}^\infty I_j, \, I_j \text{ open intervals} \right\}.$$
    <2>2. For each integer $k \ge 1$, by the definition of the infimum, there exists a countable collection of open intervals $\{I_{j, k}\}_{j=1}^\infty$ covering $E$ such that
    $$\sum_{j=1}^\infty |I_{j, k}| < m_*(E) + \frac{1}{k}.$$
    <2>3. Define the open set $U_k = \bigcup_{j=1}^\infty I_{j, k}$.
    <2>4. Then $E \subseteq U_k$, and by countable subadditivity, $m_*(U_k) \le \sum_{j=1}^\infty |I_{j, k}| < m_*(E) + \frac{1}{k}$.
    <2>5. Define the $G_\delta$ set $B = \bigcap_{k=1}^\infty U_k$.
    <2>6. Since $B$ is a countable intersection of open sets, $B$ is a Borel set.
    <2>7. Since $E \subseteq U_k$ for every $k$, $E \subseteq B$.
    <2>8. By monotonicity of outer measure:
    $$m_*(E) \le m_*(B) \le m_*(U_k) < m_*(E) + \frac{1}{k} \quad \text{for all } k \ge 1.$$
    <2>9. Taking $k \to \infty$ gives $m_*(B) = m_*(E)$.

:::

<1>2. Part (a): Case $m_*(E) = \infty$.
::: {.proof}
    <2>1. Partition $\mathbb{R}$ into bounded, pairwise disjoint intervals $J_n = [n, n+1)$ for $n \in \mathbb{Z}$.
    <2>2. Define $E_n = E \cap J_n$ for each $n \in \mathbb{Z}$.
    <2>3. Since $E_n \subseteq J_n$, $m_*(E_n) \le m_*(J_n) = 1 < \infty$.
    <2>4. By <1>1, for each $n \in \mathbb{Z}$, there exists a Borel set $B_n \supseteq E_n$ such that $m_*(B_n) = m_*(E_n)$.
    <2>5. Define $B = \bigcup_{n \in \mathbb{Z}} B_n$.
    <2>6. As a countable union of Borel sets, $B$ is Borel, and $E = \bigcup_{n \in \mathbb{Z}} E_n \subseteq \bigcup_{n \in \mathbb{Z}} B_n = B$.
    <2>7. Since $E \subseteq B$, $m_*(E) \le m_*(B)$.
    <2>8. Since $m_*(E) = \infty$, $m_*(B) = \infty = m_*(E)$.

:::

<1>3. Part (b): Case $m_*(E) < \infty$.
::: {.proof}
    <2>1. By <1>1, choose a Borel set $B \supseteq E$ such that $m_*(B) = m_*(E) < \infty$.
    <2>2. Apply Carathéodory's condition to the test set $A = B$:
    $$m_*(B) = m_*(B \cap E) + m_*(B \cap E^c).$$
    <2>3. Since $E \subseteq B$, $B \cap E = E$ and $B \cap E^c = B \setminus E$.
    <2>4. Thus:
    $$m_*(B) = m_*(E) + m_*(B \setminus E).$$
    <2>5. Since $m_*(B) = m_*(E) < \infty$, subtract $m_*(E)$ from both sides:
    $$m_*(B \setminus E) = m_*(B) - m_*(E) = 0.$$
    <2>6. Set $N = B \setminus E$. Then $m_*(N) = 0$ and $E = B \setminus N$.

:::

<1>4. Part (b): Case $m_*(E) = \infty$.
::: {.proof}
    <2>1. Again partition $\mathbb{R}$ via $J_n = [n, n+1)$ for $n \in \mathbb{Z}$, and set $E_n = E \cap J_n$.
    <2>2. Since $E$ is Carathéodory-measurable and each interval $J_n$ is measurable, each $E_n = E \cap J_n$ is Carathéodory-measurable with $m_*(E_n) \le 1 < \infty$.
    <2>3. By <1>3, for each $n \in \mathbb{Z}$, there exists a Borel set $B_n \supseteq E_n$ such that $N_n = B_n \setminus E_n$ has $m_*(N_n) = 0$.
    <2>4. Define $B = \bigcup_{n \in \mathbb{Z}} B_n$. Then $B$ is a Borel set containing $E$.
    <2>5. Define $N = B \setminus E = \left( \bigcup_{n \in \mathbb{Z}} B_n \right) \setminus \left( \bigcup_{n \in \mathbb{Z}} E_n \right) \subseteq \bigcup_{n \in \mathbb{Z}} (B_n \setminus E_n) = \bigcup_{n \in \mathbb{Z}} N_n$.
    <2>6. By countable subadditivity of outer measure:
    $$m_*(N) \le \sum_{n \in \mathbb{Z}} m_*(N_n) = \sum_{n \in \mathbb{Z}} 0 = 0.$$
    <2>7. Thus $m_*(N) = 0$ and $E = B \setminus N$.

:::

<1>5. Conclusion:
::: {.proof}
    Every set $E$ is contained in a Borel set of equal outer measure, and every Carathéodory-measurable set is of the form $E = B \setminus N$ where $B$ is Borel and $m_*(N) = 0$.
:::
:::
