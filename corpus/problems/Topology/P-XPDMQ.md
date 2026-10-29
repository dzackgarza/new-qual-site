---
schema: qual/card@1
id: P-XPDMQ
kind: problem
title: Maps into $S^n$ that are never antipodal are homotopic
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Degree
relations: []
review: draft
audit:
- event: statement-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source problem block held a worked answer opening 'Main Idea: Exact same idea as 1, just a more complicated check', which refers to a part not on this card; the statement now poses the claim that answer proves, and the title names it instead of the homotopy formula."
---

::: {.problem}
Let $X$ be a topological space and let $f, g\colon X \to S^n$ be continuous maps such that $f(x) \neq -g(x)$ for every $x \in X$.
Show that $f$ and $g$ are homotopic.
:::

::: {.solution}
Let $P(v)=v/\norm{v}$ for $v \in \RR^{n+1}\setminus\{0\}$.

::: pf

::: {.pf-step #nonzero}
For all $x \in X$ and $t \in [0,1]$, $tf(x)+(1-t)g(x) \neq 0$.

::: pf-proof
If $tf(x)+(1-t)g(x)=0$, then taking norms, with $\norm{f(x)} = \norm{g(x)} = 1$, gives $t=1-t$, so $t=1/2$ and $f(x)=-g(x)$, contrary to hypothesis.
:::

:::

::: pf-step
$H(x,t)=P(tf(x)+(1-t)g(x))$ is a homotopy from $g$ to $f$.

::: pf-proof
By step [](#nonzero){.pf-ref}, $H$ is a well-defined continuous map $X \times [0,1] \to S^n$.
Since $f(x), g(x) \in S^n$, normalization fixes them, so $H(x,0)=g(x)$ and $H(x,1)=f(x)$.
:::

:::

:::

:::
