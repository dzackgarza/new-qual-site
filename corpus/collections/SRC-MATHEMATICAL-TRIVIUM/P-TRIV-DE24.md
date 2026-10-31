---
schema: qual/card@1
id: P-TRIV-DE24
kind: problem
title: Frobenius series for the Bessel functions $J_{\pm p}$
classification:
  areas: [prelim]
  topics:
  - Frobenius Method
  - Bessel Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 24, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed stray =0 residue against Differential Equations Problem 24 on page 24 of the source PDF and added a remark on the source's undefined n in the normalization.
---

::: {.problem}
Bessel equation of order $p$ is
$$
x^2 y'' + x y' + (x^2 - p^2) y = 0
\tag{36}
$$
Assuming $y = \sum_{m=0} a_m x^{r+m}$, find the two roots of the indicial equation (the two possible values of $r$).
For both of them, solve the recurrence relation for the $a_i$.
You should find, for the largest root, $J_p(x) = \sum_{k=0}^\infty \frac{(-1)^k}{k!\,\Gamma(k+p+1)} \left(\frac{x}{2}\right)^{2k+p}$, and for the smallest $J_{-p}(x) = \sum_{k=0}^\infty \frac{(-1)^k}{k!\,\Gamma(k-p+1)} \left(\frac{x}{2}\right)^{2k-p}$ (for the normalization, assume that $a_0 = \frac{1}{2^n n!}$).
These are Bessel function of the first kind.
:::

::: {.remark}
The normalization $a_0 = \frac{1}{2^n n!}$ in the source uses an undefined $n$.
The stated series have leading coefficient $a_0 = \frac{1}{2^p\,\Gamma(p+1)}$ for $J_p$ and $a_0 = \frac{1}{2^{-p}\,\Gamma(1-p)}$ for $J_{-p}$; the source's formula is the case $p = n \in \NN_0$ of the first.
:::

::: {.solution}

Take
$$
y(x)=\sum_{m=0}^{\infty}a_mx^{r+m},
\qquad a_0\ne0.
$$

::: pf

::: {.pf-step #s1-1}

The indicial equation is
$$
r^2-p^2=0,
$$
with roots
$$
\boxed{r=p\quad\text{and}\quad r=-p}.
$$


::: pf-proof

Substitution into Bessel's equation gives
$$
\sum_{m=0}^{\infty}\bigl((r+m)^2-p^2\bigr)a_mx^{r+m}
+\sum_{m=0}^{\infty}a_mx^{r+m+2}=0.
$$
The coefficient of the lowest power $x^r$ is $(r^2-p^2)a_0$. Since $a_0\ne0$, it vanishes exactly for $r=\pm p$.

:::

:::

::: {.pf-step #s1-2}

For either indicial root, $a_1=0$ and, for $m\geq2$,
$$
\boxed{a_m=-\frac{a_{m-2}}{(r+m)^2-p^2}}.
$$


::: pf-proof

Shift the second sum in step [](#s1-1){.pf-ref} by two indices. For $m\geq2$, the coefficient of $x^{r+m}$ is
$$
\bigl((r+m)^2-p^2\bigr)a_m+a_{m-2}.
$$
For $m=1$, the coefficient is $((r+1)^2-p^2)a_1$, which gives $a_1=0$ whenever that factor is nonzero. Thus all odd coefficients vanish in the generic Frobenius case, and the displayed recurrence determines the even coefficients.

:::

:::

::: {.pf-step #s1-3}

For the root $r=p$,
$$
a_{2k}=(-1)^k a_0\frac{\Gamma(p+1)}{4^k k!\,\Gamma(k+p+1)}.
$$


::: pf-proof

With $r=p$, step [](#s1-2){.pf-ref} becomes
$$
a_{2k}=-\frac{a_{2k-2}}{(p+2k)^2-p^2}
=-\frac{a_{2k-2}}{4k(k+p)}.
$$
Iterating gives
$$
a_{2k}=\frac{(-1)^ka_0}{4^k k!(p+1)(p+2)\cdots(p+k)}.
$$
Since
$$
(p+1)\cdots(p+k)=\frac{\Gamma(p+k+1)}{\Gamma(p+1)},
$$
the formula follows.

:::

:::

::: {.pf-step #s1-4}

Choosing $a_0=1/(2^p\Gamma(p+1))$ gives
$$
\boxed{
J_p(x)=\sum_{k=0}^{\infty}
\frac{(-1)^k}{k!\,\Gamma(k+p+1)}
\left(\frac x2\right)^{2k+p}}.
$$


::: pf-proof

Insert the normalization into step [](#s1-3){.pf-ref} and multiply $a_{2k}$ by $x^{p+2k}$. The factors $2^p4^k=2^{p+2k}$ combine into $(x/2)^{p+2k}$.

:::

:::

::: {.pf-step #s1-5}

For the root $r=-p$,
$$
a_{2k}=(-1)^ka_0\frac{\Gamma(1-p)}{4^k k!\,\Gamma(k-p+1)}.
$$


::: pf-proof

With $r=-p$, step [](#s1-2){.pf-ref} gives
$$
a_{2k}=-\frac{a_{2k-2}}{(-p+2k)^2-p^2}
=-\frac{a_{2k-2}}{4k(k-p)}.
$$
Iteration and the identity
$$
(1-p)(2-p)\cdots(k-p)=\frac{\Gamma(k-p+1)}{\Gamma(1-p)}
$$
give the result.

:::

:::

::: {.pf-step #s1-6}

Choosing $a_0=2^p/\Gamma(1-p)$ gives
$$
\boxed{
J_{-p}(x)=\sum_{k=0}^{\infty}
\frac{(-1)^k}{k!\,\Gamma(k-p+1)}
\left(\frac x2\right)^{2k-p}}.
$$


::: pf-proof

Insert this normalization into step [](#s1-5){.pf-ref} and multiply by $x^{-p+2k}$. Since $2^{-p+2k}=4^k/2^p$, the coefficients take exactly the displayed form.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} give the indicial roots and recurrence, while steps [](#s1-3){.pf-ref} through [](#s1-6){.pf-ref} give the two normalized Frobenius series requested in the problem.

:::

:::

:::
