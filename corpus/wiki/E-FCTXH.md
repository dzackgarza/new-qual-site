---
schema: qual/card@1
id: E-FCTXH
kind: exercise
title: "Prove that $\\displaystyle{f(z)=-\\frac{1}{2}\\left(z+\\frac{1}{z}\\right)}$ is a conformal map from the half disc $\\{z=x+iy:\\ |z|<1,\\ y>0\\}$ to $\\HH \\da \\{z=x+iy:\\ y>0\\}$."
classification:
  areas:
  - complex-analysis
  topics:
  - conformal-maps
  - geometry
relations: []
review: draft
solved: true
---
:::{.problem title="?"}
Prove that
$\displaystyle{f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)}$ is a
conformal map from the half disc 
\[
\{z=x+iy:\ |z|<1,\ y>0\}
\]
to $\HH \da \{z=x+iy:\ y>0\}$.
:::


:::{.solution}
Consider the images of arcs $\gamma_R(t) \da Re^{it}$ for $t\in [0, \pi]$ and $0<R<1$, which fill out the upper half disc:
\[
f(Re^{it}) = - {1\over 2}\qty{ \qty{R+R\inv}\cos(t) + i(R-R\inv)\sin(t) } \da H_R\cos(t) + V_R\sin(t)
,\]
where $H_R \da -{1\over 2}{R+R\inv}$ and $V_R \da -{1\over 2}(R-R\inv)$.
Note that $H_R\in (-\infty, -1]$ and $V_R \in (0, \infty)$ -- in particular, since $V_R>0$, as $t$ ranges through $(0, \pi)$, this traces out the *top* half of an ellipse (noting that $V_R<0$ would trace out the bottom).

As $R$ ranges from $(0, 1)$, $V_R$ ranges from $(0, \infty)$, so this traces out all such elliptic arcs in $\HH$ passing through $H_R <0, iV_R \in \HH, -H_R>0$.
So these trace out all of $\HH$.

:::






