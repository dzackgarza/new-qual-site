---
schema: qual/card@1
id: E-SS9.EX-2
kind: problem
title: The zeros minus the poles of an elliptic function lie in the period lattice
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the translation of the parallelogram, the logarithmic
    derivative and its residue count, the pairing of opposite sides by periodicity, and the conclusion that
    the sum is a period. No retained solution set covers this exercise (the collection retains the textbook,
    not a solutions manual), so the argument is the card's own.
---

::: {.exercise}
Suppose that $a_1, \ldots, a_r$ and $b_1, \ldots, b_r$ are the zeros and poles, respectively, in the fundamental parallelogram of an elliptic function $f$. Show that
$$
a_1 + \cdots + a_r - b_1 - \cdots - b_r = n\omega_1 + m\omega_2
$$
for some integers $n$ and $m$.

[Hint: If the boundary of the parallelogram contains no zeros or poles, simply integrate $zf'(z)/f(z)$ over that boundary, and observe that the integral of $f'(z)/f(z)$ over a side is an integer multiple of $2\pi i$. If there are zeros or poles on the side of the parallelogram, translate it by a small amount to reduce the problem to the first case.]
:::

::: {.solution}
No retained solution set covers this exercise; the collection retains the textbook (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`) and no solutions manual, so the argument is the card's own. Write $f$ for the elliptic function with periods $\omega_{1},\omega_{2}$ and $P$ for its fundamental parallelogram.

::: pf

::: {.pf-step #translate}
$P$ may be translated so that its boundary contains no zero and no pole of $f$.

::: pf-proof
The zeros and poles of an elliptic function are finite in number in a fundamental parallelogram, since $f$ is meromorphic and not identically zero. A translate of the boundary can therefore be chosen avoiding the finitely many resulting lattice points: only countably many translations put a given zero or pole on the boundary, and among uncountably many choices one avoids all of them. The translated parallelogram is again a fundamental domain for the same lattice.
:::

:::

::: {.pf-step #residues}
$\dfrac{1}{2\pi i}\displaystyle\int_{\partial P} z\,g(z)\,dz=\sum_{j}a_{j}-\sum_{j}b_{j}$, where $g=f'/f$.

::: pf-proof
$g=f'/f$ is meromorphic with simple poles exactly at the zeros and poles of $f$: near a zero of order $m$ at $a$ one has $f(z)=(z-a)^{m}h$ with $h$ nonzero, so $g=m/(z-a)+(\text{regular})$ and $zg=ma/(z-a)+(\text{regular})$, with residue $ma$; near a pole of order $m$ at $b$ the same computation gives $-mb$. Since $\partial P$ contains none of these points, the residue theorem applies and sums these residues, giving the displayed total when zeros and poles are counted with multiplicity.
:::

:::

::: {.pf-step #pairs}
The two pairs of opposite sides contribute $-m\omega_{2}-n\omega_{1}$ multiples of $2\pi i$.

::: pf-proof
Periodicity $g(z+\omega_{2})=g(z)$ pairs the bottom side, parametrized $z=z_{0}+t\omega_{1}$, with the oppositely oriented top side $z=z_{0}+\omega_{2}+t\omega_{1}$:
$$
\int_{\text{bottom}}zg(z)dz+\int_{\text{top}}zg(z)dz=\int_{0}^{1}\bigl[(z_{0}+t\omega_{1})-(z_{0}+\omega_{2}+t\omega_{1})\bigr]g(z_{0}+t\omega_{1})\,\omega_{1}dt=-\omega_{2}\int_{\text{bottom}}g(z)\,dz,
$$
where the minus sign comes from the opposite orientation of the top side. Similarly the left and right sides pair to give $+\omega_{1}\int_{\text{left}}g(z)dz$.
:::

:::

::: {.pf-step}
$\sum_{j}a_{j}-\sum_{j}b_{j}=n\omega_{1}+m\omega_{2}$ with $n,m\in\ZZ$.

::: pf-proof
By step [](#pairs){.pf-ref}, $\frac{1}{2\pi i}\int_{\partial P}zg(z)dz=-\frac{\omega_{2}}{2\pi i}\int_{\text{bottom}}g\,dz+\frac{\omega_{1}}{2\pi i}\int_{\text{left}}g\,dz$. Each of $\frac{1}{2\pi i}\int g\,dz$ over a closed loop counts the zeros minus the poles of $f$ inside, an integer, because $g$ is the logarithmic derivative; so the first coefficient is an integer $m$ and the second an integer $n$. With step [](#residues){.pf-ref} this gives $a_{1}+\cdots+a_{r}-b_{1}-\cdots-b_{r}=n\omega_{1}+m\omega_{2}$, as claimed.
:::

:::

:::
:::
