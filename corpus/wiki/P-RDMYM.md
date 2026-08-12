---
schema: qual/card@1
id: P-RDMYM
kind: problem
title: "Let $f, g \\in L^1(\\RR)$ be Borel measurable. Show that The function $F(x, y) \\definedas f(x-y) g(y)$ is Borel\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Let $f, g \in L^1(\RR)$ be Borel measurable.

- Show that 
  - The function $$F(x, y) \definedas f(x-y) g(y)$$ is Borel measurable on $\RR^2$, and
  - For almost every $x\in \RR$, the function $f(x-y)g(y)$ is integrable with respect to $y$ on $\RR$.

- Show that $f\ast g \in L^1(\RR)$ and
\[
\|f * g\|_{1} \leq \|f\|_{1} \|g\|_{1}
\]
:::

:::{.solution .foldopen}
\envlist

- $F \in \mcb(\RR^2)$:
  - Write a function $\tilde f(x, y) \da f(x)$
  - Write a linear transformation $T = \matt 1 0 0 {-1} \in \GL_2$, so $T\tv{x, y} = \tv{x-y, 0}$
  - Write $f(x-y) \da (\tilde f \circ T)(x, y)$, which is a composition of measurable functions and thus measurable.
  - A product of measurable functions is measurable.


- $f\convolve g \in L^1(\RR)$: estimate
\[
\int \abs{ f\convolve g} d\mu 
&= \int_\RR \int_\RR \abs{f(x-y)g(y)}\dx \dy \\
&= \int_\RR \int_\RR \abs{f(x-y)}\abs{g(y)}\dx \dy \\
&= \int_\RR \abs{g(y)} \int_\RR \abs{f(x-y)}\dx \dy \\
&= \norm{g}_1 \norm{f}_1
,\]
where we've used translation invariance of the $L^1$ norm and Fubini-Tonelli justified by the finite result.

- $F_x(y) \da f(x-y)g(y)$ is integrable with respect to $y$ for almost every $x$:
  - This follows from Fubini-Tonelli, which says that if $F(x, y)$ is integrable, the slices $F^x(y)$ are integrable for almost every $x$.
  Here take $F(x, y) \da f(x-y)g(y)$.

:::

