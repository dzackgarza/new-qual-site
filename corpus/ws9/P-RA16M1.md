---
schema: qual/card@1
id: P-RA16M1
kind: problem
title: 'UGA analysis qualifying exam, May 2016, problem 1'
classification:
  areas:
  - real-analysis
  topics:
  - continuity
  - uniform-continuity
relations: []
review: draft
---

:::{.problem title="?"}
Consider the function
$$f(x)=\frac{x}{1-x^2},\qquad x\in(0,1).$$

(a) By using the $\varepsilon$-$\delta$ definition of the limit only, prove that $f$ is continuous on $(0,1)$.
(Note: You are not allowed to trivialize the problem by using properties of limits.)

(b) Is $f$ uniformly continuous on $(0,1)$? Justify your answer.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** (a) Prove $f(x) = \frac{x}{1-x^2}$ is continuous on $(0,1)$ using only the $\varepsilon$-$\delta$ definition; (b) decide uniform continuity on $(0,1)$.

<1>1. (a) Fix $x_0 \in (0,1)$ and $\varepsilon > 0$.
    <2>1. Difference quotient identity: $f(x) - f(x_0) = \frac{(x - x_0)(1 + x_0x)}{(1-x^2)(1-x_0^2)}$.
        Proof: $f(x) - f(x_0) = \frac{x(1-x_0^2) - x_0(1-x^2)}{(1-x^2)(1-x_0^2)} = \frac{x - xx_0^2 - x_0 + x_0x^2}{(1-x^2)(1-x_0^2)} = \frac{(x-x_0)(1+x_0x)}{(1-x^2)(1-x_0^2)}$.
    <2>2. Localize: set $b := \frac{1+x_0}{2} \in (x_0, 1)$ and $\delta_0 := \min(x_0/2, (1-x_0)/2) > 0$; then $|x - x_0| < \delta_0 \Rightarrow x \in [x_0/2, b] \subset (0,1)$.
        Proof: $x > x_0 - \delta_0 \ge x_0 - x_0/2 = x_0/2$ and $x < x_0 + \delta_0 \le x_0 + (1-x_0)/2 = (1+x_0)/2 = b$.
    <2>3. On this neighborhood, $|1 + x_0x| \le 1 + x_0b$ and $1 - x^2 \ge 1 - b^2 > 0$; also $1 - x_0^2 > 0$.
        Proof: $x \le b < 1$ gives $x_0x \le x_0b$ and $x^2 \le b^2$, so $1 - x^2 \ge 1 - b^2 > 0$ since $b < 1$.
    <2>4. Hence $|f(x) - f(x_0)| \le C|x - x_0|$ for $C := \frac{1 + x_0b}{(1-b^2)(1-x_0^2)}$, a constant depending only on $x_0$.
        Proof: from <2>1 and <2>3, $|f(x) - f(x_0)| = |x-x_0|\frac{|1+x_0x|}{(1-x^2)(1-x_0^2)} \le |x-x_0|\frac{1+x_0b}{(1-b^2)(1-x_0^2)}$.
    <2>5. Choose $\delta := \min(\delta_0, \varepsilon/C)$; then $|x - x_0| < \delta \Rightarrow |f(x) - f(x_0)| \le C|x - x_0| < C\delta \le \varepsilon$.
        Proof: <2>2 gives $x$ in the localized range (so <2>4 applies) and <2>4 gives the Lipschitz bound.
    <2>6. Q.E.D.
        Proof: <2>5 is the $\varepsilon$-$\delta$ condition at $x_0$; $x_0 \in (0,1)$ was arbitrary, so $f$ is continuous on $(0,1)$.

<1>2. (b) $f$ is NOT uniformly continuous on $(0,1)$.
    <2>1. $f$ is unbounded on $(0,1)$: $f(x) \to +\infty$ as $x \to 1^-$.
        Proof: $1 - x^2 = (1-x)(1+x) \le 2(1-x)$, so $f(x) = \frac{x}{1-x^2} \ge \frac{x}{2(1-x)} \to +\infty$ as $x \to 1^-$.
    <2>2. A uniformly continuous function on a bounded interval is bounded.
        Proof: uniform continuity with $\varepsilon = 1$ gives $\delta > 0$ with $|x-y| < \delta \Rightarrow |f(x) - f(y)| < 1$; $(0,1)$ is covered by finitely many $\delta$-balls, along which $f$ changes by at most $1$ each, so $|f|$ is bounded.
    <2>3. Q.E.D.
        Proof: <2>1 contradicts <2>2; hence $f$ is not uniformly continuous on $(0,1)$.

:::
