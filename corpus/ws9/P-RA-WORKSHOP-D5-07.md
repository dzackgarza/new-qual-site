---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-07
kind: problem
title: 'A bounded derivative gives a one-sided limit'
classification:
  areas:
  - real-analysis
  topics:
  - differentiation
  - limits
  - mean-value-theorem
relations: []
review: draft
---

::: {.problem title="?"}
(June 2008 #3a) Prove that if $f'$ exists and is bounded on $(a,b]$, then $$\lim_{x\to a^+}f(x)$$ exists.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $f$ is Lipschitz on $(a,b]$.
    Proof: $|f'| \le M$ on $(a,b]$ for some $M$; by the mean value theorem, for $a < x < y \le b$ there is $\xi \in (x,y)$ with $f(y) - f(x) = f'(\xi)(y-x)$, so $|f(y) - f(x)| \le M|y - x|$.
<1>2. $f$ satisfies the Cauchy criterion as $x \to a^+$.
    Proof: let $\epsilon > 0$ and choose $\delta = \epsilon/(2M)$. For $a < x, y < a + \delta$: $|f(x) - f(y)| \le M|x - y| < M\delta = \epsilon/2 < \epsilon$.
<1>3. Conclude the limit exists.
    Proof: by the Cauchy criterion for functions (a real-valued function satisfies the Cauchy condition at $a^+$ iff its limit exists there — e.g. take a sequence $x_n \searrow a$; $(f(x_n))$ is Cauchy by <1>2, so it converges, and the limit is independent of the sequence by the Lipschitz bound), $\lim_{x\to a^+} f(x)$ exists (in $\mathbb{R}$).
<1>4. Q.E.D.
:::
