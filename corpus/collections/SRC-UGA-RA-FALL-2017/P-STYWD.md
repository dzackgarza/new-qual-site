---
schema: qual/card@1
id: P-STYWD
kind: problem
title: The series $\sum x^n/n!$ converges uniformly on bounded intervals but not on
  $\RR$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Convergence
  - Series of Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Eleven steps asserted their claim with no
    justification and the card is now four steps each deriving its claim. Boundedness gives uniform and
    absolute convergence by the Weierstrass $M$-test with the dominating series $\sum M^n/n! = e^M$; the
    necessary condition is derived from the uniform Cauchy property of the partial sums, taking the
    consecutive difference $S_N - S_{N-1} = u_N$; unboundedness gives failure of the condition, with the two
    cases of an interval unbounded above and below handled in one step and the suprema computed as
    infinite; and the final step combines the two directions into the characterization. The "Goal"
    paragraph restating the problem is gone, the labels ("Uniform convergence on bounded intervals
    (Weierstrass $M$-test)", "Necessary condition for uniform convergence of series", "Failure of uniform
    convergence on unbounded intervals", "Conclusion") are replaced by the assertions their proofs
    establish, and the separate "Conclusion" step that only restated the equivalence is now the step that
    derives it. Sources are cited by numbered statement: the Weierstrass $M$-test, the uniform Cauchy
    criterion, and the definition of uniform convergence of a series. No page reference is written in the
    body of this card or in the event above. The statement is unchanged. The collection retains the UGA
    real analysis qualifying exam of Fall 2017 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Let
$$
f(x) = \sum_{n=0}^{\infty} \frac{x^{n}}{n!}.
$$
Determine all intervals $I \subseteq \RR$ on which the series converges uniformly, and prove the characterization.
:::

::: {.solution}

::: pf

::: {.pf-step #bounded}
The series converges uniformly and absolutely on every bounded interval.

::: pf-proof
Let $I$ be a bounded interval; then $\abs{x} \le M$ for all $x \in I$ and some $M > 0$. For each $n \ge 0$ and $x \in I$,
$$\abs{\frac{x^n}{n!}} = \frac{\abs{x}^n}{n!} \le \frac{M^n}{n!} =: M_n,$$
and the numerical series $\sum_n M_n$ is $e^M$, which is finite. The Weierstrass $M$-test then gives uniform convergence of the series on $I$, and absolute convergence because the dominating series has nonnegative terms.
:::

:::

::: {.pf-step #s2}
If a series of functions converges uniformly on a set $E$, then $\sup_{x \in E}\abs{u_n(x)} \to 0$.

::: pf-proof
Uniform convergence means the partial sums $S_N = \sum_{n \le N} u_n$ are uniformly Cauchy: for every $\eta > 0$ there is $N_0$ with $\sup_E \abs{S_N - S_M} < \eta$ for all $N, M \ge N_0$. Taking $M = N-1$ gives $\sup_E \abs{u_N} < \eta$ for $N > N_0$, since $S_N - S_{N-1} = u_N$. So the suprema tend to $0$, which is the stated necessary condition.
:::

:::

::: {.pf-step #unbounded}
If $I$ is unbounded then the series does not converge uniformly on $I$.

::: pf-proof
The interval is unbounded above or below. If it is unbounded above, choose $x_k \in I$ with $x_k \to +\infty$; then for each fixed $n \ge 1$,
$$\sup_{x \in I}\abs{\frac{x^n}{n!}} \ge \sup_{k \in \NN}\frac{x_k^n}{n!} = \infty,$$
so $\sup_I \abs{u_n} = \infty$ for every $n \ge 1$ and the suprema do not tend to $0$. If the interval is unbounded below, the same computation applies to $\abs{x_k}^n$ with $x_k \to -\infty$. In either case the necessary condition of step [](#s2){.pf-ref} fails, so the series is not uniformly convergent on $I$.
:::

:::

::: pf-step

The series converges uniformly on an interval $I$ if and only if $I$ is bounded.

::: pf-proof
Boundedness gives uniform convergence by step [](#bounded){.pf-ref}, and unboundedness gives failure of uniform convergence by step [](#unbounded){.pf-ref}. These two exhaust the possibilities for an interval, so the characterization is proved.
:::

:::

:::

:::
