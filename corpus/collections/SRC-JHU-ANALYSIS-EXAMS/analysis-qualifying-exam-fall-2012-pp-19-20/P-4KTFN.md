---
schema: qual/card@1
id: P-4KTFN
kind: problem
title: "Fatou's lemma, the dominated convergence theorem, and a counterexample"
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Dominated Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked against Problem 6 of the JHU Fall 2012 analysis qualifying exam. The source first restricts the problem to functions on [0,1] but part (c) then prints an integral from -infinity to +infinity; the card corrects that inconsistent bound to [0,1], matching the stated domain and the intended moving-spike example.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
6. For this problem, consider just Lebesgue measurable functions $f : [ 0 , 1 ] \to \mathbb { R }$ . together with the Lebesgue measure.

(a) State Fatou’s lemma (no proof required).

(b) State and prove the Dominated Convergence Theorem.

(c) Give an example where $f_n(x) \to 0$ a.e. on $[0,1]$, but $\int_0^1 f_n(x)\,dx \to 1$.
:::

::: {.solution}
Throughout, $(X,\mu)$ is $[0,1]$ with Lebesgue measure.

::: pf

::: {.pf-step #fatous-lemma-statement}
(a) Fatou's lemma: if $f_n\ge0$ are measurable, then $\int\liminf_n f_n\le\liminf_n\int f_n$.

::: pf-proof
This is the requested statement.
:::

:::

::: {.pf-step #dominated-convergence-theorem}
(b) If $f_n\to f$ a.e., and $\abs{f_n}\le g$ a.e. for all $n$ with $g\in L^1$, then $f\in L^1$ and $\int f_n\to\int f$.

::: pf-proof

::: {.pf-step #f-in-l1}
$f\in L^1$.

::: pf-proof
Letting $n\to\infty$ in $\abs{f_n}\le g$ gives $\abs f\le g$ a.e., and $g$ is integrable.
:::

:::

::: {.pf-step #liminf-bound}
$\int f\le\liminf_n\int f_n$.

::: pf-proof
Fatou's lemma applied to $g+f_n\ge0$ gives $\int(g+f)\le\int g+\liminf_n\int f_n$, and $\int g$ is finite.
:::

:::

::: {.pf-step #limsup-bound}
$\limsup_n\int f_n\le\int f$.

::: pf-proof
Fatou's lemma applied to $g-f_n\ge0$ gives $\int(g-f)\le\int g-\limsup_n\int f_n$, and $\int g$ is finite.
:::

:::

::: pf-qed
Steps [](#liminf-bound){.pf-ref} and [](#limsup-bound){.pf-ref} give $\limsup_n\int f_n\le\int f\le\liminf_n\int f_n$, so $\int f_n\to\int f$; step [](#f-in-l1){.pf-ref} gives $f\in L^1$.
:::

:::

:::

::: {.pf-step #moving-spike-example}
(c) $\boxed{f_n=n\,\mathbf 1_{(0,1/n)}}$ satisfies $f_n\to0$ everywhere on $[0,1]$ and $\int_0^1f_n=1$ for all $n$.

::: pf-proof
$f_n(0)=0$, and for $x\in(0,1]$, $f_n(x)=0$ once $n>1/x$. Also $\int_0^1f_n=n\cdot\frac1n=1$.
:::

:::

::: pf-qed
Steps [](#fatous-lemma-statement){.pf-ref}, [](#dominated-convergence-theorem){.pf-ref} and [](#moving-spike-example){.pf-ref} answer parts (a), (b) and (c).
:::

:::
:::
