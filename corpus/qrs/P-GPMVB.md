---
schema: qual/card@1
id: P-GPMVB
kind: problem
title: All roots of $z^7-5z^3+12$ lie in the annulus $1<|z|<2$
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
relations: []
review: draft
solved: true
---

::: problem
Prove that all the roots of the complex polynomial

$$z^7 - 5 z^3 +12 =0$$ lie between the circles $|z|=1$ and $|z|=2$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove all roots of $p(z) = z^7 - 5z^3 + 12$ satisfy $1 < \abs{z} < 2$.

<1>1. $p$ has no zeros in $\abs{z} \leq 1$.
Proof: On $\abs{z} = 1$, $\abs{z^7 - 5z^3} \leq \abs{z}^7 + 5\abs{z}^3 = 6 < 12 = \abs{12}$, so by Rouch\'e's theorem applied to $f(z) = 12$ and $g(z) = z^7 - 5z^3$, the functions $12$ and $12 + (z^7 - 5z^3) = p$ have the same number of zeros in $\abs{z} < 1$, namely none; the strict inequality also rules out zeros on $\abs{z} = 1$.

<1>2. $p$ has exactly 7 zeros in $\abs{z} < 2$, counted with multiplicity.
Proof: On $\abs{z} = 2$, $\abs{-5z^3 + 12} \leq 5\abs{z}^3 + 12 = 40 + 12 = 52 < 128 = \abs{z}^7$, so Rouch\'e applied to $f(z) = z^7$ and $g(z) = -5z^3 + 12$ shows $p = z^7 + (-5z^3 + 12)$ has exactly as many zeros in $\abs{z} < 2$ as $z^7$, i.e. $7$.

<1>3. All 7 roots of $p$ lie in the annulus $1 < \abs{z} < 2$.
Proof: $p$ has degree 7, so by the fundamental theorem of algebra it has exactly 7 roots in $\CC$ counting multiplicity.
By <1>2 all of them lie in $\abs{z} < 2$, and by <1>1 none lies in $\abs{z} \leq 1$; hence all lie between the two circles.

<1>4. Q.E.D. Proof: <1>3 is exactly the claim.
:::
