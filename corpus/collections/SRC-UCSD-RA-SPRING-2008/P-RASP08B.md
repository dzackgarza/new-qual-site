---
schema: qual/card@1
id: P-RASP08B
kind: problem
title: "Convergence of level sets under monotone a.e. convergence"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Repaired and restructured. The card was a stack of label-steps with no proofs and twenty-one
    nested one-sentence claims carrying the mathematics with nothing behind them. It is now four
    proved steps: the null-set reduction with the countable union, part (a) by continuity from
    below along the increasing sets with both inclusions verified through f = sup f_n, part (b)
    by continuity from above (which is where mu(X) < infinity is used) with the squeeze between
    {f < a} and {f <= a}, and the counterexample, which is the card's own (f_n = -1/n on [0,1])
    and now says explicitly that the whole discrepancy is carried by mu{f = 0}. Answers
    unchanged. Not claimed: a retained solution set; the collection's provenance is the
    examination paper only.
---

::: {.problem}
Let $(X, \mu)$ be a measure space and $f, f_n : X \to \RR$ measurable functions such that $f_1 \leq f_2 \leq \cdots \leq f_n \leq \cdots$ a.e. and $\lim_{n \to \infty} f_n = f$ a.e.

(a) For every $a \in \RR$, show that $\lim_{n \to \infty} \mu(\{x : f_n(x) > a\})$ exists and
$$
\lim_{n \to \infty} \mu(\{x : f_n(x) > a\}) = \mu(\{x : f(x) > a\}).
$$

(b) Assume that $\mu(X) < \infty$.
Show that $\lim_{n \to \infty} \mu(\{x : f_n(x) < a\})$ exists for every $a \in \RR$ and
$$
\mu(\{x : f(x) < a\}) \leq \lim_{n \to \infty} \mu(\{x : f_n(x) < a\}) \leq \mu(\{x : f(x) < a\}) + \mu(\{x : f(x) = a\}).
$$
Give an example where
$$
\mu(\{x : f(x) < a\}) < \lim_{n \to \infty} \mu(\{x : f_n(x) < a\})
$$
for some $a \in \RR$.
:::

::: {.solution}
Throughout $(X,\mu)$ is a measure space, $f_{n}, f\colon X \to \RR$ are measurable with $f_{1} \le f_{2} \le \cdots$ almost everywhere and $f_{n} \to f$ almost everywhere, and $\theset{f > a}$ abbreviates $\theset{x \in X \mid f(x) > a}$. Reductions to null sets use the fact that a countable union of null sets is null. The collection's `provenance` is the Spring 2008 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #null}
There is a null set $N$ off which $f_{1} \le f_{2} \le \cdots$ and $f_{n} \to f$ pointwise.

::: pf-proof
Let $N_{k} \coloneqq \theset{f_{k} > f_{k+1}}$, a null set by the almost-everywhere monotonicity, and $N_{0}$ a null set off which the convergence holds; then $N \coloneqq N_{0} \cup \bigcup_{k}N_{k}$ is a countable union of null sets, hence null, and off it both properties hold at every point. Off $N$ the sequence $(f_{n}(x))$ is increasing with limit $f(x)$, so $f(x) = \sup_{n}f_{n}(x)$ there.

:::

:::

::: {.pf-step #a}
(a) $\mu\theset{f_{n} > a} \to \mu\theset{f > a}$ for every $a \in \RR$.

::: pf-proof
Put $E_{n} \coloneqq \theset{f_{n} > a} \cap (X \setminus N)$ and $E \coloneqq \theset{f > a} \cap (X\setminus N)$; these differ from the sets in the statement by $N$, hence have the same measures. If $x \in E_{n}$ then $f(x) \ge f_{n}(x) > a$, so $E_{n} \subseteq E$; if $x \in E$ then $f(x) > a$, and since $f(x) = \sup_{n}f_{n}(x)$ some $n$ has $f_{n}(x) > a$, so $x \in E_{n}$. Hence $E_{n} \subseteq E_{n+1}$ and $\bigcup_{n}E_{n} = E$, and continuity of $\mu$ from below along an increasing sequence gives $\mu(E_{n}) \to \mu(E)$.

:::

:::

::: {.pf-step #b}
(b) If $\mu(X) < \infty$ then the limit of $\mu\theset{f_{n} < a}$ exists and $\mu\theset{f < a} \le \lim_{n}\mu\theset{f_{n} < a} \le \mu\theset{f < a} + \mu\theset{f = a}$.

::: pf-proof
Now $A_{n} \coloneqq \theset{f_{n} < a}\cap(X\setminus N)$ is decreasing, because $f_{n} \le f_{n+1}$ gives $\theset{f_{n+1} < a} \subseteq \theset{f_{n} < a}$. Its intersection is squeezed: if $f(x) < a$ then $f_{n}(x) \le f(x) < a$ for every $n$, so $\theset{f < a}\setminus N \subseteq \bigcap_{n}A_{n}$, while every $x \in \bigcap_{n}A_{n}$ has $f_{n}(x) < a$ for all $n$ and hence $f(x) = \sup_{n}f_{n}(x) \le a$. Thus $\theset{f < a}\setminus N \subseteq \bigcap_{n}A_{n} \subseteq \theset{f \le a}\setminus N$. Since $\mu(A_{1}) \le \mu(X) < \infty$, continuity from above gives $\mu(A_{n}) \to \mu(\bigcap_{n}A_{n})$, and monotonicity of $\mu$ gives the chain $\mu\theset{f < a} \le \mu(\bigcap_{n}A_{n}) \le \mu\theset{f \le a} = \mu\theset{f < a} + \mu\theset{f = a}$, the last equality because $\theset{f \le a}$ is the disjoint union of $\theset{f < a}$ and $\theset{f = a}$.

:::

:::

::: pf-step
The bound in (b) is attained: on $X = [0,1]$ with Lebesgue measure, $f_{n} \equiv -1/n$ and $f \equiv 0$ give $0 = m\theset{f < 0} < \lim_{n}m\theset{f_{n} < 0} = 1$.

::: pf-proof
Take $a = 0$. The constant functions satisfy $f_{1} \le f_{2} \le \cdots$ everywhere and $f_{n} \to 0 = f$ pointwise, and $m([0,1]) = 1 < \infty$. For every $n$ the set $\theset{f_{n} < 0} = [0,1]$, so the limit of the measures is $1$; while $\theset{f < 0} = \varnothing$, of measure $0$. This is the strict inequality the exercise asks for, and it sits exactly at the gap allowed by step [](#b){.pf-ref}, since $\mu\theset{f = 0} = 1$ carries the difference.

:::

:::

:::
:::
