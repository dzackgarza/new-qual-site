---
schema: qual/card@1
id: P-WESRA08-I3
kind: problem
title: State the monotone convergence theorem
classification:
  areas: [real-analysis]
  topics: [Measure Theory, Monotone Convergence]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    The examination asks for the statement of the monotone convergence theorem, so the statement
    is kept as the answer and the pf block records the argument that it is true and complete:
    measurability of the almost everywhere limit, monotonicity of the integrals, and the two
    inequalities, the second by Fatou's lemma rather than by the theorem being stated. No
    statement was weakened or added to; the collection's provenance is the Wesleyan analysis
    compilation, and no solutions sheet accompanies it.
---

::: {.problem}
State the Lebesgue monotone convergence theorem in an abstract measure space.
:::

::: {.solution}
The examination asks for the statement, so what follows states it and records the argument that the stated theorem is true, which is what makes the statement usable. Throughout $(X,\mathcal{M},\mu)$ is a measure space and integrals are Lebesgue integrals of measurable functions into $[0,\infty]$, with the convention that $\int f\,d\mu = +\infty$ is allowed.

::: pf

::: {.pf-step #hypotheses}
The hypotheses are: $f_{1}, f_{2}, \\ldots \\colon X \\to [0,\\infty]$ are measurable, $0 \\le f_{1}(x) \\le f_{2}(x) \\le \\cdots$ for every $x \\in X$, and $f_{n}(x) \\to f(x)$ for almost every $x \\in X$.

::: pf-proof
These are the three conditions the theorem assumes, recorded here as the hypothesis of the statement.

:::

:::

::: {.pf-step #measurable}
The limit function $f$ may be taken measurable.

::: pf-proof
Put $g(x) \\coloneqq \\lim_{n}f_{n}(x)$ where the limit exists in $[0,\\infty]$ and $g(x) \\coloneqq 0$ elsewhere. The set where the limit fails is null, and on the set where it exists $g = \\limsup_{n}f_{n}$ is measurable because each $f_{n}$ is; a function differing from a measurable function on a null set is measurable, and $f = g$ almost everywhere.

:::

:::

::: {.pf-step #monotone-integrals}
The sequence $\\int f_{n}\\,d\\mu$ increases, so $L \\coloneqq \\lim_{n}\\int f_{n}\\,d\\mu = \\sup_{n}\\int f_{n}\\,d\\mu \\in [0,\\infty]$ exists.

::: pf-proof
$f_{n} \\le f_{n+1}$ pointwise by hypothesis, and the integral is monotone: $h \\le k$ pointwise implies $\\int h \\le \\int k$, since $\\int k = \\int h + \\int (k-h)$ and the last integral is $\\ge 0$. An increasing sequence in $[0,\\infty]$ has a limit there.

:::

:::

::: {.pf-step #two-bounds}
$L \\le \\int f\\,d\\mu$ and $\\int f\\,d\\mu \\le L$.

::: pf-proof
For the first, $f_{n} \\le f$ holds almost everywhere for every $n$, because the sequence increases to $f$ wherever it converges; monotonicity of the integral and the vanishing of integrals over null sets give $\\int f_{n} \\le \\int f$, hence $L \\le \\int f$. For the second, Fatou's lemma applied to the sequence $(f_{n})$, which is nonnegative and measurable, gives $\\int \\liminf_{n} f_{n}\\,d\\mu \\le \\liminf_{n}\\int f_{n}\\,d\\mu$; here $\\liminf_{n}f_{n} = f$ almost everywhere and $\\liminf_{n}\\int f_{n} = L$, so $\\int f \\le L$. Fatou's lemma is used rather than the monotone convergence theorem itself, so the argument does not assume what it proves.

:::

:::

::: pf-step
Lebesgue's monotone convergence theorem: under the hypotheses of step [](#hypotheses){.pf-ref}, $f$ is measurable and $\\int_{X} f\\,d\\mu = \\lim_{n\\to\\infty}\\int_{X} f_{n}\\,d\\mu$, both sides allowed to be $+\\infty$.

::: pf-proof
Measurability is step [](#measurable){.pf-ref}. Steps [](#monotone-integrals){.pf-ref} and [](#two-bounds){.pf-ref} give $L \\le \\int f$ and $\\int f \\le L$, so the two sides of the displayed equality are equal in $[0,\\infty]$, which is the assertion.

:::

:::

:::
:::
