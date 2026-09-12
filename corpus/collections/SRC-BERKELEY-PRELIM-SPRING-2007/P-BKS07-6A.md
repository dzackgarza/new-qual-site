---
schema: qual/card@1
id: P-BKS07-6A
kind: problem
title: UC Berkeley Spring 2007 prelim 6A
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let
\[
A=\alpha_1\sigma_1+\alpha_2\sigma_2+\alpha_3\sigma_3,
\qquad \alpha_1,\alpha_2,\alpha_3\in\mathbb C,
\]
where
\[
\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]
Let $\beta\in\mathbb C$ be any square root of $\alpha_1^2+\alpha_2^2+\alpha_3^2$.

(a) Prove that
\[
\exp(A)=\cosh(\beta)I+\frac{\sinh\beta}{\beta}A,
\]
where $\frac{\sinh\beta}{\beta}$ is interpreted as $1$ if $\beta=0$.
(Hint: first show that $A^2$ is a scalar multiple of the identity.)

(b) Evaluate $\exp(A)$ explicitly when $\alpha_1=i\pi$, $\alpha_2=i\pi$, and $\alpha_3=\pi$.
:::

::: {.solution}
(a) An explicit calculation shows that $A ^ { 2 } = ( \alpha _ { 1 } ^ { 2 } + \alpha _ { 2 } ^ { 2 } + \alpha _ { 3 } ^ { 2 } ) I = \beta ^ { 2 } I$ . Thus

$$
{ \begin{array} { r l } & { \exp ( A ) = I + A + { \cfrac { 1 } { 2 ! } } A ^ { 2 } + { \cfrac { 1 } { 3 ! } } A ^ { 3 } + \cdots } \\ & { ~ = I + A + { \cfrac { \beta ^ { 2 } } { 2 ! } } I + { \cfrac { \beta ^ { 2 } } { 3 ! } } A + { \cfrac { \beta ^ { 4 } } { 4 ! } } I + { \cfrac { \beta ^ { 4 } } { 5 ! } } A + \cdots } \\ & { ~ = \cosh ( \beta ) + { \cfrac { \sinh \beta } { \beta } } A , } \end{array} }
$$

where the last step is valid (with our convention) even if $\beta = 0$

(b) The values $\alpha _ { 1 } = i \pi , \alpha _ { 2 } = i \pi , \alpha _ { 3 } = \pi \mathrm { g i v e } \beta ^ { 2 } = - \pi ^ { 2 }$ , so we choose $\beta = i \pi$ and obtain cosh $( \beta ) = \cos ( i \beta ) = \cos ( - \pi ) = - 1 , \sinh ( \beta ) = - i \sin ( i \beta ) = - i \sin ( - \pi ) = 0$ , and $\exp ( A ) = - I$
:::
