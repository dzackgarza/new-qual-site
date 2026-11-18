---
schema: qual/card@1
id: P-CASP06A
kind: problem
title: "Analytic hull properties: distance to boundary and containment in convex hull"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $\Omega$ be an open subset of $\CC$.
For a compact subset $K$ of $\Omega$, define the hull $$\hat{K} = \{z \in \Omega : \abs{f(z)} \leq \sup_{w \in K} \abs{f(w)}, \text{ for every } f \in \mathcal{O}(\Omega)\}.$$ Let $\hat{K}_c$ be the convex hull of $K$, namely the smallest convex subset of $\CC$ containing $K$.
Show that

(a) $d(K, \CC \setminus \Omega) = d(\hat{K}, \CC \setminus \Omega)$;

(b) $\hat{K} \subset \hat{K}_c$.

Hint: A set $S \subset \CC$ is convex if and only if $tz_1 + (1-t)z_2 \in S$ for all $t \in [0,1]$ whenever $z_1, z_2 \in S$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the one inequality from $K\subseteq\widehat K$, the reciprocal-function estimate and the separation argument for (b) as separate steps.

Let $\Omega\subseteq\CC$ be open, $K\Subset\Omega$ compact, and $\widehat K=\theset{z\in\Omega\mid \abs{f(z)}\le\sup_K\abs f\ \text{for all}\ f\in\mathcal O(\Omega)}$.

::: pf

::: {.pf-step #one-way}
$d(\widehat K,\CC\setminus\Omega)\le d(K,\CC\setminus\Omega)$.

::: pf-proof
$K\subseteq\widehat K$, because for $z\in K$ the inequality $\abs{f(z)}\le\sup_K\abs f$ is trivial. The distance to a fixed closed set is monotone under inclusion, so the inequality follows.
:::

:::

::: {.pf-step #reverse}
$d(\widehat K,\CC\setminus\Omega)\ge d(K,\CC\setminus\Omega)$.

::: pf-proof
Fix $a\in\CC\setminus\Omega$; then $f(z)=1/(z-a)$ is holomorphic on $\Omega$. Put $\delta=\inf_{w\in K}\abs{w-a}$, so $\delta\ge d(K,\CC\setminus\Omega)$. For $z\in\widehat K$ the defining inequality gives $\frac{1}{\abs{z-a}}\le\sup_{w\in K}\frac{1}{\abs{w-a}}=\frac1\delta$, hence $\abs{z-a}\ge\delta$. So every $z\in\widehat K$ satisfies $\abs{z-a}\ge d(K,\CC\setminus\Omega)$, and taking the infimum over $z$ and then over $a$ gives the reverse inequality.
:::

:::

::: {.pf-step #separation}
If $z_{0}\notin K_{c}$, the convex hull of $K$, then $z_{0}\notin\widehat K$.

::: pf-proof
$K_{c}$ is compact and convex, so a point outside it is strictly separated: there is $\zeta\in\CC\setminus\{0\}$ with $\operatorname{Re}(\zeta z_{0})>\sup_{w\in K}\operatorname{Re}(\zeta w)$ (supporting-line form of the Hahn–Banach theorem for a compact convex set). The exponential $f(w)=e^{\zeta w}$ is entire, hence in $\mathcal O(\Omega)$, and $\abs{f(w)}=e^{\operatorname{Re}(\zeta w)}$; therefore $\abs{f(z_{0})}=e^{\operatorname{Re}(\zeta z_{0})}>e^{\sup_K\operatorname{Re}(\zeta w)}=\sup_K\abs f$, so $z_{0}$ fails the defining condition of $\widehat K$.
:::

:::

::: {.pf-qed}
(a) is steps [](#one-way){.pf-ref} and [](#reverse){.pf-ref}. (b): by step [](#separation){.pf-ref} the complement of $K_{c}$ is contained in the complement of $\widehat K$, that is $\widehat K\subseteq K_{c}=\overline{\mathrm{conv}}(K)$.
:::

:::

:::
