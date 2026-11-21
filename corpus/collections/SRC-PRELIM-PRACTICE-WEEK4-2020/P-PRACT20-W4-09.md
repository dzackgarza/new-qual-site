---
schema: qual/card@1
id: P-PRACT20-W4-09
kind: problem
title: The Bernoulli equation $y'+\frac4xy=x^3y^2$ and the substitution for $y^\alpha$
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-18
  note: >-
    Read against the retained solution booklet of the collection,
    assets/attachments/Week4_solns.pdf, where Problem 9 is on page 3 with its solution running onto
    page 4: "(Bernoulli Equations) Find the general solution of the differential equation
    y' + 4/x y = x^3 y^2 by making the substitution u = 1/y. Can you generalize this substitution so
    that it would work if y^2 on the right hand side was replaced by y^alpha for any alpha != 0, 1?"
    The extraction of the PDF flattens the fraction 4/x to "x4", which is a typesetting artifact of
    the text layer, not the booklet's statement; the card states the equation in the form the
    booklet's own solution uses. The stored statement is the printed one.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the prose solution into a Lamport proof. The card's prose was already the booklet's
    argument; the steps now record what it left implicit, namely that y = 0 is a separate solution
    and why (1/u cannot vanish), that the integrating factor is x^{-4} for x > 0 with the computation
    of (u/x^4)' shown, and that the exponent beta = 1 - alpha is forced rather than merely
    sufficient. Both answers, the general solution and the linearised equation, are unchanged and
    agree with the booklet.
---

::: {.problem}
(Bernoulli Equations)

(a) Find the general solution of the differential equation $y' + \frac{4}{x} y = x^{3} y^{2}$ by making the substitution $u = 1/y$.

(b) Generalize this substitution so that it works if $y^{2}$ on the right hand side is replaced by $y^{\alpha}$ for any $\alpha \neq 0, 1$.
:::

::: {.solution}
The retained solution booklet answers both parts — **Christian Parkinson, *GRE Prep: Diff. Eq. & Lin. Alg. Practice Problem Solutions*, Problem 9, pages 3--4 of `assets/attachments/Week4_solns.pdf`** — and the steps below are its argument with each integration written out. Work on an interval where $x>0$.

::: pf

::: {.pf-step #zero}
$y\equiv0$ solves $y'+\frac{4}{x}y=x^{3}y^{2}$.

::: pf-proof
Both sides vanish identically: the left side is $0+\frac{4}{x}\cdot0=0$ and the right side is $x^{3}\cdot0=0$.
:::

:::

::: {.pf-step #substitution}
On an interval where $y\ne0$, the function $u=1/y$ satisfies $u'=\frac{4}{x}u-x^{3}$.

::: pf-proof
Differentiating $u=y^{-1}$ gives $u'=-y^{-2}y'$. Solving the equation for $y'$ and substituting, $y'=-\frac{4}{x}y+x^{3}y^{2}$, so
$$u'=-y^{-2}\Bigl(-\frac{4}{x}y+x^{3}y^{2}\Bigr)=\frac{4}{x}y^{-1}-x^{3}=\frac{4}{x}u-x^{3}.$$
:::

:::

::: {.pf-step #integrating-factor}
$\dfrac{d}{dx}\Bigl(\dfrac{u}{x^{4}}\Bigr)=-\dfrac{1}{x}$.

::: pf-proof
The equation of step [](#substitution){.pf-ref} reads $u'-\frac{4}{x}u=-x^{3}$, which is linear with coefficient $-\frac{4}{x}$. Since $\int-\frac{4}{x}dx=-4\log x$, the integrating factor is $e^{-4\log x}=x^{-4}$ for $x>0$. Then $\bigl(ux^{-4}\bigr)'=x^{-4}u'-\frac{4}{x^{5}}u=x^{-4}\bigl(u'-\frac{4}{x}u\bigr)=x^{-4}(-x^{3})=-\frac{1}{x}$.
:::

:::

::: {.pf-step #integrate}
$u(x)=Cx^{4}-x^{4}\log x$ for a constant $C$.

::: pf-proof
Integrating step [](#integrating-factor){.pf-ref} on $x>0$ gives $ux^{-4}=C-\log x$, since $\int-\frac{dx}{x}=-\log x$; multiplying by $x^{4}$ gives the displayed $u$.
:::

:::

::: {.pf-step #answer-a}
(a) $\boxed{y(x)=\dfrac{1}{Cx^{4}-x^{4}\log x}}$ on intervals where the denominator does not vanish, together with $y\equiv0$.

::: pf-proof
Inverting $u=1/y$ in step [](#integrate){.pf-ref} gives the displayed $y$ on any interval where $y\ne0$, that is where $Cx^{4}-x^{4}\log x\ne0$; an interval where it vanishes is excluded because $u$ is then undefined there. The zero solution of step [](#zero){.pf-ref} is not of this form for any $C$, since $1/u$ cannot vanish, so it is listed separately.
:::

:::

::: {.pf-step #general}
For $y'+p(x)y=q(x)y^{\alpha}$ with $\alpha\ne0,1$, the substitution $u=y^{1-\alpha}$ linearises the equation as $u'+(1-\alpha)p(x)u=(1-\alpha)q(x)$.

::: pf-proof
On an interval where $y>0$, put $u=y^{\beta}$. Then $u'=\beta y^{\beta-1}y'=\beta y^{\beta-1}\bigl(-p(x)y+q(x)y^{\alpha}\bigr)=-\beta p(x)y^{\beta}+\beta q(x)y^{\alpha+\beta-1}=-\beta p(x)u+\beta q(x)y^{\alpha+\beta-1}$. The last term still carries a power of $y$ unless $\alpha+\beta-1=0$, that is $\beta=1-\alpha$; and $\beta\ne0$ because $\alpha\ne1$, so $u$ is a genuine substitution. With that choice, $u'=-(1-\alpha)p(x)u+(1-\alpha)q(x)$, which is the displayed linear equation.
:::

:::

::: {.pf-step #answer-b}
(b) The substitution is $u=y^{1-\alpha}$, and it is the choice $\beta=1-\alpha$ that is forced.

::: pf-proof
Step [](#general){.pf-ref} exhibits $u=y^{1-\alpha}$ and the linear equation it satisfies. Uniqueness of the exponent: the coefficient of the offending term is $\beta q(x)y^{\alpha+\beta-1}$, which vanishes identically only if $\alpha+\beta-1=0$, so no other $\beta$ works. For $\alpha=2$ this recovers $\beta=-1$, that is $u=1/y$, the substitution of part (a).
:::

:::

:::
:::
