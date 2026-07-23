---
schema: qual/card@1
id: P-6BURM
kind: problem
title: "Let $n\\in \\ZZ^{\\geq 0}$ and show that the equation"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $n\in \ZZ^{\geq 0}$ and show that the equation
\[
e^z = az^n
\]
has $n$ solutions in the open unit disc if $\abs{a} > e$, and no solutions if $\abs{a} < {1\over e}$.

:::

:::{.solution}
Note that $\abs{e^z} = e^{\Re(z)}$, which is maximizes on $S^1$ at $z=1 \in \RR$ and minimized at $z=-1$.
Write $f(z) = e^z-az^n$, so solution correspond to zeros of $f$.

Case 1: suppose $\abs{a} > e$.
Big: $M(z) = az^n$.
Small: $m(z) = e^z$.
On $\abs{z} = 1$,
\[
\abs{m(z)} = \abs{e^z} = e^\Re(z) \leq e^1 < \abs{a} = \abs{az^n} = \abs{M(z)}
,\]
so $f$ has $\size Z_M = n$ zeros.

Case 2: suppose $\abs{a} < 1/e$.
Big: $M(z) = e^z$.
Small: $m(z) = az^n$.
On $\abs{z} = 1$,
\[
\abs{m(z)} = \abs{az^n} = \abs{a} < e\inv \leq e^{\Re(z)} = \abs{e^z} = \abs{M(z)}
,\]
and $M$ has no zeros in $\DD$ (and in fact none in $\CC$), so neither does $f$.
:::

