---
schema: qual/card@1
id: P-CAEXAMPREP-15
kind: problem
title: Flow around the upper half of the unit circle
classification: {areas: [complex-analysis], topics: [Harmonic Functions, Conformal Maps]}
relations: []
review: draft
audit:
  - event: source-checked
    by: gpt-5.6-sol
    date: 2026-09-14
    note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Let
$$
A=\{z:\operatorname{Im}z>0,\ \abs{z}>1\}.
$$
Find the flow around the upper half of the unit circle when the velocity is parallel to the $x$-axis and is $\alpha$ at infinity.
:::

::: {.solution}

Write $z=re^{i\theta}$ with $r>1$ and $0<\theta<\pi$, and let
$$
J(z)=z+\frac1z.
$$

::: pf

::: {.pf-step #s1-1}

The Joukowski map $J$ is a biholomorphism from $A$ onto the upper half-plane $\halfplane$.


::: pf-proof

For $z=re^{i\theta}\in A$,
$$
\operatorname{Im}J(z)
=\left(r-\frac1r\right)\sin\theta>0,
$$
so $J(A)\subseteq\halfplane$. If $J(z_1)=J(z_2)$, then
$$
(z_1-z_2)\left(1-\frac1{z_1z_2}\right)=0.
$$
Since $\abs{z_1z_2}>1$, the second factor cannot vanish; hence $z_1=z_2$.

Conversely, let $w\in\halfplane$. The roots of
$$
z^2-wz+1=0
$$
have product $1$. No root has modulus $1$, because for $\abs{z}=1$ one has $z+z^{-1}=2\operatorname{Re}z\in\RR$, whereas $w\notin\RR$. Thus exactly one root has modulus greater than $1$. For that root,
$$
\operatorname{Im}w
=\operatorname{Im}\left(z+\frac1z\right)
=\left(r-\frac1r\right)\sin\theta>0,
$$
so $\sin\theta>0$ and therefore $\operatorname{Im}z>0$. Hence that root lies in $A$, proving surjectivity. Finally,
$$
J'(z)=1-\frac1{z^2}\ne0
$$
on $A$, so $J$ is biholomorphic.

:::

:::

::: {.pf-step #s1-2}

The complex potential
$$
F(z)=\alpha J(z)=\alpha\left(z+\frac1z\right)
$$
has the boundary of $A$ as a streamline.


::: pf-proof

The uniform horizontal flow on $\halfplane$ has complex potential $F_0(w)=\alpha w$, whose stream function is $\operatorname{Im}F_0(w)=\alpha\operatorname{Im}w$ and hence vanishes on $\partial\halfplane=\RR$. By step [](#s1-1){.pf-ref}, pulling this potential back by $J$ gives $F=F_0\circ J$ on $A$.

Equivalently, for $z=re^{i\theta}$,
$$
\operatorname{Im}F(z)
=\alpha\left(r-\frac1r\right)\sin\theta.
$$
This vanishes when $r=1$ and also when $\theta=0$ or $\theta=\pi$, so every boundary component of $A$ is a streamline.

:::

:::

::: {.pf-step #s1-3}

The velocity tends to the prescribed horizontal velocity $\alpha$ at infinity.


::: pf-proof

With the standard convention that the complex velocity is $F'(z)=u-iv$,
$$
F'(z)=\alpha\left(1-\frac1{z^2}\right)\longrightarrow\alpha
\qquad (\abs{z}\to\infty).
$$
Thus $u\to\alpha$ and $v\to0$, so the limiting velocity is parallel to the $x$-axis with the prescribed $x$-component $\alpha$.

:::

:::

::: {.pf-step #s1-4}

The required flow is
$$
\boxed{
\begin{aligned}
F(z)&=\alpha\left(z+\frac1z\right),\\
\phi(r,\theta)&=\alpha\left(r+\frac1r\right)\cos\theta,\\
\psi(r,\theta)&=\alpha\left(r-\frac1r\right)\sin\theta.
\end{aligned}}
$$


::: pf-proof

Since
$$
z+\frac1z
=\left(r+\frac1r\right)\cos\theta
+i\left(r-\frac1r\right)\sin\theta,
$$
the real and imaginary parts of the potential in step [](#s1-2){.pf-ref} are exactly the displayed velocity potential $\phi$ and stream function $\psi$. Steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref} verify the boundary and far-field conditions.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required flow.

:::

:::

:::
