---
schema: qual/card@1
id: P-KH5ZV
kind: problem
title: Absolute continuity of $\int_E\abs{f}$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - Continuity of Measure
  - L¹
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card was a label-step shed with an empty proof over thirteen
    nested one-sentence claims and a stray '**Goal:**' paragraph before the proof. It is now
    three proved steps: the truncations are measurable, bounded by N, increasing and convergent,
    with the monotonicity checked in the two cases; monotone convergence giving the tail
    estimate and hence N; and the estimate itself, with delta = epsilon/(2N) exhibited and the
    split of the integral written out. The proof's content is unchanged — the same truncate-
    then-MCT strategy the card's goal paragraph described. Not claimed: a retained solution set;
    the collection's provenance is the examination paper only.
---

::: {.problem}
Let $f \in L^1(\RR)$. Prove that for every $\varepsilon > 0$, there exists $\delta > 0$ such that for every Lebesgue measurable set $E \subseteq \RR$ with $m(E) < \delta$,
$$
\int_E \abs{f(x)} \, dx < \varepsilon.
$$
:::

::: {.solution}
Throughout $f \in L^{1}(\RR)$, $m$ is Lebesgue measure, and for $N \ge 1$ the truncation is $f_{N} \coloneqq \min(\abs f, N)$, that is $f_{N}(x) = \abs{f(x)}$ where $\abs{f(x)} \le N$ and $f_{N}(x) = N$ where $\abs{f(x)} > N$. The collection's `provenance` is the Fall 2014 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #truncation}
Each $f_{N}$ is measurable, satisfies $0 \le f_{N} \le N$, and $f_{N}(x) \to \abs{f(x)}$ increasingly at every $x$.

::: pf-proof
$\abs f$ is measurable and $N$ is constant, so $f_{N} = \min(\abs f, N)$ is measurable; the bounds $0 \le f_{N} \le N$ are immediate from the definition. Monotonicity: if $\abs{f(x)} \le N$ then $f_{N}(x) = \abs{f(x)}$ and $f_{N+1}(x) = \min(\abs{f(x)}, N+1) = \abs{f(x)}$; if $\abs{f(x)} > N$ then $f_{N}(x) = N \le \min(\abs{f(x)}, N+1) = f_{N+1}(x)$. Convergence: for fixed $x$, once $N \ge \abs{f(x)}$ one has $f_{N}(x) = \abs{f(x)}$.

:::

:::

::: {.pf-step #mct}
$\int f_{N} \to \int\abs f$; consequently there is $N$ with $\int\bigl(\abs f - f_{N}\bigr) < \varepsilon/2$.

::: pf-proof
The sequence $(f_{N})$ increases pointwise to the integrable function $\abs f$, so the monotone convergence theorem gives $\int f_{N} \to \int\abs f$, the integrals being finite. Hence $\int(\abs f - f_{N}) = \int\abs f - \int f_{N} \to 0$; being a sequence of nonnegative numbers tending to $0$, it is eventually below $\varepsilon/2$.

:::

:::

::: pf-step
For every $\varepsilon > 0$ there is $\delta > 0$ such that $m(E) < \delta$ implies $\int_{E}\abs f < \varepsilon$.

::: pf-proof
Let $\varepsilon > 0$ and choose $N$ as in step [](#mct){.pf-ref}; put $\delta \coloneqq \varepsilon/(2N)$, which is positive. For a measurable $E$ with $m(E) < \delta$, split the integral: $\int_{E}\abs f = \int_{E}(\abs f - f_{N}) + \int_{E}f_{N} \le \int_{\RR}(\abs f - f_{N}) + N\\,m(E) < \frac{\varepsilon}{2} + N\cdot\frac{\varepsilon}{2N} = \varepsilon$, using $f_{N} \le N$ on $E$ and the choice of $N$. Since $f_{N}$ does not depend on $E$, the constant $\delta$ works for every such set.

:::

:::

:::
:::

