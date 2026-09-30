---
schema: qual/card@1
id: E-F8UOA
kind: problem
title: Continuity sets are $G_\delta$; no function is continuous exactly on a countable dense set
classification:
  areas:
  - topology
  topics:
  - Baire Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Prove the following.

Theorem.
If $D$ is a countable dense subset of $\mathbb{R}$, there is no function $f: \mathbb{R} \to \mathbb{R}$ that is continuous precisely at the points of $D$.

(a) Show that if $f: \mathbb{R} \to \mathbb{R}$, then the set $C$ of points at which $f$ is continuous is a $G_\delta$ set in $\mathbb{R}$.
[Hint: Let $U_n$ be the union of all open sets $U$ of $\mathbb{R}$ such that $\operatorname{diam} f(U) < 1/n$. Show that $C = \bigcap U_n$.]

(b) Show that $D$ is not a $G_\delta$ set in $\mathbb{R}$.
[Hint: Suppose $D = \bigcap W_n$, where $W_n$ is open in $\mathbb{R}$. For $d \in D$, set $V_d = \mathbb{R} - \theset{d}$. Show $W_n$ and $V_d$ are dense in $\mathbb{R}$.]
:::

::: {.solution}
For $n \in \ZZ_+$ let $U_n$ be the union of all open sets $U \subseteq \RR$ with $\operatorname{diam} f(U) < 1/n$. Each $U_n$ is open, as a union of open sets.

::: pf

::: {.pf-step #s1}

(a) $C = \bigcap_{n=1}^\infty U_n$, so $C$ is a $G_\delta$ set.

::: pf-proof

::: {.pf-step #s1-1}

$C \subseteq \bigcap_n U_n$.

::: pf-proof

Let $x_0 \in C$ and $n \in \ZZ_+$. By continuity at $x_0$, there is an open interval $U \ni x_0$ with $f(U) \subseteq (f(x_0) - \frac{1}{3n}, f(x_0) + \frac{1}{3n})$. Then $\operatorname{diam} f(U) \le \frac{2}{3n} < \frac1n$, so $x_0 \in U \subseteq U_n$.

:::

:::

::: {.pf-step #s1-2}

$\bigcap_n U_n \subseteq C$.

::: pf-proof

Let $x_0 \in \bigcap_n U_n$ and $\varepsilon > 0$; choose $n$ with $1/n < \varepsilon$. Since $x_0 \in U_n$, some open $U \ni x_0$ has $\operatorname{diam} f(U) < 1/n$. For $y \in U$, $\abs{f(y) - f(x_0)} \le \operatorname{diam} f(U) < \varepsilon$. So $f$ is continuous at $x_0$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give $C = \bigcap_n U_n$, a countable intersection of open sets.

:::

:::

:::

::: {.pf-step #s2}

(b) $D$ is not a $G_\delta$ set.

::: pf-proof

Write $D = \{d_k : k \in \ZZ_+\}$ and suppose $D = \bigcap_n W_n$ with each $W_n$ open. Each $W_n$ contains the dense set $D$, so it is dense. Each $V_k = \RR \setminus \{d_k\}$ is open, and it is dense because $\RR$ has no isolated points. By the Baire category theorem for the complete metric space $\RR$, the intersection of the countable family of dense open sets $W_n$ and $V_k$ is dense, hence nonempty. But
$$\bigcap_n W_n \cap \bigcap_k V_k = D \cap (\RR \setminus D) = \varnothing.$$

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a) and step [](#s2){.pf-ref} proves part (b). If $f$ were continuous precisely at the points of $D$, then $D = C$ would be a $G_\delta$ set by step [](#s1){.pf-ref}, contradicting step [](#s2){.pf-ref}.

:::

:::

:::
