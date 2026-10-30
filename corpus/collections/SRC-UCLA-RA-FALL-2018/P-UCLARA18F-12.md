---
schema: qual/card@1
id: P-UCLARA18F-12
kind: problem
title: Roots of $e^z(z-1)^n=\alpha$ in the right half-plane
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 12. If $\alpha\in\CC$ satisfies $0<\abs{\alpha}<1$ and if $n\in\NN=\{1,2,3,\ldots\}$, show that the equation
$$
e^z(z-1)^n=\alpha
$$
has exactly $n$ simple roots in the half-plane
$$
\{z:\operatorname{Re}z>0\}.
$$
:::

::: {.solution}

Write
$$
H(z)=e^z(z-1)^n,
\qquad
F(z)=H(z)-\alpha.
$$

::: pf

::: {.pf-step #s1-1}

If $R>2$ and
$$
D_R=\{z:\operatorname{Re}z>0,\ \abs{z}<R\},
$$
then $\abs{H(z)}>\abs{\alpha}$ for every $z\in\partial D_R$.


::: pf-proof

On the imaginary-axis part of the boundary, write $z=iy$. Then
$$
\abs{H(iy)}
=\abs{e^{iy}}\,\abs{iy-1}^n
=(1+y^2)^{n/2}
\ge1
>\abs{\alpha}.
$$
On the semicircular part, $\abs{z}=R$ and $\operatorname{Re}z\ge0$, so
$$
\abs{H(z)}
=e^{\operatorname{Re}z}\abs{z-1}^n
\ge (R-1)^n
>1
>\abs{\alpha}.
$$
Thus the strict inequality holds on all of $\partial D_R$.

:::

:::

::: {.pf-step #s1-2}

The function $H$ has exactly $n$ zeros in $D_R$, counted with multiplicity.


::: pf-proof

The exponential function has no zeros. Hence the only zero of $H(z)=e^z(z-1)^n$ is $z=1$, with multiplicity $n$. Since $R>2$, the point $1$ lies in $D_R$, so $H$ has exactly $n$ zeros there when multiplicity is counted.

:::

:::

::: {.pf-step #s1-3}

For every $R>2$, the equation $F(z)=0$ has exactly $n$ roots in $D_R$, counted with multiplicity.


::: pf-proof

On $\partial D_R$, step [](#s1-1){.pf-ref} gives
$$
\abs{{-\alpha}}<\abs{H(z)}.
$$
Rouché's theorem therefore implies that $H$ and
$$
H-\alpha=F
$$
have the same number of zeros in $D_R$, counted with multiplicity. Step [](#s1-2){.pf-ref} gives that number as $n$.

:::

:::

::: {.pf-step #s1-4}

The equation $F(z)=0$ has exactly $n$ roots in the entire half-plane $\{\operatorname{Re}z>0\}$, counted with multiplicity.


::: pf-proof

Step [](#s1-3){.pf-ref} already gives $n$ roots in every $D_R$ with $R>2$. If there were any additional root $w$ in the right half-plane outside one such half-disc, choose $R>\abs{w}$. Then $D_R$ would contain the $n$ roots already counted together with $w$, contradicting step [](#s1-3){.pf-ref}. Since the increasing union of the sets $D_R$ is the whole open right half-plane, the total number there is exactly $n$, counted with multiplicity.

:::

:::

::: {.pf-step #s1-5}

Every root of $F$ in the right half-plane is simple.


::: pf-proof

Differentiating gives
$$
F'(z)=H'(z)
=e^z(z-1)^{n-1}(z+n-1).
$$
At a zero of $F$, one has $H(z)=\alpha\ne0$, so $z\ne1$. Therefore a multiple zero of $F$ would have to satisfy
$$
z+n-1=0,
\qquad\text{hence}\qquad
z=1-n.
$$
But $1-n\le0$ is real, so it does not lie in the open right half-plane. Thus every root counted in step [](#s1-4){.pf-ref} is simple.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} show that there are exactly $n$ roots in the right half-plane and that all of them are simple.

:::

:::

:::
