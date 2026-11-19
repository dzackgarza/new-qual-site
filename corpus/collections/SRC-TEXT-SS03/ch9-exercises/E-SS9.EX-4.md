---
schema: qual/card@1
id: E-SS9.EX-4
kind: problem
title: Periodicity of $\wp$ by rearranging its series
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Weierstrass P
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Lamport structure over the prose that was already there. The three estimates are now
    separate steps with their reasons: the difference 1/(z+w)^2 - 1/w^2 = O(|w|^-3)
    uniformly off the poles, the lattice count giving sum |w|^-3 = O(R^-1), the exact
    cancellation of the two constant sums in the reindexed difference, and the count of
    lattice points in the annulus R-|lambda| < |eta| < R+|lambda| being O(R). Nothing is
    differentiated, as the exercise requires. Not checked: the book's own text of the
    exercise, since no copy of Stein and Shakarchi is retained in this checkout; the
    statement is as transcribed on the card. No retained solution set covers the exercise
    (the collection's provenance is a Google Books record), so the argument is the card's
    own. No statement repair.
---

::: {.exercise}
By rearranging the series
$$
\frac{1}{z^2} + \sum_{\omega \in \Lambda^*} \left[ \frac{1}{(z + \omega)^2} - \frac{1}{\omega^2} \right],
$$
show directly, without differentiation, that $\wp(z + \omega) = \wp(z)$ whenever $\omega \in \Lambda$.

[Hint: For $R$ sufficiently large, note that $\wp(z) = \wp^R(z) + O(1/R)$ where $\wp^R(z) = z^{-2} + \sum_{0 < \abs{\omega} < R} ((z + \omega)^{-2} - \omega^{-2})$. Next, observe that both $\wp^R(z + 1) - \wp^R(z)$ and $\wp^R(z + \tau) - \wp^R(z)$ are $O\left( \sum_{R - c < \abs{\omega} < R + c} \abs{\omega}^{-2} \right) = O(1/R)$.]
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Let $\Lambda\subset\CC$ be a lattice, $\lambda\in\Lambda$, $\lambda\ne0$, and for $R>0$ set
$$
\wp^R(z)=\frac{1}{z^2}+\sum_{0<\abs{\omega}<R}\Bigl(\frac{1}{(z+\omega)^2}-\frac{1}{\omega^2}\Bigr)=\sum_{\abs{\omega}<R}\frac{1}{(z+\omega)^2}-\sum_{0<\abs{\omega}<R}\frac{1}{\omega^2},
$$
the second expression because the $1/z^2$ term is the $\omega=0$ term of the first sum. Let $K$ be a compact set disjoint from $-\Lambda$.

::: pf

::: {.pf-step #tail}
$\wp(z)-\wp^R(z)=O(R^{-1})$ uniformly on $K$.

::: pf-proof
For $z\in K$ and $\abs{\omega}\ge2\max_{K}\abs{z}$ one has $\abs{z+\omega}\ge\abs{\omega}/2$, so
$$
\frac{1}{(z+\omega)^2}-\frac{1}{\omega^2}=\frac{\omega^2-(z+\omega)^2}{\omega^2(z+\omega)^2}=\frac{-2z\omega-z^2}{\omega^2(z+\omega)^2}=O\bigl(\abs{\omega}^{-3}\bigr),
$$
uniformly on $K$; the finite set of $\omega$ with $\abs{\omega}$ smaller is harmless since $K$ misses $-\Lambda$. So the tail is $O\bigl(\sum_{\abs{\omega}\ge R}\abs{\omega}^{-3}\bigr)$. To estimate that sum, count lattice points in annuli: there is $C$ with $\#\{\omega\in\Lambda:k\le\abs{\omega}<k+1\}\le Ck$ for all $k\ge1$, because a lattice is uniformly discrete and a disc of radius $k+1$ has area $O(k^2)$. Hence $\sum_{\abs{\omega}\ge R}\abs{\omega}^{-3}\le\sum_{k\ge R}Ck\cdot k^{-3}=O(R^{-1})$, since $\sum_{k\ge R}k^{-2}=O(R^{-1})$.
:::

:::

::: {.pf-step #reindex}
$\wp^R(z+\lambda)-\wp^R(z)=\displaystyle\sum_{\abs{\eta-\lambda}<R}\frac{1}{(z+\eta)^2}-\sum_{\abs{\eta}<R}\frac{1}{(z+\eta)^2}$.

::: pf-proof
By the second expression for $\wp^R$, $\wp^R(z+\lambda)=\sum_{\abs{\omega}<R}(z+\lambda+\omega)^{-2}-\sum_{0<\abs{\omega}<R}\omega^{-2}$, and $\wp^R(z)=\sum_{\abs{\omega}<R}(z+\omega)^{-2}-\sum_{0<\abs{\omega}<R}\omega^{-2}$; the two constant sums are identical and cancel. In the first sum substitute $\eta=\omega+\lambda$, which is a bijection of $\Lambda$ onto itself, so the condition $\abs{\omega}<R$ becomes $\abs{\eta-\lambda}<R$; renaming $\eta$ in the second sum gives the display.
:::

:::

::: {.pf-step #annulus}
The nonvanishing terms of step [](#reindex){.pf-ref} have $\eta$ in the annulus $R-\abs{\lambda}<\abs{\eta}<R+\abs{\lambda}$, and there are $O(R)$ such lattice points, each contributing $O(R^{-2})$ uniformly on $K$.

::: pf-proof
A lattice point contributes to the difference exactly when it lies in one of the discs but not the other, that is when $\abs{\eta}<R\le\abs{\eta-\lambda}$ or $\abs{\eta-\lambda}<R\le\abs{\eta}$; by the triangle inequality either alternative forces $\abs{\abs{\eta}-\abs{\lambda}}<R$, which is the annulus. Its area is $\pi\bigl((R+\abs\lambda)^2-(R-\abs\lambda)^2\bigr)=4\pi R\abs{\lambda}$, so by the counting estimate used in step [](#tail){.pf-ref} it contains $O(R)$ lattice points. For such $\eta$ and $z\in K$, $\abs{z+\eta}\to\infty$ like $R$, so $\abs{(z+\eta)^{-2}}=O(R^{-2})$ uniformly; the finitely many $\eta$ with $z+\eta$ in a fixed compact part of $K$ are absorbed into the constant.
:::

:::

::: {.pf-step #uniform}
$\wp^R(z+\lambda)-\wp^R(z)=O(R^{-1})$ uniformly on $K$.

::: pf-proof
By steps [](#reindex){.pf-ref} and [](#annulus){.pf-ref} the difference is a sum of $O(R)$ terms each $O(R^{-2})$, hence $O(R^{-1})$.
:::

:::

::: {.pf-step}
$\wp(z+\lambda)=\wp(z)$ for every $z\in\CC\setminus\Lambda$, that is every $\lambda\in\Lambda$ is a period of $\wp$.

::: pf-proof
By steps [](#tail){.pf-ref} and [](#uniform){.pf-ref},
$$
\wp(z+\lambda)-\wp(z)=\bigl(\wp(z+\lambda)-\wp^R(z+\lambda)\bigr)+\bigl(\wp^R(z+\lambda)-\wp^R(z)\bigr)+\bigl(\wp^R(z)-\wp(z)\bigr)=O(R^{-1})
$$
uniformly on $K$, for every $R$. A quantity bounded by $CR^{-1}$ for all large $R$ is $0$, so $\wp(z+\lambda)=\wp(z)$ on $K$, and $K$ was any compact set off $-\Lambda= \Lambda$. Both sides are meromorphic on $\CC$ with poles only at $\Lambda$, so by the identity theorem for meromorphic functions the identity extends across the poles; hence $\lambda$ is a period. Since $\lambda\in\Lambda$ was arbitrary, $\Lambda$ is contained in the period group of $\wp$, and no differentiation was used anywhere in the argument.
:::

:::

:::

:::
