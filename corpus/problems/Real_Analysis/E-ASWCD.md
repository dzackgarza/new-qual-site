---
schema: qual/card@1
id: E-ASWCD
kind: exercise
title: Continuity of outer measure from above and below
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- Show that continuity of measure from above/below holds for outer measures.
:::

::: {.solution}
**Goal:** Show that the continuity properties of a measure hold for an outer measure $\mu^*$: continuity from below always, and continuity from above provided the first set has finite outer measure.

<1>1. Continuity from below: if $E_1 \subseteq E_2 \subseteq \cdots$, then $\mu^*\!\left(\bigcup_n E_n\right) = \lim_n \mu^*(E_n)$.
<2>1. The limit exists since $\{\mu^*(E_n)\}$ is monotone increasing.
::: {.proof}
$\mu^*$ is monotone and $E_n \subseteq E_{n+1}$, so $\mu^*(E_n) \leq \mu^*(E_{n+1})$; hence $\lim_n \mu^*(E_n) = \sup_n \mu^*(E_n) \in [0, \infty]$.
:::
<2>2. $\mu^*\!\left(\bigcup_n E_n\right) \leq \sup_n \mu^*(E_n)$.
::: {.proof}
set $E_0 := \emptyset$; countable subadditivity gives $\mu^*(\bigcup_n E_n) \leq \sum_n \mu^*(E_n \setminus E_{n-1})$; but each $E_n \setminus E_{n-1} \subseteq E_n$, so $\sum_{n=1}^N \mu^*(E_n \setminus E_{n-1}) \leq \sum_{n=1}^N \big(\mu^*(E_n) - \mu^*(E_{n-1})\big) = \mu^*(E_N)$, using monotonicity and finiteness of each term (if all $\mu^*(E_n) = \infty$ there is nothing to prove).
:::
Taking $N \to \infty$: $\sum_n \mu^*(E_n \setminus E_{n-1}) \leq \sup_n \mu^*(E_n)$.
<2>3. $\mu^*\!\left(\bigcup_n E_n\right) \geq \sup_n \mu^*(E_n)$.
::: {.proof}
$E_n \subseteq \bigcup_n E_n$ and $\mu^*$ is monotone, so $\mu^*(E_n) \leq \mu^*(\bigcup_n E_n)$ for every $n$.
:::
<2>4. Q.E.D.
::: {.proof}
<2>2 and <2>3 sandwich the two sides.
:::

<1>2. Continuity from above: if $E_1 \supseteq E_2 \supseteq \cdots$ with $\mu^*(E_1) < \infty$, then $\mu^*\!\left(\bigcap_n E_n\right) = \lim_n \mu^*(E_n)$.
<2>1. The sequence $\mu^*(E_n)$ is decreasing and bounded below by $\mu^*(\bigcap_n E_n)$, so it converges to some $L \geq \mu^*(\bigcap_n E_n)$.
::: {.proof}
monotonicity of $\mu^*$ and $E_{n+1} \subseteq E_n \supseteq \bigcap_n E_n$.
:::
<2>2. $L \leq \mu^*\!\left(\bigcap_n E_n\right)$.
::: {.proof}
apply continuity from below (<1>1) to the increasing sequence $F_n := E_1 \setminus E_n$: $\mu^*(\bigcup_n F_n) = \lim_n \mu^*(F_n)$.
:::
Since $\bigcup_n F_n = E_1 \setminus \bigcap_n E_n$ and $\mu^*(E_1) < \infty$, subadditivity gives $\mu^*(E_1) \leq \mu^*(E_1 \setminus \bigcap_n E_n) + \mu^*(\bigcap_n E_n)$ and likewise $\mu^*(F_n) = \mu^*(E_1) - \mu^*(E_n)$ (both sides finite).
Hence $\mu^*(E_1) - \mu^*(\bigcap_n E_n) \leq \lim_n \big(\mu^*(E_1) - \mu^*(E_n)\big)$, i.e. $L = \lim_n \mu^*(E_n) \leq \mu^*(\bigcap_n E_n)$.
<2>3. Q.E.D.
::: {.proof}
<2>1 and <2>2 together give equality.
:::

<1>3. The finiteness assumption in <1>2 is necessary.
::: {.proof}
e.g. $\mu^* =$ counting measure on $\mathbb{R}$ and $E_n = [n, \infty)$: each $\mu^*(E_n) = \infty$, but $\mu^*(\bigcap_n E_n) = \mu^*(\emptyset) = 0$, so the equality fails.
:::
Continuity from above for measures/outer measures requires $\mu^*(E_1) < \infty$.
:::
