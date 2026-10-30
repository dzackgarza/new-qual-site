---
schema: qual/card@1
id: P-BKS07-3A
kind: problem
title: A $2\pi$-periodic real-analytic function extends to a periodic holomorphic function on a strip
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Suppose $f : \RR \to \RR$ is real analytic and periodic with period 2π. Prove that $f$ has an analytic continuation F defined on a strip

$$
S = \{ x + i y \in \CC ~ : ~ \abs{ y } < \rho \}
$$

with $\rho > 0$ , and that $F ( z + 2 \pi ) = F ( z )$ for $z \in S$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For each $x\in\RR$ there is $r_x>0$ such that the Taylor series of $f$ at $x$ converges on the disk $B(x,r_x)\subseteq\CC$ and equals $f$ on $(x-r_x,x+r_x)$. Its sum $F_x$ is holomorphic on $B(x,r_x)$, and we may take $r_{x+2\pi}=r_x$.

::: pf-proof

This is the definition of real analyticity, together with the fact that a power series converges on a complex disk with the same radius as on the real interval. Since $f$ is $2\pi$-periodic, $f^{(k)}(x+2\pi)=f^{(k)}(x)$ for every $k$, so the Taylor series at $x$ and at $x+2\pi$ have the same coefficients.

:::

:::

::: {.pf-step #s2}

If $z\in B(x,r_x)\cap B(x',r_{x'})$ with $x,x'\in\RR$, then $F_x(z)=F_{x'}(z)$.

::: pf-proof

The intersection of two disks centered on $\RR$ is convex, hence connected, and it is symmetric about $\RR$. If it is nonempty, it contains a real point, and so it meets $\RR$ in a nonempty open interval. On that interval $F_x=f=F_{x'}$. By the identity theorem, $F_x=F_{x'}$ on the whole intersection.

:::

:::

::: {.pf-step #s3}

There is $\rho>0$ such that the strip $S=\{\abs{\operatorname{Im}z}<\rho\}$ is covered by the disks $B(x,r_x)$, $x\in\RR$.

::: pf-proof

The compact interval $[0,2\pi]$ is covered by finitely many intervals $(x_i-\frac12r_{x_i},x_i+\frac12r_{x_i})$, $1\le i\le N$. Let $\rho=\min_i\frac12r_{x_i}$. If $z=s+it$ with $s\in[0,2\pi]$ and $\abs t<\rho$, choose $i$ with $\abs{s-x_i}<\frac12r_{x_i}$. Then $\abs{z-x_i}<\frac12r_{x_i}+\frac12r_{x_i}=r_{x_i}$. For general $s$, translate by a multiple of $2\pi$ and use $r_{x+2\pi}=r_x$.

:::

:::

::: pf-qed

By steps [](#s2){.pf-ref} and [](#s3){.pf-ref}, setting $F(z)=F_x(z)$ for any $x$ with $z\in B(x,r_x)$ defines a holomorphic function on $S$ that equals $f$ on $\RR$. If $z\in B(x,r_x)$, then $z+2\pi\in B(x+2\pi,r_x)$, and by step [](#s1){.pf-ref} $F_{x+2\pi}(z+2\pi)=F_x(z)$, because both power series have the same coefficients. Hence $F(z+2\pi)=F(z)$.

:::

:::

:::
