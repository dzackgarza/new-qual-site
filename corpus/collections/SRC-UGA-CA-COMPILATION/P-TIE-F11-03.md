---
schema: qual/card@1
id: P-TIE-F11-03
kind: problem
title: Lagrange inversion for $z-a-qf(z)=0$ via the residue theorem
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2011, question 3.
---

::: {.problem}
Suppose that f is an analytic function in the region D which contains the point a. Let

$$
F ( z ) = z - a - q f ( z ) , \quad { \mathrm { w h e r e } } \quad q { \mathrm { ~ i s ~ a ~ c o m p l e x ~ p a r a m e t e r . } }
$$

(1) Let $K \subset D$ be a circle with the center at point a and also we assume that $f ( z ) \neq 0$ for $z \in K$ . Prove that the function F has one and only one zero $z = w$ on the closed disc K whose boundary is the circle K if $\abs{ q } < \operatorname* { m i n } _ { z \in K } { \frac { \abs{ z - a } } { \abs{ f ( z ) } } }$

(2) Let $G ( z )$ be an analytic function on the disk K. Apply the residue theorem to prove that $\frac { G ( w ) } { F ^ { \prime } ( w ) } = \frac { 1 } { 2 \pi i } \int _ { K } \frac { G ( z ) } { F ( z ) }$ dz, where w is the zero from (1).

(3) $\mathrm { I f } ~ z \in { K }$ , prove that the function $\displaystyle \frac { 1 } { F ( z ) }$ can be represented as a convergent series with respect to $q \colon { \frac { 1 } { F ( z ) } } = \sum _ { n = 0 } ^ { \infty } { \frac { ( q f ( z ) ) ^ { n } } { ( z - a ) ^ { n + 1 } } }$
:::

::: {.solution}

Write
$$
K=\{z:\abs{z-a}=\rho\},
$$
let $\Delta$ be its interior, orient $K$ positively, and set
$$
m\coloneqq\min_{z\in K}\frac{\abs{z-a}}{\abs{f(z)}}.
$$
The hypothesis is $\abs{q}<m$.

::: pf

::: {.pf-step #s1-1}

On $K$ one has
$$
\abs{qf(z)}<\abs{z-a}.
$$


::: pf-proof

For $z\in K$,
$$
\frac{\abs{z-a}}{\abs{f(z)}}\ge m>\abs{q}.
$$
Since $f(z)\ne0$ on $K$, multiplication by $\abs{f(z)}$ gives the asserted inequality.

:::

:::

::: {.pf-step #s1-2}

The function $F(z)=z-a-qf(z)$ has exactly one zero $w$ in $\Delta$, counted with multiplicity; in particular, $w$ is simple and $F'(w)\ne0$.


::: pf-proof

On $K$, step [](#s1-1){.pf-ref} gives
$$
\abs{F(z)-(z-a)}
=
\abs{qf(z)}
<
\abs{z-a}.
$$
Rouché's theorem therefore implies that $F$ and $z-a$ have the same number of zeros in $\Delta$, counted with multiplicity. The function $z-a$ has exactly one zero there, of multiplicity one. Hence $F$ also has exactly one zero $w$, its multiplicity is one, and thus $F'(w)\ne0$. The strict boundary inequality also shows that $F$ has no zero on $K$.

:::

:::

::: {.pf-step #s1-3}

For $G$ as in part (2),
$$
\boxed{
\frac{G(w)}{F'(w)}
=
\frac{1}{2\pi i}\int_K\frac{G(z)}{F(z)}\,dz.
}
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, $G/F$ is meromorphic on $\Delta$ with a single pole, at the simple zero $w$ of $F$. Its residue there is
$$
\operatorname{Res}_{z=w}\frac{G(z)}{F(z)}
=
\frac{G(w)}{F'(w)}.
$$
The residue theorem gives
$$
\int_K\frac{G(z)}{F(z)}\,dz
=
2\pi i\frac{G(w)}{F'(w)},
$$
which is the displayed identity.

:::

:::

::: {.pf-step #s1-4}

For $z\in K$,
$$
\abs{\frac{qf(z)}{z-a}}
\le
\frac{\abs{q}}{m}
<1.
$$


::: pf-proof

By the definition of $m$,
$$
\frac{\abs{z-a}}{\abs{f(z)}}\ge m
$$
for every $z\in K$. Taking reciprocals and multiplying by $\abs{q}$ gives the stated estimate.

:::

:::

::: {.pf-step #s1-5}

For every $z\in K$,
$$
\boxed{
\frac1{F(z)}
=
\sum_{n=0}^{\infty}
\frac{(qf(z))^n}{(z-a)^{n+1}}.
}
$$
Moreover, the series converges uniformly on $K$.


::: pf-proof

Since $z\ne a$ on $K$,
$$
\frac1{F(z)}
=
\frac1{z-a}
\frac1{1-\frac{qf(z)}{z-a}}.
$$
By step [](#s1-4){.pf-ref}, the quantity $qf(z)/(z-a)$ has modulus at most the constant $\abs{q}/m<1$. Hence the geometric series gives
$$
\frac1{1-\frac{qf(z)}{z-a}}
=
\sum_{n=0}^{\infty}
\left(\frac{qf(z)}{z-a}\right)^n.
$$
Multiplying by $1/(z-a)$ yields the displayed expansion. The bound in step [](#s1-4){.pf-ref} is uniform in $z\in K$, so the geometric series converges uniformly on $K$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (1), step [](#s1-3){.pf-ref} proves part (2), and step [](#s1-5){.pf-ref} proves part (3).

:::

:::

:::
