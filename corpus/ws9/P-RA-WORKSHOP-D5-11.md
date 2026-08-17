---
schema: qual/card@1
id: P-RA-WORKSHOP-D5-11
kind: problem
title: 'A function vanishing at both endpoints has a large derivative'
classification:
  areas:
  - real-analysis
  topics:
  - mean-value-theorem
  - differentiation
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Assume that $f:[0,1]\to\mathbb R$ is continuous on $[0,1]$ and differentiable on $(0,1)$ with $f(0)=f(1)=0$ and $f(c)=1$ for some $c\in(0,1)$.
Prove that there exists some $s\in(0,1)$ such that $|f'(s)|>2$.
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. If $c \ne 1/2$, use the mean value theorem directly.
Proof: if $c < 1/2$, MVT on $[0,c]$: $f'(s) = \frac{f(c) - f(0)}{c} = \frac{1}{c} > 2$ for some $s \in (0,c)$.
If $c > 1/2$, MVT on $[c,1]$: $f'(s) = \frac{f(1) - f(c)}{1 - c} = -\frac{1}{1-c}$ with $\frac{1}{1-c} > 2$, so $|f'(s)| > 2$.
<1>2. The critical case $c = 1/2$: suppose, toward a contradiction, that $|f'(x)| \le 2$ for all $x \in (0,1)$.
<1>3. $f$ is the tent function on $[0,1/2]$.
Proof: for $0 \le x \le 1/2$, MVT on $[0,x]$ gives $f(x) = f'(\xi)x$ with $|f'(\xi)| \le 2$, so $f(x) \le 2x$; MVT on $[x, 1/2]$ gives $1 - f(x) = f'(\eta)(1/2 - x)$ with $|f'(\eta)| \le 2$, so $f(x) \ge 1 - 2(1/2 - x) = 2x$.
Hence $f(x) = 2x$ for all $x \in [0,1/2]$.
<1>4. $f$ is the tent function on $[1/2,1]$ as well.
Proof: for $1/2 \le x \le 1$, the same argument on $[x,1]$ and $[1/2, x]$ gives $f(x) = 2 - 2x$ for all $x \in [1/2,1]$.
<1>5. Contradiction with differentiability at $1/2$.
Proof: the left derivative of the tent at $1/2$ is $2$ (from $f = 2x$), while the right derivative is $-2$ (from $f = 2-2x$); they differ, so $f$ is not differentiable at $1/2 \in (0,1)$ — contradicting differentiability on $(0,1)$.
Hence $|f'(x)| \le 2$ is impossible, and there is $s \in (0,1)$ with $|f'(s)| > 2$.
<1>6. Q.E.D.
:::
