---
schema: qual/card@1
id: P-L7QND
kind: problem
title: Constructing a harmonic conjugate by a path-independent integral
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
relations: []
review: draft
---

::: {.problem}
Let $u$ be harmonic on an open disk of radius $R>0$, with continuous
second partial derivatives. Fix $(a,b)$ in the disk and define
\[
v(x,y)=\int_{(a,b)}^{(x,y)}(-u_y\,dx+u_x\,dy).
\]
(a) Show that the integral is path-independent. (b) Show that $u+iv$ is
analytic. (c) Show that $v$ is harmonic.
:::

::: {.solution}
The one-form
\[
\eta=-u_y\,dx+u_x\,dy
\]
is closed because
\[
\frac{\partial(-u_y)}{\partial y}
=-u_{yy}=u_{xx}
=\frac{\partial u_x}{\partial x},
\]
using $u_{xx}+u_{yy}=0$. A disk is simply connected, so the integral of
$\eta$ is path-independent. Hence
\[
v_x=-u_y,\qquad v_y=u_x,
\]
which are the Cauchy--Riemann equations for $u+iv$; therefore $u+iv$ is
analytic. Finally,
\[
v_{xx}+v_{yy}=-u_{yx}+u_{xy}=0,
\]
so $v$ is harmonic.
:::