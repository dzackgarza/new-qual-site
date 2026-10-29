---
schema: qual/card@1
id: E-XQW4K
kind: problem
title: Removable singularities and expansion of $1/\sin z - 1/z + 2z/(z^2-\pi^2)$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Laurent Series
  - Trigonometry
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Consider
$$
f(z) \coloneqq \frac{1}{\sin(z)} - \frac{1}{z} + \frac{2z}{z^2-\pi^2}.
$$
Show that on $\abs{z} < 2\pi$, all singularities are removable, and find a Laurent expansion about $z=0$.
:::

::: {.solution}
Note that $\frac{2z}{z^2-\pi^2} = \frac{1}{z-\pi} + \frac{1}{z+\pi}$.

::: pf

::: {.pf-step #simple-poles}
In $\abs{z}<2\pi$, the singularities of $f$ are at most simple poles at $0$, $\pi$, $-\pi$.

::: pf-proof
The zeros of $\sin z$ in $\abs{z}<2\pi$ are $0,\pm\pi$, all simple since $\cos(k\pi)\neq0$, so $1/\sin z$ has simple poles there; the other two terms have simple poles at $0$ and at $\pm\pi$ respectively, and $f$ is holomorphic elsewhere in the disc.
:::

:::

::: {.pf-step #removable}
Each singularity of $f$ in $\abs{z}<2\pi$ is removable.

::: pf-proof
By step [](#simple-poles){.pf-ref}, it suffices that each residue vanishes.
At $a\in\{0,\pi,-\pi\}$, $\operatorname{Res}_a \frac{1}{\sin z} = \frac{1}{\cos a}$, which is $1$ at $0$ and $-1$ at $\pm\pi$.
The residue of $-\frac1z$ at $0$ is $-1$, and the residues of $\frac1{z-\pi}$ at $\pi$ and of $\frac1{z+\pi}$ at $-\pi$ are $1$.
So $\operatorname{Res}_a f = 0$ at each $a$.
:::

:::

::: pf-step
About $z=0$, valid on $\abs{z}<2\pi$,
$$
\boxed{f(z) = \qty{\frac16 - \frac{2}{\pi^2}}z + \qty{\frac{7}{360} - \frac{2}{\pi^4}}z^3 + O(z^5)}.
$$

::: pf-proof
By step [](#removable){.pf-ref}, $f$ extends holomorphically to $\abs{z}<2\pi$, so its Laurent expansion about $0$ is a Taylor series converging there.
From $\sin z = z\qty(1 - \frac{z^2}{6} + \frac{z^4}{120} - \cdots)$,
$$
\frac{1}{\sin z} = \frac1z\qty(1 + \frac{z^2}{6} + \qty(\frac1{36}-\frac1{120})z^4 + O(z^6)) = \frac1z + \frac z6 + \frac{7z^3}{360} + O(z^5).
$$
For $\abs{z}<\pi$,
$$
\frac{2z}{z^2-\pi^2} = -\frac{2z}{\pi^2}\sum_{k\ge0}\qty(\frac z\pi)^{2k} = -\frac{2z}{\pi^2} - \frac{2z^3}{\pi^4} + O(z^5).
$$
Adding these and $-\frac1z$ gives the expansion.
:::

:::

:::

:::
