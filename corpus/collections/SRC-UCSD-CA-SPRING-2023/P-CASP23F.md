---
schema: qual/card@1
id: P-CASP23F
kind: problem
title: 'Green''s function on $\DD\setminus\theset{a}$ and failure of the Dirichlet problem'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Dirichlet Problem
  - Green's Function
  - Boundary Values
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the two parts already on the card, both of which are
    correct. Added: the decomposition of v into two logarithmic potentials with the reason each
    is harmonic and where the logarithm of 1 - bar a z is defined; the verification |1 - bar a
    z| = |z - a| on the circle written out (multiplying by |z| = 1); the explicit remark that
    the formula reduces to log(1/|z|) at a = 0, which is the case the hint names; the
    quantitative bound |u - 2| <= 1 on a punctured disc that makes the removable-singularity
    theorem applicable; and the continuity of the extension up to the closed disc, which the
    maximum principle needs. No statement was changed. Not claimed: a retained solution set; the
    collection's provenance is the examination paper only.
---

::: {.problem}
Let $a \in \DD$ and $G = \DD \setminus \{a\}$.

(a) Construct a harmonic function $v$ on $G$ such that the following two conditions are satisfied: $\lim_{z \to z^*} v(z) = 0$ for all $z^* \in \circlegroup$ and $\lim_{z \to a} v(z) = +\infty$.
Write down an explicit formula for the function $v$ you constructed. (Hint: you only need to find one such function; first think about the case $a = 0$.)

(b) Let $f \in C(\partial G)$ be defined as $f(z) = 0$ for $z \in \circlegroup$ and $f(a) = 2$.
Prove that the Dirichlet problem on $G$ with boundary data $f$ has no solution: there is no harmonic function $u$ on $G$ such that $\lim_{z \to z_0} u(z) = f(z_0)$ for all $z_0 \in \partial G$. (Hint: argue by contradiction, making use of the function you constructed in part (a).)
:::

::: {.solution}
Throughout $a \in \DD$, $G = \DD\setminus\theset{a}$, $\circlegroup$ is the unit circle, and $\partial G = \circlegroup \cup \theset{a}$. The collection's `provenance` is the Spring 2023 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #a-harmonic}
(a) $v(z) = \log\abs{\frac{1 - \bar a z}{z - a}}$ is harmonic on $G$.

::: pf-proof
$v = \log\abs{1 - \bar a z} - \log\abs{z - a}$. The first term is the real part of the holomorphic function $\log(1 - \bar a z)$, defined on $\DD$ because $\abs{\bar a z} \le \abs{a}\abs{z} < 1$ there, hence harmonic; the second is the real part of $\log(z - a)$, holomorphic on $\CC\setminus\theset{a}$, hence harmonic there. A difference of harmonic functions is harmonic, and $G$ omits $a$.

:::

:::

::: {.pf-step #a-circle}
(a) $v(z) \to 0$ as $z \to z^{*}$ for every $z^{*} \in \circlegroup$.

::: pf-proof
For $\abs{z} = 1$ one has $\abs{1 - \bar a z} = \abs{z}\abs{1 - \bar a z} = \abs{\bar z - \bar a \bar z z} = \abs{\bar z - \bar a} = \abs{z - a}$, multiplying by $\abs{z} = 1$ and using $z\bar z = 1$; so $v = 0$ on the circle, and the limit at each boundary point of the circle is $0$ by continuity of $v$ up to that circle away from $a$.

:::

:::

::: {.pf-step #a-pole}
(a) $v(z) \to +\infty$ as $z \to a$.

::: pf-proof
As $z \to a$ the numerator $1 - \bar a z$ tends to $1 - \abs{a}^{2} > 0$, because $\abs{a} < 1$, while the denominator $z - a$ tends to $0$; so the modulus of the quotient tends to $+\infty$ and its logarithm does too. As a check, for $a = 0$ the formula reduces to $v(z) = \log\frac{1}{\abs{z}}$, which is the case the hint asks for first.

:::

:::

::: {.pf-step #b-bounded}
(b) If $u$ is harmonic on $G$ with $u(z) \to f(z_{0})$ at every $z_{0} \in \partial G$, then $u$ extends to a harmonic function on $\DD$.

::: pf-proof
The limit at $a$ is $f(a) = 2$, so there is $\delta > 0$ with $\abs{u(z) - 2} \le 1$, in particular $\abs{u} \le 3$, on $G \cap B(a,\delta)$. Thus $a$ is an isolated singularity of the harmonic function $u$ near which $u$ is bounded, and the removable-singularity theorem for harmonic functions makes $a$ removable: $u$ extends harmonically across $a$, with value $2$ there. The result is harmonic on $\DD$.

:::

:::

::: {.pf-step #b-contradiction}
(b) The extension is identically zero on $\DD$.

::: pf-proof
The extension is continuous on the closed disc: it is harmonic hence continuous inside, and at each $z_{0} \in \circlegroup$ the boundary limit is $f(z_{0}) = 0$. Its values on the boundary circle are $0$, so the maximum and minimum principles give $0 \le u \le 0$ on $\DD$, that is $u \equiv 0$.

:::

:::

::: pf-step
(b) The Dirichlet problem on $G$ with data $f$ has no solution.

::: pf-proof
By steps [](#b-bounded){.pf-ref} and [](#b-contradiction){.pf-ref} any solution would extend to a harmonic function on $\DD$ vanishing identically, and that extension takes the value $2$ at $a$; the contradiction shows that no such $u$ exists. Part (a)'s $v$ is what makes the boundary data admissible-looking while the problem is still unsolvable: it separates $a$ from the circle harmonically, so boundedness near $a$ is exactly what the data force and exactly what the maximum principle then forbids.

:::

:::

:::
:::
