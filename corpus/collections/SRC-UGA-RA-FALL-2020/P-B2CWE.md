---
schema: qual/card@1
id: P-B2CWE
kind: problem
title: Convolution against dilates of an $L^1$ kernel is bounded on $L^1$ and converges
  to $\alpha f$
classification:
  areas:
  - real-analysis
  topics:
  - Approximations to the Identity
  - Convolution
  - L¹
relations: []
review: draft
---

:::{.problem}
Suppose $\varphi\in L^1(\RR)$ with 
\[  
\int \varphi(x) \, dx = \alpha
.\]
For each $\delta > 0$ and $f\in L^1(\RR)$, define
\[  
A_\delta f(x) \da \int f(x-y) \delta^{-1} \varphi\qty{\delta^{-1} y}\, dy
.\]

a.
Prove that for all $\delta > 0$,
\[  
\norm{A_\delta f}_1 \leq \norm{\varphi}_1 \norm{f}_1
.\]

b.
Prove that 
\[  
A_\delta f \to \alpha f \text{ in } L^1(\RR) \qtext{as} \delta\to 0^+
.\]

> Hint: you may use without proof the fact that for all $f\in L^1(\RR)$,
\[  
\lim_{y\to 0} \int_\RR \abs{f(x-y) - f(x)}\, dx = 0
.\]

:::

:::{.remark}
See Folland 8.14.
:::

:::{.solution}
This is a direct application of Fubini-Tonelli:
\[
\norm{A_\delta f} 
&\da \int \abs{ \int f(x-y)\delta\inv \varphi(\delta\inv y)\dy} \dx\\
&\leq \int \int \abs{f(x-y)\delta\inv \varphi(\delta\inv y)} \dy \dx\\
&\equalsbecause{FT} \int \int \abs{ f(x-y) } \cdot \abs{\delta\inv \varphi(\delta\inv y)} \dx\dy\\
&= \int \abs{ \delta\inv \varphi(\delta\inv y) } \qty{ \int \abs{ f(x-y) }\dx } \dy \\
&= \int \abs{ \delta\inv \varphi(\delta\inv y)}\cdot  \norm{f} \dy \\
&= \norm{f} \cdot \int \abs{ \delta\inv \varphi(\delta\inv y) }  \dy \\
&= \norm{f} \cdot \norm{\varphi} 
.\]
Here we've used translation and dilation invariance of the Lebesgue integral.

:::

:::{.solution .foldopen}
Write $\phi_\delta(y) \da \delta\inv\phi(\delta\inv y)$, then
\[
\norm{A_\delta f - \alpha f}_1
&\da \int \abs{A_\delta f(x) - \alpha f(x) } \dx \\
&= \int \abs{ \int {f(x-y) \phi_\delta(y) } \dy - \alpha f(x) }\dx \\
&= \int \abs{ \int { \tau_y f (x) \phi_\delta(y) } \dy - \int f(x) \phi_\delta(y) \dy }\dx \\
&\leq \int\int \abs{\tau_y f(x) - f(x)}\cdot \abs{\phi_\delta(y)} \dy\dx\\
&= \int\int \abs{\tau_y f(x) - f(x)}\cdot \abs{\phi_\delta(y)} \dx\dy \\
&= \int\abs{\phi_\delta(y)}\cdot \norm{\tau_yf - f}_1 \dy
,\]
where the interchange of integration order is justified by Tonelli since the integrands are positive.
The goal is to now make this small when $\delta$ is small.

One way to do this immediately: make a change of variables $y=tz$ to get
\[
\norm{A_\delta f - \alpha f}_1 \leq\int {\abs{\phi(z)}} \norm{\tau_{tz}f -f}_1 \dz
,\]
use that $\norm{\tau_{tz} f- f}_1 \leq 2\norm{f}_1 < \infty$ by the triangle inequality and apply the DCT:
\[
\lim_{t\to 0}
\int {\abs{\phi(z)}} \cdot \norm{\tau_{tz}f -f}_1 \dz =
\int {\abs{\phi(z)}} \lim_{t\to 0} \norm{\tau_{tz}f -f}_1 \dz = 0
.\]

More directly, use continuity in $L^1$ (as per the hint) to pick a $h>0$ such that \[
\norm{\tau_y f - f}< \eps \quad \text{ for } y\in A \da \ts{y\st \abs{y} \leq h}
.\]
Now choose $\delta_0 \gg 1$ large enough so that 
\[
\int_{A^c}\abs{\phi_\delta(y)}\dy < \eps \quad \text{ for all }\delta > \delta_0
.\]
Now
\[
\int_\RR \abs{\phi_\delta(y)}\cdot \norm{\tau_yf - f}_1 \dy
&=
\int_A \abs{\phi_\delta(y)}\cdot \norm{\tau_yf - f}_1 \dy + \int_{A^c} \abs{\phi_\delta(y)}\cdot \norm{\tau_yf - f}_1 \dy \\
&\leq 
\int_A \abs{\phi_\delta(y)}\cdot \eps \dy + \int_{A^c} \abs{\phi_\delta(y)} \cdot 2\norm{f}_1 \dy \\
&\leq \eps\norm{\phi_\delta}_1 + 2\eps\norm{f}_1 \\
&\too 0
.\]
:::

