---
schema: qual/card@1
id: P-JMOGT
kind: problem
title: $\lim_{x\to 0}\int_{\RR}|f(y-x)-f(y)|\,dy=0$ for $f\in L^1(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - L¹
  - Continuity
  - Density
relations: []
review: draft
---

Let $f\in L^1(\RR)$.
Show that
\[
\lim _{x \to 0} \int _{\RR} \abs{f(y-x)-f(y)} \, dy = 0
\]

:::{.solution}
:::{.concept}
- $C_c^\infty \injects L^p$ is dense.
- If $f$...?
:::

- Fixing notation, set $\tau_x f(y) \definedas f(y-x)$; we then want to show
\[  
\norm{\tau_x f -f}_{L^1} \converges{x\to 0}\to 0
.\]
- Claim: by an $\eps/3$ argument, it suffices to show this for compactly supported functions:
  - Since $f\in L^1$, choose $g_n\subset C_c^\infty(\RR^1)$ smooth and compactly supported so that $$\norm{f-g}_{L^1} < \eps.$$
  - Claim: $\norm{\tau_x f - \tau_x g} < \eps$.
    - Proof 1: translation invariance of the integral.
    - Proof 2: Apply a change of variables:
  \[  
    \norm{\tau_x f - \tau_x g}_1
    &\definedas \int_\RR \abs{\tau_x f(y) - \tau_x g(y)}\, dy \\
    &= \int_\RR \abs{f(y-x) - g(y-x)}\, dy  \\
    &= \int_\RR \abs{f(u) - g(u)}\, du \qquad (u=y-x,\, du=dy) \\
    &= \norm{f-g}_1 \\
    &< \eps
  .\]
  - Then
  \[  
  \norm{\tau_x f - f}_1 
  &= \norm{\tau_x f - \tau_x g + \tau_x g - g +g - f}_{1} \\
  &\leq \norm{\tau_x f - \tau_x g}_1 + \norm{\tau_x g - g}_1 + \norm{g - f}_{1} \\
  &\leq 2\eps + \norm{\tau_x g - g}_1
  .\]

- To show this for compactly supported functions:
  - Let $g\in C_c^\infty(\RR^1)$, let $E = \supp(g)$, and write
  \[  
  \norm{\tau_x g - g}_1 
  &= \int_\RR \abs{g(y-x) - g(y)}\,dy \\
  &= \int_E \abs{g(y-x) - g(y)} \,dy + \int_{E^c} \abs{g(y-x) - g(y)} \,dy\\
  &= \int_E \abs{g(y-x) - g(y)} \,dy 
  .\]

  - But $g$ is smooth and compactly supported on $E$, and thus uniformly continuous on $E$, so
  \[  
  \lim_{x\to 0} \int_E \abs{g(y-x) - g(y)} \,dy 
  &= \int_E \lim_{x\to 0} \abs{g(y-x) - g(y)} \,dy \\
  &= \int_E 0 \,dy \\
  &= 0
  .\]
:::

