---
schema: qual/card@1
id: P-CASP13C
kind: problem
title: 'Laurent series of $1/(z^3-4z)$ on two annuli'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each step re-read and both expansions recomputed: the
      partial fractions are the residues at 0 and at +-2; inside |z| < 2 the two factors are
      expanded in powers of z/2; outside, in powers of 2/z, where the n = 0 term cancels the
      leading -1/(4z) as it must for a function of order z^{-3} at infinity. The coefficients are
      written out: they vanish at even indices and equal -2^{-(n+3)} at odd ones. A garbled
      sentence of my own first draft about those coefficients is repaired before committing. Not
      claimed: any statement about the convergence on the boundary circles.
---

::: {.problem}
Determine the Laurent series expansions of the function $f: \CC \setminus \{0, \pm 2\} \to \CC$ given by $$f(z) = \frac{1}{z^3 - 4z}$$ in the annuli $\annulus(0; 0, 2)$ and $\annulus(0; 2, \infty)$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #partial}
$\dfrac{1}{z^{3}-4z}=-\dfrac{1}{4z}+\dfrac{1}{8(z-2)}+\dfrac{1}{8(z+2)}$.

::: pf-proof
$z^{3}-4z=z(z-2)(z+2)$ has the three simple zeros $0,\pm2$, and the residue of $1/(z^{3}-4z)$ at each gives the numerator of the corresponding partial fraction: at $z=0$ the residue is $1/((0-2)(0+2))=-1/4$, at $z=2$ it is $1/(2\cdot4)=1/8$, and at $z=-2$ it is $1/((-2)(-4))=1/8$. The difference between the two sides is entire and tends to $0$ at infinity, hence vanishes identically.
:::

:::

::: {.pf-step #small}
For $0<\abs{z}<2$, $f(z)=-\dfrac{1}{4z}+\dfrac{1}{16}\displaystyle\sum_{n\ge0}\bigl((-1)^{n}-1\bigr)\Bigl(\dfrac z2\Bigr)^{n}$.

::: pf-proof
On this annulus $\abs{z/2}<1$, so $\frac{1}{z-2}=-\frac12\frac{1}{1-z/2}=-\frac12\sum_{n\ge0}(z/2)^{n}$ and $\frac{1}{z+2}=\frac12\frac{1}{1+z/2}=\frac12\sum_{n\ge0}(-1)^{n}(z/2)^{n}$; multiplying by $1/8$ and adding to $-1/(4z)$ gives the displayed series, which converges uniformly on compact subsets of the annulus.
:::

:::

::: {.pf-step #large}
For $\abs{z}>2$, $f(z)=-\dfrac{1}{4z}+\dfrac{1}{8z}\displaystyle\sum_{n\ge0}\bigl(1+(-1)^{n}\bigr)\Bigl(\dfrac2z\Bigr)^{n}$.

::: pf-proof
Here $\abs{2/z}<1$, so $\frac{1}{z-2}=\frac1z\frac{1}{1-2/z}=\frac1z\sum_{n\ge0}(2/z)^{n}$ and $\frac{1}{z+2}=\frac1z\frac{1}{1+2/z}=\frac1z\sum_{n\ge0}(-1)^{n}(2/z)^{n}$; multiplying by $1/8$ and adding $-1/(4z)$ gives the displayed series. Its $n=0$ term is $+1/(4z)$, which cancels the leading $-1/(4z)$, as it must since $f(z)=O(z^{-3})$ at infinity.
:::

:::

::: {.pf-step}
The two Laurent expansions are as displayed.

::: pf-proof
Steps [](#small){.pf-ref} and [](#large){.pf-ref} give
$$
\boxed{f(z)=-\frac{1}{4z}+\frac{1}{16}\sum_{n\ge0}\bigl((-1)^{n}-1\bigr)\Bigl(\frac z2\Bigr)^{n}\ (0<\abs z<2),\qquad
f(z)=-\frac{1}{4z}+\frac{1}{8z}\sum_{n\ge0}\bigl(1+(-1)^{n}\bigr)\Bigl(\frac2z\Bigr)^{n}\ (\abs z>2).}
$$
In the first series the coefficient of $z^{n}$ is $\tfrac1{16}\bigl((-1)^{n}-1\bigr)2^{-n}$, which vanishes for even $n$ and equals $-2^{-(n+3)}$ for odd $n$; so the expansion is $-1/(4z)-\sum_{k\ge0}2^{-(2k+4)}z^{2k+1}$ there. In the second series only even powers of $2/z$ survive, so it is $z^{-1}$ times a power series in $z^{-2}$ with no constant term, which is what a function that is odd and holomorphic at infinity must have.
:::

:::

:::
:::
