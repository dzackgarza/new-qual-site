---
schema: qual/card@1
id: P-CAF11E
kind: problem
title: "A continuous function harmonic on the punctured disk is harmonic on the full disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: problem
Let $u$ be a real-valued continuous function on $\overline{\mathbb{D}}$, and assume that $u$ is harmonic in $\mathbb{D} \setminus \{0\}$.
Prove that $u$ is harmonic in $\mathbb{D}$.

Hint: Consider $v(r) := \int_{-\pi}^{\pi} u(re^{i\theta})\,d\theta$.
You may use without proof Laplace's equation in polar coordinates: $$r\frac{\partial}{\partial r}\!\left(r\frac{\partial U}{\partial r}\right) + \frac{\partial^2 U}{\partial \theta^2} = 0,$$ where $U(r, \theta) = u(re^{i\theta})$.
You may also use without proof the fact that a harmonic function in $\mathbb{D} \setminus \{0\}$ that depends only on $|z|$ is necessarily of the form $u(z) = a\log|z| + b$, where $a$ and $b$ are real constants.
:::

::: solution
Fix $0<R<1$. Let $h$ be the harmonic function on $B(0,R)$ whose boundary
values on $|z|=R$ agree with $u$; for example, $h$ is given by the Poisson
integral of $u|_{|z|=R}$. Put
\[
w=u-h.
\]
Then $w$ is continuous on $\overline{B(0,R)}$, harmonic on
$B(0,R)\setminus\{0\}$, and $w=0$ on $|z|=R$.

Let
\[
M=\max_{|z|\le R}|w(z)|.
\]
Fix $z$ with $0<|z|<R$ and choose $0<\varepsilon<|z|$. On the annulus
$\varepsilon<|\zeta|<R$, the harmonic function
\[
q_\varepsilon(\zeta)
=M\frac{\log(R/|\zeta|)}{\log(R/\varepsilon)}
\]
equals $M$ on $|\zeta|=\varepsilon$ and $0$ on $|\zeta|=R$. Since
$|w|\le M$ on the inner circle and $w=0$ on the outer circle, the maximum
principle applied to $w-q_\varepsilon$ and $-w-q_\varepsilon$ gives
\[
|w(z)|\le q_\varepsilon(z)
=M\frac{\log(R/|z|)}{\log(R/\varepsilon)}.
\]
Letting $\varepsilon\downarrow0$ yields $w(z)=0$. Hence $u=h$ on the punctured
disk $0<|z|<R$, and continuity gives equality also at $0$.

Thus $u$ agrees near $0$ with the harmonic function $h$, so $u$ is harmonic at
$0$. Since it was already harmonic away from $0$, it is harmonic on all of
$\mathbb D$.
:::
