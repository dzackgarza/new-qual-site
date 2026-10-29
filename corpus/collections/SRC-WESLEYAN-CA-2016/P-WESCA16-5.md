---
schema: qual/card@1
id: P-WESCA16-5
kind: problem
title: 'Conformal maps from a sector disk to a quadrant'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md. Flash garbles part (b) typographically, but the question “How many conformal maps are there between these two sets? Prove it.” is explicit.
---

::: {.problem}
Let
$$
\Omega_1=\{z:|z|<1,\ 0<\arg z<\alpha<2\pi\},
\qquad
\Omega_2=\{x+iy:x,y>0\}.
$$
(a) Find an explicit conformal map $\Omega_1\to\Omega_2$.

(b) How many conformal maps are there between these two domains?
Prove your answer.
:::

::: {.solution}

On $\Omega_1$, use the branch
$$
\Log z=\log|z|+i\arg z,
\qquad
0<\arg z<\alpha,
$$
and define
$$
z^{\pi/\alpha}
=\exp\!\left(\frac{\pi}{\alpha}\Log z\right).
$$

::: pf

::: {.pf-step #s1-1}

The map
$$
P(z)=z^{\pi/\alpha}
$$
is a conformal bijection from $\Omega_1$ onto the upper half-disk
$$
H_1=\{w:|w|<1,\ \operatorname{Im}w>0\}.
$$


::: pf-proof

If $z=re^{i\theta}$ with
$$
0<r<1,
\qquad
0<\theta<\alpha,
$$
then
$$
P(z)=r^{\pi/\alpha}e^{i\pi\theta/\alpha}.
$$
Thus
$$
0<|P(z)|<1,
\qquad
0<\arg P(z)<\pi,
$$
so $P(z)\in H_1$.

Conversely, if $w=\rho e^{i\phi}\in H_1$, then
$$
z=\rho^{\alpha/\pi}e^{i\alpha\phi/\pi}
$$
lies in $\Omega_1$ and satisfies $P(z)=w$. Hence $P$ is bijective.
Its derivative is
$$
P'(z)=\frac{\pi}{\alpha}z^{\pi/\alpha-1},
$$
which never vanishes on $\Omega_1$, so $P$ is conformal.

:::

:::

::: {.pf-step #s1-2}

The Möbius transformation
$$
C(w)=\frac{1+w}{1-w}
$$
is a conformal bijection from $H_1$ onto
$$
\Omega_2=\{\zeta:\operatorname{Re}\zeta>0,\quad
\operatorname{Im}\zeta>0\}.
$$


::: pf-proof

The inverse Möbius transformation is
$$
C^{-1}(\zeta)=\frac{\zeta-1}{\zeta+1}.
$$
Let
$$
w=C^{-1}(\zeta).
$$
Then
$$
|w|<1
\quad\Longleftrightarrow\quad
|\zeta-1|<|\zeta+1|
\quad\Longleftrightarrow\quad
\operatorname{Re}\zeta>0.
$$
Moreover,
$$
\operatorname{Im}w
=\frac{2\operatorname{Im}\zeta}{|\zeta+1|^2}.
$$
Hence
$$
|w|<1,\ \operatorname{Im}w>0
\quad\Longleftrightarrow\quad
\operatorname{Re}\zeta>0,\ \operatorname{Im}\zeta>0.
$$
Thus $C$ maps $H_1$ bijectively onto $\Omega_2$. Being Möbius with no pole on
$H_1$, it is conformal.

:::

:::

::: {.pf-step #s1-3}

An explicit conformal map in part (a) is
$$
\boxed{
F(z)=
\frac{1+z^{\pi/\alpha}}
     {1-z^{\pi/\alpha}} }.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref},
$$
F=C\circ P
$$
is a composition of conformal bijections
$$
\Omega_1\xrightarrow{\ P\ }H_1\xrightarrow{\ C\ }\Omega_2.
$$
Hence it is a conformal bijection from $\Omega_1$ to $\Omega_2$.

:::

:::

::: {.pf-step #s1-4}

There are at least $\mathfrak c$ conformal maps
$\Omega_1\to\Omega_2$.


::: pf-proof

For every real $t>0$, multiplication
$$
\zeta\longmapsto t\zeta
$$
is a conformal automorphism of the first quadrant. Therefore
$$
F_t(z)=tF(z)
$$
is a conformal bijection $\Omega_1\to\Omega_2$. Distinct positive values of
$t$ give distinct maps, and
$$
|(0,\infty)|=\mathfrak c.
$$

:::

:::

::: {.pf-step #s1-5}

There are at most $\mathfrak c$ conformal maps
$\Omega_1\to\Omega_2$.


::: pf-proof

Choose a countable dense subset $Q\subseteq\Omega_1$. A continuous function
on $\Omega_1$ is uniquely determined by its values on $Q$, because equality
on a dense set passes to all points by continuity. Hence restriction gives an
injection from the set of conformal maps into
$$
\Omega_2^Q.
$$
Since
$$
|\Omega_2|=\mathfrak c
\qquad\text{and}\qquad
|Q|=\aleph_0,
$$
one has
$$
|\Omega_2^Q|
=\mathfrak c^{\aleph_0}
=(2^{\aleph_0})^{\aleph_0}
=\mathfrak c.
$$
Thus there are at most $\mathfrak c$ such maps.

:::

:::

::: {.pf-step #s1-6}

The answer to part (b) is
$$
\boxed{\mathfrak c\text{ conformal maps}}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives the lower bound and step [](#s1-5){.pf-ref} gives the upper bound.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} gives the explicit map requested in part (a), and step [](#s1-6){.pf-ref} answers
part (b).

:::

:::

:::
