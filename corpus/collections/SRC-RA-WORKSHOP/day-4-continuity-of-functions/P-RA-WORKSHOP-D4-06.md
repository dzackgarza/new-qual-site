---
schema: qual/card@1
id: P-RA-WORKSHOP-D4-06
kind: problem
title: Uniform continuity of the logarithm on $(0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Counterexamples
relations: []
review: draft
---

::: {.problem}
(January 2009 #2a, obfuscated) Is $f(x)=\ln x$ uniformly continuous on $(0,1]$?
Prove your answer.
(You may also wish to try the same question with $f(x)=\sin(1/x)$ on $(0,\pi]$.)
:::

:::: {.solution}
> **AI-Generated Solution**

<1>1. $f(x) = \ln x$ is NOT uniformly continuous on $(0,1]$.
Proof: take $x_n = e^{-n}$ and $y_n = e^{-n-1}$.
Then $x_n, y_n \in (0,1]$ and \[|x_n - y_n| = e^{-n-1}(e - 1) \to 0,\] but $|\ln x_n - \ln y_n| = |-n - (-n-1)| = 1$ for all $n$.
Hence for $\epsilon = 1$ (say $\epsilon = 1/2$) there is no $\delta > 0$ working for all pairs; the $\epsilon$-$\delta$ definition of uniform continuity fails.
<1>2. (Suggested variant) $g(x) = \sin(1/x)$ is also NOT uniformly continuous on $(0,\pi]$.
Proof: take $x_n = \frac{1}{\pi/2 + 2\pi n}$ and $y_n = \frac{1}{3\pi/2 + 2\pi n}$.
Both lie in $(0,\pi]$, and $|x_n - y_n| \to 0$, while $g(x_n) = \sin(\pi/2 + 2\pi n) = 1$ and $g(y_n) = \sin(3\pi/2 + 2\pi n) = -1$, so $|g(x_n) - g(y_n)| = 2$ for all $n$.
Not uniformly continuous.
<1>3. Q.E.D.
:::
