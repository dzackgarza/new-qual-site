---
schema: qual/card@1
id: P-JHUFA08ANA
kind: problem
title: 'Iteration of $s\mapsto s^2$ on $[0,1]$: pushforward measures and their weak limit'
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Weak Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Consider the mapping $F \colon [0, 1] \to [0, 1]$ given by $F(s) = s^{2}$.

Let $F^{-j}(A)$ be the inverse image of $j$ iterates of $F$ applied to a measurable subset $A \subset [0, 1]$. That is, if $F = F^{1}$ and $F^{j}$, $j = 2, 3, \ldots$, is defined inductively as $F^{j} = F^{j-1} \circ F$, then $F^{-j}(A) = \{x \st F^{j}x = y \text{ for some } y \in A\}$.

(a) Given $N = 1, 2, \dots$, show that $\mu_{N}(A) = N^{-1}\sum_{j < N} \setmeasure{F^{-j}(A)}$ is a measure which is absolutely continuous with respect to Lebesgue measure. Here $\setmeasure{B}$ denotes the Lebesgue measure of a measurable set.

(b) Show that $\mu_{N}([a, b]) \to 0$ if $0 < a < b \leq 1$.

(c) If $f$ is a continuous function on $[0, 1]$ does
$$
\lim_{N \to \infty} \int_{[0, 1]} f(s) \, d\mu_{N}(s)
$$
tend to a limit? If so, what is the limit?
:::

::: {.solution}

The argument is the card's own: the pushforwards of Lebesgue measure under the iterates, their absolute continuity through the inverse branches, and the Cesàro limit $f(0)$. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $F(s)=s^{2}$ on $[0,1]$, so that $F^{j}(s)=s^{2^{j}}$, and for a measurable $A\subseteq[0,1]$ put $\nu_{j}(A)=\setmeasure{F^{-j}(A)}$, where $\setmeasure{\cdot}$ is Lebesgue measure on $[0,1]$. Then $\mu_{N}=\frac1N\sum_{j=0}^{N-1}\nu_{j}$.

::: pf

