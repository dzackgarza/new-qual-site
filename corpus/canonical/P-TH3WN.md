---
schema: qual/card@1
id: P-TH3WN
kind: problem
title: Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous partial...
classification:
  areas:
  - complex-analysis
  topics:
  - cauchy-riemann
relations: []
review: draft
---

::: problem
Let $f=u+iv$ be differentiable (i.e. $f'(z)$ exists) with continuous
partial derivatives at a point $z=re^{i\theta}$, $r\not= 0$. Show
that
$$\frac{\partial u}{\partial r}=\frac{1}{r}\frac{\partial v}{\partial \theta},\quad
\frac{\partial v}{\partial r}=-\frac{1}{r}\frac{\partial u}{\partial \theta}.$$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Since $f(z)$ is complex differentiable at $z$, the Cartesian Cauchy-Riemann equations hold:
$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}.
$$

The polar coordinates $(r, \theta)$ are related to $(x, y)$ by:
$$
x = r \cos \theta, \qquad y = r \sin \theta.
$$
By the multivariable chain rule:
$$
\frac{\partial u}{\partial r} = \frac{\partial u}{\partial x} \frac{\partial x}{\partial r} + \frac{\partial u}{\partial y} \frac{\partial y}{\partial r} = \frac{\partial u}{\partial x} \cos \theta + \frac{\partial u}{\partial y} \sin \theta,
$$
$$
\frac{\partial u}{\partial \theta} = \frac{\partial u}{\partial x} \frac{\partial x}{\partial \theta} + \frac{\partial u}{\partial y} \frac{\partial y}{\partial \theta} = -\frac{\partial u}{\partial x} r \sin \theta + \frac{\partial u}{\partial y} r \cos \theta.
$$
Similarly, for $v$:
$$
\frac{\partial v}{\partial r} = \frac{\partial v}{\partial x} \cos \theta + \frac{\partial v}{\partial y} \sin \theta,
$$
$$
\frac{\partial v}{\partial \theta} = -\frac{\partial v}{\partial x} r \sin \theta + \frac{\partial v}{\partial y} r \cos \theta.
$$

Now substitute the Cartesian Cauchy-Riemann equations ($\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}$ and $\frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$) into the expression for $\frac{1}{r}\frac{\partial v}{\partial \theta}$:
$$
\frac{1}{r}\frac{\partial v}{\partial \theta} = -\frac{\partial v}{\partial x} \sin \theta + \frac{\partial v}{\partial y} \cos \theta = \frac{\partial u}{\partial y} \sin \theta + \frac{\partial u}{\partial x} \cos \theta = \frac{\partial u}{\partial r}.
$$
Similarly, substitute into $-\frac{1}{r}\frac{\partial u}{\partial \theta}$:
$$
-\frac{1}{r}\frac{\partial u}{\partial \theta} = \frac{\partial u}{\partial x} \sin \theta - \frac{\partial u}{\partial y} \cos \theta = \frac{\partial v}{\partial y} \sin \theta - \left(-\frac{\partial v}{\partial x}\right) \cos \theta = \frac{\partial v}{\partial x} \cos \theta + \frac{\partial v}{\partial y} \sin \theta = \frac{\partial v}{\partial r}.
$$

Thus, the polar Cauchy-Riemann equations hold:
$$
\frac{\partial u}{\partial r} = \frac{1}{r}\frac{\partial v}{\partial \theta}, \qquad \frac{\partial v}{\partial r} = -\frac{1}{r}\frac{\partial u}{\partial \theta}.
$$
:::
