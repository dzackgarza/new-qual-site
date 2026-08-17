---
schema: qual/card@1
id: P-HBWN6
kind: problem
title: "Let $f, g\\in L^1(\\RR)$."
classification:
  areas:
  - real-analysis
  topics:
  - convolution
  - fubini-tonelli
  - l1
relations: []
review: draft
solved: true
---
Let $f, g\in L^1(\RR)$. 
Argue that $H(x, y) \definedas f(y) g(x-y)$ defines a function in $L^1(\RR^2)$ and deduce from this fact that
\[
(f\ast g)(x) \definedas \int_\RR f(y) g(x-y) \,dy
\]
defines a function in $L^1(\RR)$ that satisfies 
\[
\norm{f\ast g}_1 \leq \norm{f}_1 \norm{g}_1
.\]


:::{.strategy}
Just do it! 
Sort out the justification afterward.
Use Tonelli.
:::

:::{.concept}
\envlist
- Tonelli: non-negative and measurable yields measurability of slices and equality of iterated integrals
- Fubini: $f(x, y) \in L^1$ yields *integrable* slices and equality of iterated integrals
- F/T: apply Tonelli to $\abs{f}$; if finite, $f\in L^1$ and apply Fubini to $f$
- See Folland's Real Analysis II, p. 68 for a discussion of using Fubini *and* Tonelli.
:::

:::{.solution}
- If these norms can be computed via iterated integrals, we have
\[
\norm{f\ast g}_1 
&\da \int_\RR \abs{(f\ast g)(x)} \dx \\
&\da \int_\RR \abs{\int_\RR H(x, y) \dy} \dx \\
&\da \int_\RR \abs{\int_\RR f(y)g(x-y) \dy} \dx \\
&\leq \int_\RR \int_\RR \abs{f(y) g(x-y)} \dx \dy \\
&\da \int_\RR \int_\RR \abs{H(x ,y)}\dx \dy \\
&\da \int_{\RR^2} \abs{H} \dmu_{\RR^2} \\
&\da \norm{H}_{L^1(\RR^2)}
.\]
  So it suffices to show $\norm{H}_1 < \infty$.

- A preliminary computation, the validity of which we will show afterward:
\[
\norm{H}_1
&\da \norm{H}_{L^1(\RR^2)} \\
&= \int _\RR \qty{ \int_\RR \abs{f(y)g(x-y)}  \, dy } \, dx && \text{Tonelli} \\ 
&= \int _\RR \qty{ \int_\RR \abs{f(y)g(x-y)}  \, dx} \, dy && \text{Tonelli} \\
&= \int _\RR \qty{ \int_\RR \abs{f(y)g(t)}  \, dt} \, dy && \text{setting } t=x-y, \,dt = - dx \\
&= \int _\RR \qty{ \int_\RR \abs{f(y)}\cdot \abs{g(t)}  \, dt}\, dy \\
&= \int _\RR \abs{f(y)} \cdot \qty{ \int_\RR \abs{g(t)}  \, dt}\, dy \\
&\definedas \int _\RR \abs{f(y)} \cdot \norm{g}_1 \,dy \\
&= \norm{g}_1 \int _\RR \abs{f(y)} \,dy &&\text{the norm is a constant} \\
&\definedas \norm{g}_1 \norm{f}_1  \\
&< \infty && \text{by assumption}
.\]

- We've used Tonelli twice: to equate the integral to the iterated integral, and to switch the order of integration, so it remains to show the hypothesis of Tonelli are fulfilled.


:::{.claim}
$H$ is measurable on $\RR^2$:
:::


:::{.proof title="?"}
\envlist

- It suffices to show $\tilde f(x, y) \definedas f(y)$ and $\tilde g(x, y) \definedas g(x-y)$ are both measurable on $\RR^2$. 
  - Then use that products of measurable functions are measurable.
  
-  $f \in L^1$ by assumption, and $L^1$ functions are measurable by definition.
- The function $(x, y) \mapsto g(x-y)$ is measurable on $\RR^2$:
  - $g$ is measurable on $\RR$ by assumption, so the cylinder function $G(x, y) \da g(x)$ on $\RR^2$ is measurable (result from course).
  - Define a linear transformation 
  \[
  T \da 
  \begin{bmatrix}
  1 & -1 
  \\
  0 & 1
  \end{bmatrix}
  \in \GL_2(\RR)
  && \implies \,\,\,
  T
  \begin{bmatrix}
   x 
  \\
   y 
  \end{bmatrix}
  =
  \begin{bmatrix}
  x-y   
  \\
  y  
  \end{bmatrix}
  ,\]
  and linear functions are measurable.
  - Write
  \[
  \tilde g(x-y) \da G(x-y, y) \da (G\circ T)(x, y)
  ,\]
  and compositions of measurable functions are measurable.

:::



- Apply **Tonelli** to $\abs{H}$
  - $H$ measurable implies $\abs{H}$ is measurable.
  - $\abs{H}$ is non-negative.
  - So the iterated integrals are equal in the extended sense
  - The calculation shows the iterated integral is finite, so $\int \abs{H}$ is finite and $H$ is thus integrable on $\RR^2$.

> Note: Fubini is not needed, since we're not calculating the actual integral, just showing $H$ is integrable.


:::


