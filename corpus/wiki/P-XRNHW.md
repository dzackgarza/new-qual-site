---
schema: qual/card@1
id: P-XRNHW
kind: problem
title: "Let $F \\subset \\mathbb{R}$ be closed, and define $\\delta_{F}(y):=\\inf _{x \\in F}|x-y|$ For $y \\notin F$, show that $\\int_{F}|x-y|^{-2} d x \\leq \\frac{2}{\\delta_F(y)}$ Let $F \\subset \\mathbb{R}$ be a\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.problem title="?"}
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

If $x\not\in F$, pick an $\eps\dash$ball $A$ about $x$ avoiding $F$ so that $\abs{x-y}> \eps$ for any $y\in A^c$ and thus $(x-y)^{-2} \leq \eps^{-2}$.
Note that $\delta_F(y)\geq \eps$, so
\[
I(x) 
&= \int_\RR\delta_F(y) (x-y)^{-2} \dy \\
&\geq \int_{A^c} \delta_F(y) (x-y)^{-2} \dy \\
&\geq \int_{A^c} \delta_F(y) \eps^{-2} \dy\\
&\geq \int_{A^c} \eps^{-1} \dy \\
&= \mu(A^c)\eps^{-1}
,\]
which can be made arbitrarily large by taking $\eps\to 0$.

#todo: Not great, $A^c$ depends on $\eps$ so this ratio has a competing numerator...

:::


