---
schema: qual/card@1
id: P-BKS17-4A
kind: problem
title: Legendre's relation for the Weierstrass zeta function
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the three-item property list (both quasi-periodicity relations and the pole condition as bullets) and inline-math spacing against Sp17_Exam_0.pdf page 5 problem 4A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 residue-theorem solution and checked the orientation sign by the determinant of the ordered basis $(\omega_1,\omega_2)$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the translated fundamental parallelogram has exactly one enclosed pole, the paired-side integral calculation, and the sign $\operatorname{sgn}\Im(\omega_2/\omega_1)$.
---

::: {.problem}
The Weierstrass zeta function $\zeta$ is a meromorphic function satisfying

- $\zeta(z + \omega_1) = \zeta(z) + \eta_1$
- $\zeta(z + \omega_2) = \zeta(z) + \eta_2$
- The singularities of $\zeta$ are poles of residue 1 at the points $m\omega_1 + n\omega_2$ for $m, n \in \ZZ$

Here $\omega_1, \omega_2, \eta_1, \eta_2$ are complex constants with $\omega_2 / \omega_1$ not real. Use Cauchy's residue theorem to prove Legendre's relation $\omega_2 \eta_1 - \omega_1 \eta_2 = \pm 2\pi i$ and express the sign in terms of $\omega_1$ and $\omega_2$.
:::

::: {.solution}

Put
$$
s\coloneqq\operatorname{sgn}\!\left(\Im\frac{\omega_2}{\omega_1}\right)\in\{\pm1\}.
$$

::: pf

::: {.pf-step #s1-1}

Let $P$ be the parallelogram with initial vertex
$$
z_0\coloneqq-\frac{\omega_1+\omega_2}{2}
$$
and ordered edge vectors $\omega_1,\omega_2$. Its boundary contains no pole of $\zeta$, and its interior contains exactly the pole at $0$.


::: pf-proof

Every point of $P$ has the form
$$
a\omega_1+b\omega_2,
\qquad
-\frac12\leq a,b\leq\frac12.
$$
A lattice point $m\omega_1+n\omega_2$ can lie in $P$ only when the integers $m,n$ both lie in $[-1/2,1/2]$, hence only when $m=n=0$. The point $0$ corresponds to $a=b=0$, so it lies in the interior. No lattice point lies on the boundary.

:::

:::

::: {.pf-step #s1-2}

If $\partial P$ is traversed in the order determined by the edges $\omega_1,\omega_2$, then
$$
\int_{\partial P}\zeta(z)\,dz
=
\omega_2\eta_1-\omega_1\eta_2.
$$


::: pf-proof

Write the four sides as
$$
z_0\to z_0+\omega_1,
\quad
z_0+\omega_1\to z_0+\omega_1+\omega_2,
\quad
z_0+\omega_1+\omega_2\to z_0+\omega_2,
\quad
z_0+\omega_2\to z_0.
$$
Let
$$
I_1\coloneqq\int_{z_0}^{z_0+\omega_1}\zeta(z)\,dz,
\qquad
I_2\coloneqq\int_{z_0}^{z_0+\omega_2}\zeta(z)\,dz.
$$
On the second side, substitute $z=w+\omega_1$ and use quasi-periodicity:
$$
\int_{z_0+\omega_1}^{z_0+\omega_1+\omega_2}\zeta(z)\,dz
=
I_2+\eta_1\omega_2.
$$
On the third side, reverse orientation and substitute $z=w+\omega_2$:
$$
\int_{z_0+\omega_1+\omega_2}^{z_0+\omega_2}\zeta(z)\,dz
=
-I_1-\eta_2\omega_1.
$$
The fourth side contributes $-I_2$. Adding the four side integrals gives
$$
\int_{\partial P}\zeta(z)\,dz
=
\eta_1\omega_2-\eta_2\omega_1.
$$

:::

:::

::: {.pf-step #s1-3}

The winding number of the ordered boundary $\partial P$ about $0$ is $s$.


::: pf-proof

Regard $\CC$ as the oriented real plane. The signed area determinant of the ordered edge vectors is
$$
\det_{\RR}(\omega_1,\omega_2)
=
\abs{\omega_1}^2\Im\!\left(\frac{\omega_2}{\omega_1}\right).
$$
Thus the traversal in step [](#s1-2){.pf-ref} is counterclockwise exactly when $s=1$ and clockwise exactly when $s=-1$. Since $0$ lies in the interior by step [](#s1-1){.pf-ref}, its winding number is therefore $s$.

:::

:::

::: {.pf-step #s1-4}

Legendre's relation is
$$
\boxed{
\omega_2\eta_1-\omega_1\eta_2
=
2\pi i\,
\operatorname{sgn}\!\left(\Im\frac{\omega_2}{\omega_1}\right)
}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $\zeta$ has exactly one pole inside $P$, namely $0$, and its residue there is $1$. Cauchy's residue theorem for a contour of winding number $s$ gives
$$
\int_{\partial P}\zeta(z)\,dz
=
2\pi i\,s.
$$
Step [](#s1-2){.pf-ref} identifies the left side with $\omega_2\eta_1-\omega_1\eta_2$, and step [](#s1-3){.pf-ref} identifies $s$ with the displayed sign.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required relation with its sign expressed in terms of $\omega_1$ and $\omega_2$.

:::

:::

:::
