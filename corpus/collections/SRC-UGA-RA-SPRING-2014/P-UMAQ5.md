---
schema: qual/card@1
id: P-UMAQ5
kind: problem
title: A continuous $f\in L^1(\RR)$ need not tend to $0$ at infinity, but a uniformly
  continuous one must
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - L¹
  - Counterexamples
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Thirteen steps asserted their claim with no
    justification and the card is now four steps each deriving its claim. Part (a): one step constructs the
    tents $f_n(x) = \max\{0, 1 - n^2\abs{x-n}\}$ and shows $f = \sum f_n$ is continuous, the point being
    that distinct supports are disjoint because $\abs{n-m} \ge 1 > 1/n^2 + 1/m^2$, so at most one term is
    nonzero at a point and only finitely many supports meet a bounded interval; one step computes
    $\int f_n = 1/n^2$ as a triangle's area and sums it by monotone convergence, so $f \in L^1$; one step
    observes $f(n) = 1$, which refutes the limit. Part (b): a single step gives the whole contradiction —
    the negation of the limit produces $\varepsilon_0$ and a sequence going to infinity, uniform continuity
    produces $\delta$, the bound $\abs{f} \ge \varepsilon_0/2$ holds on each $\delta$-interval, a subsequence
    makes those intervals pairwise disjoint, and the sum of their integrals is $\varepsilon_0\delta$ per term,
    hence infinite, contradicting $f \in L^1$. The "Goal" paragraph restating the problem is gone, the
    label-claims ("Continuity", "Integrability", "Failure to converge to 0", "Conclusion", and the "Part (a)"
    and "Part (b)" labels) are replaced by the assertions their proofs establish, and the closing step that
    only summarised the two parts is gone. Sources are cited by numbered statement: the monotone convergence
    theorem, and the definition of uniform continuity. No page reference is written in the body of this card
    or in the event above. The statement is unchanged. The collection retains the UGA real analysis
    qualifying exam of Spring 2014 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
(a) Give an example of a continuous function $f \in L^1(\RR)$ such that $f(x) \not\to 0$ as $\abs{x} \to \infty$.

(b) Show that if $f \in L^1(\RR)$ is *uniformly continuous*, then
$$
\lim_{\abs{x} \to \infty} f(x) = 0.
$$
:::

::: {.solution}
**Goal:** Construct a sequence of narrowing triangular spikes of height 1 in (a), and use uniform continuity to lower-bound the integral on disjoint intervals in (b).

::: pf

::: {.pf-step #construction}
The series $f = \sum_{n \ge 2} f_n$ of triangular spikes converges pointwise to a continuous function.

::: pf-proof
For $n \ge 2$ let $f_n$ be the tent of height $1$ with support $[n - 1/n^2, n + 1/n^2]$, given by $f_n(x) = \max\{0, 1 - n^2\abs{x-n}\}$. Distinct indices $n \ne m$ give disjoint supports, because a point of both supports would satisfy $\abs{n - m} \le 1/n^2 + 1/m^2 \le 1/4 + 1/4 < 1$ while $\abs{n-m} \ge 1$. A point $x$ therefore lies in at most one support, so the series has at most one nonzero term at each $x$, and it converges to $f(x)$; and $f$ agrees with one continuous $f_n$ on a neighbourhood of $x$, since the supports are closed and locally finite in the bounded sense that only finitely many meet a bounded interval. Hence $f$ is continuous at every $x$.
:::

:::

::: {.pf-step #integrable}
$f \in L^1(\RR)$.

::: pf-proof
Each tent has integral $\tfrac12 \cdot \tfrac{2}{n^2}\cdot 1 = 1/n^2$, being a triangle of base $2/n^2$ and height $1$. The terms are nonnegative and measurable, so the monotone convergence theorem applies to the partial sums and gives $\int_\RR \abs{f} = \sum_{n\ge2} 1/n^2$, which is finite because that series converges. Hence $f \in L^1(\RR)$.
:::

:::

::: {.pf-step #no-limit}
$f(x)$ does not tend to $0$ as $\abs{x} \to \infty$.

::: pf-proof
At the integer $n \ge 2$ the only nonzero term is $f_n$, whose value there is $1$, so $f(n) = 1$ for every $n \ge 2$. The sequence $n \to \infty$ therefore has $f(n) = 1$, and a function tending to $0$ at infinity would have $\abs{f}$ eventually below $1/2$ along it. So the limit is not $0$.
:::

:::

::: {.pf-step #uniform-implies-limit}
If $f \in L^1(\RR)$ is uniformly continuous then $f(x) \to 0$ as $\abs{x} \to \infty$.

::: pf-proof
Suppose $f(x)$ does not tend to $0$ at infinity. Then there are $\varepsilon_0 > 0$ and a sequence with $\abs{x_n} \to \infty$ and $\abs{f(x_n)} \ge \varepsilon_0$ for every $n$: a function tending to $0$ would have $\abs{f} < \varepsilon_0$ outside some bounded set, and the negation of that gives the sequence.

Uniform continuity supplies $\delta > 0$ with $\abs{f(x) - f(y)} < \varepsilon_0/2$ whenever $\abs{x - y} < \delta$. For every $n$ and every $x \in (x_n - \delta, x_n + \delta)$ one then has
$$\abs{f(x)} \ge \abs{f(x_n)} - \abs{f(x) - f(x_n)} \ge \varepsilon_0 - \varepsilon_0/2 = \varepsilon_0/2.$$
Since $\abs{x_n} \to \infty$, a subsequence can be chosen with $\abs{x_{n_{k+1}} - x_{n_k}} \ge 2\delta$, so the intervals $I_k = (x_{n_k} - \delta, x_{n_k} + \delta)$ are pairwise disjoint. Summing over them,
$$\int_\RR \abs{f} \ge \sum_{k=1}^\infty \int_{I_k} \abs{f} \ge \sum_{k=1}^\infty \frac{\varepsilon_0}{2}\cdot 2\delta = \infty,$$
so $f \notin L^1(\RR)$, contradicting the hypothesis. Hence the limit is $0$.
:::

:::

:::


:::
