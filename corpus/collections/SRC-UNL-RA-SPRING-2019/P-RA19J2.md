---
schema: qual/card@1
id: P-RA19J2
kind: problem
title: Boundedness and closedness of the self-maps of $[0,1]$ in $C_b([0,1])$
classification:
  areas:
  - real-analysis
  topics:
  - Function Spaces
  - Compactness
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked directly against Problem 2 in the preserved UNL January 2019 qualifying-exam PDF/extraction.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card carried no audit list; this one records the change. Seven steps asserted their claim with no
    justification and each now carries one: the bound $\rho_\infty \le 1$ and the exact diameter from the
    constant functions, the passage from convergence in $\rho_\infty$ to uniform convergence with
    continuity and boundedness of the limit, the closedness of $[0,1]$ that puts the limit in $A$, the
    boundedness and closedness assembled for part (c), the failure of uniform convergence for $x^n$ from
    the discontinuity of its pointwise limit, and the compact-to-sequentially-compact argument that
    excludes compactness. Seven run-in "Proof:" labels sat inside step claims, which STYLE-07 forbids, and
    their text is now the body of the corresponding proof; the three pf-qed blocks whose whole content
    pointed back at the steps above are gone, and a "Goal" paragraph restating the problem is gone.
    Sources are cited by numbered statement: Arzelà--Ascoli, and the theorem that a compact metric space
    is sequentially compact. No page reference is written in the body of this card or in the event above.
    The statement is unchanged. The collection retains the UNL real analysis qualifying exam of Spring
    2019 and no solution sheet, so the argument is the card's own.
---

::: {.problem}
Consider the following subset of the metric space $(C_b([0,1]),\rho_\infty)$: $$A:=\{f\in C_b([0,1]):f([0,1])\subseteq[0,1]\}.$$

(a) Determine whether $A$ is bounded, and if so what is its diameter.

(b) Determine whether $A$ is closed in $C_b([0,1])$.

(c) Determine whether $A$ is compact in $C_b([0,1])$.
:::

:::: {.solution}

::: pf

::: {.pf-step #s1}

(a) $A$ is bounded, with diameter $1$.

::: pf-proof

::: {.pf-step #s1-1}

$\rho_\infty(f,g) \le 1$ for all $f, g \in A$.


::: pf-proof
Both functions take values in $[0,1]$ at every point, so $\abs{f(x) - g(x)} \le 1$ for every $x$; the supremum over $x$ of a quantity bounded by $1$ is at most $1$, and $\rho_\infty$ is that supremum.
:::

:::

::: {.pf-step #s1-2}

The diameter of $A$ is exactly $1$.


::: pf-proof
The constant functions $0$ and $1$ are continuous and bounded with values in $[0,1]$, so they lie in $A$; their distance is $\sup_x \abs{0 - 1} = 1$. A set whose distances are at most $1$ and which contains a pair at distance $1$ has diameter exactly $1$.
:::

:::

:::

:::

::: {.pf-step #s2}

(b) $A$ is closed in $C_b[0,1]$.

::: pf-proof

::: pf-step

A uniform limit of a sequence in $A$ lies in $A$.


::: pf-proof
Convergence in $\rho_\infty$ is uniform convergence: $\rho_\infty(f_n,f) \to 0$ says the suprema of $\abs{f_n - f}$ tend to $0$, which is the definition. A uniform limit of continuous functions is continuous, and it is bounded because it is continuous on the compact interval $[0,1]$, so $f \in C_b([0,1])$.
:::

:::

::: {.pf-step #s2-2}

Such a limit satisfies $f(x) \in [0,1]$ for every $x$.


::: pf-proof
For each fixed $x$ the numbers $f_n(x)$ lie in $[0,1]$, so $\abs{f_n(x) - f(x)} \le \rho_\infty(f_n,f) \to 0$, which is pointwise convergence and gives $f(x) = \lim_n f_n(x)$. The interval $[0,1]$ is closed, so a limit of points of $[0,1]$ lies in $[0,1]$; hence $f([0,1]) \subseteq [0,1]$ and $f \in A$.
:::

:::

:::

:::

::: pf-step

(c) $A$ is NOT compact.

::: pf-proof

::: pf-step

$A$ is closed and bounded.


::: pf-proof
Boundedness is part (a) and closedness is part (b), established by the steps of those parts. Their two claims together are the stated one.
:::

:::

::: {.pf-step #s3-2}

The sequence $f_n(x) = x^n$ lies in $A$ and has no uniformly convergent subsequence.


::: pf-proof
Each $f_n$ is continuous with $x^n \in [0,1]$ for $x \in [0,1]$, so $f_n \in A$. If a subsequence converged uniformly, its limit would be continuous, being a uniform limit of continuous functions; but the subsequence converges pointwise, for $x < 1$ to $0$ and at $x = 1$ to $1$, and a pointwise limit is unique, so that discontinuous function would be the uniform limit, a contradiction.
:::

:::

::: {.pf-step #s3-3}

$A$ is not compact.


::: pf-proof
A compact metric space is sequentially compact: every sequence has a convergent subsequence, the balls of radius $1/k$ around a finite subcover of the cover by all balls giving a point whose every neighbourhood the sequence visits infinitely often. The sequence of the previous step has no uniformly convergent subsequence, and $\rho_\infty$ is the metric, so no subsequence converges at all; hence $A$ is not sequentially compact and therefore not compact. Equivalently, in the language of the Arzelà--Ascoli theorem, a compact subset of $C[0,1]$ is equicontinuous and this family is not.
:::

:::

:::

:::

:::

:::
