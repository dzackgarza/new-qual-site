---
schema: qual/card@1
id: E-SS8.PR-4
kind: problem
title: SU(1,1) and automorphisms of the unit disc
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Mappings
relations: []
review: draft
---

::: {.exercise}
Let $\mathrm{SU}(1,1)$ be the group of matrices $M=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with complex entries, determinant $1$, and
$$
\inner{MZ}{MW}=\inner{Z}{W},\qquad
\inner{Z}{W}=z_1\overline{w_1}-z_2\overline{w_2}
$$
for all $Z,W\in\CC^2$.

(a) Prove that every matrix in $\mathrm{SU}(1,1)$ has the form
$$
\begin{pmatrix}a&b\\\overline b&\overline a\end{pmatrix},
\qquad \abs{a}^2-\abs{b}^2=1.
$$
Use $J=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ and $\inner{Z}{W}=\overline W^{,t}JZ$.

(b) Associate to $M$ the fractional linear map $z\mapsto(az+b)/(cz+d)$. Prove that $\mathrm{SU}(1,1)/\{\pm I\}$ is isomorphic to the group of automorphisms of the unit disc.
:::

::: {.hint}
In (b), associate $e^{2i\theta}(z-\alpha)/(1-\overline\alpha z)$ with
$$
\frac{1}{\sqrt{1-\abs{\alpha}^2}}
\begin{pmatrix}
e^{i\theta}&-\alpha e^{i\theta}\\
-\overline\alpha e^{-i\theta}&e^{-i\theta}
\end{pmatrix}.
$$
:::
