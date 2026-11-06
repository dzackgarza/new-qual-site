---
schema: qual/card@1
id: E-AMD-BYJBCLC5
kind: problem
title: Normality of $\QQ(\sqrt[3]{2})/\QQ$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (a
    yes/no question with the answer "no", no repair needed), and the existing prose
    solution against a fresh re-derivation: x^3 - 2 has no rational root (the
    candidates are the integers dividing 2, and f at 1, -1, 2, -2 is -1, -3, 6,
    -10), so it is irreducible and is the minimal polynomial of alpha = cuberoot 2;
    the roots in C are alpha, alpha*zeta, alpha*zeta^2 with zeta a primitive cube
    root of unity, and they are distinct; Q(alpha) lies in R because alpha does,
    while the other two roots have imaginary parts +-alpha*sqrt(3)/2; so an
    irreducible polynomial with a root in Q(alpha) does not split there. Correct.
    The prose said "irreducible by Eisenstein at 2", which is true but leaves the
    reader to check the hypothesis; the structured proof gives the rational root
    argument instead and states the definition of normality it uses. No source
    solution is retained for this card, so no source comparison was made. What was
    not checked: any printed source.
---

::: {.exercise}
Is $\QQ(2^{1/3})/\QQ$ normal?
:::

::: {.solution}
Let $\alpha=\sqrt[3]{2}\in\RR$, let $f(x)=x^3-2$, and let $\zeta$ be a primitive cube root of unity, so that $\zeta^3=1$, $\zeta\neq1$ and $1+\zeta+\zeta^2=0$. Recall that $K/\QQ$ is normal when every irreducible polynomial over $\QQ$ having one root in $K$ splits into linear factors over $K$.

::: pf

::: {.pf-step #irreducible}
$f$ is irreducible over $\QQ$, so $f$ is the minimal polynomial of $\alpha$ and $[\QQ(\alpha):\QQ]=3$.

::: pf-proof
$f$ is monic and satisfies $f(\alpha)=\alpha^3-2=0$. A rational root of $x^3-2$ would be an integer $d$ dividing $2$, and $f(1)=-1$, $f(-1)=-3$, $f(2)=6$, $f(-2)=-10$ are all nonzero, so $f$ has no rational root; a cubic over a field with no root is irreducible. The degree of a simple algebraic extension is the degree of the minimal polynomial, so $[\QQ(\alpha):\QQ]=3$.
:::

:::

::: {.pf-step #roots}
The roots of $f$ in $\CC$ are exactly $\alpha$, $\alpha\zeta$ and $\alpha\zeta^2$, and they are distinct.

::: pf-proof
The roots of $x^3=2$ are the three numbers whose cube is $2$; since $(\alpha\zeta)^3=\alpha^3\zeta^3=2$ and $(\alpha\zeta^2)^3=\alpha^3\zeta^6=2$, and a nonzero cubic has at most three roots in the field $\CC$, these three are all of them. They are distinct because $\alpha\neq0$ and $1,\zeta,\zeta^2$ are distinct.
:::

:::

::: {.pf-step #real}
$\QQ(\alpha)\subseteq\RR$, while $\alpha\zeta$ and $\alpha\zeta^2$ are not real.

::: pf-proof
$\alpha\in\RR$ and $\QQ\subseteq\RR$, so every element of $\QQ(\alpha)$ — a rational function in $\alpha$ with rational coefficients — is real. For the other two roots, write $\zeta=-\tfrac12+\tfrac{\sqrt3}{2}i$ and $\zeta^2=-\tfrac12-\tfrac{\sqrt3}{2}i$; then $\alpha\zeta$ has imaginary part $\alpha\sqrt3/2$ and $\alpha\zeta^2$ has imaginary part $-\alpha\sqrt3/2$, both nonzero because $\alpha>1>0$.
:::

:::

::: {.pf-step}
$\QQ(\sqrt[3]{2})/\QQ$ is not normal, so the answer to the question is no.

::: pf-proof
By step [](#irreducible){.pf-ref}, $f$ is an irreducible polynomial over $\QQ$; by step [](#roots){.pf-ref} it has the root $\alpha\in\QQ(\alpha)$; and by steps [](#roots){.pf-ref} and [](#real){.pf-ref} its two remaining roots $\alpha\zeta$ and $\alpha\zeta^2$ are distinct from $\alpha$ and are not elements of $\QQ(\alpha)\subseteq\RR$. So $f$ has a root in $\QQ(\alpha)$ but does not split into linear factors over $\QQ(\alpha)$, which is precisely the failure of normality.
:::

:::

:::
:::
