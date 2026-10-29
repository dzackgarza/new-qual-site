---
schema: qual/card@1
id: P-Y5SS5
kind: problem
title: A nowhere-vanishing holomorphic function on a simply connected domain is of
  the form $e^g$
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Logarithm
  - Holomorphic Functions
relations: []
review: draft
---

::: {.exercise}
Prove that if $D$ is a [[D-GFM35|simply connected]] domain and $f(z)$ is [[D-E7A5W|holomorphic]] and nonzero on $D$, then $f(z)=e^{g(z)}$, where $g(z)$ is holomorphic on $D$.
:::

::: {.solution}

::: pf

::: {.pf-step #primitive}
There is a holomorphic $F$ on $D$ with $F'=f'/f$.

::: pf-proof
Since $f$ is nonzero on $D$, $f'/f$ is holomorphic on $D$, and a holomorphic function on a simply connected domain has a primitive.
:::

:::

::: {.pf-step #constant}
$e^{-F}f$ is a nonzero constant $c$ on $D$.

::: pf-proof
By step [](#primitive){.pf-ref},
$$
\qty{e^{-F}f}'=e^{-F}\qty{-F'f+f'}=e^{-F}\qty{-\frac{f'}{f}f+f'}=0,
$$
so $e^{-F}f$ is constant on the connected set $D$. It is nonzero because $e^{-F}$ and $f$ are.
:::

:::

::: pf-step
$f=e^g$ with $g$ holomorphic on $D$.

::: pf-proof
Choose $\alpha\in\CC$ with $e^\alpha=c$. By step [](#constant){.pf-ref}, $f=e^{F+\alpha}$, and $g\coloneqq F+\alpha$ is holomorphic on $D$.
:::

:::

:::

:::
