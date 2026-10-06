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
<1>1. Let $U\subset\mathbb C$ be open and let
\[
f:U\to\mathbb C
\]
be holomorphic. Let
\[
\Gamma
\]
be a closed piecewise-$C^1$ integral $1$-cycle in $U$ which is homologous
to zero in $U$:
\[
[\Gamma]=0
\in
H_1(U;\mathbb Z).
\]
Then the general Cauchy theorem is
\[
\boxed{
\int_\Gamma f(z)\,dz=0.
}
\]

::: {.proof}
This is the homological form of Cauchy's integral theorem. The following
steps give a proof.
:::

<1>2. Write
\[
f=u+iv
\]
and
\[
z=x+iy.
\]
Then the complex-valued $1$-form
\[
\omega
\coloneqq
f(z)\,dz
\]
is closed:
\[
d\omega=0.
\]

::: {.proof}
Expand
\[
\omega
=(u+iv)(dx+i,dy)
=(u,dx-v,dy)
+
i(v,dx+u,dy).
\]

For the real part,
\[
\begin{aligned}
d(u,dx-v,dy)
&=
du\wedge dx-dv\wedge dy\\
&=
-(u_y+v_x)\,dx\wedge dy.
\end{aligned}
\]
The Cauchy--Riemann equation
\[
u_y=-v_x
\]
makes this zero.

For the imaginary part,
\[
\begin{aligned}
d(v,dx+u,dy)
&=
dv\wedge dx+du\wedge dy\\
&=
(u_x-v_y)\,dx\wedge dy.
\end{aligned}
\]
The other Cauchy--Riemann equation
\[
u_x=v_y
\]
makes this zero as well. Hence
\[
d\omega=0.
\]
:::

<1>3. Since
\[
[\Gamma]=0
\in
H_1(U;\mathbb Z),
\]
there is a finite oriented $2$-chain $C$ in $U$ with
\[
\partial C=\Gamma.
\]

::: {.proof}
This is exactly the meaning of the cycle $\Gamma$ representing the zero
homology class. A singular chain may be replaced, after subdivision and
smooth approximation inside the open set $U$, by a piecewise-smooth chain
with the same boundary for purposes of integration.
:::

<1>4. Stokes' theorem gives
\[
\int_\Gamma f(z)\,dz
=
0.
\]

::: {.proof}
By steps <1>2--<1>3,
\[
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
\]
:::

<1>5. For a closed cycle $\Gamma\subset U$, the condition that it be
null-homologous in $U$ can equivalently be expressed by the winding-number
condition
\[
\operatorname{Ind}(\Gamma,a)
=
0
\qquad
(a\in\mathbb C\setminus U),
\]
where
\[
\operatorname{Ind}(\Gamma,a)
\coloneqq
\frac1{2\pi i}
\int_\Gamma\frac{dz}{z-a}.
\]

::: {.proof}
For planar domains, the homology class of a closed cycle is detected by its
winding numbers around the complementary components. Thus the class
vanishes precisely when the index about every point outside the domain is
zero.
:::

<1>6. Consequently an equivalent standard formulation is:
if $f$ is holomorphic on $U$ and $\Gamma$ is a closed piecewise-$C^1$
cycle in $U$ satisfying
\[
\operatorname{Ind}(\Gamma,a)=0
\qquad
(a\notin U),
\]
then
\[
\boxed{
\int_\Gamma f(z)\,dz=0.
}
\]

::: {.proof}
By step <1>5, the winding-number hypothesis says exactly that $\Gamma$ is
homologous to zero in $U$. Apply step <1>4.
:::

<1>7. In particular, if $U$ is simply connected, then every closed curve
in $U$ is null-homologous, so
\[
\int_\Gamma f(z)\,dz=0
\]
for every closed piecewise-$C^1$ curve $\Gamma\subset U$.

::: {.proof}
A simply connected domain has
\[
H_1(U;\mathbb Z)=0.
\]
Apply step <1>1.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1 and <1>6 state the most general planar Cauchy theorem in its
homological and winding-number forms; steps <1>2--<1>4 prove it.
:::
:::
