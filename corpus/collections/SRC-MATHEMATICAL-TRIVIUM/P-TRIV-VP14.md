---
schema: qual/card@1
id: P-TRIV-VP14
kind: problem
title: Q-ball ansatz in the Euler--Lagrange equations of a complex scalar field
classification:
  areas: [prelim]
  topics:
  - Euler-Lagrange Equations
  - Field Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 14, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash concatenates the `14.` marker to the end of Problem 13; source order unambiguously separates this as Problem 14.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed a stray extraction digit against Variational Principle Problem 14 on page 21 of the source PDF and added a remark on the source's variable x for r.
---

::: {.problem}
Consider the functional $S[\phi, \phi^*] = 4\pi \int_{-\infty}^{\infty} dt \int_0^\infty dr\, r^2 \left(\dot{\phi}\dot{\phi}^* - \phi'\phi'^* - U(\phi\phi^*)\right)$, where $U \in C^1(\RR)$ and $\phi$ is a $C^2(\RR \times [0, \infty))$ complex-valued function of $t$ and $x$.

(a) Varying with respect to $\phi$ and $\phi^*$, obtain the Euler-Lagrange equation and its conjugated.
Substituting the *ansatz* $\phi(r, t) = f(r) e^{i\omega t}$, rewrite them as an equation on a function $f$ of a single variable $r$.

(b) Substitute the ansatz $\phi(r, t) = f(r) e^{i\omega t}$ into the functional $S[\phi, \phi^*]$ first, and, varying with respect to $f$, obtain the Euler-Lagrange equation on $f$.
Compare with the result of the previous point.
:::

::: {.remark}
The source says $\phi$ is a function "of $t$ and $x$", but the functional and the ansatz use the radial variable $r \in [0, \infty)$, with $\dot{\phi} = \partial_t \phi$ and $\phi' = \partial_r \phi$; the intended variables are $t$ and $r$.
After the harmonic ansatz is substituted, the integrand is independent of $t$, so the printed integral over all $t\in\RR$ contributes an infinite common factor. Part (b) is therefore interpreted as variation of the reduced action per unit time, equivalently as variation on any finite time interval before removing that overall factor.
:::

::: {.solution}

Write
$$
s=\phi\phi^*.
$$
Treat $\phi$ and $\phi^*$ as independent fields in the variation.

::: pf

