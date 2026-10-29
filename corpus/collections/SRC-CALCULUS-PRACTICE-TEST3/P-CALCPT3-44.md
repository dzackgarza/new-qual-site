---
schema: qual/card@1
id: P-CALCPT3-44
kind: problem
title: "Second symmetric difference quotient of a polynomial with step $3h$"
classification:
  areas: [prelim]
  topics: [Taylor Series, Limits]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 44 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction, which drops choice (E). The 300 dpi page render reads (E) as infinity."
---

::: {.problem}
If $x$ is a real number and $P$ is a polynomial function, then
$$\lim_{h\to0}\frac{P(x+3h)+P(x-3h)-2P(x)}{h^2}=$$

(A) $0$
(B) $6P'(x)$
(C) $3P''(x)$
(D) $9P''(x)$
(E) $\infty$
:::

::: {.solution}
Fix $x$ and let $d\coloneqq\deg P$. A polynomial equals its Taylor expansion at $x$: $P(x+t)=\sum_{j=0}^{d}\frac{P^{(j)}(x)}{j!}t^j$ for all real $t$.

::: pf

::: {.pf-step #expand}
$P(x+3h)+P(x-3h)-2P(x)=9P''(x)h^2+\sum_{j\ge4,\ j\text{ even}}\frac{2\cdot3^jP^{(j)}(x)}{j!}h^j$.

::: pf-proof
Add the expansions at $t=3h$ and $t=-3h$. Odd powers of $t$ cancel, and the constant terms cancel against $-2P(x)$. The $t^2$ terms give $2\cdot\frac{P''(x)}2(3h)^2=9P''(x)h^2$.
:::

:::

::: {.pf-step #limit}
The limit is $\boxed{9P''(x)}$, choice (D).

::: pf-proof
Divide step [](#expand){.pf-ref} by $h^2$. The remaining sum is a polynomial in $h$ with no constant term, so it tends to $0$ as $h\to0$.
:::

:::

::: pf-step
Choices (A), (B), (C), and (E) are wrong.

::: pf-proof
Take $P(t)=t^2$ and $x=0$. By step [](#limit){.pf-ref} the limit is $18$, while (A), (B), (C), (E) give $0$, $0$, $6$, $\infty$.
:::

:::

:::

:::
