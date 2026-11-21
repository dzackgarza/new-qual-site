---
schema: qual/card@1
id: P-CAF06C
kind: problem
title: "Conformal map from a simply connected region to a disk without using the full Riemann mapping theorem"
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
    Lamport structure, and one arithmetic slip repaired. The prose concluded the strict inequality |F'(0)| > 1 from "(1 - |a|)^2 > 0"; the correct comparison is 1 + |a| > 2 sqrt(|a|), which is (1 - sqrt(|a|))^2 > 0, so the parenthetical factor is (1 - sqrt |a|)^2, not (1 - |a|)^2. Everything else was checked: phi'(0) = 1 - |a|^2, b^2 = phi(0) = -a so |b|^2 = |a|, |psi_b'(b)| = 1/(1-|b|^2), and the product (1+|a|)/(2 sqrt |a|). The square root's existence on the simply connected zero-free region, its injectivity, and the final normalisation f = F/lambda with r = 1/lambda are now steps. No retained solution set covers the exercise; the card says the argument is its own (the hint's Koebe step).
---

::: {.problem}
Let $Y$ be a simply-connected region contained inside the disk $D = \{z : \abs{z} < 1\}$.
Assume $0 \in Y \neq D$.
Without appealing to the Riemann mapping theorem itself, prove that there exists an $r$ with $1 > r > 0$ and a univalent conformal map $f: Y \to D(r) = \{z : \abs{z} < r\}$ with $f(0) = 0$ and $f'(0) = 1$.

Hint: You may use part of the proof of the Riemann mapping theorem.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own, and it is the Koebe step from the proof of the Riemann mapping theorem, as the hint allows.

::: pf

::: {.pf-step #phi}
Choose $a\in\DD\setminus Y$; then $a\ne0$, and $\phi(z)=\dfrac{z-a}{1-\overline az}$ maps $\DD$ conformally onto $\DD$ with $\phi(a)=0$ and no zeros on $Y$.

::: pf-proof
$Y\ne\DD$ and $Y\subseteq\DD$ give $a$; $0\in Y$ gives $a\ne0$. $\phi$ is Möbius with pole $1/\overline a\notin\DD$ (as $\abs a<1$), it maps $\DD$ onto $\DD$ (the disc automorphisms $\frac{w-c}{1-\overline cw}$), and $\phi(a)=0$. Its only zero in $\DD$ is $a$, which is not in $Y$.
:::

:::

::: {.pf-step #sqrt}
There is a holomorphic $q$ on $Y$ with $q^2=\phi$; it is injective and $\abs{q}<1$ on $Y$.

::: pf-proof
$\phi$ is holomorphic and zero-free on the simply connected region $Y$, so it has a holomorphic square root there (a zero-free holomorphic function on a simply connected domain has a holomorphic logarithm, and half the logarithm exponentiates to $q$). If $q(z)=q(w)$ then $\phi(z)=q(z)^2=q(w)^2=\phi(w)$, so $z=w$ by injectivity of $\phi$; and $\abs{q(z)}^2=\abs{\phi(z)}<1$.
:::

:::

::: {.pf-step #F}
With $b=q(0)$ and $\psi_b(w)=\frac{w-b}{1-\overline bw}$, the map $F=\psi_b\circ q:Y\to\DD$ is univalent with $F(0)=0$.

::: pf-proof
$b\ne0$ because $q(0)^2=\phi(0)=-a\ne0$. $\psi_b$ is a disc automorphism as in step [](#phi){.pf-ref}, so $F$ is holomorphic and univalent, being a composite of injective maps, and $F(0)=\psi_b(b)=0$.
:::

:::

::: {.pf-step #derivative}
$\abs{F'(0)}=\dfrac{1+\abs a}{2\sqrt{\abs a}}>1$.

::: pf-proof
From $q^2=\phi$ we get $2q(0)q'(0)=\phi'(0)$, and $\phi'(z)=\frac{(1-\overline az)+\overline a(z-a)}{(1-\overline az)^2}=\frac{1-\abs a^2}{(1-\overline az)^2}$ gives $\phi'(0)=1-\abs a^2$. Also $b^2=\phi(0)=-a$ gives $\abs b^2=\abs a$. Hence
$$
\abs{q'(0)}=\frac{1-\abs a^2}{2\abs b}=\frac{1-\abs a^2}{2\sqrt{\abs a}},
\qquad
\abs{\psi_b'(b)}=\frac{1-\abs b^2}{(1-\abs b^2)^2}=\frac1{1-\abs a},
$$
the second from $\psi_b'(w)=\frac{1-\abs b^2}{(1-\overline bw)^2}$. Multiplying,
$$
\abs{F'(0)}=\abs{\psi_b'(b)}\abs{q'(0)}=\frac{(1-\abs a)(1+\abs a)}{2\sqrt{\abs a}(1-\abs a)}=\frac{1+\abs a}{2\sqrt{\abs a}},
$$
and $1+\abs a-2\sqrt{\abs a}=(1-\sqrt{\abs a})^2>0$ because $\abs a\ne1$, which gives the strict inequality $>1$.
:::

:::

::: {.pf-step}
There are $r\in(0,1)$ and a univalent conformal $f:Y\to D(r)$ with $f(0)=0$ and $f'(0)=1$.

::: pf-proof
Let $\lambda=\abs{F'(0)}>1$ and choose $\abs{c}=1$ with $cF'(0)=\lambda$; replacing $F$ by $cF$ keeps it univalent, keeps $F(0)=0$ and makes $F'(0)=\lambda>0$. Put $r=1/\lambda\in(0,1)$ and $f=F/\lambda$. Then $f$ is univalent and conformal on $Y$, $f(0)=0$, $f'(0)=1$, and $\abs{f(z)}=\abs{F(z)}/\lambda<1/\lambda=r$ because $\abs{F(z)}<1$ on $Y$; so $f$ maps $Y$ into $D(r)$.
:::

:::

:::
:::
