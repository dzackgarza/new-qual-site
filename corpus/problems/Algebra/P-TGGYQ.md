---
schema: qual/card@1
id: P-TGGYQ
kind: problem
title: $[\QQ(\sqrt{2}+\sqrt{3}):\QQ]$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
---

::: {.problem}
Compute
$$
[\QQ(\sqrt2+\sqrt3):\QQ].
$$
:::

::: {.solution}
Let $\alpha=\sqrt2+\sqrt3$.

::: pf

::: {.pf-step #generates}
$\QQ(\alpha)=\QQ(\sqrt2,\sqrt3)$.

::: pf-proof
Since $(\sqrt3+\sqrt2)(\sqrt3-\sqrt2)=1$, $\alpha^{-1}=\sqrt3-\sqrt2\in\QQ(\alpha)$.
Hence $\sqrt3=(\alpha+\alpha^{-1})/2$ and $\sqrt2=(\alpha-\alpha^{-1})/2$ lie in $\QQ(\alpha)$, and the reverse inclusion is clear.
:::

:::

::: {.pf-step #sqrt3}
$\sqrt3\notin\QQ(\sqrt2)$.

::: pf-proof
Suppose $\sqrt3=a+b\sqrt2$ with $a,b\in\QQ$. Squaring gives $3=a^2+2b^2+2ab\sqrt2$, so $2ab=0$ because $\sqrt2\notin\QQ$.
Then $3=a^2$ or $3=2b^2$, and neither has a rational solution.
:::

:::

::: pf-step
$[\QQ(\sqrt2+\sqrt3):\QQ]=\boxed{4}$.

::: pf-proof
$[\QQ(\sqrt2):\QQ]=2$, and by step [](#sqrt3){.pf-ref} $[\QQ(\sqrt2,\sqrt3):\QQ(\sqrt2)]=2$.
The tower law and step [](#generates){.pf-ref} give degree $4$.
Accordingly, $\alpha$ is a root of $x^4-10x^2+1$, which is its minimal polynomial.
:::

:::

:::

:::
