---
schema: qual/card@1
id: P-WESCA13J-II3
kind: problem
title: 'Must an entire function with an entire square root be constant?'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. This is the deterministic Flash reading. As written it is false (for example $f(z)=z^2$ admits the entire square root $g(z)=z$), so no unrecorded correction has been made.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source asks to prove that an entire $f$ with an entire square root $g=\sqrt f$ must be constant, which is false ($f=z^2$, $g=z$). The statement now asks to prove or disprove the claim.
---

::: {.problem}
Let $f$ be entire and suppose the function
\[
g(z)=\sqrt{f(z)}
\]
is also entire, that is, $g$ is entire and $g^2=f$.
Prove or disprove: $f$ must be constant.
:::

::: {.solution}
The claim is false.

::: pf

::: {.pf-step #s1-1}
Let $g(z)=z$ and $f(z)=z^2$. Then $f$ and $g$ are entire, $g^2=f$, and $f$ is nonconstant.

::: pf-proof
Both functions are polynomials, hence entire. By construction $g(z)^2=z^2=f(z)$ for every $z\in\CC$, and $f(1)=1\neq0=f(0)$.
:::

:::

::: pf-step
Hence an entire function with an entire square root need not be constant. More generally, $f=h^2$, $g=h$ is a counterexample for every nonconstant entire $h$.

::: pf-proof
Step [](#s1-1){.pf-ref} gives one counterexample. For a nonconstant entire $h$, both $h$ and $h^2$ are entire, $h^2$ is nonconstant because $h$ is (a constant square $h^2=c$ forces $h$ to take at most two values, so the continuous $h$ on the connected plane is constant), and $h$ is an entire square root of $h^2$.
:::

:::

:::

:::
