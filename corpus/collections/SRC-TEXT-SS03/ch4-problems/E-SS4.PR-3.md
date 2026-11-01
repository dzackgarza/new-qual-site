---
schema: qual/card@1
id: E-SS4.PR-3
kind: problem
title: Three-lines lemma for bounded holomorphic functions
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Stein--Shakarchi, *Complex Analysis*, Chapter 4, §5.5, exercise 3, read
    from `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`. The card matches the printed
    exercise, parts (a)--(c) and both hints; nothing was changed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    Parts (a)--(c) proved. (a) is the $F_\varepsilon=F e^{-\varepsilon z^2}$ argument with the
    maximum principle on a truncated rectangle; (b) is the hint applied literally after the rotation
    $\zeta=-iz$, which turns the card's horizontal strip into the vertical one the hint is written
    for: $G(\zeta)=M_0^{\zeta-1}M_1^{-\zeta}F(i\zeta)$ has $|G|\le1$ on both boundary lines, so (a)
    gives $|F(x+iy)|\le M_0^{1-y}M_1^y$; (c) is (b) applied to $w\mapsto F(w+iy_1)$ on a strip of
    height $y_2-y_1$. The degenerate cases $M_j=0$ and $M_j=\infty$ are treated by a limiting
    argument and the triviality of the right-hand side; no other case is left open.
---

::: {.exercise}
In this problem, we investigate the behavior of certain bounded holomorphic functions in an infinite strip. The particular result described here is sometimes called the three-lines lemma.

(a) Suppose $F(z)$ is holomorphic and bounded in the strip $0<\Im z<1$ and continuous on its closure. If $\abs{F(z)}\leq 1$ on the boundary lines, then prove that $\abs{F(z)}\leq 1$ throughout the strip.

(b) For the more general $F$, let $M_0=\sup_{x\in\RR}\abs{F(x)}$ and $M_1=\sup_{x\in\RR}\abs{F(x+i)}$. Prove that
$$
\sup_{x\in\RR}\abs{F(x+iy)}\leq M_0^{1-y}M_1^y,\qquad 0\leq y\leq 1.
$$

(c) As a consequence, prove that $\log\sup_{x\in\RR}\abs{F(x+iy)}$ is a convex function of $y$ for $0\leq y\leq 1$.
:::

::: {.hint}
For (a), apply the maximum modulus principle to $F_\varepsilon(z)=F(z)e^{-\varepsilon z^2}$. For (b), consider $M_0^{z-1}M_1^{-z}F(z)$.
:::

::: {.solution}

Throughout, $S=\{z:0<\operatorname{Im}z<1\}$ and $M=\sup_{S}\abs{F}<\infty$, which exists because $F$ is bounded in the strip.

::: pf

