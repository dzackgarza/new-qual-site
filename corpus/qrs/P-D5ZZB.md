---
schema: qual/card@1
id: P-D5ZZB
kind: problem
title: "Define"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Define
\[
f(x) = \sum_{n=1}^{\infty} \frac{1}{n^{x}}.
\] 
Show that $f$ converges to a differentiable function on $(1, \infty)$ and that
\[
f'(x)  =\sum_{n=1}^{\infty}\left(\frac{1}{n^{x}}\right)^{\prime}.
\]

> Hint:
\[
\left(\frac{1}{n^{x}}\right)' = -\frac{1}{n^{x}} \ln n
\]

:::{.solution}
\envlist
:::{.concept}
\envlist
- ?
:::

- Set $f_N(x) \definedas \sum_{n=1}^N n^{-x}$, so $f(x) = \lim_{N\to\infty} f_N(x)$.
- If an interchange of limits is justified, we have
\[  
\dd{}{x} \lim_{N\to\infty} \sum_{n=1}^N n^{-x}
&= \lim_{h\to 0} \lim_{N\to\infty} {1\over h} \left[ \qty{\sum_{n=1}^N n^{-x}} - \qty{\sum_{n=1}^N n^{-(x+h)} }\right] \\
&\eq_{?} \lim_{N\to\infty} \lim_{h\to 0} {1\over h} \left[ \qty{\sum_{n=1}^N n^{-x}} - \qty{\sum_{n=1}^N n^{-(x+h)} }\right] \\
&= \lim_{N\to\infty} \lim_{h\to 0} {1\over h} \left[ {\sum_{n=1}^N n^{-x}} - {n^{-(x+h)} }\right] \quad\text{(1)} \\
&= \lim_{N\to\infty} \sum_{n=1}^N \lim_{h\to 0} {1\over h} \left[ n^{-x} - n^{-(x+h)} \right] \quad\text{since this is a finite sum} \\
&\definedas \lim_{N\to\infty} \sum_{n=1}^N \dd{}{x}\qty{1 \over n^x} \\ 
&= \lim_{N\to\infty} \sum_{n=1}^N -{\ln(n) \over n^x}
,\]
  where the combining of sums in (1) is valid because $\sum n^{-x}$ is absolutely convergent for $x>1$ by the $p\dash$test.

- Thus it suffices to justify the interchange of limits and show that the last sum converges on $(1, \infty)$.

- Claim: $\sum n^{-x}\ln(n)$ converges.
  - Use the fact that for any fixed $\eps>0$,
  \[  
  \lim_{n\to\infty} {\ln(n) \over n^\eps} 
  \eq^{L.H.} \lim_{n\to\infty}{1/n \over \eps n^{\eps-1}} 
  = \lim_{n\to\infty} {1\over \eps n^\eps} = 0
  ,\]
  - This implies that for a fixed $\eps >0$ and for any constant $c>0$ there exists an $N$ large enough such that $n\geq N$ implies $\ln(n)/n^\eps < c$, i.e. $\ln(n) < c n^{\eps}$.
  - Taking $c=1$, we have $n\geq N \implies \ln(n) < n^\eps$
  - We thus break up the sum:
  \[  
  \sum_{n\in \NN} {\ln(n) \over n^x} 
  &= \sum_{n=1}^{N-1} { \ln(n) \over n^x} + \sum_{n=N}^\infty {\ln(n) \over n^x} \\
  &\leq \sum_{n=1}^{N-1} { \ln(n) \over n^x} + \sum_{n=N}^\infty {n^\eps \over n^x} \\
  &\definedas C_\eps + \sum_{n=N}^\infty {n^\eps \over n^x} \quad \text{with $C_\eps<\infty$ a constant}\\
  &= C_\eps + \sum_{n=N}^\infty {1 \over n^{x-\eps}}
  ,\]
  where the last term converges by the $p\dash$test if $x-\eps > 1$.

  - But $\eps$ can depend on $x$, and if $x\in (1, \infty)$ is fixed we can choose $\eps < \abs{x-1}$ to ensure this. 

- Claim: the interchange of limits is justified.

:::

