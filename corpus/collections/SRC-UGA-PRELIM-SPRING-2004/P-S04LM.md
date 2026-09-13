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

::: problem
Suppose $L$ is a real number and $f, g: \mathbb{R} \to \mathbb{R}$.
Prove that if $\lim_{x \to 0} g(x) = L$ and $f$ is continuous at $L$, then $\lim_{x \to 0} f(g(x))$ also exists.
:::

::: solution
<1>1. We claim that
\[
\lim_{x\to0}f(g(x))=f(L).
\]
:::

<1>2. Let $\varepsilon>0$. Since $f$ is continuous at $L$, there exists $\eta>0$ such that
\[
|y-L|<\eta\implies |f(y)-f(L)|<\varepsilon.
\]

<1>3. Since $g(x)\to L$ as $x\to0$, there exists $\delta>0$ such that
\[
0<|x|<\delta\implies |g(x)-L|<\eta.
\]

<1>4. Therefore, whenever $0<|x|<\delta$,
\[
|f(g(x))-f(L)|<\varepsilon.
\]
::: {.proof}
By <1>3, the number $g(x)$ satisfies $|g(x)-L|<\eta$; applying <1>2 with $y=g(x)$ yields the displayed inequality.
:::

<1>5. Hence $\lim_{x\to0}f(g(x))$ exists and equals $f(L)$.
::: {.proof}
This is exactly the $\varepsilon$-$\delta$ definition of the limit, using <1>4.
:::
