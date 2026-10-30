---
schema: qual/card@1
id: P-S04LM
kind: problem
title: Continuity preserves sequential limits of $g$
classification:
  areas:
  - prelim
  topics:
  - Continuity
  - Limits
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Suppose $L$ is a real number and $f, g: \RR \to \RR$.
Prove that if $\lim_{x \to 0} g(x) = L$ and $f$ is continuous at $L$, then $\lim_{x \to 0} f(g(x))$ also exists.
:::

::: {.solution}

::: pf

::: pf-step
We claim that
$$
\lim_{x\to0}f(g(x))=f(L).
$$
:::

::: {.pf-step #s2}
Let $\varepsilon>0$. Since $f$ is continuous at $L$, there exists $\eta>0$ such that
$$
\abs{y-L}<\eta\implies \abs{f(y)-f(L)}<\varepsilon.
$$
:::

::: {.pf-step #s3}
Since $g(x)\to L$ as $x\to0$, there exists $\delta>0$ such that
$$
0<\abs{x}<\delta\implies \abs{g(x)-L}<\eta.
$$
:::

::: {.pf-step #s4}
Therefore, whenever $0<\abs{x}<\delta$,
$$
\abs{f(g(x))-f(L)}<\varepsilon.
$$

::: pf-proof
By step [](#s3){.pf-ref}, the number $g(x)$ satisfies $\abs{g(x)-L}<\eta$; applying step [](#s2){.pf-ref} with $y=g(x)$ yields the displayed inequality.
:::

:::

::: pf-step
Hence $\lim_{x\to0}f(g(x))$ exists and equals $f(L)$.

::: pf-proof
This is exactly the $\varepsilon$-$\delta$ definition of the limit, using step [](#s4){.pf-ref}.
:::

:::

:::
:::
