---
schema: qual/card@1
id: P-JHUFA01RAC
kind: problem
title: '$L^{4/3}$ boundedness plus convergence in measure implies $L^1$ convergence'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the JHU Real Analysis Qualifying Exam, Fall 2001, in the preserved exam compilation.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The exponents in Hölder are checked (1/(4/3) + 1/4 = 1), the integrability bound is carried into the estimate rather than dropped, the cut set is stated to be measurable, and the final epsilon bookkeeping is made explicit: with eta = eps/2 and m{|f_n| > eta} < eta^4 the total is below eps. The original used eps and eps/2 in a way that left the second threshold unstated. No retained solution set covers the exercise (the provenance is the JHU examination papers), so the card says the argument is its own. No statement repair.
---

::: {.problem}
Let $(f_n)$ be real-valued functions in $L^{4/3}(0,1)$ such that $f_n\to0$ in measure and
$$
\int_0^1 \abs{f_n(x)}^{4/3}\,dx\le1
\qquad(n\ge1).
$$
Show that
$$
\int_0^1\abs{f_n(x)}\,dx\longrightarrow0.
$$
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is the JHU examination papers and the card records only the statement. The argument is the card's own.

::: pf

::: {.pf-step #split}
For $\eta>0$ and each $n$,
$$
\int_0^1\abs{f_n}=\int_{\{\abs{f_n}\le\eta\}}\abs{f_n}+\int_{\{\abs{f_n}>\eta\}}\abs{f_n},
$$
and the first summand is at most $\eta$.

::: pf-proof
The two sets $\{\abs{f_n}\le\eta\}$ and $\{\abs{f_n}>\eta\}$ are measurable and partition $[0,1]$, so the integral is additive over them. On the first, the integrand is bounded by $\eta$ and the measure of the set is at most $1$.
:::

:::

::: {.pf-step #holder}
With exponents $p=4/3$ and $q=4$, for every $n$
$$
\int_{\{\abs{f_n}>\eta\}}\abs{f_n}\le\norm{f_n}_{4/3}\,m\{\abs{f_n}>\eta\}^{1/4}\le m\{\abs{f_n}>\eta\}^{1/4}.
$$

::: pf-proof
$\frac1p+\frac1q=\frac34+\frac14=1$, so Hölder's inequality on the set $E_n=\{\abs{f_n}>\eta\}$ gives $\int_{E_n}\abs{f_n}\le\left(\int_{E_n}\abs{f_n}^{4/3}\right)^{3/4}m(E_n)^{1/4}$, and $\int_{E_n}\abs{f_n}^{4/3}\le\int_0^1\abs{f_n}^{4/3}\le1$ by hypothesis. (Since $m(E_n)\le1$, no further factor is needed.)
:::

:::

::: {.pf-step #measure}
$m\{\abs{f_n}>\eta\}\to0$ for each fixed $\eta>0$.

::: pf-proof
This is the definition of convergence in measure to $0$: for every $\eta>0$, $m\{x:\abs{f_n(x)-0}>\eta\}\to0$.
:::

:::

::: {.pf-step #conclusion}
$\int_0^1\abs{f_n}\to0$.

::: pf-proof
Let $\varepsilon>0$ and put $\eta=\varepsilon/2$. By steps [](#split){.pf-ref} and [](#holder){.pf-ref},
$$
\int_0^1\abs{f_n}\le\eta+m\{\abs{f_n}>\eta\}^{1/4},
$$
and by step [](#measure){.pf-ref} there is $N$ with $m\{\abs{f_n}>\eta\}<\eta^4$ for $n\ge N$, whence $\int_0^1\abs{f_n}<\eta+\eta=\varepsilon$ for $n\ge N$.
:::

:::

:::
:::
