---
schema: qual/card@1
id: P-CASP17E
kind: problem
title: 'Holomorphic functions on $\DD$ with $f(0)=1$ and $\Re f>0$ form a normal family'
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Montel
relations: []
review: draft
---

::: {.problem}
Let $\mathcal{F}$ be the family of holomorphic functions $f : \DD \to \CC$ defined over the open unit disc with $f(0) = 1$ and $\operatorname{Re} f > 0$.
Show that $\mathcal{F}$ is a normal family.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own argument follows, with the Cayley transform, Schwarz's lemma and the resulting bound separated.

::: pf

::: {.pf-step #cayley}
For $f\in\mathcal{F}$ the function $\phi_{f}(z)=\dfrac{f(z)-1}{f(z)+1}$ is holomorphic on $\DD$ with values in $\DD$ and $\phi_{f}(0)=0$.

::: pf-proof
$f$ is holomorphic and $f(z)+1\ne0$ on $\DD$ because $\operatorname{Re}f>0$ forces $f(z)\ne-1$; so $\phi_{f}$ is holomorphic. For $w$ with $\operatorname{Re}w>0$ one has $\abs{w-1}^{2}<\abs{w+1}^{2}$ — their difference is $-4\operatorname{Re}w<0$ — so $\abs{\phi_{f}(z)}<1$. Finally $\phi_{f}(0)=\dfrac{f(0)-1}{f(0)+1}=\dfrac{0}{2}=0$ since $f(0)=1$.
:::

:::

::: {.pf-step #schwarz}
$\abs{\phi_{f}(z)}\le\abs{z}$ for every $z\in\DD$ and every $f\in\mathcal{F}$.

::: pf-proof
$\phi_{f}$ is holomorphic on $\DD$, bounded by $1$ there and vanishes at $0$, so the Schwarz lemma applies and gives the inequality.
:::

:::

::: {.pf-step #bound}
For $0<r<1$ and $\abs{z}\le r$ one has $\abs{f(z)}\le\dfrac{1+r}{1-r}$ for every $f\in\mathcal{F}$.

::: pf-proof
Since $f=\dfrac{1+\phi_{f}}{1-\phi_{f}}$, one has $\abs{f(z)}\le\dfrac{1+\abs{\phi_{f}(z)}}{1-\abs{\phi_{f}(z)}}\le\dfrac{1+r}{1-r}$, where the first inequality uses $\abs{1-\phi_{f}}\ge1-\abs{\phi_{f}}>0$ and the second step [](#schwarz){.pf-ref} together with $\abs{z}\le r$.
:::

:::

::: {.pf-qed}
$\mathcal{F}$ is locally uniformly bounded by step [](#bound){.pf-ref} on every compact subset of $\DD$, so it is a normal family by Montel's theorem.
:::

:::

:::
