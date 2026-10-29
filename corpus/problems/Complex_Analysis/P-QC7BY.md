---
schema: qual/card@1
id: P-QC7BY
kind: problem
title: $f=u+iv$ is complex differentiable at $z_0$ iff $\lim_{r\to 0}\frac{1}{\pi
  r^2}\int_{|z-z_0|=r}f(z)\,dz=0$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Contour Integration
  - Holomorphic Functions
  - Morera
relations: []
review: draft
---

::: {.problem}
Assume two functions $u, v: \RR^2 \to \RR$ have continuous partial derivatives at $(x_0 ,y_0)$.
Show that $f \definedas u + iv$ has derivative $f'(z_0)$ at $z_0 = x_0 + iy_0$ if and only if
$$
\lim _{r \rightarrow 0} \frac{1}{\pi r^{2}} \int_{\left|z-z_{0}\right|=r} f(z) d z=0
.$$
:::

::: {.solution}
Put $h=z-z_0$ and
$$
B\coloneqq\frac12\bigl(u_x-v_y+i(v_x+u_y)\bigr)(x_0,y_0).
$$

::: pf

::: {.pf-step #expansion}

There is a constant $A$ with $f(z_0+h)=f(z_0)+Ah+B\bar h+o(\abs h)$ as $h\to0$.

::: pf-proof

The partial derivatives of $u$ and $v$ are continuous at $(x_0,y_0)$, so $f$ is real differentiable there. Writing its real derivative in terms of $h$ and $\bar h$ gives the expansion with $A=\frac12(f_x-if_y)$ and $B=\frac12(f_x+if_y)$, which is the displayed value.

:::

:::

::: {.pf-step #limit}

$\displaystyle\lim_{r\to0}\frac1{\pi r^2}\int_{\abs{z-z_0}=r}f(z)\,dz=2iB$.

::: pf-proof

We have $\int_{\abs h=r}dh=\int_{\abs h=r}h\,dh=0$, and on $\abs h=r$, $\bar h=r^2/h$, so $\int_{\abs h=r}\bar h\,dh=2\pi ir^2$. The remainder in step [](#expansion){.pf-ref} contributes at most $o(r)\cdot2\pi r=o(r^2)$. Hence
$$
\int_{\abs{z-z_0}=r}f(z)\,dz=2\pi ir^2B+o(r^2).
$$

:::

:::

::: pf-step

$f'(z_0)$ exists if and only if the limit is $0$.

::: pf-proof

By step [](#limit){.pf-ref}, the limit is $0$ exactly when $B=0$, that is, when $u_x=v_y$ and $u_y=-v_x$ at $(x_0,y_0)$. Since $f$ is real differentiable at $z_0$, these Cauchy--Riemann equations hold at $z_0$ exactly when $f$ is complex differentiable there.

:::

:::

:::

:::
