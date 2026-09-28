---
schema: qual/card@1
id: E-SS1.EX-8
kind: problem
title: "The chain rule for the dz and dzbz derivatives"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.exercise}
8. Suppose U and $V$ are open sets in the complex plane.
   Prove that if $f : U \to V$ and $g : V \to \mathbb { C }$ are two functions that are diferentiable (in the real sense, that is, as functions of the two real variables x and $y )$ , and $h = g \circ f$ , then

$$
\frac {\partial h}{\partial z} = \frac {\partial g}{\partial z} \frac {\partial f}{\partial z} + \frac {\partial g}{\partial \overline {{z}}} \frac {\partial \overline {{f}}}{\partial z}
$$

and

$$
\frac {\partial h}{\partial \overline {{z}}} = \frac {\partial g}{\partial z} \frac {\partial f}{\partial \overline {{z}}} + \frac {\partial g}{\partial \overline {{z}}} \frac {\partial \overline {{f}}}{\partial \overline {{z}}}.
$$

This is the complex version of the chain rule.
:::

::: {.solution}
Write the real-differentiable map $f$ locally as a function of $z$ and $\bar z$. Its differential is
\[
df=f_z\,dz+f_{\bar z}\,d\bar z,
\qquad
d\bar f=\bar f_z\,dz+\bar f_{\bar z}\,d\bar z.
\]
Likewise, for $g$, viewed at the point $f(z)$,
\[
dg=g_z\,dw+g_{\bar z}\,d\bar w.
\]
For $h=g\circ f$, substitute $w=f(z)$:
\[
\begin{aligned}
dh
&=g_z\,df+g_{\bar z}\,d\bar f\\
&=g_z(f_z\,dz+f_{\bar z}\,d\bar z)
 +g_{\bar z}(\bar f_z\,dz+\bar f_{\bar z}\,d\bar z)\\
&=(g_zf_z+g_{\bar z}\bar f_z)\,dz
 +(g_zf_{\bar z}+g_{\bar z}\bar f_{\bar z})\,d\bar z.
\end{aligned}
\]
Comparing the coefficients of $dz$ and $d\bar z$ yields
\[
h_z=g_zf_z+g_{\bar z}\bar f_z,
\qquad
h_{\bar z}=g_zf_{\bar z}+g_{\bar z}\bar f_{\bar z},
\]
which are the desired formulas.
:::
