---
schema: qual/card@1
id: P-WESRA16-B3
kind: problem
title: '$L^1$ convergence implies convergence in measure'
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Group B, problem B3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Let $(X,\mathcal M,\mu)$ be a measure space and let $f_n:X\to\RR$ be measurable.

(a) Define $f_n\to0$ in $L^1$ and define $f_n\to0$ in measure.

(b) Prove that $L^1$ convergence to $0$ implies convergence in measure to $0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The statement $f_n\to0$ in $L^1$ means that each $f_n$ is integrable and
$$
\norm{f_n}_{L^1}
=\int_X\abs{f_n}\,d\mu
\longrightarrow0.
$$


::: pf-proof

This is the definition of convergence to zero in the $L^1$ norm. This gives the first definition requested in part (a).

:::

:::

::: {.pf-step #s1-2}

The statement $f_n\to0$ in measure means that for every $\varepsilon>0$,
$$
\mu\bigl(\{x:\abs{f_n(x)}\geq\varepsilon\}\bigr)
\longrightarrow0.
$$


::: pf-proof

This is the definition of convergence in measure to zero. Replacing $\geq\varepsilon$ by $>\varepsilon$ gives an equivalent definition. This completes part (a).

:::

:::

::: {.pf-step #s1-3}

For every $\varepsilon>0$ and every $n$,
$$
\varepsilon\,
\mu\bigl(\{x:\abs{f_n(x)}\geq\varepsilon\}\bigr)
\leq
\norm{f_n}_{L^1}.
$$


::: pf-proof

Let
$$
E_{n,\varepsilon}=\{x:\abs{f_n(x)}\geq\varepsilon\}.
$$
Pointwise on $X$,
$$
\varepsilon\mathbf1_{E_{n,\varepsilon}}
\leq\abs{f_n}.
$$
Integrating this inequality gives
$$
\varepsilon\mu(E_{n,\varepsilon})
\leq\int_X\abs{f_n}\,d\mu
=\norm{f_n}_{L^1}.
$$

:::

:::

::: {.pf-step #s1-4}

If $f_n\to0$ in $L^1$, then
$$
\boxed{f_n\to0\text{ in measure}.}
$$


::: pf-proof

Fix $\varepsilon>0$. By step [](#s1-3){.pf-ref},
$$
0\leq
\mu\bigl(\{x:\abs{f_n(x)}\geq\varepsilon\}\bigr)
\leq
\frac{\norm{f_n}_{L^1}}{\varepsilon}.
$$
If $f_n\to0$ in $L^1$, then the right-hand side tends to zero. Hence the measure of the exceptional set tends to zero. By step [](#s1-2){.pf-ref}, this is convergence in measure. This proves part (b).

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give the requested definitions, and step [](#s1-4){.pf-ref} proves the implication.

:::

:::

:::
