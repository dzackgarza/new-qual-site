---
schema: qual/card@1
id: P-CASP04B
kind: problem
title: "Schwarz-Pick inequality for self-maps of the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $f \in \mathcal{O}(\DD)$ and assume that $\abs{f(z)} \leq 1$ in $\DD$.
Show that $$\frac{\abs{f(0)} - \abs{z}}{1 + \abs{f(0)}\abs{z}} \leq \abs{f(z)} \leq \frac{\abs{f(0)} + \abs{z}}{1 - \abs{f(0)}\abs{z}}.$$
:::

::: {.solution}

No retained solution set covers this exercise: the collection's provenance is the exam paper `assets/attachments/SP04_220_Complex_Analysis_Qual.pdf` and no solutions sheet accompanies it, so the argument below is the card's own. It rests on Schwarz--Pick and on the maximum modulus principle, and the three points the earlier version of the card left implicit are supplied: that $\abs{f(0)}<1$ unless $f$ is constant, that the denominator $1-\overline{a}f(z)$ does not vanish, and that the divisions by $1+Ar$ and $1-Ar$ are legitimate.

Throughout, $f$ is holomorphic on $\DD$ with $\abs{f(z)}\leq1$ there, $a\coloneqq f(0)$, $A\coloneqq\abs{a}\leq1$, and for a fixed $z\in\DD$ one writes $r\coloneqq\abs{z}$ and $s\coloneqq\abs{f(z)}\leq1$.

::: pf

::: {.pf-step #constant-case}
If $f$ is constant, the two inequalities hold.

::: pf-proof
Then $s=A$, so the left side is $\frac{A-r}{1+Ar}\leq A$ because $A-r\leq A+rA^{2}$ (the right-hand difference is $rA^{2}+r\geq0$), and the right side is $A\leq\frac{A+r}{1-Ar}$ because $A(1-Ar)=A-A^{2}r\leq A+r$; also $1-Ar>0$ since $A\leq1$ and $r<1$.
:::

:::

::: {.pf-step #nonconstant}
If $f$ is not constant, then $A<1$ and $1-\overline{a}f(z)\neq0$ for every $z\in\DD$.

::: pf-proof
If $A=1$ then $\abs{f}$ attains its maximum at the interior point $0$, so the maximum modulus principle makes $f$ constant, contrary to the hypothesis; hence $A<1$. Then $\abs{\overline{a}f(z)}=A\abs{f(z)}\leq A<1$, so $1-\overline{a}f(z)\neq0$.
:::

:::

::: {.pf-step #schwarz-pick}
$\abs{f(z)-a}\leq r\,\abs{1-\overline{a}f(z)}\leq r(1+As)$.

::: pf-proof
Schwarz--Pick applied to the self-map $f$ of $\DD$ with $f(0)=a$ gives $\Big|\frac{f(z)-a}{1-\overline{a}f(z)}\Big|\leq\abs{z}=r$, the denominator being nonzero by step [](#nonconstant){.pf-ref}. Multiplying by $\abs{1-\overline{a}f(z)}$ gives the first inequality, and $\abs{1-\overline{a}f(z)}\leq1+\abs{\overline{a}f(z)}=1+As$ gives the second.
:::

:::

::: {.pf-step #lower-bound}
$\dfrac{A-r}{1+Ar}\leq s$.

::: pf-proof
By the reverse triangle inequality, $A-s=\abs{a}-\abs{f(z)}\leq\abs{a-f(z)}=\abs{f(z)-a}\leq r(1+As)$ by step [](#schwarz-pick){.pf-ref}. Rearranging, $A-r\leq s+rAs=s(1+Ar)$, and $1+Ar\geq1>0$, so dividing gives $\frac{A-r}{1+Ar}\leq s$.
:::

:::

::: pf-step
Therefore
$$
\boxed{\frac{\abs{f(0)}-\abs{z}}{1+\abs{f(0)}\abs{z}}\ \leq\ \abs{f(z)}\ \leq\ \frac{\abs{f(0)}+\abs{z}}{1-\abs{f(0)}\abs{z}}.}
$$

::: pf-proof
The lower bound is step [](#lower-bound){.pf-ref} in the non-constant case and step [](#constant-case){.pf-ref} in the constant one. For the upper bound, the reverse triangle inequality gives $s-A=\abs{f(z)}-\abs{a}\leq\abs{f(z)-a}\leq r(1+As)$ by step [](#schwarz-pick){.pf-ref}, so $s(1-Ar)\leq A+r$; since $Ar\leq A<1$ in the non-constant case and $Ar<1$ in the constant one, $1-Ar>0$ and division gives $s\leq\frac{A+r}{1-Ar}$, again with step [](#constant-case){.pf-ref} covering the constant case. Substituting $A=\abs{f(0)}$, $r=\abs{z}$ and $s=\abs{f(z)}$ yields the displayed pair of inequalities.
:::

:::

:::

:::
