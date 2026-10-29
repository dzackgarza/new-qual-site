---
schema: qual/card@1
id: P-TRIV-DE20
kind: problem
title: Frobenius series of $(\xi u')'+(\frac12E\xi+\alpha-\frac{m^2}{4\xi}-\frac14F\xi^2)u=0$ at $\xi=0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 20, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Given the differential equation

$$
\frac { d } { d \xi } \left( \xi \frac { d u } { d \xi } \right) + \left( \frac { 1 } { 2 } E \xi + \alpha - \frac { m ^ { 2 } } { 4 \xi } - \frac { 1 } { 4 } F \xi ^ { 2 } \right) u = 0\tag{29}
$$

Find the first three terms of a series solution around $\xi = 0$ by using the largest solution of the indicial equation.
:::

::: {.solution}

Seek a Frobenius solution
$$
u(\xi)=\xi^r\sum_{n=0}^{\infty}a_n\xi^n,
\qquad a_0\ne0.
$$

::: pf

::: {.pf-step #s1-1}

The indicial equation is
$$
r^2-\frac{m^2}{4}=0,
$$
so its largest root is
$$
r=\frac{|m|}{2}.
$$


::: pf-proof

For the declared Frobenius series,
$$
\frac d{d\xi}\left(\xi u'\right)
=\sum_{n=0}^{\infty}(n+r)^2a_n\xi^{n+r-1}.
$$
The only other contribution to the lowest power $\xi^{r-1}$ is
$$
-\frac{m^2}{4\xi}u,
$$
whose coefficient is $-m^2a_0/4$. Since $a_0\ne0$, the coefficient of $\xi^{r-1}$ vanishes exactly when $r^2-m^2/4=0$. The larger of the two roots $\pm |m|/2$ is $|m|/2$.

:::

:::

::: {.pf-step #s1-2}

With $a_{-1}=a_{-2}=a_{-3}=0$, the coefficients satisfy
$$
\left((n+r)^2-\frac{m^2}{4}\right)a_n
+\alpha a_{n-1}
+\frac E2a_{n-2}
-\frac F4a_{n-3}=0
\qquad(n\geq0).
$$


::: pf-proof

Substitute the Frobenius series into the differential equation and collect the coefficient of $\xi^{n+r-1}$. The derivative term and the $m^2/(4\xi)$ term contribute the coefficient multiplying $a_n$; multiplication by $\alpha$, $E\xi/2$, and $-F\xi^2/4$ shifts the coefficient index by one, two, and three respectively.

:::

:::

::: {.pf-step #s1-3}

The coefficient of the second term is
$$
a_1=-\frac{\alpha}{2r+1}a_0.
$$


::: pf-proof

Set $n=1$ in step [](#s1-2){.pf-ref}. Since $r^2=m^2/4$ by step [](#s1-1){.pf-ref},
$$
\bigl((r+1)^2-r^2\bigr)a_1+\alpha a_0=0.
$$
The difference of squares is $2r+1$, which gives the formula.

:::

:::

::: {.pf-step #s1-4}

The coefficient of the third term is
$$
a_2=\frac{a_0}{4(r+1)}
\left(\frac{\alpha^2}{2r+1}-\frac E2\right).
$$


::: pf-proof

Set $n=2$ in step [](#s1-2){.pf-ref} and use step [](#s1-1){.pf-ref}:
$$
4(r+1)a_2+\alpha a_1+\frac E2a_0=0.
$$
Substituting $a_1$ from step [](#s1-3){.pf-ref} and solving for $a_2$ gives the displayed expression.

:::

:::

::: {.pf-step #s1-5}

Therefore, with $r=|m|/2$, the first three terms are
$$
\boxed{
u(\xi)=a_0\xi^r
\left[
1-\frac{\alpha}{2r+1}\xi
+\frac{1}{4(r+1)}
\left(\frac{\alpha^2}{2r+1}-\frac E2\right)\xi^2
+O(\xi^3)
\right]}.
$$


::: pf-proof

Insert the coefficients from steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} into the Frobenius series. The parameter $F$ first occurs in the recurrence at $n=3$, so it does not enter the first three terms.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the requested three-term series corresponding to the largest indicial root.

:::

:::

:::
