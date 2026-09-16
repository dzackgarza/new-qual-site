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
\[
\lim _{r \rightarrow 0} \frac{1}{\pi r^{2}} \int_{\left|z-z_{0}\right|=r} f(z) d z=0
.\]
:::

::: {.solution}
Put $h=z-z_0$. Real differentiability at $(x_0,y_0)$ gives
\[
f(z_0+h)=f(z_0)+A h+B\bar h+o(|h|),
\]
where
\[
B={1\over2}\left(u_x-v_y+i(v_x+u_y)\right)_{(x_0,y_0)}.
\]
On $|h|=r$ we have $\bar h=r^2/h$, and therefore
\[
\begin{aligned}
\int_{|z-z_0|=r}f(z)\,dz
&=A\int_{|h|=r}h\,dh
 +B\int_{|h|=r}\bar h\,dh+o(r^2)\\
&=2\pi i r^2B+o(r^2).
\end{aligned}
\]
Consequently
\[
\lim_{r\to0}{1\over\pi r^2}
\int_{|z-z_0|=r}f(z)\,dz
=2iB.
\]
This limit is zero exactly when
\[
u_x=v_y,
\qquad
u_y=-v_x
\]
at $(x_0,y_0)$, i.e. exactly when the Cauchy--Riemann equations hold there.
Because the real partial derivatives are continuous at the point, the usual
Cauchy--Riemann criterion applies, so this is equivalent to complex
differentiability of $f$ at $z_0$.
:::
