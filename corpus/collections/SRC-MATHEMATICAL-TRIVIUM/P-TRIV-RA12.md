---
schema: qual/card@1
id: P-TRIV-RA12
kind: problem
title: $\lim_{x\to0}\frac{\sin x}{x}$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 12, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $\lim_{x \to 0} \frac{\sin x}{x}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $0<x<\pi/2$,
$$
\sin x<x<\tan x.
$$


::: pf-proof

Comparing the inscribed triangle, circular sector, and tangent triangle in the
unit circle gives
$$
\frac12\sin x<\frac x2<\frac12\tan x.
$$
Multiplying by $2$ gives the claim.

:::

:::

::: {.pf-step #s1-2}

Hence, for $0<x<\pi/2$,
$$
\cos x<\frac{\sin x}{x}<1.
$$


::: pf-proof

The first inequality in step [](#s1-1){.pf-ref} gives $\sin x/x<1$. The second gives
$$
x<\frac{\sin x}{\cos x},
$$
and since $x>0$ and $\cos x>0$, this rearranges to
$$
\cos x<\frac{\sin x}{x}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\lim_{x\to0^+}\frac{\sin x}{x}=1.
$$


::: pf-proof

Step [](#s1-2){.pf-ref} and $\cos x\to1$ give the result by the squeeze theorem.

:::

:::

::: {.pf-step #s1-4}

The function
$$
x\longmapsto\frac{\sin x}{x}
$$
is even on $\RR\setminus\{0\}$.


::: pf-proof

For $x\neq0$,
$$
\frac{\sin(-x)}{-x}
=
\frac{-\sin x}{-x}
=
\frac{\sin x}{x}.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
\lim_{x\to0}\frac{\sin x}{x}=1.
}
$$


::: pf-proof

By step [](#s1-4){.pf-ref}, the left-hand limit equals the right-hand limit from step [](#s1-3){.pf-ref}.
Thus the two-sided limit exists and equals $1$.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required limit.

:::

:::

:::
