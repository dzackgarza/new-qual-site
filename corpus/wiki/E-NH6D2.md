---
schema: qual/card@1
id: E-NH6D2
kind: exercise
title: "The equality case"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="The equality case"}
Suppose $f:\DD\to \DD$ and $f(0) = 0$.
Show that
\[
\abs{f(z) + f(-z)} \leq 2\abs{z}^2
,\]
with equality only if $f(z) = \lambda z^2$ for some $\abs{\lambda} = 1$.

#complex/exercise/completed

:::

:::{.solution}
Define $F(z) \da { f(z) + f(-z) \over 2 z^2}$, then $F(0) = 0$ and thus Schwarz applies and yields the desired inequality.
If $\abs{F(z)} = \abs{z}$ for any $z$, then $F(z) = \lambda z^2$ is a rotation and $f(z) + f(-z) = \lambda z$.
Noting that $F$ is an even function, $f(z) = \lambda z^2 + f_o(z)$ for $f_o$ some odd function.

:::{.claim}
$f_0$ is identically zero.
:::

Given this, the result follows immediately since $f(z) = \lambda z^2$.

:::{.proof title="of claim"}
Note that on the LHS, $\abs{ f(re^{it})} \to 1$ as $r\to 1$ for any $t$.
So this must be true on the RHS, and the first term $\lambda \abs{ re^{it}}^2 \to 1$, forcing $\abs{h(re^{it})} \to 0$.
So $h\equiv 0$ on $\abs{z} = 1$, and by the MMP, $\abs{h} = 0$ in $\DD$, making $h\equiv 0$ on $\DD$.
:::

:::
