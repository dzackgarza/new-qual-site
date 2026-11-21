---
schema: qual/card@1
id: P-FIOQC
kind: problem
title: Simple zeros of $\sin(\pi z)$ at the integers, and $\operatorname{Res}_{z=n}\frac{1}{\sin(\pi
  z)}$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Residues
  - Trigonometry
  - Poles
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Each equivalence is now an argument: sin(pi z) = 0 iff e^{2 pi i z} = 1 (multiplying by e^{i pi z}), the passage from that to z in Z by modulus and real part, simplicity from the nonvanishing derivative pi(-1)^n, and the residue from the simple pole formula Res = 1/g'(n) rather than quoted. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own (the formula used is the one the exercise supplies). No statement repair.
---

::: {.problem}
Use the following formula to show that the complex zeros of $\sin(\pi z)$ are exactly the integers, and they are each of order 1:
$$
\sin \pi z=\frac{e^{i \pi z}-e^{-i \pi z}}{2 i}
.$$

Calculate the residue of ${1\over \sin(\pi z)}$ at $z=n\in \ZZ$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, using the formula the exercise supplies.

::: pf

::: {.pf-step #zero}
$\sin(\pi z)=0$ if and only if $e^{2\pi iz}=1$.

::: pf-proof
$\sin(\pi z)=\dfrac{e^{i\pi z}-e^{-i\pi z}}{2i}$, and $2i\ne0$, so $\sin(\pi z)=0$ exactly when $e^{i\pi z}=e^{-i\pi z}$. Multiplying that equation by $e^{i\pi z}$, which is never zero, gives $e^{2\pi iz}=1$; conversely $e^{2\pi iz}=1$ gives $e^{i\pi z}=e^{-i\pi z}$ after dividing by $e^{i\pi z}$.
:::

:::

::: {.pf-step #integers}
$e^{2\pi iz}=1$ if and only if $z\in\ZZ$.

::: pf-proof
Write $z=x+iy$ with $x,y\in\RR$. Then $\abs{e^{2\pi iz}}=e^{-2\pi y}$, and $\abs{1}=1$, so $e^{2\pi iz}=1$ forces $y=0$. With $y=0$, $e^{2\pi ix}=\cos(2\pi x)+i\sin(2\pi x)=1$ forces $\sin(2\pi x)=0$ and $\cos(2\pi x)=1$, which happens exactly when $x\in\ZZ$. Conversely $z=x\in\ZZ$ gives $e^{2\pi ix}=1$.
:::

:::

::: {.pf-step #simple}
Every zero of $\sin(\pi z)$ is simple.

::: pf-proof
$\frac{d}{dz}\sin(\pi z)=\pi\cos(\pi z)$, whose value at $z=n\in\ZZ$ is $\pi\cos(\pi n)=\pi(-1)^n\ne0$. A zero at which the derivative does not vanish is a simple zero, so the zeros $n$, which are all of them by steps [](#zero){.pf-ref} and [](#integers){.pf-ref}, are simple.
:::

:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=n}\dfrac1{\sin(\pi z)}=\dfrac{(-1)^n}{\pi}$ for every $n\in\ZZ$.

::: pf-proof
Let $g(z)=\sin(\pi z)$ and $h(z)=1/g$. Since $g$ has a simple zero at $n$ with $g'(n)=\pi(-1)^n\ne0$ (step [](#simple){.pf-ref}), $h$ has a simple pole at $n$, and the residue there is
$$
\operatorname{Res}_{z=n}h=\lim_{z\to n}(z-n)h(z)=\frac{1}{g'(n)}=\frac{1}{\pi(-1)^n}=\frac{(-1)^n}{\pi},
$$
using $1/(z-n)\sim g'(n)/(g(z)-g(n))=g'(n)/g(z)$ as $z\to n$ and $g(n)=0$.
:::

:::

:::
:::
