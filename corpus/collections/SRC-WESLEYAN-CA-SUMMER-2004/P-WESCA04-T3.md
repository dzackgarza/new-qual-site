---
schema: qual/card@1
id: P-WESCA04-T3
kind: problem
title: "State the most general version of Cauchy's Theorem"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.1, item 3 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
State the most general version of Cauchy's Theorem.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let $U\subset\CC$ be open and let
$$
f:U\to\CC
$$
be holomorphic. Let
$$
\Gamma
$$
be a closed piecewise-$C^1$ integral $1$-cycle in $U$ which is homologous
to zero in $U$:
$$
[\Gamma]=0
\in
H_1(U;\ZZ).
$$
Then the general Cauchy theorem is
$$
\boxed{
\int_\Gamma f(z)\,dz=0.
}
$$


::: pf-proof

This is the homological form of Cauchy's integral theorem. The following
steps give a proof.

:::

:::

::: {.pf-step #s1-2}

Write
$$
f=u+iv
$$
and
$$
z=x+iy.
$$
Then the complex-valued $1$-form
$$
\omega
\coloneqq
f(z)\,dz
$$
is closed:
$$
d\omega=0.
$$


::: pf-proof

Expand
$$
\omega
=(u+iv)(dx+i\,dy)
=(u\,dx-v\,dy)
+
i(v\,dx+u\,dy).
$$

For the real part,
$$
\begin{aligned}
d(u\,dx-v\,dy)
&=
du\wedge dx-dv\wedge dy\\
&=
-(u_y+v_x)\,dx\wedge dy.
\end{aligned}
$$
The Cauchy--Riemann equation
$$
u_y=-v_x
$$
makes this zero.

For the imaginary part,
$$
\begin{aligned}
d(v\,dx+u\,dy)
&=
dv\wedge dx+du\wedge dy\\
&=
(u_x-v_y)\,dx\wedge dy.
\end{aligned}
$$
The other Cauchy--Riemann equation
$$
u_x=v_y
$$
makes this zero as well. Hence
$$
d\omega=0.
$$

:::

:::

::: {.pf-step #s1-3}

Since
$$
[\Gamma]=0
\in
H_1(U;\ZZ),
$$
there is a finite oriented $2$-chain $C$ in $U$ with
$$
\partial C=\Gamma.
$$


::: pf-proof

This is exactly the meaning of the cycle $\Gamma$ representing the zero
homology class. A singular chain may be replaced, after subdivision and
smooth approximation inside the open set $U$, by a piecewise-smooth chain
with the same boundary for purposes of integration.

:::

:::

::: {.pf-step #s1-4}

Stokes' theorem gives
$$
\int_\Gamma f(z)\,dz
=
0.
$$


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
\begin{aligned}
\int_\Gamma f(z)\,dz
&=
\int_{\partial C}\omega\\
&=
\int_C d\omega\\
&=
\int_C0\\
&=
0.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

For a closed cycle $\Gamma\subset U$, the condition that it be
null-homologous in $U$ can equivalently be expressed by the winding-number
condition
$$
\operatorname{Ind}(\Gamma,a)
=
0
\qquad
(a\in\CC\setminus U),
$$
where
$$
\operatorname{Ind}(\Gamma,a)
\coloneqq
\frac1{2\pi i}
\int_\Gamma\frac{dz}{z-a}.
$$


::: pf-proof

For planar domains, the homology class of a closed cycle is detected by its
winding numbers around the complementary components. Thus the class
vanishes precisely when the index about every point outside the domain is
zero.

:::

:::

::: {.pf-step #s1-6}

Consequently an equivalent standard formulation is:
if $f$ is holomorphic on $U$ and $\Gamma$ is a closed piecewise-$C^1$
cycle in $U$ satisfying
$$
\operatorname{Ind}(\Gamma,a)=0
\qquad
(a\notin U),
$$
then
$$
\boxed{
\int_\Gamma f(z)\,dz=0.
}
$$


::: pf-proof

By step [](#s1-5){.pf-ref}, the winding-number hypothesis says exactly that $\Gamma$ is
homologous to zero in $U$. Apply step [](#s1-4){.pf-ref}.

:::

:::

::: pf-step

In particular, if $U$ is simply connected, then every closed curve
in $U$ is null-homologous, so
$$
\int_\Gamma f(z)\,dz=0
$$
for every closed piecewise-$C^1$ curve $\Gamma\subset U$.


::: pf-proof

A simply connected domain has
$$
H_1(U;\ZZ)=0.
$$
Apply step [](#s1-1){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-6){.pf-ref} state the most general planar Cauchy theorem in its
homological and winding-number forms; steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} prove it.

:::

:::

:::
