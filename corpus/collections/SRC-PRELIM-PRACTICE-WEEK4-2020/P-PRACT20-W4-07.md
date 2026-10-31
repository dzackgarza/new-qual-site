---
schema: qual/card@1
id: P-PRACT20-W4-07
kind: problem
title: Solutions of $yy''-2(y')^2=0$ through $(1,1)$
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
Find all the solutions of the equation $y y'' - 2(y')^{2} = 0$ which pass through $x = 1$, $y = 1$.
:::

::: {.solution}
Near $x=1$ we have $y>0$, so the equation reads $y''=2(y')^2/y$, whose right side is smooth in $(y,y')$ for $y>0$. A solution is therefore determined by $y(1)=1$ and the slope $C:=y'(1)$. On an interval where $y>0$,

$$
\frac{d}{dx}\left(\frac{y'}{y^2}\right)=\frac{yy''-2(y')^2}{y^3}=0,
$$

so $y'/y^2$ is constant, equal to its value $C$ at $x=1$. Integrating again gives

$$
-\frac1y=Cx+D\Longrightarrow y(x)=\frac{1}{-D-Cx},
$$

and $y(1)=1$ gives $-D-C=1$. So the solutions through $(1,1)$ are

$$
\boxed{y(x)=\frac{1}{1+C(1-x)}},\qquad C\in\RR,
$$

each on the interval containing $1$ where $1+C(1-x)>0$. The case $C=0$ is the constant solution $y\equiv1$. Conversely, each of these functions satisfies the equation: with $u=1+C(1-x)$, $y'=C/u^2$ and $y''=2C^2/u^3$, so $yy''=2C^2/u^4=2(y')^2$.
:::
