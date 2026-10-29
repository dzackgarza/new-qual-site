---
schema: qual/card@1
id: P-CWXEW
kind: problem
title: "Conformal map from a slit lens to the upper half plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Find a bijective conformal map from $G$ to $\HH = \{w \in \CC \mid \operatorname{Im}(w) > 0\}$, where
$$G \coloneqq \{z \in \CC \mid \abs{z-1} < \sqrt{2}, \, \abs{z+1} < \sqrt{2}\} \setminus [0, i).$$
:::

::: {.solution}

Every square root below is the principal branch.

::: pf

::: {.pf-step #sector}
$\zeta\coloneqq-\frac{z-i}{z+i}$ maps $G$ biholomorphically onto $\{\abs{\arg\zeta}<\pi/4\}\setminus(0,1]$.

::: pf-proof
The circles $\abs{z-1}=\sqrt2$ and $\abs{z+1}=\sqrt2$ meet orthogonally at $\pm i$.
$T(z)\coloneqq\frac{z-i}{z+i}$ sends $i\mapsto0$ and $-i\mapsto\infty$, so it sends both circles to lines through $0$, and the lens to a sector of opening $\pi/2$; since $T(0)=-1$, that sector is $3\pi/4<\arg w<5\pi/4$.
For $0\le t<1$, $T(it)=\frac{t-1}{t+1}\in[-1,0)$, so the slit goes to $[-1,0)$.
Multiplying by $-1$ gives the claim.
:::

:::

::: {.pf-step #slit-disk}
$v\coloneqq\frac{\zeta^2-1}{\zeta^2+1}$ maps the region of step [](#sector){.pf-ref} biholomorphically onto $\DD\setminus(-1,0]$.

::: pf-proof
Squaring maps the slit sector onto $\{\Re u>0\}\setminus(0,1]$, and the Cayley transform $u\mapsto\frac{u-1}{u+1}$ maps the right half-plane onto $\DD$ and $(0,1]$ onto $(-1,0]$.
:::

:::

::: {.pf-step #half-disk}
$s\coloneqq\sqrt v$ maps $\DD\setminus(-1,0]$ biholomorphically onto $H_+\coloneqq\{\abs{s}<1,\ \Re s>0\}$.

::: pf-proof
The principal square root is a biholomorphism of $\CC\setminus(-\infty,0]$ onto the right half-plane, and it preserves $\abs{\cdot}<1$.
:::

:::

::: {.pf-step #quadrant}
$q\coloneqq\frac{s-i}{s+i}$ maps $H_+$ biholomorphically onto the third quadrant.

::: pf-proof
$q$ maps the imaginary diameter $s=it$, $-1<t<1$, to $\frac{t-1}{t+1}$, the negative real axis, and the semicircle $\abs{s}=1$, $\Re s>0$, to the negative imaginary axis; $q(1/2)=-\frac35-\frac45i$ lies in the third quadrant.
:::

:::

::: pf-step
The composition
$$
z\mapsto\left(\frac{s-i}{s+i}\right)^2,\qquad
s=\sqrt{\frac{T(z)^2-1}{T(z)^2+1}},\quad T(z)=\frac{z-i}{z+i},
$$
is a bijective conformal map $G\to\HH$.

::: pf-proof
Squaring maps the third quadrant biholomorphically onto $\HH$.
Compose with steps [](#sector){.pf-ref}, [](#slit-disk){.pf-ref}, [](#half-disk){.pf-ref} and [](#quadrant){.pf-ref}, noting $\zeta^2=T(z)^2$.
:::

:::

:::

:::
