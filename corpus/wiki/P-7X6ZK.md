---
schema: qual/card@1
id: P-7X6ZK
kind: problem
title: "$\\displaystyle \\int_{0}^{\\pi} \\sqrt {1 + \\cos (2x)} ~dx= \\color {blue} {2\\sqrt {2}}$ Solution: $\\sqrt {1 + \\cos (2x)} = \\sqrt {2 \\cos ^2 (x)} = \\sqrt {2} \\cos (x)$"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - trigonometry
relations: []
review: draft
solved: true
---

::: problem
1. $\displaystyle \int_{0}^{\pi} \sqrt {1 + \cos (2x)} ~dx= \color {blue} {2\sqrt {2}}$

- **Solution:** $\sqrt {1 + \cos (2x)} = \sqrt {2 \cos ^2 (x)} = \sqrt {2} \cos (x)$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Evaluate the definite integral $\int_{0}^{\pi} \sqrt{1 + \cos(2x)} \, dx$.

<1>1. Trigonometric simplification: For all $x \in [0, \pi]$, $1 + \cos(2x) = 2\cos^2(x)$, hence $\sqrt{1 + \cos(2x)} = \sqrt{2}|\cos(x)|$.
Proof: By the cosine double-angle formula $\cos(2x) = 2\cos^2(x) - 1$.
Taking the principal square root gives $\sqrt{2\cos^2(x)} = \sqrt{2}\sqrt{\cos^2(x)} = \sqrt{2}|\cos(x)|$.

<1>2. Partitioning the integral over intervals of constant sign of $\cos(x)$: $$\int_0^\pi |\cos(x)| \, dx = \int_0^{\pi/2} \cos(x) \, dx + \int_{\pi/2}^\pi (-\cos(x)) \, dx.$$ Proof: <2>1. On $[0, \pi/2]$, $\cos(x) \ge 0 \implies |\cos(x)| = \cos(x)$.
<2>2. On $[\pi/2, \pi]$, $\cos(x) \le 0 \implies |\cos(x)| = -\cos(x)$.

<1>3. Computing each piece: Proof: <2>1. $\int_0^{\pi/2} \cos(x) \, dx = [\sin(x)]_0^{\pi/2} = \sin(\pi/2) - \sin(0) = 1 - 0 = 1$.
<2>2. $\int_{\pi/2}^\pi (-\cos(x)) \, dx = [-\sin(x)]_{\pi/2}^\pi = -\sin(\pi) - (-\sin(\pi/2)) = 0 + 1 = 1$.
<2>3. Thus $\int_0^\pi |\cos(x)| \, dx = 1 + 1 = 2$.

<1>4. Conclusion: $$\int_0^\pi \sqrt{1+\cos(2x)} \, dx = \sqrt{2} \int_0^\pi |\cos(x)| \, dx = 2\sqrt{2}.$$ Proof: By <1>1 and <1>3. Q.E.D.
:::
