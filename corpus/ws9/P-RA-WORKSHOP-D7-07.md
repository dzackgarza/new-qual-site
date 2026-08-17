---
schema: qual/card@1
id: P-RA-WORKSHOP-D7-07
kind: problem
title: 'Equicontinuity of the family $x/(1+nx^2)$ on compact intervals'
classification:
  areas:
  - real-analysis
  topics:
  - equicontinuity
  - convergence-of-functions
relations: []
review: draft
---

::: {.problem title="?"}
(January 2008 #5a) Let $$f_n(x)=\frac{x}{1+nx^2}$$ for $n\in\mathbb N$.
Let $\mathcal F=\{f_n:n=1,2,3,\ldots\}$ and let $[a,b]$ be any compact subset of $\mathbb R$.
Is $\mathcal F$ equicontinuous?
Justify your answer.
:::

:::: {.solution}
> **AI-Generated Solution**
**Goal:** Decide whether $\mathcal F = \{f_n(x) = x/(1+nx^2)\}$ is equicontinuous on a compact interval $[a,b] \subset \mathbb R$.

<1>1. Yes, $\mathcal F$ is equicontinuous on every $[a,b]$.
    <2>1. Each $f_n$ is differentiable with $|f_n'(x)| \le 1$ for all $x \in \mathbb R$.
        Proof: $f_n'(x) = \frac{1 - nx^2}{(1+nx^2)^2}$. Writing $t = \sqrt n\,|x|$, we get $|f_n'(x)| = \frac{|1 - t^2|}{(1+t^2)^2}$. For $t \le 1$ this is $\le 1$; for $t \ge 1$, $|1-t^2| = t^2 - 1 < t^2 + 1$, so $\frac{t^2-1}{(t^2+1)^2} < \frac{1}{t^2+1} \le \frac12$. Hence $|f_n'| \le 1$ everywhere.
    <2>2. $|f_n(x) - f_n(y)| \le |x - y|$ for all $n$ and all $x, y$.
        Proof: the Mean Value Theorem applied to $f_n$ on the interval between $x$ and $y$, using <2>1.
    <2>3. Given $\varepsilon > 0$, choose $\delta = \varepsilon$; then $|x-y| < \delta$ forces $|f_n(x) - f_n(y)| < \varepsilon$ for every $n$ simultaneously.
        Proof: by <2>2, $|f_n(x) - f_n(y)| \le |x-y| < \delta = \varepsilon$. The choice of $\delta$ is independent of $n$ and of the points, so the family is equicontinuous (indeed uniformly equicontinuous on any $[a,b]$).
    <2>4. Q.E.D.
        Proof: <2>3 is equicontinuity of $\mathcal F$ on $[a,b]$.

:::
