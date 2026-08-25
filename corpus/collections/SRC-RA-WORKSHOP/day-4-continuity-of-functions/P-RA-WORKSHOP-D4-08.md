---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-08
kind: problem
title: Continuity and uniform continuity of a rational function
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Uniform Continuity
relations: []
review: draft
---

::: {.problem}
(June 2009 #1) Give an $\epsilon$-$\delta$ proof that $$f(x)=\frac{x^2}{1-x^2}$$ is continuous on $(0,1)$.
Is $f$ uniformly continuous on $(0,1)$?
Prove your answer.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $f(x) = \frac{x^2}{1 - x^2}$ is continuous on $(0,1)$.
Proof: fix $a \in (0,1)$ and $\epsilon > 0$.
The function $x \mapsto 1 - x^2$ is continuous and $1 - a^2 > 0$, so pick $\delta_1 > 0$ with $|x - a| < \delta_1$ implying $1 - x^2 > \frac{1 - a^2}{2}$ (hence the denominator stays bounded away from $0$). On the neighborhood $|x-a| < \delta_1$, the numerator $x^2$ is bounded by $(a + \delta_1)^2$, and the difference \[\left|\frac{x^2}{1-x^2} - \frac{a^2}{1-a^2}\right| = \frac{|x^2 - a^2|}{(1-x^2)(1-a^2)}\] satisfies $|x^2 - a^2| \le |x-a|\cdot 2(a + \delta_1)$, so choosing $\delta = \min\big(\delta_1, \frac{\epsilon(1-a^2)^2}{4(a+\delta_1)}\big)$ gives $|f(x) - f(a)| < \epsilon$ whenever $|x - a| < \delta$.
Hence $f$ is continuous at every $a \in (0,1)$.
<1>2. $f$ is NOT uniformly continuous on $(0,1)$.
Proof: take $x_n = 1 - \frac{1}{n}$ and $y_n = 1 - \frac{1}{2n}$ (so $y_n < x_n < 1$). Then $|x_n - y_n| = \frac{1}{2n} \to 0$, but \[f(x_n) = \frac{(1 - 1/n)^2}{1 - (1 - 1/n)^2} \sim \frac{1}{2/n} = \frac{n}{2} \to \infty, \quad \text{and similarly } f(y_n) \to \infty,\] so $|f(x_n) - f(y_n)| \to \infty \not\to 0$.
No $\delta$ can control pairs $(x_n, y_n)$ with $|x_n - y_n| \to 0$, so $f$ is not uniformly continuous.
(Equivalently, a uniformly continuous function on a bounded interval is bounded — here $f$ is unbounded near $1$.)
<1>3. Q.E.D.
:::
