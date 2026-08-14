---
schema: qual/card@1
id: E-MLXNX
kind: exercise
title: "- Show that the function $u=u(x,y)$ given by"
classification:
  areas:
  - complex-analysis
  topics:
  - harmonic-functions
  - pdes
  - counterexamples
relations: []
review: draft
---
:::{.problem title="?"}
 \envlist

- Show that the function $u=u(x,y)$ given by
$$u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}$$
is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for the Laplace equation
$$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$

- Show that there exist points $(x,y)\in D$ such that
$\displaystyle{\limsup_{n\to\infty} |u(x,y)|=\infty}$.


:::

