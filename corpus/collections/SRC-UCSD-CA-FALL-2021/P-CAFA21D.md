---
schema: qual/card@1
id: P-CAFA21D
kind: problem
title: "Sequence of holomorphic self-maps of the disk converging to 1"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the Schwarz-Pick
    factor zeta_n is well defined because |a_n f_n| < 1, satisfies |zeta_n| <= |z| by
    Schwarz's lemma applied to the automorphism carrying a_n to 0, inverts to
    f_n = (a_n + zeta)/(1 + conj(a_n) zeta), and gives |f_n - 1| <= (1 + r)|a_n - 1|/(1 - r)
    on |z| <= r. The prose wrote the Schwarz-Pick inequality with the right side |z| <= r,
    which is the estimate on the disc rather than at the point; the pointwise step is now
    separate from its supremum. The statement is true as printed; the limit is the constant
    1, which is stated. The collection's provenance is the examination paper only, so no
    retained solution set covers the exercise and the argument is the card's own.
---

::: {.problem}
Let $a_n \in \Delta$ be a sequence such that $a_n \to 1$.
Let $f_n : \Delta \to \Delta$ be a sequence of holomorphic functions such that $f_n(0) = a_n$.
Show that $f_n \to 1$ uniformly on compact subsets of $\Delta$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.
Fix $0<r<1$ and put
$$
\zeta_n(z)\coloneqq\frac{f_n(z)-a_n}{1-\overline{a_n}f_n(z)},\qquad \abs{z}\le r .
$$

::: pf

::: {.pf-step #well-defined}
$\zeta_n$ is defined and holomorphic on a neighbourhood of $\abs{z}\le r$, and $\abs{\zeta_n(z)}\le\abs{z}\le r$.

::: pf-proof
$\abs{a_n}<1$ and $\abs{f_n(z)}<1$ give $\abs{\overline{a_n}f_n(z)}<1$, so the denominator never vanishes. The function $\varphi_{a_n}(w)=\frac{w-a_n}{1-\overline{a_n}w}$ is the disc automorphism carrying $a_n$ to $0$, so $\varphi_{a_n}\circ f_n$ maps $\DD$ into $\DD$ and fixes $0$; Schwarz's lemma gives $\abs{\zeta_n(z)}=\abs{\varphi_{a_n}(f_n(z))}\le\abs{z}$.
:::

:::

::: {.pf-step #inverse}
$\displaystyle f_n(z)=\frac{a_n+\zeta_n(z)}{1+\overline{a_n}\zeta_n(z)}$.

::: pf-proof
$\zeta=\varphi_{a_n}(f)$ inverts to $f=\varphi_{a_n}^{-1}(\zeta)=\frac{a_n+\zeta}{1+\overline{a_n}\zeta}$, the inverse automorphism, and $\abs{\overline{a_n}\zeta}<1$ there so the formula is defined.
:::

:::

::: {.pf-step #difference}
$\displaystyle f_n(z)-1=\frac{(a_n-1)+\zeta_n(z)\left(1-\overline{a_n}\right)}{1+\overline{a_n}\zeta_n(z)}$.

::: pf-proof
Subtract $1=\frac{1+\overline{a_n}\zeta}{1+\overline{a_n}\zeta}$ from the expression of step [](#inverse){.pf-ref} and collect: the numerator becomes $a_n+\zeta-1-\overline{a_n}\zeta$.
:::

:::

::: {.pf-step #denominator}
$\abs{1+\overline{a_n}\zeta_n(z)}\ge1-r$ for $\abs{z}\le r$.

::: pf-proof
$\abs{1+\overline{a_n}\zeta}\ge1-\abs{a_n}\abs{\zeta}\ge1-r$, using $\abs{a_n}<1$ and step [](#well-defined){.pf-ref}.
:::

:::

::: {.pf-step #bound}
$\displaystyle\sup_{\abs{z}\le r}\abs{f_n(z)-1}\le\frac{(1+r)\abs{a_n-1}}{1-r}\longrightarrow0$.

::: pf-proof
By steps [](#difference){.pf-ref} and [](#denominator){.pf-ref},
$$
\abs{f_n(z)-1}\le\frac{\abs{a_n-1}+\abs{\zeta_n(z)}\abs{1-\overline{a_n}}}{1-r}\le\frac{\abs{a_n-1}+r\abs{a_n-1}}{1-r},
$$
since $\abs{1-\overline{a_n}}=\abs{1-a_n}=\abs{a_n-1}$ and $\abs{\zeta_n}\le r$; the right side is independent of $z$ and tends to $0$ as $n\to\infty$ because $a_n\to1$ and $r<1$.
:::

:::

::: {.pf-step}
$f_n\to1$ uniformly on compact subsets of $\DD$.

::: pf-proof
Let $K\subset\DD$ be compact. Since $\DD$ is the union of the discs $\abs{z}\le r$ for $r<1$ and $K$ is compact, $K$ lies in $\abs{z}\le r$ for some $r<1$; step [](#bound){.pf-ref} then bounds $\sup_K\abs{f_n-1}$ by a quantity tending to $0$, uniformly in $n$ on that disc. Hence $f_n\to1$ locally uniformly, the limit being the constant function $1$, which need not belong to $H(\DD)$'s image but is the uniform limit on compacta.
:::

:::

:::
:::
