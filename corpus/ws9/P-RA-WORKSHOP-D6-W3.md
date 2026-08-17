---
schema: qual/card@1
id: P-RA-WORKSHOP-D6-W3
kind: problem
title: 'Epsilon-delta continuity and differentiability of an integral of $1/t$'
classification:
  areas:
  - real-analysis
  topics:
  - continuity
  - differentiation
  - integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
(January 2007 #1) Let $$f(x)=\int_1^x\frac1t\,dt$$ for $x>0$.
(a) Use an $\epsilon$-$\delta$ proof to show that $f$ is continuous on $(0,\infty)$.
(b) Use an $\epsilon$-$\delta$ proof to show that $f$ is differentiable on $(0,\infty)$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. (a) $f$ is continuous on $(0,\infty)$.
Proof: fix $x_0 > 0$ and $\epsilon > 0$.
For $x$ in the neighborhood $|x - x_0| < x_0/2$ (so $x > x_0/2$), $1/t \le 2/x_0$ for $t$ between $x$ and $x_0$, and \[|f(x) - f(x_0)| = \left|\int_{x_0}^x \frac{dt}{t}\right| \le \frac{2}{x_0}|x - x_0|.\] Choose $\delta = \min(x_0/2,\ \epsilon x_0/2)$; then $|x - x_0| < \delta$ gives $|f(x) - f(x_0)| < \epsilon$.
<1>2. (b) $f$ is differentiable on $(0,\infty)$ with $f'(x) = 1/x$.
Proof: fix $x > 0$ and consider the difference quotient; for $h \ne 0$ with $|h| < x/2$, \[\frac{f(x+h) - f(x)}{h} = \frac{1}{h}\int_x^{x+h}\frac{dt}{t}.\] Since $1/t$ is continuous at $x$, for every $\epsilon > 0$ there is $\delta < x/2$ with $|1/t - 1/x| < \epsilon$ for $|t - x| < \delta$.
For $0 < |h| < \delta$, \[\left|\frac{1}{h}\int_x^{x+h}\frac{dt}{t} - \frac{1}{x}\right| = \left|\frac{1}{h}\int_x^{x+h}\left(\frac{1}{t} - \frac{1}{x}\right)dt\right| \le \frac{1}{|h|}\int_x^{x+h}\left|\frac{1}{t} - \frac{1}{x}\right|dt \le \epsilon.\] Hence the quotient tends to $1/x$, so $f'(x) = 1/x$.
<1>3. Q.E.D.
:::
