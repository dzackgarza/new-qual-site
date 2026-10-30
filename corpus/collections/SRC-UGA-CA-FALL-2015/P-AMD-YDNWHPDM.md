---
schema: qual/card@1
id: P-AMD-YDNWHPDM
kind: problem
title: $2^{n-1}\prod_{k=1}^{n-1}\sin(k\pi/n)=n$, polar Cauchy–Riemann equations, and
  holomorphy of $\log z$
classification:
  areas:
  - complex-analysis
  topics:
  - Trigonometry
  - Polynomials
  - Cauchy-Riemann
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: {.problem}
Use $n$-th roots of unity (i.e. solutions of $z^n - 1 = 0$) to show that
$$
2^{n-1} \sin\frac{\pi}{n} \sin\frac{2\pi}{n} \cdots \sin\frac{(n-1)\pi}{n} = n.
$$

Hint: $1 - \cos 2\theta = 2 \sin^2 \theta$, $\sin 2\theta = 2 \sin \theta \cos \theta$.

(a) Show that in polar coordinates, the Cauchy-Riemann equations take the form
$$
\frac{\partial u}{\partial r} = \frac{1}{r} \frac{\partial v}{\partial \theta}
\quad\text{and}\quad
\frac{\partial v}{\partial r} = -\frac{1}{r} \frac{\partial u}{\partial \theta}.
$$

(b) Use these equations to show that the logarithm function defined by
$$
\log z = \log r + i\theta \quad\text{where } z = re^{i\theta} \text{ with } -\pi < \theta < \pi
$$
is a holomorphic function in the region $r > 0$, $-\pi < \theta < \pi$. Also show that $\log z$ defined above is not continuous in $r > 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #prod}

For $n\ge2$, $\prod_{k=1}^{n-1}\bigl(1-e^{2\pi ik/n}\bigr)=n$.

::: pf-proof

The roots of $z^n-1$ are the $n$ distinct numbers $\omega_k=e^{2\pi ik/n}$, $0\le k\le n-1$, and $\omega_0=1$. Hence
$$
1+z+\cdots+z^{n-1}=\frac{z^n-1}{z-1}=\prod_{k=1}^{n-1}(z-\omega_k).
$$
Evaluation at $z=1$ gives the claim.

:::

:::

::: {.pf-step #mod}

For $1\le k\le n-1$, $\abs{1-e^{2\pi ik/n}}=2\sin\frac{k\pi}{n}$.

::: pf-proof

For real $\phi$, $\abs{1-e^{i\phi}}^2=(1-\cos\phi)^2+\sin^2\phi=2(1-\cos\phi)=4\sin^2\frac{\phi}{2}$ by the hint. With $\phi=2\pi k/n$, the number $\frac{\phi}{2}=\frac{k\pi}{n}$ lies in $(0,\pi)$, so $\sin\frac{k\pi}{n}>0$.

:::

:::

::: {.pf-step #sines}

$$
\boxed{2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=n}
$$

::: pf-proof

Take the modulus of both sides of Step [](#prod){.pf-ref} and apply Step [](#mod){.pf-ref} to each factor.

:::

:::

::: {.pf-step #polar}

If $f=u+iv$ is complex differentiable at $z=re^{i\theta}\ne0$, then $u_r=\frac1rv_\theta$ and $v_r=-\frac1ru_\theta$ there.

::: pf-proof

With $x=r\cos\theta$ and $y=r\sin\theta$, the chain rule gives
$$
u_r=u_x\cos\theta+u_y\sin\theta,\qquad u_\theta=r(-u_x\sin\theta+u_y\cos\theta),
$$
and the same formulas for $v$. Substitute the Cartesian equations $u_x=v_y$ and $u_y=-v_x$:
$$
v_\theta=r(-v_x\sin\theta+v_y\cos\theta)=r(u_y\sin\theta+u_x\cos\theta)=ru_r,
$$
$$
u_\theta=r(-v_y\sin\theta-v_x\cos\theta)=-rv_r.
$$
Divide by $r>0$.

:::

:::

::: {.pf-step #holo}

$\log z$ is holomorphic on $U=\{re^{i\theta}:r>0,\ -\pi<\theta<\pi\}$.

::: pf-proof

The map $(r,\theta)\mapsto re^{i\theta}$ is a $C^1$ diffeomorphism of $(0,\infty)\times(-\pi,\pi)$ onto $U$, so $u=\log r$ and $v=\theta$ are $C^1$ functions of $(x,y)$ on $U$. They satisfy $u_r=\frac1r=\frac1rv_\theta$ and $v_r=0=-\frac1ru_\theta$. The chain-rule relations of Step [](#polar){.pf-ref} are invertible for $r>0$, so these polar equations are equivalent to $u_x=v_y$ and $u_y=-v_x$. A $C^1$ function that satisfies the Cauchy-Riemann equations is holomorphic.

:::

:::

::: {.pf-step #disc}

$\log z$ has no continuous extension to the region $r>0$.

::: pf-proof

Let $x<0$. As $\theta\to\pi^-$, $\log(\abs{x}e^{i\theta})\to\log\abs{x}+i\pi$. As $\theta\to-\pi^+$, $\log(\abs{x}e^{i\theta})\to\log\abs{x}-i\pi$. Both paths converge to $x$, and the limits differ, so no value at $x$ makes $\log z$ continuous at $x$.

:::

:::

::: pf-qed

Step [](#sines){.pf-ref} proves the product formula, Step [](#polar){.pf-ref} proves part (a), and Steps [](#holo){.pf-ref} and [](#disc){.pf-ref} prove part (b).

:::

:::

:::
