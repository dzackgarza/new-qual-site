---
schema: qual/card@1
id: P-BKS06-2A
kind: problem
title: Values of $c$ for which $f''-cf'+16f=0$, $f(0)=f(1)=1$ has no solution
classification:
  areas: [prelim]
  topics:
  - Calculus
relations: []
review: draft
---

::: {.problem}
Find (with proof) all real numbers $c$ such that the differential equation with boundary conditions
$$
f'' - c f' + 16 f = 0, \qquad f(0) = f(1) = 1
$$
has no solution.
:::

::: {.solution}

The answer is $c=\pm\sqrt{64-4\pi^2}$.

::: pf

::: {.pf-step #s1}

If $c=\pm8$, the problem has a solution.

::: pf-proof

Then $x^2-cx+16$ has the double root $r=c/2=\pm4$, and the solutions are $f(t)=(at+b)e^{rt}$. The conditions $f(0)=1$, $f(1)=1$ read $b=1$ and $(a+1)e^{r}=1$, which hold for $a=e^{-r}-1$.

:::

:::

::: {.pf-step #s2}

If $c\ne\pm8$, let $\alpha\ne\beta$ be the complex roots of $x^2-cx+16$. The problem has a solution if and only if the system
$$
a+b=1,\qquad ae^{\alpha}+be^{\beta}=1
$$
has a solution $(a,b)\in\CC^2$.

::: pf-proof

The complex solutions of the equation are $f(t)=ae^{\alpha t}+be^{\beta t}$, and the boundary conditions are the displayed system. If a complex solution $f$ exists, then $\operatorname{Re}f$ is a real solution with the same real boundary values, because the equation has real coefficients. A real solution is a complex solution.

:::

:::

::: {.pf-step #s3}

If $e^{\alpha}\ne e^{\beta}$, the system of step [](#s2){.pf-ref} has a solution.

::: pf-proof

Its determinant is $e^{\beta}-e^{\alpha}\ne0$.

:::

:::

::: {.pf-step #s4}

If $e^{\alpha}=e^{\beta}$, the system of step [](#s2){.pf-ref} has no solution.

::: pf-proof

The system then forces $(a+b)e^{\alpha}=1$ with $a+b=1$, so $e^{\alpha}=1=e^{\beta}$. Then $e^{c}=e^{\alpha+\beta}=1$, so $c=0$. For $c=0$ the roots are $\pm4i$, and $e^{4i}\ne e^{-4i}$ because $\sin4\ne0$. This contradicts $e^{\alpha}=e^{\beta}$.

:::

:::

::: {.pf-step #s5}

For $c\ne\pm8$, $e^{\alpha}=e^{\beta}$ if and only if $c=\pm\sqrt{64-4\pi^2}$.

::: pf-proof

$e^{\alpha}=e^{\beta}$ means $\alpha-\beta=2\pi ik$ for a nonzero integer $k$, and we may take $k>0$. Since $(\alpha-\beta)^2=c^2-64$, this means $c^2=64-4\pi^2k^2$. A real $c$ exists only when $4\pi^2k^2\le64$, that is $k=1$, because $4\pi^2<64<16\pi^2$. Conversely, for $c=\pm\sqrt{64-4\pi^2}$ the roots are $c/2\pm\pi i$, whose difference is $2\pi i$.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} to [](#s5){.pf-ref}, the problem has no solution exactly when $c=\pm\sqrt{64-4\pi^2}$.

:::

:::

:::
