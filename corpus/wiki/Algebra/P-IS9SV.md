---
schema: qual/card@1
id: P-IS9SV
kind: problem
title: Evaluation makes $A$ a module over $\mathrm{End}(A)$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Rings
  - Homomorphisms
relations: []
review: draft
---

::: problem
For arbitrary $x, y \in A$, we need to check the following:

a. $f\actson (x+y) = f\actson x + f \actson y$
b. $(f+g)\actson x = f \actson x + g \actson x$
c. $f\circ g \actson x = f \actson (g \actson x)$
d. $\id_a \actson x = x$


For (a):
\[
\begin{align*}
f \actson (x + y) &\definedas f(x + y) \\
&= f(x) + f(y)\quad\quad\text{since $f$ is a homomorphism} \\
&= f\actson x + f \actson y \\
.\end{align*}
\]

For (b):
\[
\begin{align*}
(f+g)\actson x &= (f+g)(x) \\
&= f(x) + g(x) \\
&= f \actson x + g \actson x
.\end{align*}
\]

For (c):
\[
\begin{align*}
f\circ g \actson x &= (f\circ g)(x)  \\
&= f(g(x)) \\
&= f \actson g(x) \\
&= f \actson (g \actson x)
.\end{align*}
\]

For (d):
\[
\begin{align*}
\id_A \actson x &= \id_A(x) = x
.\end{align*}
\]
:::
