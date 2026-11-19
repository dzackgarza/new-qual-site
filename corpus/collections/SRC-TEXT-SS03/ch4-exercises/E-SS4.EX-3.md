---
schema: qual/card@1
id: E-SS4.EX-3
kind: problem
title: The Fourier transform pair $\frac1\pi\frac{a}{a^2+x^2}$ and $e^{-2\pi a\abs\xi}$
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Residues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Stein--Shakarchi Chapter 4 notation and exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured both halves into numbered steps, and wrote out the parts the transcription left as
    one line each: the modulus identity |e^{-2 pi i z xi}| = e^{2 pi xi Im z} and the resulting decay
    on the closing semicircle in the direction chosen for the sign of xi, the residue at z = -ia with
    its numerator evaluated, the sign conventions for a clockwise contour, the separate computation
    at xi = 0, and the split of the inverse integral into two elementary exponentials. Checked: the
    two residues give pi e^{-2 pi a xi} for xi > 0 and pi e^{2 pi a xi} for xi < 0, which agree with
    pi e^{-2 pi a|xi|}; and the sum of the two half-integrals is (1 / pi) a/(a^2 + x^2). Every macro
    used is one the preamble defines. Not checked this session: the printed statement page.

---

::: {.exercise}
Show, by contour integration, that if $a > 0$ and $\xi \in \RR$ then

$$
\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \frac {a}{a ^ {2} + x ^ {2}} e ^ {- 2 \pi i x \xi} d x = e ^ {- 2 \pi a \abs{ \xi }},
$$

and check that

$$
\int_ {- \infty} ^ {\infty} e ^ {- 2 \pi a \abs{ \xi }} e ^ {2 \pi i \xi x} d \xi = \frac {1}{\pi} \frac {a}{a ^ {2} + x ^ {2}}.
$$
:::

::: {.solution}

The computation is the card's own; the statement is the exercise stored on the card, and no source text or solution set is retained for it.

Let $a>0$ and $I(\xi)=\int_{-\infty}^{\infty}\frac{a}{a^{2}+x^{2}}e^{-2\pi ix\xi}dx$, and put $G(z)=\frac{ae^{-2\pi iz\xi}}{z^{2}+a^{2}}$.

::: pf

