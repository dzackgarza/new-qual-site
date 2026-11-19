---
schema: qual/card@1
id: P-CASP19F
kind: problem
title: "Analytic function on the punctured disk vanishing on a boundary arc is identically zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Analytic Continuation
  - Boundary Values
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/Complex-Qual-220-Spring-2019.pdf,
    problem 6: "Let f be a continuous function on {z in C : 0 < |z| <= 1} that is analytic on
    {z in C : 0 < |z| < 1}. Assume f(z) = 0 for every z = e^{i theta} with pi/4 < theta < pi/3.
    Prove f = 0." The card's statement is that problem verbatim.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Made explicit the three things the
    prose left implicit: that the closed subarc is chosen strictly inside the open arc so that a
    one-sided outer neighbourhood of it exists; that the extension is continuous at interior points
    of the arc, using continuity of f up to the circle and the vanishing of the boundary value; and
    that Morera's theorem applies to a triangle crossing the arc, the integral over the outer part
    vanishing identically and the one over the inner part by Cauchy's theorem with the subarc
    contributing nothing. The final step records that the punctured disc is connected, which is what
    carries the vanishing from an open subset to all of it. No retained published solution covers
    this problem.
---

::: {.problem}
Let $f$ be a continuous function on $\{z \in \CC : 0 < \abs{z} \leq 1\}$ that is analytic on $\{z \in \CC : 0 < \abs{z} < 1\}$.
Assume $f(z) = 0$ for every $z = e^{i\theta}$ with $\frac{\pi}{4} < \theta < \frac{\pi}{3}$.
Prove $f \equiv 0$.
:::

::: {.solution}
This is Problem 6 of the UCSD complex-analysis qualifying exam of Spring 2019 (`assets/attachments/Complex-Qual-220-Spring-2019.pdf`). No published solution set is transcribed: the argument is the card's own, and it is the reflection-across-the-arc argument the problem is designed for.

::: pf

::: {.pf-step #arc}
There are $\alpha<\beta$ with $\pi/4<\alpha<\beta<\pi/3$ and $S_{0}=\theset{e^{i\theta}\mid\alpha\leq\theta\leq\beta}\subset\theset{e^{i\theta}\mid\pi/4<\theta<\pi/3}$.

::: pf-proof
The closed interval $[\alpha,\beta]$ is chosen inside the open interval $(\pi/4,\pi/3)$, which is possible since that interval is nonempty and open.
:::
:::

::: {.pf-step #extension}
Define $F$ on the domain $\Omega=\DD\cup\theset{z\mid1<\abs{z}<1+\delta,\ \arg z\in(\alpha,\beta)}\cup S_{0}^{o}$ by $F=f$ inside the punctured disc and $F=0$ on the outer piece; for small $\delta>0$ this $F$ is a well-defined continuous function, holomorphic off $S_{0}$.

::: pf-proof
The inner piece $\theset{0<\abs{z}<1}$ and the outer piece are disjoint and their closures meet exactly at interior points of the arc $S_{0}$. On the inner piece $F=f$ is analytic by hypothesis. On the outer piece $F=0$ is analytic. At a point $\zeta=e^{i\theta}$ with $\alpha<\theta<\beta$, continuity of $f$ on $\theset{0<\abs{z}\leq1}$ and $f(\zeta)=0$ give $F(z)\to0=F(\zeta)$ as $z\to\zeta$ from inside, and $F\equiv0$ near $\zeta$ outside; so $F$ is continuous at $\zeta$. Choosing $\delta>0$ so that the outer piece stays away from the ends of the arc keeps $\Omega$ a domain on which $F$ is defined and continuous.
:::
:::

::: {.pf-step #morera}
$F$ is holomorphic on $\Omega$.

::: pf-proof
Let $T\subset\Omega$ be a closed triangle. If $T$ misses $S_{0}$ it lies in one of the two pieces, where $F$ is holomorphic, so $\int_{\partial T}F\,dz=0$ by Cauchy's theorem. Otherwise $T$ meets $S_{0}$ in a segment cutting $T$ into an inner and an outer part, and $\int_{\partial T}F\,dz$ is the sum of the two boundary integrals: the outer one vanishes because $F=0$ there, and the inner one vanishes by Cauchy's theorem applied to the inner part, whose boundary includes a subarc of $S_{0}$ on which $F=f=0$. By Morera's theorem, $F$ is holomorphic on $\Omega$.
:::
:::

::: {.pf-step #identity}
$f\equiv0$ on $\theset{0<\abs{z}<1}$.

::: pf-proof
The outer piece of $\Omega$ is a nonempty open set on which $F=0$, so the identity theorem gives $F\equiv0$ on the domain $\Omega$; in particular $f=F=0$ on a nonempty open subset of the punctured disc $\theset{0<\abs{z}<1}$. That punctured disc is connected, and $f$ is analytic on it, so the identity theorem gives $f\equiv0$ there, which is the assertion.
:::
:::
:::

:::
