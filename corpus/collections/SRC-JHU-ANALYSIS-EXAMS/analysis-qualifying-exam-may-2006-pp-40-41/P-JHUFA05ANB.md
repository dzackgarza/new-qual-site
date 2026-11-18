---
schema: qual/card@1
id: P-JHUFA05ANB
kind: problem
title: 'Translation continuity of $L^1$ functions on the line'
classification:
  areas:
  - real-analysis
  topics:
  - L1 Spaces
  - Convolution
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the preserved JHU analysis qualifying exam collection containing this May 2006 card.
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
    Restructured as a Lamport proof of the same three-epsilon argument. The two facts the argument
    leans on are now named where they are used: the density of C_c in L^1 for the choice of g, and the
    translation invariance of Lebesgue measure for the middle comparison. The bound on the continuous
    part is justified by uniform continuity on a fixed compact interval that contains the support of g
    and of its translates for small h, which the prose had compressed into a single line. No published
    solution located; the card keeps its own argument and says so.
---

::: {.problem}
Let $f\in L^1(\RR)$. Prove that
$$
\lim_{h\to0}\int_{\RR}\abs{f(x+h)-f(x)}\,dx=0.
$$
:::

::: {.solution}

No published solution was located for this examination problem; the argument is the standard three-epsilon one, and it is the card's own. The two steps it turns on are named: the density of $C_{c}(\RR)$ in $L^{1}(\RR)$, and the translation invariance of Lebesgue measure, which is what lets the comparison be made at the translated point.

The statement was checked against Problem 2 of the JHU analysis qualifying examination of May 2006, as preserved in the collection holding this card. Throughout $f\in L^{1}(\RR)$, $\norm{\cdot}_{1}$ is the $L^{1}$ norm, and $f(\cdot+h)$ denotes the translate $x\mapsto f(x+h)$.

::: pf

::: {.pf-step #approximate}

For $\varepsilon>0$ there is $g\in C_{c}(\RR)$ with $\norm{f-g}_{1}<\varepsilon/3$.

::: pf-proof

$C_{c}(\RR)$ is dense in $L^{1}(\RR)$, so such a $g$ exists.

:::

:::

::: {.pf-step #translate}

For every $h$ one has $\norm{f(\cdot+h)-g(\cdot+h)}_{1}=\norm{f-g}_{1}<\varepsilon/3$.

::: pf-proof

Lebesgue measure is translation invariant: $\int\abs{f(x+h)-g(x+h)}\,dx=\int\abs{f(u)-g(u)}\,du$ under the substitution $u=x+h$, the substitution being a measure-preserving change of variable.

:::

:::

::: {.pf-step #continuous-case}

There is $\delta>0$ such that $\abs{h}<\delta$ implies $\norm{g(\cdot+h)-g}_{1}<\varepsilon/3$.

::: pf-proof

$g$ is continuous and compactly supported, hence uniformly continuous, and its support lies in a compact interval $K_{0}$; for $\abs{h}\leq1$ the support of $g(\cdot+h)$ lies in a fixed compact interval $K\supset K_{0}$. For such $h$,
$$
\norm{g(\cdot+h)-g}_{1}\leq m(K)\sup_{x\in K}\abs{g(x+h)-g(x)},
$$
and the supremum tends to $0$ as $h\to0$ by uniform continuity; so the norm does too, and some $\delta>0$ makes it smaller than $\varepsilon/3$.

:::

:::

::: pf-step

$\lim_{h\to0}\int_{\RR}\abs{f(x+h)-f(x)}\,dx=0$.

::: pf-proof

Let $\varepsilon>0$ and take $g$ and $\delta$ from steps [](#approximate){.pf-ref} and [](#continuous-case){.pf-ref}. For $\abs{h}<\delta$, the triangle inequality for the $L^{1}$ norm gives
$$
\norm{f(\cdot+h)-f}_{1}\leq\norm{f(\cdot+h)-g(\cdot+h)}_{1}+\norm{g(\cdot+h)-g}_{1}+\norm{g-f}_{1}<\frac{\varepsilon}{3}+\frac{\varepsilon}{3}+\frac{\varepsilon}{3}=\varepsilon,
$$
the first term bounded by step [](#translate){.pf-ref} and the third by the choice of $g$. As $\varepsilon$ was arbitrary, the limit is $0$.

:::

:::

:::

:::
