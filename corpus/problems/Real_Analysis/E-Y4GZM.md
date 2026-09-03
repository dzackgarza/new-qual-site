---
schema: qual/card@1
id: E-Y4GZM
kind: problem
title: Convolution of continuous compactly supported functions is continuous and compactly
  supported
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Continuity
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: exercise
- Show that if $f, g$ are continuous and compactly supported, then so is $f\ast g$.
:::

::: {.solution}
<1>1. $f \ast g$ is continuous.
<2>1. $|f \ast g(x + h) - f \ast g(x)| \le \|g\|_1 \sup_{z}|f(z + h) - f(z)|$.
::: {.proof}
$|f\ast g(x+h) - f\ast g(x)| = \left|\int (f(x + h - y) - f(x - y))g(y)\,dy\right| \le \int |f(x+h-y) - f(x-y)|\,|g(y)|\,dy \le \|g\|_1 \sup_z|f(z+h) - f(z)|$.
:::
<2>2. $\sup_z|f(z + h) - f(z)| \to 0$ as $h \to 0$.
::: {.proof}
$f$ is continuous with compact support, hence uniformly continuous.
:::
<2>3. Q.E.D.
::: {.proof}
<2>1 and <2>2 give $\|f\ast g(\cdot + h) - f\ast g(\cdot)\|_\infty \to 0$, i.e. uniform, hence pointwise, continuity.
:::

<1>2. $f \ast g$ is compactly supported.
<2>1. $\supp(f \ast g) \subseteq \overline{\supp f + \supp g}$.
::: {.proof}
if $x \notin \overline{\supp f + \supp g}$, then $(x - \supp g) \cap \supp f = \emptyset$, so $f(x - y) = 0$ for every $y \in \supp g$ and $f\ast g(x) = 0$.
:::
<2>2. $\overline{\supp f + \supp g}$ is compact.
::: {.proof}
$\supp f + \supp g$ is the image of the compact set $\supp f \times \supp g$ under the continuous map $(a,b) \mapsto a + b$, hence compact (and closed).
:::
<2>3. Q.E.D.
::: {.proof}
<2>1 and <2>2.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
