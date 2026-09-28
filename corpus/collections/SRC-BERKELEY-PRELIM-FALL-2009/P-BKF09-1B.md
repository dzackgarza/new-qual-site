---
schema: qual/card@1
id: P-BKF09-1B
kind: problem
title: Convergence of the improper integral $\int_1^\infty x^2\cos(x^\beta)\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the real values of $\beta$ for which the following limit exists and is finite:
$$
\lim_{R\to\infty}\int_1^R x^2\cos(x^\beta)\,dx.
$$
:::

::: {.solution}
When $\beta\le0$, $\cos(x^\beta)$ tends to a positive limit as $x\to\infty$, and hence
$$
\lim_{R\to\infty}\int_1^R x^2\cos(x^\beta)\,dx=\infty.
$$
When $\beta>0$, write the integral as $I(R)\coloneqq\beta^{-1}\int_1^R x^{3-\beta}\,d\sin(x^\beta)$.
When $0<\beta\le3$, the limit does not exist, since the differences $I((2\pi k+\pi/2)^{1/\beta})-I((2\pi k-\pi/2)^{1/\beta})$ do not tend to $0$ as $k\to\infty$.
When $\beta>3$, integration by parts shows that
$$
I(R)=\text{const}+\text{const}\,R^{3-\beta}\sin(R^\beta)+\text{const}\int_1^R x^{2-\beta}\sin(x^\beta)\,dx.
$$
The integral on the right has a limit since $\sin(x^\beta)$ is bounded, and $\int_1^\infty x^{2-\beta}\,dx$ converges absolutely when $2-\beta<-1$.
The finite terms have a limit since $R^{3-\beta}\to0$.
Therefore, when $\beta>3$, the limit of $I(R)$ exists and is finite.
:::
