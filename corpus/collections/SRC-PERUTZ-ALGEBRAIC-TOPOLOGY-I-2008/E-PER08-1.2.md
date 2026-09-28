---
schema: qual/card@1
id: E-PER08-1.2
kind: problem
title: Equivalent characterizations of contractibility
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 1.2 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified all four implications, including the every-point clause by extracting paths from a contraction homotopy.
---

::: {.problem}
Let $X$ be a nonempty space.
Show that the following conditions are equivalent:

1. $X$ is homotopy equivalent to a one-point space.

2. For every $x\in X$, the inclusion $\{x\}\hookrightarrow X$ is a homotopy equivalence.

3. For some $x\in X$, the inclusion $\{x\}\hookrightarrow X$ is a homotopy equivalence.

4. For some $x\in X$, the constant map $c_x:X\to X$ is homotopic to $\operatorname{id}_X$.
:::

::: {.solution}
For $x\in X$, let
\[
i_x:\{x\}\hookrightarrow X
\]
be the inclusion and let
\[
r_x:X\to\{x\}
\]
be the unique map.

<1>1. For a fixed $x\in X$, $i_x$ is a homotopy equivalence if and only if $c_x\simeq\operatorname{id}_X$.
::: {.proof}
We always have
\[
r_xi_x=\operatorname{id}_{\{x\}}
\]
and
\[
i_xr_x=c_x.
\]
Thus $r_x$ is a homotopy inverse for $i_x$ exactly when
\[
c_x=i_xr_x\simeq\operatorname{id}_X.
\]
:::

<1>2. Condition 3 is equivalent to condition 4.
::: {.proof}
This is immediate from <1>1 after choosing the point whose existence is asserted in either condition.
:::

<1>3. Condition 3 implies condition 1.
::: {.proof}
If $i_x:\{x\}\to X$ is a homotopy equivalence, then $X$ is homotopy equivalent to the one-point space $\{x\}$.
:::

<1>4. Condition 1 implies condition 4.
::: {.proof}
Let $\ast$ be a one-point space and suppose
\[
f:X\to\ast
\]
is a homotopy equivalence with homotopy inverse
\[
g:\ast\to X.
\]
Write $x_0=g(\ast)$. Since $f$ is the unique map from $X$ to $\ast$,
\[
gf=c_{x_0}.
\]
The homotopy-inverse relation gives
\[
gf\simeq\operatorname{id}_X,
\]
so
\[
c_{x_0}\simeq\operatorname{id}_X.
\]
Thus condition 4 holds.
:::

<1>5. Condition 4 implies condition 2.
::: {.proof}
Assume that for some $x_0\in X$ there is a homotopy
\[
H:[0,1]\times X\to X
\]
from $c_{x_0}$ to $\operatorname{id}_X$.

Fix any $x\in X$. Evaluating $H$ at $x$ gives a path
\[
p_x(t):=H(t,x)
\]
from $x_0$ to $x$. Hence
\[
K_x(t,y):=p_x(t)
\]
defines a homotopy from $c_{x_0}$ to $c_x$. Therefore
\[
c_x\simeq c_{x_0}\simeq\operatorname{id}_X.
\]
By <1>1, the inclusion $i_x:\{x\}\hookrightarrow X$ is a homotopy equivalence. Since $x$ was arbitrary, condition 2 holds.
:::

<1>6. Condition 2 implies condition 3.
::: {.proof}
Because $X$ is nonempty, choose $x\in X$. Condition 2 says in particular that $i_x$ is a homotopy equivalence, which is condition 3.
:::

The implications
\[
(1)\Rightarrow(4)\Rightarrow(2)\Rightarrow(3)\Rightarrow(1)
\]
from <1>3--<1>6 show that all four conditions are equivalent.
:::
