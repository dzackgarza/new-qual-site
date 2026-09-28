---
schema: qual/card@1
id: E-3M6WZ
kind: problem
title: Unique fractional linear transformation sending one circle to another with
  two prescribed values
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
  - Blaschke Factors
relations: []
review: draft
---

::: {.problem}
Let $C$ and $C'$ be two circles and let $z_1 \in C$, $z_2 \notin C$, $z'_1 \in C'$, $z'_2 \notin C'$.
Show that there is a unique fractional linear transformation $f$ with $f(C) = C'$ and $f(z_1) = z'_1$, $f(z_2) = z'_2$.
:::

::: {.solution}
<1>1. For a circle $C$ and a point $z_2\notin C$, there is a fractional linear transformation $F$ with $F(C)=S^1$ and $F(z_2)=0$.

::: {.proof}
If $C$ has center $c$ and radius $\rho$, then $f_1(z)=(z-c)/\rho$ sends $C$ to $S^1$.
If $\abs{f_1(z_2)}>1$, let $f_2(z)=1/z$; otherwise let $f_2=\id$.
In either case $f_2$ preserves $S^1$ and $a\coloneqq f_2(f_1(z_2))\in\DD$.
The Blaschke factor $\psi_a(z)=(a-z)/(1-\bar a z)$ preserves $S^1$ and sends $a$ to $0$.
Put $F\coloneqq\psi_a\circ f_2\circ f_1$.
:::

<1>2. There is a fractional linear transformation $f$ with $f(C)=C'$, $f(z_1)=z_1'$ and $f(z_2)=z_2'$.

::: {.proof}
Let $F$ and $G$ be the maps of step <1>1 for $(C,z_2)$ and $(C',z_2')$.
Then $F(z_1)$ and $G(z_1')$ lie on $S^1$, so $\lambda\coloneqq G(z_1')/F(z_1)$ has $\abs\lambda=1$ and $h(z)=\lambda z$ preserves $S^1$.
Put $f\coloneqq \inverseof{G}\circ h\circ F$.
Then $f(C)=\inverseof{G}(S^1)=C'$, $f(z_2)=\inverseof{G}(0)=z_2'$ and $f(z_1)=\inverseof{G}(G(z_1'))=z_1'$.
:::

<1>3. If $f$ and $\tilde f$ both satisfy the conditions, then $f=\tilde f$.

::: {.proof}
Let $\varphi\coloneqq F\circ\inverseof{\tilde f}\circ f\circ \inverseof{F}$.
It is a fractional linear transformation with $\varphi(S^1)=S^1$, $\varphi(0)=0$ and $\varphi(F(z_1))=F(z_1)$.
A fractional linear transformation maps the two components of $\widehat\CC\setminus S^1$ onto the two components, and $\varphi(0)=0$, so $\varphi(\DD)=\DD$.
By the Schwarz lemma, an automorphism of $\DD$ fixing $0$ is a rotation $z\mapsto\mu z$.
It fixes $F(z_1)\ne0$, so $\mu=1$ and $\varphi=\id$, that is, $f=\tilde f$.
:::

<1>4. Q.E.D.

::: {.proof}
Steps <1>2 and <1>3 give existence and uniqueness.
:::
:::
