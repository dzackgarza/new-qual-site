---
schema: qual/card@1
id: P-CALCPT3-06
kind: problem
title: "Minimize $\\int_b^{b+1}(x^2+x)\\,dx$ over $b$"
classification:
  areas: [prelim]
  topics: [Integrals, Fundamental Theorem of Calculus, Extremal Problems]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 6 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree."
---

::: {.problem}
For what value of $b$ is the value of
$$\int_b^{b+1}(x^2+x)\,dx$$
a minimum?

(A) $0$
(B) $-1$
(C) $-2$
(D) $-3$
(E) $-4$
:::

::: {.solution}
Write $f(x)=x^2+x$ and $F(b)=\int_b^{b+1}f(x)\,dx$.

::: pf

::: {.pf-step #derivative}
$F'(b)=2b+2$ for every real $b$.

::: pf-proof
Since $f$ is continuous, the fundamental theorem of calculus gives $F'(b)=f(b+1)-f(b)=(b+1)^2+(b+1)-b^2-b=2b+2$.
:::

:::

::: pf-step
The minimum occurs at $\boxed{b=-1}$, choice (B).

::: pf-proof
By step [](#derivative){.pf-ref}, $F'(b)<0$ for $b<-1$ and $F'(b)>0$ for $b>-1$, so $F$ decreases on $(-\infty,-1]$ and increases on $[-1,\infty)$.
Hence $F$ attains its global minimum at $b=-1$ and nowhere else.
:::

:::

:::

:::
