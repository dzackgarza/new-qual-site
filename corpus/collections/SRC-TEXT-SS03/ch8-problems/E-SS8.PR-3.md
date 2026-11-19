---
schema: qual/card@1
id: E-SS8.PR-3
kind: problem
title: Hyperbolic metric on the disc and the Schwarz-Pick lemma
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, one per part with the converse of (b)
    last. Added the reasons the argument needs: that preserving d is the same as preserving delta
    because t -> (1/2) log((1+t)/(1-t)) is strictly increasing, which the prose used silently when it
    passed between the two; that delta(z,w)^2 as a function of c = cos(arg z - arg w) is strictly
    monotone, its derivative having the sign of -(1-r^2)(1-s^2), which is what makes c determined by
    r, s and delta; and that the substitution in (d) is legitimate without assuming r(t) monotone,
    since the antiderivative is evaluated at the endpoints. Checked the equality case in (d) (the
    radial segment) and that delta < 1 for points of the disc, which is what lets (d) be applied to
    delta. Not checked: the printed problem, which was not re-read in this pass.
---

::: {.exercise}
The Schwarz-Pick lemma (see Exercise 13) is the infinitesimal version of an important observation in complex analysis and geometry.

For complex numbers $w \in \CC$ and $z \in \DD$ we define the hyperbolic length of $w$ at $z$ by

$$
\norm{ w } _ {z} = \frac{\abs{ w }}{1 - \abs{ z } ^ {2}},
$$

where $\abs{w}$ and $\abs{z}$ denote the usual absolute values.
This length is sometimes referred to as the Poincaré metric, and as a Riemann metric it is written as

$$
d s ^ {2} = \frac{\abs{ d z } ^ {2}}{(1 - \abs{ z } ^ {2}) ^ {2}}.
$$

The idea is to think of $w$ as a vector lying in the tangent space at $z$.
Observe that for a fixed $w$, its hyperbolic length grows to infinity as $z$ approaches the boundary of the disc.
We pass from the infinitesimal hyperbolic length of tangent vectors to the global hyperbolic distance between two points by integration.

(a) Given two complex numbers $z_1$ and $z_2$ in the disc, we define the hyperbolic distance between them by