::: {.pf-step #modulus}
$\abs{e^{-2\pi iz\xi}}=e^{2\pi\xi\Im z}$ for $z\in\CC$, so the exponential decays on a semicircle in the lower half-plane when $\xi>0$ and in the upper half-plane when $\xi<0$.

::: pf-proof
Writing $z=u+iv$, $-2\pi iz\xi=-2\pi i(u+iv)\xi=-2\pi iu\xi+2\pi v\xi$, whose real part is $2\pi v\xi$. Hence the modulus is $e^{2\pi v\xi}$, which tends to $0$ as $v\to-\infty$ for $\xi>0$ and as $v\to+\infty$ for $\xi<0$.
:::

:::

::: {.pf-step #arc}
On a semicircle of radius $R>a$ in the half-plane where the exponential decays, the integral of $G$ is bounded by $\pi R\,a\,\sup e^{2\pi v\xi}/(R^{2}-a^{2})\to0$ as $R\to\infty$.

::: pf-proof
On such an arc $\abs{z}=R$ and $\abs{z^{2}+a^{2}}\geq R^{2}-a^{2}>0$, while $\abs{e^{-2\pi iz\xi}}\leq\sup$ over the arc; the ML estimate with arc length $\pi R$ gives the bound, and for fixed $\xi$ the supremum is $1$ on the arc through $v=0$ (it is at most $e^{2\pi\xi v}$ with $v$ bounded by $0$ in the decaying half), so the bound is $\pi Ra/(R^{2}-a^{2})\to0$.
:::

:::

::: {.pf-step #heavy}
For $\xi>0$, $I(\xi)=\pi e^{-2\pi a\xi}$.

::: pf-proof
Close in the lower half-plane, where $G$ has the single pole $z=-ia$; the contour is traversed clockwise, so the residue theorem gives $I(\xi)=-2\pi i\operatorname{Res}_{z=-ia}G$. At the simple pole, $\operatorname{Res}_{z=-ia}G=\restrictionof{\dfrac{ae^{-2\pi iz\xi}}{2z}}{z=-ia}=\dfrac{ae^{-2\pi a\xi}}{-2ia}=-\dfrac{e^{-2\pi a\xi}}{2i}$, using $-2\pi i(-ia)\xi=2\pi i\cdot ia\xi=-2\pi a\xi$. Hence $I(\xi)=-2\pi i\cdot\bigl(-\tfrac{1}{2i}e^{-2\pi a\xi}\bigr)=\pi e^{-2\pi a\xi}$, the arc contributing nothing by step [](#arc){.pf-ref}.
:::

:::

::: {.pf-step #light}
For $\xi<0$, $I(\xi)=\pi e^{2\pi a\xi}$.

::: pf-proof
Close in the upper half-plane, where the only pole is $z=ia$; the contour is counterclockwise, so $I(\xi)=2\pi i\operatorname{Res}_{z=ia}G$. Here $\operatorname{Res}_{z=ia}G=\dfrac{ae^{-2\pi i(ia)\xi}}{2ia}=-\dfrac{i}{2}e^{2\pi a\xi}$ since $-2\pi i(ia)\xi=2\pi a\xi$ and $a/(2ia)=1/(2i)=-i/2$. Then $I(\xi)=2\pi i\cdot\bigl(-\tfrac{i}{2}\bigr)e^{2\pi a\xi}=\pi e^{2\pi a\xi}$.
:::

:::

::: {.pf-step #zero}
$I(0)=\pi$.

::: pf-proof
At $\xi=0$ the integrand is $a/(a^{2}+x^{2})$, and $\int_{-\infty}^{\infty}\frac{a}{a^{2}+x^{2}}dx=a\cdot\frac{1}{a}\bigl[\arctan(x/a)\bigr]_{-\infty}^{\infty}=a\cdot\frac{1}{a}\cdot\pi=\pi$.
:::

:::

::: {.pf-step #first}
$\frac{1}{\pi}I(\xi)=e^{-2\pi a\abs{\xi}}$.

::: pf-proof
For $\xi>0$, step [](#heavy){.pf-ref} gives $\frac{1}{\pi}I(\xi)=e^{-2\pi a\xi}=e^{-2\pi a\abs{\xi}}$; for $\xi<0$, step [](#light){.pf-ref} gives $\frac{1}{\pi}I(\xi)=e^{2\pi a\xi}=e^{-2\pi a\abs{\xi}}$; and for $\xi=0$ step [](#zero){.pf-ref} gives $1=e^{0}$. These three cases exhaust $\RR$.
:::

:::

::: {.pf-step #inverse}
$\int_{-\infty}^{\infty}e^{-2\pi a\abs{\xi}}e^{2\pi i\xi x}d\xi=\frac{1}{\pi}\frac{a}{a^{2}+x^{2}}$.

::: pf-proof
Split at $\xi=0$. For $\xi>0$ the integrand is $e^{-2\pi(a-ix)\xi}$, whose integral over $(0,\infty)$ is $\frac{1}{2\pi(a-ix)}$ because $\Re(2\pi(a-ix))=2\pi a>0$. For $\xi<0$ substituting $\xi=-\eta$ turns the integral into $\int_{0}^{\infty}e^{-2\pi(a+ix)\eta}d\eta=\frac{1}{2\pi(a+ix)}$. Adding,
$$
\frac{1}{2\pi}\Bigl(\frac{1}{a-ix}+\frac{1}{a+ix}\Bigr)=\frac{1}{2\pi}\cdot\frac{2a}{a^{2}+x^{2}}=\frac{1}{\pi}\frac{a}{a^{2}+x^{2}}.
$$
:::

:::

:::

:::