::: {.pf-step #s1}

Part (a): if $\abs{F}\le1$ on the two boundary lines $\operatorname{Im}z=0$ and $\operatorname{Im}z=1$, then $\abs{F}\le1$ on $S$.

::: pf-proof

For $\varepsilon>0$ set $F_\varepsilon(z)=F(z)e^{-\varepsilon z^2}$, which is holomorphic on $S$ and continuous on $\overline S$. For $z=x+iy$ with $0\le y\le1$,
$$
\abs{F_\varepsilon(z)}=\abs{F(z)}e^{-\varepsilon\operatorname{Re}(z^2)}\le Me^{\varepsilon y^2}e^{-\varepsilon x^2}\le Me^{\varepsilon}e^{-\varepsilon x^2},
$$
which tends to $0$ as $\abs{x}\to\infty$, uniformly in $y\in[0,1]$.

Fix $T>0$ and let $R_T=\{z:\abs{\operatorname{Re}z}\le T,\ 0\le\operatorname{Im}z\le1\}$. On the two horizontal sides of $R_T$ we have $y\in\{0,1\}$ and $\abs{F}\le1$, so $\abs{F_\varepsilon}\le\abs{F}e^{-\varepsilon x^2}\le1$. On the vertical sides $\abs{\operatorname{Re}z}=T$ and $\abs{F_\varepsilon}\le Me^{\varepsilon}e^{-\varepsilon T^2}<1$ once $T$ is large. The maximum modulus principle on the bounded region $\operatorname{int}R_T$ therefore gives $\abs{F_\varepsilon}\le1$ on $R_T$.

Hence for $z\in S$ and every small $\varepsilon>0$,
$$
\abs{F(z)}\le e^{\varepsilon\operatorname{Re}(z^2)} .
$$
Letting $\varepsilon\to0$ with $z$ fixed gives $\abs{F(z)}\le1$.

:::

:::

::: {.pf-step #s2}

Part (b): $\sup_{x\in\RR}\abs{F(x+iy)}\le M_0^{1-y}M_1^{y}$ for $0\le y\le1$, where $M_0=\sup_{x}\abs{F(x)}$ and $M_1=\sup_x\abs{F(x+i)}$.

::: pf-proof

First suppose $0<M_0,M_1<\infty$. Put $\zeta=-iz$, so that $z=i\zeta$ and the strip $S$ corresponds to $\Pi=\{\zeta:0<\operatorname{Re}\zeta<1\}$, with $\operatorname{Re}\zeta=y$ when $z=x+iy$. Let $\widetilde F(\zeta)=F(i\zeta)$, holomorphic and bounded on $\Pi$ and continuous on $\overline\Pi$, and note
$$
\sup_{\operatorname{Re}\zeta=0}\abs{\widetilde F}=M_0,\qquad \sup_{\operatorname{Re}\zeta=1}\abs{\widetilde F}=M_1 .
$$
Define on $\Pi$
$$
G(\zeta)=M_0^{\zeta-1}M_1^{-\zeta}\widetilde F(\zeta),
$$
where $M_0^{w}=\exp(w\log M_0)$ with the real logarithm. Then $\abs{M_0^{\zeta-1}}=M_0^{\operatorname{Re}\zeta-1}$ and $\abs{M_1^{-\zeta}}=M_1^{-\operatorname{Re}\zeta}$, so
$$
\abs{G(\zeta)}=\frac{\abs{\widetilde F(\zeta)}}{M_0^{1-\operatorname{Re}\zeta}M_1^{\operatorname{Re}\zeta}} .
$$
On the line $\operatorname{Re}\zeta=0$ this is at most $M_0/M_0=1$, and on $\operatorname{Re}\zeta=1$ at most $M_1/M_1=1$. By part [](#s1){.pf-ref}, applied to the strip $\Pi$ after the change of variable, $\abs{G}\le1$ on $\Pi$. Therefore
$$
\abs{F(i\zeta)}=\abs{\widetilde F(\zeta)}\le M_0^{1-\operatorname{Re}\zeta}M_1^{\operatorname{Re}\zeta},
$$
and putting $\zeta=y-ix$, so that $i\zeta=x+iy$ and $\operatorname{Re}\zeta=y$, gives $\abs{F(x+iy)}\le M_0^{1-y}M_1^{y}$ for every $x$ and every $0\le y\le1$.

If $M_0=\infty$ or $M_1=\infty$ the right-hand side is infinite and the inequality is void. If $M_j=0$ for some $j$, apply the preceding paragraph with $M_j$ replaced by $\delta>0$, which is legitimate since the hypothesis is only that $M_j$ dominates $\abs{F}$ on the corresponding line; then let $\delta\to0$. For $y<1$ this gives $\abs{F(x+iy)}=0$, and for $y=1$ the two sides are $M_1$ and $M_1$, so the asserted inequality holds throughout.

:::

:::

::: {.pf-step #s3}

Part (c): $y\mapsto\log\sup_{x\in\RR}\abs{F(x+iy)}$ is convex on $[0,1]$.

::: pf-proof

Let $m(y)=\sup_{x}\abs{F(x+iy)}$; by boundedness of $F$ in the strip, $m(y)<\infty$ for every $y$. The statement is that for $0\le y_1<y_2\le1$ and $0\le t\le1$,
$$
\log m\bigl((1-t)y_1+ty_2\bigr)\le(1-t)\log m(y_1)+t\log m(y_2).
$$

Assume first that $m(y_1)$ and $m(y_2)$ are both positive and finite. Put $h=y_2-y_1>0$ and $\widehat F(w)=F(w+iy_1)$ for $0<\operatorname{Im}w<h$, which is holomorphic and bounded there and continuous on the closure. Part [](#s2){.pf-ref} applied to the strip of height $h$ — the same proof, with $e^{-\varepsilon w^2}$ unchanged and the normalization $G(\zeta)=M_0^{\zeta/h-1}M_1^{-\zeta/h}$ — gives, at $\operatorname{Im}w=th$,
$$
\sup_x\abs{\widehat F(x+ith)}\le m(y_1)^{1-t}m(y_2)^{t},
$$
which is the displayed inequality, since $\widehat F(x+ith)=F(x+i(y_1+th))$ and $(1-t)y_1+ty_2=y_1+th$.

If $m(y_1)$ or $m(y_2)$ vanishes the same limiting argument as in part [](#s2){.pf-ref} applies, and if one of them is infinite the inequality is void. Hence $\log m$ satisfies the convexity inequality on every subinterval of $[0,1]$, which is convexity.

:::

:::

:::

:::

::: {.remark}
The hint for part (b) names the factor $M_0^{z-1}M_1^{-z}$. That is the normalization for a strip in the $\operatorname{Re}z$ variable; for the strip $0<\operatorname{Im}z<1$ used here it becomes $M_0^{\zeta-1}M_1^{-\zeta}$ after the rotation $\zeta=-iz$, which is how step [](#s2){.pf-ref} uses it.
:::