::: {.pf-step #s1-1}

The Lagrangian density, including the radial measure factor, is
$$
\mathcal L
=
r^2
\left(
\dot\phi\dot\phi^*
-
\phi'\phi'^*
-
U(s)
\right).
$$


::: pf-proof

This is the integrand of the given functional after omitting the constant factor $4\pi$.

:::

:::

::: {.pf-step #s1-2}

Variation with respect to $\phi^*$ gives
$$
\frac{\partial\mathcal L}{\partial\phi^*}
-
\partial_t
\frac{\partial\mathcal L}{\partial\dot\phi^*}
-
\partial_r
\frac{\partial\mathcal L}{\partial\phi'^*}
=0.
$$


::: pf-proof

This is the Euler--Lagrange equation for a field depending on the independent variables $t$ and $r$.

:::

:::

::: {.pf-step #s1-3}

The three derivatives in step [](#s1-2){.pf-ref} are
$$
\frac{\partial\mathcal L}{\partial\phi^*}
=
-r^2U'(s)\phi,
$$
$$
\frac{\partial\mathcal L}{\partial\dot\phi^*}
=
r^2\dot\phi,
$$
and
$$
\frac{\partial\mathcal L}{\partial\phi'^*}
=
-r^2\phi'.
$$


::: pf-proof

Differentiate the expression from step [](#s1-1){.pf-ref}. For the potential term, use
$$
\frac{\partial}{\partial\phi^*}U(\phi\phi^*)
=
U'(s)\phi.
$$

:::

:::

::: {.pf-step #s1-4}

Hence the field equation is
$$
\boxed{
\ddot\phi
-
\phi''
-
\frac2r\phi'
+
U'(\abs{\phi}^2)\phi
=0.
}
$$


::: pf-proof

Substitute step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref}:
$$
-r^2U'(s)\phi
-
r^2\ddot\phi
+
\partial_r(r^2\phi')
=0.
$$
Expand
$$
\partial_r(r^2\phi')
=
r^2\phi''+2r\phi'
$$
and divide by $-r^2$.

:::

:::

::: {.pf-step #s1-5}

Variation with respect to $\phi$ gives the conjugate equation
$$
\boxed{
\ddot\phi^*
-
\phi^{*\prime\prime}
-
\frac2r\phi^{*\prime}
+
U'(\abs{\phi}^2)\phi^*
=0.
}
$$


::: pf-proof

Repeat steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} with $\phi$ and $\phi^*$ interchanged. Since $U$ is real-valued, $U'(s)$ is real for real $s=\abs{\phi}^2$, so the result is the complex conjugate of step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Substitute
$$
\phi(r,t)=f(r)e^{i\omega t}
$$
with real $f$. Then
$$
\ddot\phi=-\omega^2\phi,
\qquad
\phi'=f'e^{i\omega t},
\qquad
\phi''=f''e^{i\omega t}.
$$


::: pf-proof

Differentiate the ansatz with respect to $t$ and $r$.

:::

:::

::: {.pf-step #s1-7}

Equation [](#s1-4){.pf-ref} then becomes
$$
\boxed{
f''
+
\frac2r f'
+
\omega^2 f
-
U'(f^2)f
=0.
}
$$


::: pf-proof

Substitute step [](#s1-6){.pf-ref} into step [](#s1-4){.pf-ref} and divide by the nonzero factor $e^{i\omega t}$.

:::

:::

::: {.pf-step #s1-8}

The conjugate equation gives the same real equation for $f$.


::: pf-proof

Substitute
$$
\phi^*=f(r)e^{-i\omega t}
$$
into step [](#s1-5){.pf-ref}. The factor $e^{-i\omega t}$ cancels and yields step [](#s1-7){.pf-ref} again.

:::

:::

::: {.pf-step #s1-9}

Part (a) follows.


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-8){.pf-ref} give the field equation, its conjugate, and the reduced radial equation.

:::

:::

::: {.pf-step #s1-10}

Substituting the ansatz into the integrand first gives the reduced action per unit time
$$
\boxed{
S_{\mathrm{red}}[f]
=
4\pi
\int_0^\infty
r^2
\left(
\omega^2f^2
-
(f')^2
-
U(f^2)
\right)dr.
}
$$


::: pf-proof

For the ansatz,
$$
\dot\phi\dot\phi^*=\omega^2f^2,
$$
$$
\phi'\phi'^*=(f')^2,
$$
and
$$
\phi\phi^*=f^2.
$$
The time dependence therefore cancels completely, leaving the displayed spatial functional after dividing out the common time interval.

:::

:::

::: {.pf-step #s1-11}

The reduced Euler--Lagrange equation is
$$
\frac{\partial L_{\mathrm{red}}}{\partial f}
-
\frac d{dr}
\frac{\partial L_{\mathrm{red}}}{\partial f'}
=0,
$$
where
$$
L_{\mathrm{red}}
=
r^2
\left(
\omega^2f^2
-
(f')^2
-
U(f^2)
\right).
$$


::: pf-proof

This is the ordinary one-variable Euler--Lagrange equation for the reduced functional in step [](#s1-10){.pf-ref}.

:::

:::

::: {.pf-step #s1-12}

One has
$$
\frac{\partial L_{\mathrm{red}}}{\partial f}
=
2r^2
\left(
\omega^2f
-
U'(f^2)f
\right)
$$
and
$$
\frac{\partial L_{\mathrm{red}}}{\partial f'}
=
-2r^2f'.
$$


::: pf-proof

Differentiate the reduced Lagrangian from step [](#s1-11){.pf-ref}. For the potential term, use
$$
\frac d{df}U(f^2)
=
2fU'(f^2).
$$

:::

:::

::: {.pf-step #s1-13}

Therefore the reduced Euler--Lagrange equation is again
$$
\boxed{
f''
+
\frac2r f'
+
\omega^2 f
-
U'(f^2)f
=0.
}
$$


::: pf-proof

Substitute step [](#s1-12){.pf-ref} into step [](#s1-11){.pf-ref}:
$$
2r^2(\omega^2f-U'(f^2)f)
+
2\frac d{dr}(r^2f')
=0.
$$
Divide by $2r^2$ and expand the derivative.

:::

:::

::: {.pf-step #s1-14}

The two procedures commute for this ansatz: varying first and substituting later gives exactly the same radial equation as substituting first and varying later.


::: pf-proof

Compare steps [](#s1-7){.pf-ref} and [](#s1-13){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} proves part (a), and steps [](#s1-10){.pf-ref} through [](#s1-14){.pf-ref} prove part (b) and the requested comparison.

:::

:::

:::
