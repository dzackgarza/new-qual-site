---
schema: qual/card@1
id: E-DXQMY
kind: problem
title: Schwarz--Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
  - Fractional Linear Transformations
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "suppose $\abs{f(z)}\leq 1$" without requiring $f$ holomorphic, and allows $\abs{f}=1$, where the left side can be $0/0$; it also states the equality case "for some $z\neq w$ in either expression". The statement now takes $f:\DD\to\DD$ holomorphic and states the equality case for $z\neq w$ in the first inequality and for a single $z$ in the second.'
---

::: {.exercise}
Prove the following:
suppose $f:\DD\to\DD$ is holomorphic. Then for all $z, w\in \DD$,
$$
\abs{\frac{f(z)-f(w)}{1-\overline{f(w)} f(z)}} \leq\abs{\frac{z-w}{1-\bar{w} z}}
\quad\text{ and }\quad
\abs{f'(z)} \leq \frac{1-\abs{f(z)}^{2}}{1-\abs{z}^{2}}.
$$
If equality holds in the first inequality for some $z\neq w$, or in the second for some $z$, then $f= \lambda F$ where $F$ is a linear fractional transformation and $\abs{\lambda} = 1$, so $f\in \Aut(\DD)$.
:::

::: {.solution}

![](../../assets/figures/2021-11-27_00-55-19.png)

![](../../assets/Complex_Analysis/060_Maps%20of%20Disc/figures/2021-12-14_01-48-57.png)

:::

::: {.solution}
For $a\in\DD$, write
$$
\phi_a(\zeta)=\frac{a-\zeta}{1-\overline a\zeta}.
$$
This is an automorphism of $\DD$ that interchanges $0$ and $a$ and satisfies $\phi_a^{-1}=\phi_a$.

::: pf

::: {.pf-step #schwarz-setup}
Fix $w\in\DD$ and put $g=\phi_{f(w)}\circ f\circ\phi_w$. Then $g:\DD\to\DD$ is holomorphic, $g(0)=0$, and $\abs{g(\zeta)}\le\abs{\zeta}$ for all $\zeta\in\DD$.

::: pf-proof
$g(0)=\phi_{f(w)}(f(w))=0$, and the inequality is Schwarz's lemma.
:::

:::

::: {.pf-step #two-point}
For all $z,w\in\DD$,
$$
\abs{\frac{f(z)-f(w)}{1-\overline{f(w)}f(z)}}
\le
\abs{\frac{z-w}{1-\overline wz}}.
$$

::: pf-proof
Take $\zeta=\phi_w(z)$ in step [](#schwarz-setup){.pf-ref}. Since $\phi_w(\zeta)=z$, this gives $\abs{\phi_{f(w)}(f(z))}\le\abs{\phi_w(z)}$, which is the claim.
:::

:::

::: {.pf-step #derivative}
For all $w\in\DD$,
$$
\abs{f'(w)}\le\frac{1-\abs{f(w)}^2}{1-\abs{w}^2}.
$$

::: pf-proof
Divide the inequality of step [](#two-point){.pf-ref} by $\abs{z-w}$ and let $z\to w$. The left side tends to $\abs{f'(w)}/(1-\abs{f(w)}^2)$ and the right side to $1/(1-\abs{w}^2)$.
:::

:::

::: pf-step
If equality holds in step [](#two-point){.pf-ref} for some $z\neq w$, or in step [](#derivative){.pf-ref} for some $w$, then $f\in\Aut(\DD)$.

::: pf-proof
Equality in step [](#two-point){.pf-ref} with $z\neq w$ is equality $\abs{g(\zeta)}=\abs{\zeta}$ at the nonzero point $\zeta=\phi_w(z)$. Equality in step [](#derivative){.pf-ref} is equality $\abs{g'(0)}=1$, since $g'(0)=\phi_{f(w)}'(f(w))\,f'(w)\,\phi_w'(0)$ with $\abs{\phi_a'(a)}=1/(1-\abs a^2)$ and $\abs{\phi_a'(0)}=1-\abs a^2$.
In either case the equality case of Schwarz's lemma gives $g(\zeta)=\lambda\zeta$ with $\abs\lambda=1$. Hence $f=\phi_{f(w)}\circ g\circ\phi_w$ is a composition of disk automorphisms, so $f$ is a linear fractional transformation in $\Aut(\DD)$.
:::

:::

:::

:::

::: {.remark}
The lemma does not require $f(0) = 0$.
:::
