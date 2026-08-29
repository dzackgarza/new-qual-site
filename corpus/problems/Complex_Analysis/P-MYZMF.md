---
schema: qual/card@1
id: P-MYZMF
kind: problem
title: A holomorphic function is locally $m$-to-$1$ near a zero of multiplicity $m$
classification:
  areas:
  - complex-analysis
  topics:
  - Argument Principle
  - Open Mapping Theorem
  - Zeros
relations: []
review: draft
---

:::{.problem}
Let $f$ be analytic in a domain $D$ and fix $z_0 \in D$ with $w_0 \definedas f(z_0)$.
Suppose $z_0$ is a zero of $f(z) - w_0$ with finite multiplicity $m$.
Show that there exists $\delta >0$ and $\eps > 0$ such that for each $w$ such that $0 < \abs{w-w_0} < \eps$, the equation $f(z) - w = 0$ has exactly $m$ *distinct* solutions inside the disc $\abs{z-z_0} < \delta$.
:::

:::{.solution}
Write $g(z) \da f(z) - w_0$, then $g$ is holomorphic on $D$ and thus $w_0$ is an isolated zero.
Choose $\delta$ small enough so that $g$ is nonvanishing on $\DD_\delta(z_0)\smts{z_0}$.
Let 
\[
\gamma \da \ts{\abs{\xi - z_0} = \delta }= \bd\DD_{\delta}(z_0)
.\]
Choose $\eps < \inf\ts{w\in f(\delta)}$ so that $\abs{f(z) - w_0} > \eps$ in $\DD_\eps(w_0)\smts{w_0}$ for every $z\in \gamma$.
Let 
\[
\gamma' \da \bd \DD_{\eps}(w_0) = \ts{\abs{z-w_0} = \eps}
,\]
and
define the solution counting function:
\[
F(w) 
\da {1\over 2\pi i} \oint_{\gamma'} \logd(g(z)) \dz 
= {1\over 2\pi i } \oint_{\gamma'} {g'(z)\over g(z) }\dz
= {1\over 2\pi i} \oint_{\gamma'} {f'(z)\over f(z) - w} \dz
,\]
which counts the zeros of $g$ (since it has no poles) and consequently the number of solutions to $f(z) = w$ in $\DD_\eps(w_0)$.
This is now a continuous integer valued function on $\DD_\eps(w_0)$, and is thus constant.
Since $f(z_0) = w_0$ with $z_0$ enclosed by $\gamma$ and $w_0$ enclosed by $\gamma'$, the constant is exactly the multiplicity of the zero of $f(z) - w_0$ at $z_0$, which is $m$.
:::