::: {.pf-step #measure}
(a) Each $\nu_{j}$ is a measure on the measurable subsets of $[0,1]$, and so is $\mu_{N}$.

::: pf-proof
$\nu_{j}(\varnothing)=\setmeasure{\varnothing}=0$ and $\nu_{j}([0,1])=1$. For pairwise disjoint measurable $A_{n}$, the sets $F^{-j}(A_{n})$ are pairwise disjoint with union $F^{-j}\big(\bigcup_{n}A_{n}\big)$, so by countable additivity of Lebesgue measure
$$
\nu_{j}\Big(\bigcup_{n}A_{n}\Big)=\setmeasure{\bigcup_{n}F^{-j}(A_{n})}=\sum_{n}\setmeasure{F^{-j}(A_{n})}=\sum_{n}\nu_{j}(A_{n}).
$$
So each $\nu_{j}$ is a measure, and a convex combination of measures with weights $1/N$ is a measure.
:::

:::

::: {.pf-step #absolute-continuity}
(a) $\nu_{j}\ll\setmeasure{\cdot}$, hence $\mu_{N}\ll\setmeasure{\cdot}$.

::: pf-proof
Since $t\mapsto t^{2^{j}}$ is a bijection of $[0,1]$ with inverse $g_{j}(t)=t^{2^{-j}}$, one has $F^{-j}(A)=g_{j}(A)$ for every $A\subseteq[0,1]$, and
$$
g_{j}'(t)=2^{-j}t^{2^{-j}-1},
$$
which is integrable on $[0,1]$ because the exponent $2^{-j}-1$ exceeds $-1$. So $g_{j}$ is absolutely continuous on $[0,1]$, and an absolutely continuous function has Luzin's property (N): it maps sets of measure zero to sets of measure zero. Hence $\setmeasure{A}=0$ implies $\nu_{j}(A)=\setmeasure{g_{j}(A)}=0$, which is $\nu_{j}\ll\setmeasure{\cdot}$; a finite positive combination of measures absolutely continuous with respect to $\setmeasure{\cdot}$ is again absolutely continuous, so $\mu_{N}\ll\setmeasure{\cdot}$.
:::

:::

::: {.pf-step #interval}
(b) For $0<a<b\le1$, $\mu_{N}([a,b])=\frac1N\sum_{j=0}^{N-1}\big(b^{2^{-j}}-a^{2^{-j}}\big)\to0$.

::: pf-proof
$F^{j}$ is strictly increasing, so $F^{-j}([a,b])=\{s:s^{2^{j}}\in[a,b]\}=[a^{2^{-j}},b^{2^{-j}}]$, of measure $b^{2^{-j}}-a^{2^{-j}}$, and summing over $j<N$ and dividing by $N$ gives the displayed formula. Since $0<a<b$, one has $a^{2^{-j}}\to a^{0}=1$ and $b^{2^{-j}}\to1$ as $j\to\infty$, so each term $b^{2^{-j}}-a^{2^{-j}}\to0$. The Cesàro mean of a sequence tending to $0$ tends to $0$: given $\varepsilon>0$ fix $J$ with the term below $\varepsilon$ for $j\ge J$, and for $N>J$, since each term $b^{2^{-j}}-a^{2^{-j}}$ lies in $[0,1]$, the average is at most $\frac{J}{N}+\varepsilon$, which tends to $\varepsilon$; as $\varepsilon$ was arbitrary the average tends to $0$.
:::

:::

::: {.pf-step #pushforward}
(c) For bounded measurable $f$, $\displaystyle\int f\,d\nu_{j}=\int_{0}^{1}f(s^{2^{j}})\,ds$ and $\displaystyle\int f\,d\nu_{j}\to f(0)$.

::: pf-proof
$\nu_{j}$ is the pushforward of Lebesgue measure under $F^{j}$, so by the change-of-variables formula for pushforwards, valid for bounded measurable $f$,
$$
\int_{[0,1]}f\,d\nu_{j}=\int_{[0,1]}f\big(F^{j}(s)\big)\,ds=\int_{0}^{1}f(s^{2^{j}})\,ds .
$$
For $s\in[0,1)$ one has $s^{2^{j}}\to0$, so $f(s^{2^{j}})\to f(0)$ by continuity of $f$; the convergence holds for every $s$ except $s=1$, a null set. Since $\abs{f}$ is bounded, the dominated convergence theorem gives $\int_{0}^{1}f(s^{2^{j}})\,ds\to f(0)\cdot1=f(0)$.
:::

:::

::: {.pf-step #limit}
(c) The limit exists and equals $f(0)$: $\displaystyle\lim_{N\to\infty}\int f\,d\mu_{N}=f(0)$.

::: pf-proof
By linearity and step [](#pushforward){.pf-ref},
$$
\int f\,d\mu_{N}=\frac1N\sum_{j=0}^{N-1}\int f\,d\nu_{j}=\frac1N\sum_{j=0}^{N-1}a_{j},\qquad a_{j}=\int_{0}^{1}f(s^{2^{j}})\,ds,
$$
and $a_{j}\to f(0)$, so the Cesàro means converge to the same limit: given $\varepsilon>0$ choose $J$ with $\abs{a_{j}-f(0)}<\varepsilon$ for $j\ge J$; then for $N>J$,
$$
\abs{\frac1N\sum_{j<N}a_{j}-f(0)}\le\frac1N\sum_{j<J}\abs{a_{j}-f(0)}+\varepsilon,
$$
and the first term tends to $0$ as $N\to\infty$. Hence $\int f\,d\mu_{N}\to f(0)$ for every continuous $f$, so the limit asked for exists and equals the value of $f$ at $0$.
:::

:::

:::
:::
