---
schema: qual/card@1
id: P-PRACT20-W4-02
kind: problem
title: The initial value problem $y'+xy=x$, $y(0)=-1$
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
---

::: {.problem}
Solve the initial value problem $y' + xy = x$, $y(0) = -1$.
:::

::: {.solution}
The integrating factor is $\mu(x)=e^{\int x\,dx}=e^{x^2/2}$. We see

$$
e^{x^2/2}y'+xe^{x^2/2}y=xe^{x^2/2}\implies\frac{d}{dx}\left[e^{x^2/2}y(x)\right]=xe^{x^2/2}\implies e^{x^2/2}y(x)-y(0)=e^{x^2/2}-1.
$$

With $y(0)=-1$ this gives

$$
\boxed{y(x)=1-2e^{-x^2/2}.}
$$
:::
