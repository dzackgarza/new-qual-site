---
schema: qual/card@1
id: P-CALCPT3-10
kind: problem
title: "Solve $f''=f'$ with $f(0)=0$, $f'(0)=-1$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 10 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
If $f''(x)=f'(x)$ for all real $x$, and if $f(0)=0$ and $f'(0)=-1$, then $f(x)=$

(A) $1-e^x$
(B) $e^x-1$
(C) $e^{-x}-1$
(D) $e^{-x}$
(E) $-e^x$
:::

::: {.solution}
Write $g=f'$, so that $g'=g$ on $\RR$ and $g(0)=-1$.

::: pf

::: {.pf-step #first-derivative}
$f'(x)=-e^x$ for every real $x$.

::: pf-proof
The function $h(x)=e^{-x}g(x)$ has $h'(x)=e^{-x}\bigl(g'(x)-g(x)\bigr)=0$, so $h$ is constant on $\RR$ by the mean value theorem.
Since $h(0)=g(0)=-1$, we get $g(x)=-e^x$.
:::

:::

::: pf-step
$f(x)=\boxed{1-e^x}$, choice (A).

::: pf-proof
By step [](#first-derivative){.pf-ref}, the function $f(x)+e^x$ has zero derivative, so it is a constant $C$ by the mean value theorem.
Evaluating at $0$ gives $C=f(0)+1=1$, hence $f(x)=1-e^x$.
:::

:::

:::

:::
