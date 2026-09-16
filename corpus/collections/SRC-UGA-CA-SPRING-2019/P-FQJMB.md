---
schema: qual/card@1
id: P-FQJMB
kind: problem
title: $e^x(\cos y+i\sin y)$ is the unique entire solution of $E'=E$, $E(0)=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Entire Functions
  - Power Series
  - Identity Theorem
relations: []
review: draft
---

::: {.problem}
Define

$$
E(z)=e^{x}(\cos y+i \sin y) .
$$

- Show that $E(z)$ is the unique function analytic on $\mathbb{C}$ that satisfies

$$
E^{\prime}(z)=E(z), \quad E(0)=1 .
$$

- Conclude from the first part that 
\[
E(z)=\sum_{n=0}^{\infty} \frac{z^{n}}{n !}
.\]
:::

::: {.solution}
Write $z=x+iy$ and
\[
E(z)=u(x,y)+iv(x,y),
\qquad
u=e^x\cos y,\quad v=e^x\sin y.
\]
Then
\[
u_x=e^x\cos y=v_y,
\qquad
u_y=-e^x\sin y=-v_x,
\]
so the Cauchy--Riemann equations hold everywhere and $E$ is entire. Moreover
\[
E'(z)=u_x+iv_x=e^x(\cos y+i\sin y)=E(z),
\qquad E(0)=1.
\]

For uniqueness, suppose $F$ is entire with $F'=F$ and $F(0)=1$. Since
\[
E(z)E(-z)=1,
\]
$E$ has no zeros. Hence
\[
\left(\frac{F}{E}\right)'
=\frac{F'E-FE'}{E^2}=0.
\]
Thus $F/E$ is constant, and its value at $0$ is $1$. Therefore $F=E$.

Now let
\[
S(z)=\sum_{n=0}^{\infty}\frac{z^n}{n!}.
\]
The ratio test shows that this series has infinite radius of convergence, so
$S$ is entire and may be differentiated termwise:
\[
S'(z)=\sum_{n=1}^{\infty}\frac{n z^{n-1}}{n!}
=\sum_{m=0}^{\infty}\frac{z^m}{m!}=S(z),
\qquad S(0)=1.
\]
By the uniqueness just proved,
\[
\boxed{E(z)=\sum_{n=0}^{\infty}\frac{z^n}{n!}}.
\]
:::
