---
schema: qual/card@1
id: P-7QVGF
kind: problem
title: Show that if $f$ is continuous with compact support on $\RR$, then
classification:
  areas:
  - real-analysis
  topics:
  - approximations-to-the-identity
  - convolution
  - l1
relations: []
review: draft
---
a.
Show that if $f$ is continuous with compact support on $\RR$, then 
\[
\lim _{y \rightarrow 0} \int_{\mathbb{R}}|f(x-y)-f(x)| d x=0
\]

b. 
Let $f\in L^1(\RR)$ and for each $h > 0$ let 
\[
\mathcal{A}_{h} f(x):=\frac{1}{2 h} \int_{|y| \leq h} f(x-y) d y
\]

  - Prove that $\left\|\mathcal{A}_{h} f\right\|_{1} \leq\|f\|_{1}$ for all $h > 0$.

  - Prove that $\mathcal{A}_h f \to f$ in $L^1(\RR)$ as $h \to 0^+$.

:::{.concept}
\envlist
- Continuity in $L^1$ (recall that DCT won't work! Notes 19.4, prove it for a dense subset first).
- Lebesgue differentiation in 1-dimensional case. See HW 5.6.
:::

:::{.solution}
\envlist

:::{.proof title="of a"}

- Fix $\varepsilon > 0$.
  If we can find a set $A$ such that the following calculation holds for $h$ small enough, we're done:
  \[
  \int_\RR \abs{f(x-h) - f(x)} \dx 
  &= \int_A \abs{f(x-h) - f(x)} \dx \\
  &\leq \int_A \eps \\
  &= \eps \mu(A) \too 0
  ,\]
  provided $h\to 0$ as $\eps\to 0$, which we can arrange if $\abs{h} < \eps$.

- Choose $A\contains \supp f$ compact such that $\supp f \pm 1 \subseteq A$
  - Why this can be done: $\supp f$ is compact, so closed and bounded, and contained in some compact interval $[-M, M]$.
  So e.g. $A\da [-M-1, M+1]$ suffices.
- Note that $f$ is still continuous on $A$, since it is zero on $A\sm \supp f$, and thus uniformly continuous (by Heine-Cantor, for example).
- We can rephrase the usual definition of uniform continuity:
\[
\forall \eps \exists \delta = \delta(\eps) \text{ such that } \abs{x - y} < \delta \implies \abs{f(x) - f(y)} < \eps \quad \forall x, y\in A
\]
as
\[
\forall \eps \exists \delta = \delta(\eps) \text{ such that } \abs{h} < \delta \implies \abs{f(x-h) - f(x)} < \eps \quad \forall x \text{ such that }x, x\pm h \in A
\]

- So fix $\eps$ and choose such a $\delta$ for $A$, and choose $h$ such that $\abs{h} < \min(1, \delta)$.
  Then the desired computation goes through by uniform continuity of $f$ on $A$.

:::

:::{.proof title="of b"}
We have
\[
\int_\RR \abs{A_h(f)(x)} ~dx 
&= \int_\RR \abs{\frac{1}{2h} \int_{x-h}^{x+h} f(y)~dy} ~dx \\
&\leq \frac{1}{2h} \int_\RR \int_{x-h}^{x+h} \abs{f(y)} ~dy ~dx    \\
&=_{FT} \frac{1}{2h} \int_\RR \int_{y-h}^{y+h} \abs{f(y)} ~\mathbf{dx} ~\mathbf{dy}    \\
&= \int_\RR \abs{f(y)} ~{dy} \\
&= \norm{f}_1
,\]

and (rough sketch)

\[
\int_\RR \abs{A_h(f)(x) - f(x)} ~dx 
&= \int_\RR \abs{ \left(\frac{1}{2h} \int_{B(h, x)} f(y)~dy\right) - f(x)}~dx \\
&= \int_\RR \abs{ \left(\frac{1}{2h} \int_{B(h, x)} f(y)~dy\right) - \frac{1}{2h}\int_{B(h, x)} f(x) ~dy}~dx \\
&\leq_{FT} \frac{1}{2h} \int_\RR  \int_{B(h, x)}\abs{ f(y-x) - f(x)} ~\mathbf{dx} ~\mathbf{dy} \\
&\leq \frac 1 {2h} \int_\RR \norm{\tau_x f - f}_1 ~dy \\
&\to 0 \quad\text{by (a)}
.\]

:::

:::

:::{.remark}
This works for arbitrary $f\in L^1$, using approximation by continuous functions with compact support:

- Choose $g\in C_c^0$ such that $\norm{f- g}_1 \to 0$.

- By translation invariance, $\norm{\tau_h f - \tau_h g}_1 \to 0$.

- Write
\[
\norm{\tau f - f}_1 
&= \norm{\tau_h f - g + g - \tau_h g + \tau_h g - f}_1 \\
&\leq \norm{\tau_h f - \tau_h g} + \norm{g - f} + \norm{\tau_h g - g} \\
&\to \norm{\tau_h g - g}
,\]

  so it suffices to show that $\norm{\tau_h g - g} \to 0$.

:::
