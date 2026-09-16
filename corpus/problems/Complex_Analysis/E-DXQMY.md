---
schema: qual/card@1
id: E-DXQMY
kind: problem
title: Schwarz-Pick Lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Prove the following:
suppose $\abs{f(z)}\leq 1$, then for all $z, w\in \DD$,
\[
\left|\frac{f(z)-f(w)}{1-\overline{f(w)} f(z)}\right| \leq\left|\frac{z-w}{1-\bar{w} z}\right|
\quad\text{ and }
\left|f^{\prime}(z)\right| \leq \frac{1-|f(z)|^{2}}{1-|z|^{2}}
.\]
If equality holds for some $z\neq w$ in either expression, then $f= \lambda F$ where $F$ is a linear fractional transformation and $\abs{\lambda} = 1$, so $f\in \Aut(\DD)$.

> Note that this does not require $f(0) = 0$.

:::

::: {.proof title="of Schwarz-Pick"}

![](../../assets/figures/2021-11-27_00-55-19.png)

![](../../assets/Complex_Analysis/060_Maps%20of%20Disc/figures/2021-12-14_01-48-57.png)

:::

::: {.solution}
For $a\in\mathbb D$, write
\[
\phi_a(\zeta)=\frac{a-\zeta}{1-\overline a\zeta}.
\]
This is an automorphism of $\mathbb D$, interchanging $0$ and $a$.

Fix $w\in\mathbb D$ and define
\[
g=\phi_{f(w)}\circ f\circ\phi_w.
\]
Then $g:\mathbb D\to\mathbb D$ is holomorphic and $g(0)=0$. Schwarz's lemma
therefore gives $|g(\zeta)|\le|\zeta|$. Taking $\zeta=\phi_w(z)$ and using
$\phi_w^{-1}=\phi_w$ yields
\[
\left|\frac{f(z)-f(w)}{1-\overline{f(w)}f(z)}\right|
\le
\left|\frac{z-w}{1-\overline wz}\right|.
\]

Divide by $|z-w|$ and let $z\to w$. Since
\[
\left|\frac{z-w}{1-\overline wz}\right|
=\frac{|z-w|}{|1-\overline wz|},
\]
we obtain
\[
\frac{|f'(w)|}{1-|f(w)|^2}
\le\frac1{1-|w|^2},
\]
or equivalently
\[
|f'(w)|\le\frac{1-|f(w)|^2}{1-|w|^2}.
\]

If equality holds in the two-point inequality for some distinct $z,w$, then
Schwarz's lemma has equality at a nonzero point for the corresponding $g$, so
$g(\zeta)=\lambda\zeta$ with $|\lambda|=1$. Thus $f$ is a composition of disk
automorphisms and is itself in $\operatorname{Aut}(\mathbb D)$. The same
conclusion follows if equality holds in the derivative inequality at one point,
by the derivative equality case of Schwarz's lemma.
:::
