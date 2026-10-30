---
schema: qual/card@1
id: P-WESCA09-III1
kind: problem
title: 'A Cauchy derivative estimate at the center of a disk'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Section III, problem 1 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Let $f$ be analytic on the disk $\Delta(z_0,r)$ and suppose there is $m>0$ such that
$$
\abs{f(z)-f(z_0)}\le m\qquad(z\in\Delta(z_0,r)).
$$
Prove
$$
\abs{f'(z_0)}\le \frac mr.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $\rho$ with $0<\rho<r$,
$$
\abs{f'(z_0)}\le \frac m\rho.
$$


::: pf-proof

Set
$$
g(z)=f(z)-f(z_0).
$$
Then $g$ is analytic on $\Delta(z_0,r)$, $g'(z_0)=f'(z_0)$, and
$\abs{g(z)}\le m$ throughout the disk. For $0<\rho<r$, Cauchy's derivative
formula on the circle $\abs{\zeta-z_0}=\rho$ gives
$$
g'(z_0)
=\frac1{2\pi i}
\int_{\abs{\zeta-z_0}=\rho}
\frac{g(\zeta)}{(\zeta-z_0)^2}\,d\zeta.
$$
Therefore
$$
\abs{f'(z_0)}
=\abs{g'(z_0)}
\le \frac1{2\pi}(2\pi\rho)\frac m{\rho^2}
=\frac m\rho.
$$

:::

:::

::: {.pf-step #s1-2}

One has
$$
\boxed{\abs{f'(z_0)}\le\frac mr}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} holds for every $0<\rho<r$. Letting $\rho\uparrow r$ yields
$$
\abs{f'(z_0)}\le\frac mr.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} is the required estimate.

:::

:::

:::
