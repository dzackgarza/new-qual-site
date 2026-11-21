---
schema: qual/card@1
id: P-CASP18B
kind: problem
title: '$\int_0^\infty dt/(t^3+1)$ by residues'
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Residue Theorem
  - Improper Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the residue argument already on the card, whose
    computation is correct: the sector of angle 2 pi/3 encloses only the pole e^{i pi/3}, the
    arc contributes O(R^{-2}), the closing ray gives -e^{2 pi i/3} I, and (1 - e^{2 pi i/3}) I =
    (2 pi i/3) e^{-2 pi i/3} yields I = 2 pi/(3 sqrt 3). Added: the list of the three cube roots
    of -1 with a check that only one has its argument in the sector, the derivation of the
    residue as 1/P'(z_0), the uniform estimate on the arc, the orientation of the closing ray,
    the reasons the real integral converges, and the two complex-number evaluations that finish
    the division. Not claimed: a retained solution set; the collection's provenance is the
    examination paper only.
---

::: {.problem}
Use the method of residues to evaluate
$$
\int_0^\infty \frac{dt}{t^3 + 1}.
$$
:::

::: {.solution}
Throughout $F(z) = 1/(1+z^{3})$, $I \coloneqq \int_{0}^{\infty}\frac{dt}{1+t^{3}}$, and for $R > 0$ the closed sector is $S_{R} \coloneqq \theset{z \mid 0 \le \arg z \le 2\pi/3,\ \abs{z} \le R}$, whose boundary $\gamma_{R}$ runs along the real segment from $0$ to $R$, then along the arc $z = Re^{i\theta}$, $0 \le \theta \le 2\pi/3$, then back along the ray $z = te^{2\pi i/3}$ from $t = R$ to $t = 0$. The collection's `provenance` is the Spring 2018 examination paper, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #poles}
The only zero of $1 + z^{3}$ in $S_{R}$ is $z_{0} = e^{i\pi/3}$, and it is simple.

::: pf-proof
$1 + z^{3} = (z - \zeta_{1})(z - \zeta_{2})(z - \zeta_{3})$ where the $\zeta_{j}$ are the three cube roots of $-1$, namely $e^{i\pi/3}$, $e^{i\pi}$ and $e^{5\pi i/3} = e^{-i\pi/3}$. Their arguments are $\pi/3$, $\pi$ and $5\pi/3$; the first lies in $[0,2\pi/3]$ and the other two do not, and all three have modulus $1 \le R$. The zero is simple because the derivative $3z^{2}$ does not vanish at $\zeta_{j}$.

:::

:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=z_{0}}F = \frac{1}{3z_{0}^{2}} = \frac{e^{-2\pi i/3}}{3}$.

::: pf-proof
For a simple pole of $1/P$ at $z_{0}$, where $P$ has a simple zero at $z_{0}$, the residue is $1/P'(z_{0})$, because $1/P = \frac{1}{(z-z_{0})P'(z_{0})} + O(1)$ by Taylor's theorem. Here $P'(z_{0}) = 3z_{0}^{2}$ and $z_{0}^{2} = e^{2\pi i/3}$, so the residue is $\frac{1}{3}e^{-2\pi i/3}$.

:::

:::

::: {.pf-step #arc}
$\abs{\int_{\text{arc}}F(z)\,dz} \le \frac{2\pi R}{3(R^{3}-1)}$, which tends to $0$ as $R \to \infty$.

::: pf-proof
For $\abs{z} = R$ with $R > 1$ one has $\abs{1+z^{3}} \ge \abs{z}^{3} - 1 = R^{3} - 1$, so $\abs{F} \le \frac{1}{R^{3}-1}$ on the arc. The arc has length $\frac{2\pi}{3}R$, and the modulus of an integral is at most the maximum of the modulus times the length of the path.

:::

:::

::: {.pf-step #rays}
The real segment contributes $\int_{0}^{R}\frac{dt}{1+t^{3}} \to I$, and the ray $z = te^{2\pi i/3}$ contributes $-e^{2\pi i/3}\int_{0}^{R}\frac{dt}{1+t^{3}} \to -e^{2\pi i/3}I$.

::: pf-proof
On the real segment $z = t$ with $dz = dt$ and $z^{3} = t^{3}$. On the second ray $z = t e^{2\pi i/3}$ with $t$ decreasing from $R$ to $0$, so $dz = e^{2\pi i/3}dt$ and $z^{3} = t^{3}e^{2\pi i} = t^{3}$; the integral is therefore $\int_{R}^{0}\frac{e^{2\pi i/3}}{1+t^{3}}dt = -e^{2\pi i/3}\int_{0}^{R}\frac{dt}{1+t^{3}}$. The real integral tends to $I$ because $\frac{1}{1+t^{3}}$ is positive and continuous on $[0,\infty)$ and $O(t^{-3})$ at infinity, hence integrable there.

:::

:::

::: {.pf-step #contour}
$\oint_{\gamma_{R}}F(z)\,dz = \frac{2\pi i}{3}e^{-2\pi i/3}$ for every $R > 1$.

::: pf-proof
$\gamma_{R}$ is a closed piecewise smooth contour, positively oriented with the sector on its left, and $F$ is holomorphic on a neighbourhood of $S_{R}$ except at the single pole $z_{0}$ inside, by step [](#poles){.pf-ref}. The residue theorem gives the integral as $2\pi i$ times the residue computed in step [](#residue){.pf-ref}.

:::

:::

::: {.pf-step #equation}
$\bigl(1 - e^{2\pi i/3}\bigr)I = \frac{2\pi i}{3}e^{-2\pi i/3}$.

::: pf-proof
By steps [](#rays){.pf-ref} and [](#arc){.pf-ref} the integral over $\gamma_{R}$ is $\int_{0}^{R}\frac{dt}{1+t^{3}} - e^{2\pi i/3}\int_{0}^{R}\frac{dt}{1+t^{3}} + o(1)$ as $R \to \infty$, and by step [](#contour){.pf-ref} it equals the constant $\frac{2\pi i}{3}e^{-2\pi i/3}$ for every $R > 1$. Letting $R \to \infty$ gives the identity.

:::

:::

::: pf-step
$\int_{0}^{\infty}\frac{dt}{t^{3}+1} = \boxed{\frac{2\pi}{3\sqrt3}}$.

::: pf-proof
One has $1 - e^{2\pi i/3} = \frac{3}{2} - \frac{\sqrt3}{2}i = \sqrt3\\,e^{-i\pi/6}$, while $\frac{2\pi i}{3}e^{-2\pi i/3} = \frac{2\pi}{3}e^{i\pi/2 - 2\pi i/3} = \frac{2\pi}{3}e^{-i\pi/6}$. Dividing the identity of step [](#equation){.pf-ref} by $1 - e^{2\pi i/3}$ therefore gives $I = \frac{2\pi/3}{\sqrt3} = \frac{2\pi}{3\sqrt3}$, which is approximately $1.2092$.

:::

:::

:::
:::
