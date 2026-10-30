---
schema: qual/card@1
id: P-TRIV-VP01
kind: problem
title: Fubini instanton for the potential $-\frac\lambda4 f^4$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 1, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md. Flash prefixes “Fubini instanton” with a garbled decorative glyph; that non-problem artifact is omitted from the card.
---

::: {.problem}
"Fubini instanton" Consider the functional $S[f] = 2\pi^2\int_0^{\infty} dx\, x^3\left( \frac{1}{2}f'^2 + V(f) \right)$, where $V(f) = -\frac{\lambda}{4}f^4$, and $f \in C^2[0, \infty]$.

(a) Write the differential equation on $f$, whose solution is an extremum of $S[f]$.

(b) Find all solutions to this equation satisfying the boundary conditions $f(\infty) = f'(\infty) = 0$.

(c) Compute the value of $S[f]$ on these solutions.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The Euler--Lagrange equation for
$$
S[f]
=
2\pi^2
\int_0^\infty
x^3
\left(
\frac12(f')^2
-
\frac\lambda4f^4
\right)
\,dx
$$
is
$$
\boxed{
f''+\frac3x f'+\lambda f^3=0.
}
$$


::: pf-proof

Ignoring the constant factor $2\pi^2$, the Lagrangian is
$$
L(x,f,f')
=
x^3
\left(
\frac12(f')^2
-
\frac\lambda4f^4
\right).
$$
Thus
$$
\frac{\partial L}{\partial f'}=x^3f'
$$
and
$$
\frac{\partial L}{\partial f}=-\lambda x^3f^3.
$$
The Euler--Lagrange equation gives
$$
\frac d{dx}(x^3f')
+
\lambda x^3f^3
=0.
$$
Divide by $x^3$ for $x>0$.

:::

:::

::: {.pf-step #s1-2}

Part (a) follows.


::: pf-proof

This is step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Set
$$
x=e^t,
\qquad
f(x)=e^{-t}u(t).
$$
Then the equation in step [](#s1-1){.pf-ref} becomes
$$
u''-u+\lambda u^3=0.
$$


::: pf-proof

Since $d/dx=e^{-t}d/dt$, one computes
$$
f'
=
e^{-2t}(u'-u)
$$
and
$$
f''
=
e^{-3t}(u''-3u'+2u).
$$
Also
$$
\frac3x f'
=
3e^{-3t}(u'-u)
$$
and
$$
\lambda f^3
=
\lambda e^{-3t}u^3.
$$
Substitution and multiplication by $e^{3t}$ give the autonomous equation.

:::

:::

::: {.pf-step #s1-4}

Regularity of $f$ at $x=0$ implies
$$
u(t)\to0
$$
and
$$
u'(t)\to0
$$
as $t\to-\infty$.


::: pf-proof

Since
$$
u(t)=x f(x),
$$
boundedness of $f$ near $0$ gives $u\to0$.
Also
$$
u'=xf+x^2f',
$$
which tends to $0$ because $f$ and $f'$ remain finite at the origin.

:::

:::

::: {.pf-step #s1-5}

The autonomous equation in step [](#s1-3){.pf-ref} has first integral
$$
\frac12(u')^2
-
\frac12u^2
+
\frac\lambda4u^4
=C.
$$


::: pf-proof

Multiply
$$
u''-u+\lambda u^3=0
$$
by $u'$ and integrate with respect to $t$.

:::

:::

::: {.pf-step #s1-6}

For every regular solution arising from step [](#s1-4){.pf-ref},
$$
C=0.
$$


::: pf-proof

Let $t\to-\infty$ in the first integral from step [](#s1-5){.pf-ref}. Step [](#s1-4){.pf-ref} gives
$$
u,u'\to0,
$$
so every term tends to zero.

:::

:::

::: {.pf-step #s1-7}

Every nonzero zero-energy solution satisfies
$$
u(t)
=
\pm\sqrt{\frac2\lambda}
\operatorname{sech}(t-t_0)
$$
for some $t_0\in\RR$.


::: pf-proof

From steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref},
$$
(u')^2
=
u^2
-
\frac\lambda2u^4
=
u^2
\left(
1-\frac\lambda2u^2
\right).
$$
The nonzero homoclinic orbit reaches the turning point
$$
\abs{u}=\sqrt{\frac2\lambda}
$$
where $u'=0$. Separating variables, or direct substitution, gives
$$
u(t)
=
\pm\sqrt{\frac2\lambda}
\operatorname{sech}(t-t_0).
$$
The translation parameter $t_0$ is arbitrary because the equation is
autonomous.

:::

:::

::: {.pf-step #s1-8}

Returning to $x$, let
$$
\rho=e^{t_0}>0.
$$
Then the nonzero solutions are
$$
\boxed{
f(x)
=
\pm\sqrt{\frac8\lambda}
\frac{\rho}{x^2+\rho^2},
\qquad
\rho>0.
}
$$


::: pf-proof

Since $x=e^t$,
$$
e^{-t}
\operatorname{sech}(t-t_0)
=
\frac1x
\frac{2}{e^{t-t_0}+e^{-(t-t_0)}}.
$$
With $\rho=e^{t_0}$ this simplifies to
$$
\frac{2\rho}{x^2+\rho^2}.
$$
Multiply by $\sqrt{2/\lambda}$.

:::

:::

::: {.pf-step #s1-9}

Together with
$$
\boxed{f\equiv0},
$$
the functions in step [](#s1-8){.pf-ref} are exactly the regular solutions satisfying
$$
f(\infty)=f'(\infty)=0.
$$


::: pf-proof

The functions in step [](#s1-8){.pf-ref} decay as $x^{-2}$, and their derivatives decay as $x^{-3}$, so they satisfy the boundary conditions.
Step [](#s1-7){.pf-ref} exhausts the nonzero zero-energy trajectories compatible with regularity at $x=0$.
The zero solution is immediate.

:::

:::

::: {.pf-step #s1-10}

Part (b) follows.


::: pf-proof

This is step [](#s1-9){.pf-ref}.

:::

:::

::: pf-step

For a nonzero solution from step [](#s1-8){.pf-ref}, write
$$
A=\sqrt{\frac8\lambda}.
$$
Then
$$
f
=
A\frac{\rho}{x^2+\rho^2}
$$
up to an irrelevant overall sign, and
$$
f'
=
-2A\rho
\frac{x}{(x^2+\rho^2)^2}.
$$


::: pf-proof

Differentiate the explicit formula from step [](#s1-8){.pf-ref}. The action depends only on $f^2$ and $f^4$, so the sign does not matter.

:::

:::

::: {.pf-step #s1-12}

The action density simplifies to
$$
\frac12(f')^2
-
\frac\lambda4f^4
=
\frac{16}{\lambda}
\frac{\rho^2(x^2-\rho^2)}{(x^2+\rho^2)^4}.
$$


::: pf-proof

Using $A^2=8/\lambda$,
$$
\frac12(f')^2
=
\frac{16}{\lambda}
\frac{\rho^2x^2}{(x^2+\rho^2)^4},
$$
while
$$
-\frac\lambda4f^4
=
-\frac{16}{\lambda}
\frac{\rho^4}{(x^2+\rho^2)^4}.
$$
Subtract the numerators.

:::

:::

::: {.pf-step #s1-13}

Therefore
$$
S[f]
=
\frac{32\pi^2}{\lambda}
\int_0^\infty
\frac{x^3\rho^2(x^2-\rho^2)}{(x^2+\rho^2)^4}
\,dx.
$$


::: pf-proof

Substitute step [](#s1-12){.pf-ref} into the definition of $S[f]$ and multiply by the factor $2\pi^2$.

:::

:::

::: {.pf-step #s1-14}

With
$$
x=\rho t,
$$
the integral in step [](#s1-13){.pf-ref} becomes
$$
\int_0^\infty
\frac{t^3(t^2-1)}{(1+t^2)^4}
\,dt.
$$


::: pf-proof

Substitute $x=\rho t$ and $dx=\rho dt$.
All powers of $\rho$ cancel.

:::

:::

::: {.pf-step #s1-15}

One has
$$
\int_0^\infty
\frac{t^3(t^2-1)}{(1+t^2)^4}
\,dt
=
\frac1{12}.
$$


::: pf-proof

Set
$$
u=t^2,
\qquad
t^3dt=\frac12u\,du.
$$
Then the integral is
$$
\frac12
\int_0^\infty
\frac{u(u-1)}{(1+u)^4}
\,du.
$$
Write
$$
u(u-1)
=
(1+u)^2
-
3(1+u)
+
2.
$$
Thus the integral equals
$$
\frac12
\int_0^\infty
\left[
\frac1{(1+u)^2}
-
\frac3{(1+u)^3}
+
\frac2{(1+u)^4}
\right]du.
$$
Using
$$
\int_0^\infty(1+u)^{-m}\,du
=
\frac1{m-1}
$$
for $m>1$, this becomes
$$
\frac12
\left(
1
-
\frac32
+
\frac23
\right)
=
\frac1{12}.
$$

:::

:::

::: {.pf-step #s1-16}

Hence every nonzero solution has action
$$
\boxed{
S[f]
=
\frac{8\pi^2}{3\lambda}.
}
$$


::: pf-proof

Combine steps [](#s1-13){.pf-ref} through [](#s1-15){.pf-ref}:
$$
S[f]
=
\frac{32\pi^2}{\lambda}
\cdot
\frac1{12}
=
\frac{8\pi^2}{3\lambda}.
$$

:::

:::

::: {.pf-step #s1-17}

The zero solution has action
$$
\boxed{S[0]=0}.
$$


::: pf-proof

Substitute $f=0$ into the functional.

:::

:::

::: {.pf-step #s1-18}

Part (c) follows.


::: pf-proof

Steps [](#s1-16){.pf-ref} through [](#s1-17){.pf-ref} give the action on all solutions from part (b).

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} and [](#s1-10){.pf-ref}, and [](#s1-18){.pf-ref} establish parts (a), (b), and (c), respectively.

:::

:::

:::