$$
d (z_1, z_2) = \inf_ {\gamma} \int_ {0} ^ {1} \norm{ \gamma' (t) } _ {\gamma (t)} d t,
$$

where the infimum is taken over all smooth curves $\gamma : [0, 1] \to \DD$ joining $z_1$ and $z_2$.
Use the Schwarz-Pick lemma to prove that if $f : \DD \to \DD$ is holomorphic, then

$$
d (f (z_1), f (z_2)) \leq d (z_1, z_2) \quad \text{for any } z_1, z_2 \in \DD.
$$

In other words, holomorphic functions are distance-decreasing in the hyperbolic metric.

(b) Prove that automorphisms of the unit disc preserve the hyperbolic distance, namely

$$
d (\varphi (z_1), \varphi (z_2)) = d (z_1, z_2), \quad \text{for any } z_1, z_2 \in \DD
$$

and any automorphism $\varphi$.
Conversely, if $\varphi : \DD \to \DD$ preserves the hyperbolic distance, then either $\varphi$ or $\overline{\varphi}$ is an automorphism of $\DD$.

(c) Given two points $z_1, z_2 \in \DD$, show that there exists an automorphism $\varphi$ such that $\varphi(z_1) = 0$ and $\varphi(z_2) = s$ for some $s$ on the segment $[0, 1)$ on the real line.

(d) Prove that the hyperbolic distance between $0$ and $s \in [0, 1)$ is

$$
d (0, s) = \frac{1}{2} \log \frac{1 + s}{1 - s}.
$$

(e) Find a formula for the hyperbolic distance between any two points in the unit disc.
:::

::: {.solution}
This is Stein--Shakarchi, Chapter 8, Problem 3, parts (a)--(e). No published solution set is transcribed: the argument is the card's own, and the Schwarz--Pick lemma in the infinitesimal form (Exercise 13 of the same chapter) is used as given.

::: pf

::: {.pf-step #a}
(a) If $f\colon\DD\to\DD$ is holomorphic then $d(f(z_{1}),f(z_{2}))\leq d(z_{1},z_{2})$ for all $z_{1},z_{2}\in\DD$.

::: pf-proof
The Schwarz--Pick lemma gives $\frac{\abs{f'(z)}}{1-\abs{f(z)}^{2}}\leq\frac{1}{1-\abs{z}^{2}}$ for $z\in\DD$. For a smooth curve $\gamma$ one has $(f\circ\gamma)'(t)=f'(\gamma(t))\gamma'(t)$, so the hyperbolic speed of $f\circ\gamma$ at $t$ is at most that of $\gamma$ at $t$; integrating gives $\operatorname{length}(f\circ\gamma)\leq\operatorname{length}(\gamma)$. Taking the infimum over curves joining $z_{1}$ to $z_{2}$, and using that $f\circ\gamma$ joins $f(z_{1})$ to $f(z_{2})$, gives $d(f(z_{1}),f(z_{2}))\leq d(z_{1},z_{2})$.
:::
:::

::: {.pf-step #aut}
(b) An automorphism $\varphi$ of $\DD$ satisfies $d(\varphi(z_{1}),\varphi(z_{2}))=d(z_{1},z_{2})$.

::: pf-proof
$\varphi$ and $\varphi^{-1}$ are both holomorphic self-maps of $\DD$, so step [](#a){.pf-ref} gives $d(\varphi z_{1},\varphi z_{2})\leq d(z_{1},z_{2})$ and, applied to $\varphi^{-1}$, $d(z_{1},z_{2})\leq d(\varphi z_{1},\varphi z_{2})$. Hence equality.
:::
:::

::: {.pf-step #c}
(c) For $z_{1},z_{2}\in\DD$ there is an automorphism $\varphi$ with $\varphi(z_{1})=0$ and $\varphi(z_{2})=s\in[0,1)$.

::: pf-proof
$\phi_{z_{1}}(z)=\frac{z-z_{1}}{1-\overline{z_{1}}z}$ is an automorphism of $\DD$ sending $z_{1}$ to $0$. If $\phi_{z_{1}}(z_{2})=re^{i\theta}$, then $\varphi(z)=e^{-i\theta}\phi_{z_{1}}(z)$ is again an automorphism, being a rotation composed with one, and it sends $z_{1}$ to $0$ and $z_{2}$ to $r=\abs{\phi_{z_{1}}(z_{2})}\in[0,1)$.
:::
:::

::: {.pf-step #d}
(d) $d(0,s)=\frac12\log\frac{1+s}{1-s}$ for $s\in[0,1)$.

::: pf-proof
Let $\gamma(t)=r(t)e^{i\theta(t)}$ join $0$ to $s$, so $r(0)=0$ and $r(1)=s$. Since $\abs{\gamma'}\geq\abs{r'}$,
$$\int_{0}^{1}\frac{\abs{\gamma'(t)}}{1-r(t)^{2}}\,dt\geq\int_{0}^{1}\frac{\abs{r'(t)}}{1-r(t)^{2}}\,dt\geq\abs{\int_{0}^{1}\frac{r'(t)}{1-r(t)^{2}}\,dt}=\abs{\int_{0}^{s}\frac{dr}{1-r^{2}}}=\frac12\log\frac{1+s}{1-s},$$
the substitution being legitimate without monotonicity because the antiderivative $\frac12\log\frac{1+r}{1-r}$ is evaluated at the endpoints. The radial segment $r(t)=ts$ attains equality, so the infimum is the displayed value.
:::
:::

::: {.pf-step #e}
(e) $d(z,w)=\frac12\log\frac{1+\delta}{1-\delta}$ with $\delta=\abs{\frac{z-w}{1-\overline{w}z}}$.

::: pf-proof
By step [](#aut){.pf-ref} the hyperbolic distance is invariant under the automorphism $\phi_{w}$, and $\phi_{w}(w)=0$, $\abs{\phi_{w}(z)}=\delta(z,w)$. So $d(z,w)=d(0,\delta)$, and step [](#d){.pf-ref} applies since $\delta<1$ for $z,w\in\DD$, the strict inequality being the Schwarz--Pick estimate for $\phi_{w}$.
:::
:::

::: {.pf-step #converse}
(b) If $\varphi\colon\DD\to\DD$ preserves the hyperbolic distance, then $\varphi$ or $\overline{\varphi}$ is an automorphism of $\DD$.

::: pf-proof
Since $t\mapsto\frac12\log\frac{1+t}{1-t}$ is strictly increasing on $[0,1)$, step [](#e){.pf-ref} shows that preserving $d$ is the same as preserving $\delta$. Choose an automorphism $A$ with $A(\varphi(0))=0$ and put $S=A\circ\varphi$; then $S$ preserves $\delta$ and fixes $0$, and $\delta(0,z)=\abs{z}$ gives $\abs{S(z)}=\abs{z}$. For $\abs{z}=r,\abs{w}=s$ and $c=\cos(\arg z-\arg w)$ one has
$$\delta(z,w)^{2}=\frac{r^{2}+s^{2}-2rsc}{1+r^{2}s^{2}-2rsc},$$
whose right side is strictly monotone in $c$, since its derivative has the sign of $-\bigl(1-r^{2}\bigr)\bigl(1-s^{2}\bigr)<0$; so $c$ is determined by $r,s,\delta$. As $S$ preserves $r,s$ and $\delta$, it preserves $c$ for every pair, hence preserves the Euclidean inner products $\operatorname{Re}(z\overline{w})$ and therefore Euclidean distances. Then $S$ is a Euclidean isometry of the disc fixing $0$, so it is the restriction of an orthogonal map, that is $S(z)=e^{i\theta}z$ or $S(z)=e^{i\theta}\overline{z}$. Hence $\varphi=A^{-1}\circ S$ is an automorphism or the conjugate of one.
:::
:::
:::

:::
