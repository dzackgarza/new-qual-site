---
schema: qual/card@1
id: P-FC62S
kind: problem
title: Every functional on a reflexive Banach space attains its norm; a counterexample
  in $\ell^1$
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Norms
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and an unsupported citation replaced. The solution opened "By problem 11 in Jan 2017, we see the Ball B of X is weak compact", which cites another examination problem instead of giving an argument; the card now states and applies the actual theorem (Banach-Alaoglu plus reflexivity for weak compactness of the unit ball, with the canonical map X -> X** onto), and says which topology makes phi and |phi| continuous and why. The attainment step now runs the two-sided inequality that pins |phi(x)| = ||phi||, the norm-one claim derives ||x|| >= 1 rather than asserting it, and the rotation is justified. The counterexample keeps f = (1 - 1/n) in l_infinity = l_1* and now proves the strict inequality by exhibiting the nonzero coordinate alpha_{n_0} and the positive difference sum |alpha_n|/n. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own.
---

::: {.problem}
Assume that $X$ is a reflexive Banach space and $\phi$ is a continuous linear functional on $X$.
Prove that $\phi$ achieves its norm; that is, prove that there is a norm one vector $x$ in $X$ such that $\phi(x)=\norm{\phi}$.
Show by example that there is a continuous linear functional on the Banach space $\ell_1$ that does not achieve its norm.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own. The card previously cited "problem 11 in Jan 2017" for the weak compactness of the unit ball; that citation is not a justification, so the theorem it stood for is now stated and used.

Write $B_X=\{y\in X:\norm y\le1\}$ and let $X$ be over $\CC$ (for a real space replace the rotation below by multiplication by $\pm1$).

::: pf

::: {.pf-step #ball}
$B_X$ is weakly compact, and $\phi$ and $\abs\phi$ are weakly continuous on $X$.

::: pf-proof
By the Banach-Alaoglu theorem the closed unit ball of $X^*$ is weak-star compact; the hypothesis that $X$ is reflexive means that the canonical map $X\to X^{**}$ is onto, and then $B_X$ is the image of $B_{X^{**}}$, so it is weak-star compact in $X^{**}$ and therefore weakly compact in $X$. Every $\phi\in X^*$ is continuous for the weak topology, that topology being the weakest one making all elements of $X^*$ continuous; and $z\mapsto\abs z$ is continuous on $\CC$, so $\abs\phi$ is weakly continuous as a composite.
:::

:::

::: {.pf-step #attains}
There is $x\in B_X$ with $\abs{\phi(x)}=\norm\phi$.

::: pf-proof
$B_X$ is weakly compact and $\abs\phi$ is weakly continuous (step [](#ball){.pf-ref}), so $\abs\phi$ attains its maximum on $B_X$: there is $x\in B_X$ with
$$
\abs{\phi(x)}=\max_{y\in B_X}\abs{\phi(y)}\ge\sup\{\abs{\phi(y)}:\norm y\le1\}=\norm\phi .
$$
(Here $\norm\phi$, the operator norm, is the supremum of $\abs{\phi(y)}$ over $B_X$ — the same supremum.) Conversely $\abs{\phi(x)}\le\norm\phi\norm x\le\norm\phi$, so the two are equal.
:::

:::

::: {.pf-step #normone}
If $\phi\ne0$ the point $x$ above has $\norm x=1$, and a rotation of it satisfies the requirement.

::: pf-proof
$\abs{\phi(x)}=\norm\phi$ and $\abs{\phi(x)}\le\norm\phi\norm x$ give $\norm x\ge1$ when $\norm\phi>0$; with $\norm x\le1$ this forces $\norm x=1$. Choose $\theta$ with $e^{i\theta}\phi(x)=\abs{\phi(x)}$ (multiplying a nonzero complex number by $e^{i\theta}$ rotates its phase to $0$); then $\phi(e^{i\theta}x)=\abs{\phi(x)}=\norm\phi$ and $\norm{e^{i\theta}x}=1$. For $\phi=0$ any norm-one vector serves.
:::

:::

::: {.pf-step #counterexample}
On $\ell_1$ the functional $f=(\alpha_n)\mapsto\sum_n(1-1/n)\alpha_n$, given by the element $(1-1/n)_n\in\ell_\infty=\ell_1^*$, has norm $1$ and $\abs{f(x)}<1$ for every $x$ with $\norm x_1=1$.

::: pf-proof
$\norm f_\infty=\sup_n(1-1/n)=1$, and the dual of $\ell_1$ is $\ell_\infty$ with $\norm f=\norm{(1-1/n)}_\infty=1$. Let $x=(\alpha_n)$ with $\sum_n\abs{\alpha_n}=1$. Then $\alpha_{n_0}\ne0$ for some $n_0$, and
$$
\abs{f(x)}=\abs{\sum_n(1-1/n)\alpha_n}\le\sum_n(1-1/n)\abs{\alpha_n}=\sum_n\abs{\alpha_n}-\sum_n\frac{\abs{\alpha_n}}{n}\le1-\frac{\abs{\alpha_{n_0}}}{n_0}<1,
$$
using $(1-1/n)<1$ for every $n$. So no vector of norm $1$ attains $\norm f=1$, and $\norm x\ge1$ is needed to reach it by the same estimate.
:::

:::

::: {.pf-step}
Reflexivity forces norm attainment, and $\ell_1$ is not reflexive in this sense.

::: pf-proof
Steps [](#attains){.pf-ref} and [](#normone){.pf-ref} prove the first assertion; step [](#counterexample){.pf-ref} exhibits a functional on $\ell_1$ that does not achieve its norm, which shows in particular that the reflexivity hypothesis cannot be dropped.
:::

:::

:::
:::
