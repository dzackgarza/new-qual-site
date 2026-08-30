---
schema: qual/card@1
id: P-T6YA3
kind: problem
title: The $R/(p)$-module structure on $A/pA$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Vector Spaces
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Since $R/(p)$ is a field, we just need to show that $A/pA \actson R/(p)$ defines a module.

$r\cdot(x + y) = rx + ry$:
\[
\begin{align*}
r + (p) \actson x + pA \oplus y + pA &\definedas r + (p) \actson x + y + pA \\
&\definedas r(x+y) + pA \\
&= rx + ry + pA \\
&\definedas rx + pA \oplus ry + pA \\
&\definedas r\actson x + pA \oplus r \actson y + pA
.\end{align*}
\]

$(r + s)\cdot x = rx + sx$:
\[
\begin{align*}
r + (p) \oplus s + (p) \actson x + pA &\definedas
r + s + (p) \actson x + pA \\
&\definedas (r+s)x + pA \\
&= rx + sx + pA \\
&\definedas rx + pA \oplus sx + pA \\
&\definedas r+(p) \actson x + pA \oplus s+(p) \actson x + pA
.\end{align*}
\]

$rs\cdot x = r\cdot (s\cdot x)$:
\[
\begin{align*}
r+ (p) \cdot s + (p) \actson  x + pA &\definedas rs + (p) \actson x + pA \\
&= rsx + pA \\
&\definedas r + (p) \actson sx + pA \\
&\definedas r + (p) \actson s + (p) \actson x + pA
.\end{align*}
\]

$1\cdot x = x$:
\[
\begin{align*}
1_R + (p) \actson x + pA &= 1_R x + pA = x + pA
.\end{align*}
\]
:::

::: {.solution}
<1>1. $G$ group.
Proof: Sylow.

<1>2. Q.E.D.
Proof: <1>1.
:::
