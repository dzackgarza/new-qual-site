---
schema: qual/card@1
id: P-PMDP4
kind: problem
title: "Prove that if $xf(x) \\in L^1(\\RR)$, then $F(y) \\da \\int f(x) \\cos(yx)\\, dx$ defines a $C^1$ function. Fix $y_0$, we'll\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
Prove that if $xf(x) \in L^1(\RR)$, then
\[  
F(y) \da \int f(x) \cos(yx)\,  dx
\]
defines a $C^1$ function.
:::

:::{.solution }

- Fix $y_0$, we'll show $F'$ exists and is continuous at $y_0$.
- Fix a sequence $y_n\decreasesto y_0$ and define
\[
h_n(x) \da 
{ h(x, y_n) - h(x, y_0) \over y_n - y_0} && h(x, y) \da f(x) \cos(yx)
.\]

- We can then write 
\[
\dd{h}{y}(x, y_0) 
= \lim_{n\to \infty} h_n(x)
.\]
- Apply the MVT:
\[
h_n(x) \da { h(x, y_n) - h(x, y_0) \over y_n - y_0}
&= \dd{h}{y}(x, \tilde y) && \text{ for some } \tilde y \in [y_0, y_n]
.\]

- Use this to get a bound for DCT:
\[
\abs{h_n(x)}
&\da \abs{ h(x, y_n) - h(x, y_0) \over y_n - y_0} \\
&= \abs{ \dd{h}{y}(x, \tilde y) } \\
&\leq \sup_{y\in [y_0, y_n]} \abs{ \dd{h}{y}(x, y) } \\
&\leq \sup_{y\in [y_0, y_n]} \abs{ xf(x) \sin(yx) } \\
&\leq \abs{ xf(x) }
,\]
  and by assumption $xf(x) \in L^1$.

- So this justifies commuting an integral and a limit:
\[
F'(y_0) 
&\da \lim_{y_n\to y_0} { F(y_n) - F(y_0) \over y_n - y_0} \\
&= \lim_{n\to 0} \int {h_n(x)  } \dx \\
&\equalsbecause{\text{DCT}} \int \lim_{n\to\infty} h_n(x) \dx \\
&\da \int \dd{h}{y}(x, y_0) \dx \\
&\da - \int xf(x) \sin(yx) \dx 
,\]
and since this limit exists and is finite, $F$ is differentiable at $y_0$.

- That $F$ is continuous:
\[
\lim_{y_n \to y_0} F'(y_n)
&= \lim_{y_n \to y_0} \int \dd{h}{y}(x, y_n) \dx \\
&\equalsbecause{\text{DCT}} \int \lim_{y_n \to y_0} \dd{h}{y}(x, y_n) \dx \\
&= - \int \lim_{y_n \to y_0} xf(x) \sin(y_n x) \dx \\
&= - \int xf(x) \sin(y_0x) \dx 
,\]
where we've used that $y\mapsto \sin(yx)$ is clearly continuous.




:::

