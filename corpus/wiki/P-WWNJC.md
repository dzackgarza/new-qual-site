---
schema: qual/card@1
id: P-WWNJC
kind: problem
title: "Without using the Riesz Representation Theorem, compute"
classification:
  areas:
  - real-analysis
  topics:
  - hilbert-spaces
  - l2
  - norms
relations: []
review: draft
solved: true
---

::: problem
Without using the Riesz Representation Theorem, compute
\[
\sup \left\{\left|\int_{0}^{1} f(x) e^{x} d x\right| \suchthat f \in L^{2}([0,1], m),~~ \|f\|_{2} \leq 1\right\}
\]
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Upper bound: $|\int_0^1 f e^x\,dx| \le \norm{e^x}_{L^2}$ for $\norm{f}_2 \le 1$.
Proof: by Cauchy--Schwarz, \[ \Big|\int_0^1 f(x)e^x\,dx\Big| \le \Big(\int_0^1 |f|^2\Big)^{1/2}\Big(\int_0^1 e^{2x}\,dx\Big)^{1/2} \le 1\cdot \Big(\int_0^1 e^{2x}\,dx\Big)^{1/2} . \] <1>2. The bound is achieved.
Proof: take $f_0(x) = e^x / \norm{e^x}_2$ (so $\norm{f_0}_2 = 1$); then \[ \int_0^1 f_0(x)e^x\,dx = \frac{1}{\norm{e^x}_2}\int_0^1 e^{2x}\,dx = \frac{\norm{e^x}_2^2}{\norm{e^x}_2} = \norm{e^x}_2 . \] <1>3. The supremum equals $\norm{e^x}_2 = \sqrt{(e^2-1)/2}$.
Proof: <1>1 gives the supremum is $\le \norm{e^x}_2$, and <1>2 shows it is attained (so the sup is a max) at $f_0$, giving equality.
Explicitly, \[ \norm{e^x}_2 = \Big(\int_0^1 e^{2x}\,dx\Big)^{1/2} = \Big(\frac{e^2 - 1}{2}\Big)^{1/2} . \] <1>4. Q.E.D.

(Note: this is the Riesz-representation value $\norm{\Lambda}_{L^2\dual}$ for $\Lambda f = \int_0^1 f e^x$, computed directly.)
:::
