---
schema: qual/card@1
id: P-PRACT20-W4-09
kind: problem
title: The Bernoulli equation $y'+\frac4xy=x^3y^2$ and the substitution for $y^\alpha$
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
(Bernoulli Equations)

(a) Find the general solution of the differential equation $y' + \frac{4}{x} y = x^{3} y^{2}$ by making the substitution $u = 1/y$.

(b) Generalize this substitution so that it works if $y^{2}$ on the right hand side is replaced by $y^{\alpha}$ for any $\alpha \neq 0, 1$.
:::

::: {.solution}
(a) Work on an interval with $x>0$. The function $y\equiv0$ is a solution. On an interval where $y\ne0$, set $u=1/y$. Then

$$
u'=-\frac{1}{y^2}y'=-\frac{1}{y^2}\left(-\frac4xy+x^3y^2\right)=\frac{4}{xy}-x^3=\frac4xu-x^3.
$$

This equation is linear in $u$. We use the integrating factor $x^{-4}$:

$$
u'-\frac4xu=-x^3\quad\Longrightarrow\quad\frac{1}{x^4}u'-\frac{4}{x^5}u=-\frac1x\quad\Longrightarrow\quad\frac{d}{dx}\left[\frac{1}{x^4}u\right]=-\frac1x.
$$

Integrating gives

$$
\frac{1}{x^4}u(x)=C-\log x\Longrightarrow u(x)=Cx^4-x^4\log x.
$$

Inverting gives the general nonzero solution

$$
\boxed{y(x)=\frac{1}{u(x)}=\frac{1}{Cx^4-x^4\log x}},
$$

on intervals where the denominator does not vanish, together with $y\equiv0$.

(b) Consider the equation

$$
y'+p(x)y=q(x)y^\alpha.
$$

Make the substitution $u=y^\beta$ on an interval where $y>0$ and choose $\beta$ to linearize the equation. We get

$$
u'=\beta y^{\beta-1}y'=\beta y^{\beta-1}\bigl(-p(x)y+q(x)y^\alpha\bigr)=-\beta p(x)y^\beta+\beta q(x)y^{\alpha+\beta-1}=-\beta p(x)u+\beta q(x)y^{\alpha+\beta-1}.
$$

To eliminate the power of $y$, choose $\beta=1-\alpha$. Then $u=y^{1-\alpha}$ satisfies the linear equation

$$
u'+(1-\alpha)p(x)u=(1-\alpha)q(x).
$$
:::
