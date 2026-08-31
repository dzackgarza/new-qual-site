---
schema: qual/card@1
id: P-XRNHW
kind: problem
title: The bound $\int_F|x-y|^{-2}\,dx\leq 2/\delta_F(y)$, with $I(x)=\int\delta_F(y)/|x-y|^2\,dy$
  infinite off $F$ and finite a.e. on $F$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Integrals
  - Fubini-Tonelli
relations: []
review: draft
---

:::{.problem}
a.
Let $F \subset \mathbb{R}$ be closed, and define
\[
\delta_{F}(y):=\inf _{x \in F}|x-y| .
\]
For $y \notin F$, show that
\[
\int_{F}|x-y|^{-2} d x \leq \frac{2}{\delta_F(y)},
\]
b.
Let $F \subset \mathbb{R}$ be a closed set whose complement has finite measure, i.e. $m(\RR \sm F)< \infty$. 
Define the function
\[
I(x):=\int_{\mathbb{R}} \frac{\delta_{F}(y)}{|x-y|^{2}} d y
\]
Prove that $I(x)=\infty$ if $x \not\in F$, however $I(x)<\infty$ for almost every $x \in F$. 

  > Hint: investigate $\int_{F} I(x) d x$.

:::

:::{.solution title="Part a"}
Let $y\in F^c$ which is open, then one can find an epsilon ball about $y$ avoiding $F$.
We can take $\eps \da \delta_F(y)$ to define $A \da B_{\eps}(y)$, and we still have $A \subseteq F^c$ and $F \subseteq A^c$.
Note that $\abs{x-y}^2 = (x-y)^2$ since this is always positive, then
\[
\int_F \abs{x-y}^{-2} \dx 
&\leq \int_{A^c} \abs{x-y}^{-2} \dx \\
&= \int_{-\infty}^{-\eps} \qty{x-y}^{-2} \dx + \int_{\eps}^{\infty} \qty{x-y}^{-2}\dx \\
&= \int_{-\infty}^{-\eps} u^{-2} \dx + \int_{\eps}^{\infty} u^{-2} \dx \\
&= -u\inv \evalfrom_{u=-\eps}^{u=-\infty}- u\inv\evalfrom_{u=\infty}^{u=\eps} \\
&= {2\over \eps} \\
&\da {2\over \delta_F(y)}
.\]
:::

:::{.solution title="Part b"}
Estimate:
\[
\int_F I(x) \dx 
&\da \int_F \int_\RR {\delta_F(y) \over (x-y)^2 } \dy \dx \\
&= \int_\RR \delta_F(y) \int_F {1\over (x-y)^2} \dx \dy \\
&= \int_F \delta_F(y) \int_F {1\over (x-y)^2} \dx \dy + \int_{F^c} \delta_F(y) \int_F {1\over (x-y)^2} \dx \dy \\
&= 0 + \int_{F^c} \delta_F(y) \int_F {1\over (x-y)^2} \dx \dy \\
&\leq
\int_{F^c} 2 \dy \\
&= 2\mu(F^c) \\
&<\infty
,\]
where we've used that $y\in F\implies \delta_F(y) = 0$ and applied the bound from the first part.
We've also implicitly used Fubini-Tonelli to change the order of integration, justified by positivity of the integrand and the finite iterated integral.
This forces $I(x) < \infty$ for almost every $x\in F$, since if $I(x)$ is unbounded on any positive measure set then this integral would diverge.

If $x\not\in F$, then since $F$ is closed, $F^c$ is open, so there is $r > 0$ with $B_r(x) \subseteq F^c$; in fact $\delta_F(x) = d(x, F) > 0$, and we take $r = \delta_F(x)/2$.
For $y \in B_r(x)$, the distance from $y$ to $F$ is at least $\delta_F(x) - |x - y| \ge \delta_F(x) - r = r$ (by the triangle inequality, $d(y, F) \ge d(x, F) - |x - y|$).
Therefore
\[
I(x) = \int_\RR \frac{\delta_F(y)}{|x-y|^2}\,dy
\ge \int_{B_r(x)} \frac{\delta_F(y)}{|x-y|^2}\,dy
\ge \int_{B_r(x)} \frac{r}{|x-y|^2}\,dy
= r \cdot 2\int_0^r \frac{1}{t^2}\,dt = \infty,
\]
since $\int_0^r t^{-2}\,dt = \infty$ (the singularity at $t = 0$ is non-integrable).
Hence $I(x) = \infty$ for every $x \notin F$.

:::


