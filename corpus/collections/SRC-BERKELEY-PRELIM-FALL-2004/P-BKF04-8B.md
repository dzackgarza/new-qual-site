---
schema: qual/card@1
id: P-BKF04-8B
kind: problem
title: Positivity of $\lambda$ for $y''+\lambda a y=0$ with $y(0)=0$, $y'(1)=0$, and $a>0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
---

::: {.problem}
A $C^2$ function $y(x)$ for $0\leq x\leq1$, a positive continuous function $a(x)$ for $0\leq x\leq1$ and a real number $\lambda$ satisfy

$$
\begin{aligned}
&y''(x)+\lambda a(x)y(x)=0,\\
&y(0)=0,\\
&y'(1)=0.
\end{aligned}
$$

Suppose that $y(x)$ is not identically zero. Prove that $\lambda>0$.
:::

::: {.solution}
Multiply the differential equation by $y(x)$ and integrate from $0$ to $1$. Integration by parts with $u=y$ and $dv=y''\,dx$ gives

$$
\begin{aligned}
\lambda\int_0^1ay^2\,dx
&=-\int_0^1yy''\,dx\\
&=-yy'\Big|_0^1+\int_0^1(y')^2\,dx\\
&=\int_0^1(y')^2\,dx\\
&>0,
\end{aligned}
$$

where the boundary term vanishes because $y(0)=0$ and $y'(1)=0$, and the last inequality holds because if $y'$ were identically zero on $[0,1]$, then $y$ would be constant on $[0,1]$, making $y$ identically zero since $y(0)=0$. Since $a>0$ and $y$ is not identically zero, also $\int_0^1ay^2\,dx>0$. Thus $\lambda$ is a ratio of positive numbers, so $\lambda>0$.
:::
