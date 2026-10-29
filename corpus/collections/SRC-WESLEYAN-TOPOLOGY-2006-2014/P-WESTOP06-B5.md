---
schema: qual/card@1
id: P-WESTOP06-B5
kind: problem
title: Naturality of induced fundamental-group maps under a homotopy
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Let
$$
F:X\times I\to Y
$$
be continuous, choose $x_0\in X$, and define
$$
\alpha(t)=F(x_0,t).
$$
Prove that the diagram
$$
\begin{CD}
\pi_1(X,x_0) @>{F(-,1)_*}>> \pi_1(Y,F(x_0,1))\\
@V{F(-,0)_*}VV @VV{\widehat\alpha}V\\
\pi_1(Y,F(x_0,0)) @= \pi_1(Y,F(x_0,0))
\end{CD}
$$
commutes, where $\widehat\alpha$ is the change-of-basepoint map induced by the path $\alpha$.
:::

::: {.solution}

For $t\in I$, write
$$
F_t:X\to Y,\qquad F_t(x)=F(x,t),
$$
and let $\overline\alpha(t)=\alpha(1-t)$. Use the change-of-basepoint convention
$$
\widehat\alpha:\pi_1(Y,F(x_0,1))\to\pi_1(Y,F(x_0,0)),
\qquad
\widehat\alpha([\delta])=[\alpha*\delta*\overline\alpha].
$$

::: pf

::: pf-step

Let $\gamma:I\to X$ be any loop based at $x_0$, and set
$$
\gamma_0=F_0\circ\gamma,
\qquad
\gamma_1=F_1\circ\gamma.
$$
Then
$$
\gamma_0(0)=\gamma_0(1)=F(x_0,0),
\qquad
\gamma_1(0)=\gamma_1(1)=F(x_0,1).
$$


::: pf-proof

Because $\gamma(0)=\gamma(1)=x_0$, evaluating $F_0$ and $F_1$ at the two endpoints gives the displayed equalities.

:::

:::

::: {.pf-step #s1-2}

The map
$$
G:I\times I\to Y,
\qquad
G(u,v)=F(\gamma(u),v),
$$
has boundary paths
$$
\begin{array}{ccl}
G(u,0)&=&\gamma_0(u),\\
G(u,1)&=&\gamma_1(u),\\
G(0,v)&=&\alpha(v),\\
G(1,v)&=&\alpha(v).
\end{array}
$$


::: pf-proof

The first two identities are the definitions of $\gamma_0$ and $\gamma_1$. For the vertical sides, $\gamma(0)=\gamma(1)=x_0$, so
$$
G(0,v)=F(x_0,v)=\alpha(v)=G(1,v).
$$

:::

:::

::: {.pf-step #s1-3}

The loop $\gamma_0$ is path-homotopic relative to its endpoints to
$$
\alpha*\gamma_1*\overline\alpha.
$$


::: pf-proof

For $r\in I$, consider the path in the parameter square that starts at $(0,0)$, goes vertically to $(0,r)$, horizontally to $(1,r)$, and then vertically down to $(1,0)$. As $r$ increases continuously from $0$ to $1$, these three-sided paths vary continuously and keep the endpoints $(0,0)$ and $(1,0)$ fixed.

Composing this deformation with the continuous map $G$ from step [](#s1-2){.pf-ref} gives a path homotopy in $Y$. At $r=0$, the two vertical pieces are constant and the horizontal piece is $\gamma_0$, so the resulting path represents $[\gamma_0]$. At $r=1$, step [](#s1-2){.pf-ref} identifies the three pieces as
$$
\alpha,\qquad \gamma_1,\qquad \overline\alpha,
$$
in that order. Thus
$$
[\gamma_0]=[\alpha*\gamma_1*\overline\alpha].
$$
The harmless constant pieces at $r=0$ may be removed by the standard endpoint-fixing reparametrization homotopy.

:::

:::

::: {.pf-step #s1-4}

For every $[\gamma]\in\pi_1(X,x_0)$,
$$
F_{0*}([\gamma])
=
\widehat\alpha\bigl(F_{1*}([\gamma])\bigr).
$$


::: pf-proof

By definition,
$$
F_{0*}([\gamma])=[\gamma_0],
\qquad
F_{1*}([\gamma])=[\gamma_1].
$$
Step [](#s1-3){.pf-ref} gives
$$
[\gamma_0]
=[\alpha*\gamma_1*\overline\alpha]
=\widehat\alpha([\gamma_1]),
$$
which is the displayed identity.

:::

:::

::: {.pf-step #s1-5}

The diagram in the problem commutes.


::: pf-proof

Step [](#s1-4){.pf-ref} proves equality of the two composites from $\pi_1(X,x_0)$ to $\pi_1(Y,F(x_0,0))$:
$$
\boxed{F_{0*}=\widehat\alpha\circ F_{1*}.}
$$
This is exactly commutativity of the displayed diagram.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
