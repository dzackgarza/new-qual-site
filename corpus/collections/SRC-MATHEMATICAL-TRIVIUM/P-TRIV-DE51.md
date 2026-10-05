---
schema: qual/card@1
id: P-TRIV-DE51
kind: problem
title: Grounded conducting sphere in a uniform electric field
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 51, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash contains a leading nonprinting control byte at this source position; the byte was removed from the authored card as a nonsemantic extraction artifact.
---

::: {.problem}
A conducting sphere of radius a with zero total charge is exposed to a uniform electric field $\vec { E }$ in the z direction.
Find the electrostatic potential outside the sphere if we set the surface of the sphere to have potential zero.
:::

::: {.solution}
Use spherical coordinates with polar axis in the direction of the applied field, so the imposed far-field potential is
\[
\Phi(r,\theta)\sim-Er\cos\theta
\qquad(r\to\infty).
\]

<1>1. The most general axisymmetric harmonic potential outside the sphere compatible with the prescribed far field has the form
\[
\Phi(r,\theta)=-Er\cos\theta
+\sum_{\ell=0}^{\infty}A_\ell r^{-\ell-1}P_\ell(\cos\theta).
\]

::: {.proof}
Axisymmetric separated solutions of Laplace's equation are
\[
(C_\ell r^\ell+D_\ell r^{-\ell-1})P_\ell(\cos\theta).
\]
At infinity, the only allowed growing term is the specified uniform-field term $-ErP_1(\cos\theta)$. Every additional term must decay, giving the displayed expansion.
:::

<1>2. The condition $\Phi(a,\theta)=0$ forces
\[
A_1=Ea^3
\]
and $A_\ell=0$ for every $\ell\ne1$.

::: {.proof}
At $r=a$,
\[
0=-EaP_1(\cos\theta)
+\sum_{\ell=0}^{\infty}A_\ell a^{-\ell-1}P_\ell(\cos\theta).
\]
Uniqueness of the Legendre expansion gives $A_1a^{-2}=Ea$ and all other coefficients zero.
:::

<1>3. Thus
\[
\boxed{
\Phi(r,\theta)=-E\left(r-\frac{a^3}{r^2}\right)\cos\theta,
\qquad r\geq a.}
\]

::: {.proof}
Insert the coefficients from step <1>2 into step <1>1. The result is harmonic for $r>a$, vanishes at $r=a$, and has the required asymptotic uniform field.
:::

<1>4. The induced total charge on the sphere is zero.

::: {.proof}
The exterior radial field at the surface is
\[
E_r(a,\theta)=-\partial_r\Phi(a,\theta)=3E\cos\theta.
\]
Hence the surface charge density is proportional to $\cos\theta$. Its integral over the sphere is proportional to
\[
\int_0^\pi\cos\theta\sin\theta\,d\theta=0.
\]
Equivalently, step <1>2 has no $r^{-1}$ monopole term. Thus the solution is consistent with the stipulated zero total charge.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 gives the requested exterior potential, and step <1>4 verifies the charge condition.
:::
:::
