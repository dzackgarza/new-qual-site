---
schema: qual/card@1
id: E-HHSCS
kind: problem
title: The integral of $\log x/(1+x^a)$ over $[0,\infty)$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source prints only the identity, with no instruction and no range for a; the statement asks to show it for a > 1, where the integral converges.
---

::: {.exercise}
For $a>1$, show that
$$
\begin{aligned}
I\coloneqq \int_0^\infty {\log(x) \over 1+x^a}\dx
&= - \qty{\pi \over a}^2\cos\qty{\pi\over a}\csc^2\qty{\pi \over a} \\
&= - {\pi^2\over a^2} {\cos\qty{\pi\over a} \over \sin^2\qty{\pi\over a}}
.\end{aligned}
$$
:::

::: {.solution}
Let $\omega\coloneqq e^{i\pi/a}$ and $\zeta\coloneqq\omega^2=e^{2\pi i/a}$, and let $I'\coloneqq\int_0^\infty{dt\over1+t^a}$.
On the sector $S\coloneqq\theset{z \st 0\le\arg z\le2\pi/a}$, define $\log z$ and $z^a=e^{a\log z}$ with $\arg z\in[0,2\pi/a]$.
Let $\Gamma_{\varepsilon,R}$ be the counterclockwise boundary of $S\intersect\theset{\varepsilon\le\abs z\le R}$: the segment $\gamma_1=[\varepsilon,R]$, the arc of radius $R$, the segment $\gamma_2$ from $R\zeta$ to $\varepsilon\zeta$, and the arc of radius $\varepsilon$.

![](../../assets/Complex_Analysis/040_Residues/figures/2021-12-22_05-25-35.png)

::: pf

::: {.pf-step #pole}
For $h(z)=\log z$ or $h(z)=1$, the only pole of $h(z)/(1+z^a)$ inside $\Gamma_{\varepsilon,R}$ is $\omega$, and its residue there is $-h(\omega)\,\omega/a$.

::: pf-proof
For $z=re^{i\theta}$ in $S$, $z^a=r^ae^{ia\theta}$ with $a\theta\in[0,2\pi]$, so $z^a=-1$ exactly when $r=1$ and $\theta=\pi/a$.
The pole is simple since $\dd{}{z}(1+z^a)=az^{a-1}\neq0$ there, and the residue is $h(\omega)/(a\omega^{a-1})=h(\omega)\,\omega/(a\omega^a)=-h(\omega)\,\omega/a$.
:::

:::

::: {.pf-step #arcs}
For $h$ as in step [](#pole){.pf-ref}, the integrals of $h(z)/(1+z^a)$ over both arcs tend to $0$ as $\varepsilon\to0$ and $R\to\infty$.

::: pf-proof
By the ML estimate, the arc of radius $R$ contributes $O\qty{R\log R/R^a}$ and the arc of radius $\varepsilon$ contributes $O\qty{\varepsilon\abs{\log\varepsilon}}$, and both tend to $0$ because $a>1$.
:::

:::

::: {.pf-step #segment}
As $\varepsilon\to0$ and $R\to\infty$, the integral of ${\log z\over1+z^a}$ over $\gamma_1+\gamma_2$ tends to $(1-\zeta)I-{2\pi i\over a}\zeta I'$, and the integral of ${1\over1+z^a}$ tends to $(1-\zeta)I'$.

::: pf-proof
On $\gamma_2$, $z=\zeta t$ with $t$ from $R$ to $\varepsilon$, $z^a=t^a$ and $\log z=\log t+2\pi i/a$, so
$$
\int_{\gamma_2}{\log z\over1+z^a}\dz = -\zeta\int_\varepsilon^R{\log t+2\pi i/a\over1+t^a}\dt
,\qquad
\int_{\gamma_2}{\dz\over1+z^a} = -\zeta\int_\varepsilon^R{\dt\over1+t^a}
.$$
The integrals over $\gamma_1$ tend to $I$ and $I'$.
:::

:::

::: {.pf-step #iprime}
$I'={\pi\over a}\csc\qty{\pi\over a}$.

::: pf-proof
By the residue theorem and steps [](#pole){.pf-ref}, [](#arcs){.pf-ref} and [](#segment){.pf-ref} with $h=1$, $(1-\zeta)I'=-{2\pi i\over a}\omega$.
Since $1-\zeta=\omega(\bar\omega-\omega)=-2i\sin\qty{\pi\over a}\omega$, this gives $I'={\pi\over a\sin(\pi/a)}$.
:::

:::

::: pf-qed
By the residue theorem and steps [](#pole){.pf-ref}, [](#arcs){.pf-ref}, [](#segment){.pf-ref} and [](#iprime){.pf-ref} with $h=\log$, and $\log\omega=i\pi/a$,
$$
{2\pi^2\over a^2}\omega = 2\pi i\cdot\qty{-{i\pi\over a^2}\omega} = (1-\zeta)I-{2\pi^2\over a^2}i\zeta\csc\qty{\pi\over a}
.$$
Dividing by $\omega$ and using $\bar\omega-\omega=-2i\sin\qty{\pi\over a}$,
$$
\begin{aligned}
I &= {{2\pi^2\over a^2}\qty{1+i\omega\csc\qty{\pi\over a}}\over-2i\sin\qty{\pi\over a}}
= {\pi^2\over a^2}\csc\qty{\pi\over a}\cdot i\qty{1+i\omega\csc\qty{\pi\over a}} \\
&= {\pi^2\over a^2}\csc\qty{\pi\over a}\qty{i-\qty{\cos\qty{\pi\over a}+i\sin\qty{\pi\over a}}\csc\qty{\pi\over a}}
= -{\pi^2\over a^2}\cos\qty{\pi\over a}\csc^2\qty{\pi\over a}
.\end{aligned}
$$
:::

:::

:::
