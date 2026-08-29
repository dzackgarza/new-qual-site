---
schema: qual/card@1
id: D-HHVPT
kind: definition
title: Continuity and Uniform Continuity
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Uniform Continuity
relations: []
review: draft
---

:::{.definition}
A function $f: \RR\to \RR$ is **continuous** on $X$ iff for all $x_0\in X$,
\[
&\forall \varepsilon \quad \exists \delta(\varepsilon, x_0) \text{ such that }\quad \forall y, \abs{x_0 - y} < \delta &&\implies \abs{f(x_0) - f(y)} < \varepsilon \\
\iff &\forall \varepsilon \quad \exists \delta(\varepsilon, x_0) \text{ such that }\quad \forall h, \abs{h} < \delta &&\implies \abs{f(x_0) - f(x_0 \pm h)} < \varepsilon
.\]

$f$ is **uniformly continuous** on $X$ iff

\[
  &\forall \varepsilon \quad \exists \delta(\varepsilon) \text{ such that }\quad \forall x, y, \in X \quad \abs{x - y} < \delta &&\implies \abs{f(x) - f(y)} < \varepsilon \\
\iff &\forall \varepsilon \quad \exists \delta(\varepsilon) \text{ such that} \quad \, \forall x, h, \quad \abs{h} < \delta &&\implies \abs{f(x) - f(x \pm h)} < \varepsilon
.\]
These follow from the substitutions $x_0-y = \mp h \implies y = x_0 \pm h$.
:::
