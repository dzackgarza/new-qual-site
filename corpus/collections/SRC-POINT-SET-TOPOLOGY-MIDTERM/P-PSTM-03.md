---
schema: qual/card@1
id: P-PSTM-03
kind: problem
title: A non-Hausdorff quotient of the unit interval
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $X = [0, 1] / \left(\frac14, \frac34\right)$ be the quotient space of the unit interval, where the open interval $\left(\frac14, \frac34\right)$ is identified to a single point.
Show that $X$ is not a Hausdorff space.
:::

::: {.solution}
Write $I = [0,1]$, $A = \left(\frac14, \frac34\right)$, $q\colon I \to X = I/A$ for the quotient map, and $*$ for the point $q(A)$.
A set $U \subseteq X$ is open exactly when $q^{-1}(U)$ is open in $I$.
Let $x = q(\frac14)$ and $y = q(\frac34)$; these are distinct points of $X$, because $\frac14, \frac34 \notin A$.

::: pf

::: {.pf-step #contains-star}
Every open $U \subseteq X$ that contains $x$ or $y$ also contains $*$.

::: pf-proof
If $x \in U$, then $q^{-1}(U)$ is an open subset of $I$ that contains $\frac14$.
So it contains $[\frac14, \frac14 + \varepsilon)$ for some $\varepsilon > 0$, which meets $A$.
A point $a \in A \cap q^{-1}(U)$ gives $* = q(a) \in U$.
The same argument with $(\frac34 - \varepsilon, \frac34]$ applies to $y$.
:::

:::

::: pf-step
$X$ is not Hausdorff.

::: pf-proof
By step [](#contains-star){.pf-ref}, any open $U \ni x$ and $V \ni y$ both contain $*$, so they are not disjoint.
:::

:::

:::
:::
