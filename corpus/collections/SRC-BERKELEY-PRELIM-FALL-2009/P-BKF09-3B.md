---
schema: qual/card@1
id: P-BKF09-3B
kind: problem
title: 'The Koebe function $z/(1-z)^2$: injectivity, Taylor series and image of the disk'
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Prove that the function $f(z)=\frac{z}{(1-z)^2}$ is injective on the disk $B_1(0)=\{z\in\CC\mid\abs{z}<1\}$.
Find the Taylor series about $z=0$, and determine its radius of convergence.
What is the maximal disk $B_r(0)=\{w\in\CC\mid\abs{w}<r\}$ such that $B_r(0)\subset f(B_1(0))$?
:::

::: {.solution}
Suppose that $f(z_1)=f(z_2)$, where $\abs{z_i}<1$.
Then $\frac{z_1}{(1-z_1)^2}=\frac{z_2}{(1-z_2)^2}$, and cross-multiplying, we have $z_1(1-z_2)^2=z_2(1-z_1)^2$.
Thus, $z_1-z_2=z_2z_1^2-z_1z_2^2=z_1z_2(z_1-z_2)$.
If $z_1\neq z_2$, then dividing we see that $1=z_1z_2$, which is impossible since then we would have $1=\abs{z_1z_2}=\abs{z_1}\abs{z_2}<1$, a contradiction.
So $z_1\neq z_2$, and $f(z)$ is thus injective on $B_1(0)$.

Noting that $f(z)=\frac{z-1+1}{(1-z)^2}=\frac{-1}{1-z}+\frac{1}{(1-z)^2}$, and that $\frac{1}{(1-z)^2}=\left(\frac{1}{1-z}\right)'=(1+z+z^2+\cdots)'=1+2z+3z^2+\cdots$, we have
$$
f(z)=-1-z-z^2-\cdots+1+2z+3z^2+\cdots=z+2z^2+3z^3+\cdots.
$$
The radius of convergence is $1$, since $f(z)$ has a pole at $1$, and is analytic on $B_1(0)$.

Note that for $\abs{z}=\rho<1$, we have $\abs{f(z)}=\left\lvert\frac{z}{(1-z)^2}\right\rvert\ge\rho/(1+\rho)^2$, since $\abs{1-z}\le1+\abs{z}\le1+\rho$, and this is an equality if $z=-\rho$.
Thus, the disk $B_{\rho/(1+\rho)^2}(0)$ lies outside of the curve $f(\rho e^{i\theta})$, $0\le\theta<2\pi$.
Let $\abs{a}<1/4$, and choose $0<\rho<1$ such that $\abs{a}<\rho/(1+\rho)^2$, which we may do since $\lim_{\rho\to1}\rho/(1+\rho)^2=1/4$.
The integral $\frac{1}{2\pi i}\int_{\abs{z}=\rho}\frac{f'(z)}{f(z)-a}\,dz$ gives the multiplicity $\abs{\{z\mid f(z)=a,\ \abs{z}<\rho\}}$ by the argument principle.
Since $f$ is injective, $f(0)=0$, and $B_{\rho/(1+\rho)^2}$ lies in the complement of the contour $f(\rho e^{i\theta})$, we see that there exists $\abs{z}<\rho$ with $f(z)=a$.
:::
