---
schema: qual/card@1
id: P-BKF07-2A
kind: problem
title: Entire functions satisfying harmonic-oscillator and double-angle identities
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Fall 2007 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained reduction to f''=-f and the coefficient
    constraints imposed by the double-angle identity.
---

::: {.problem}
Let \(f,g\) be entire functions satisfying, for every \(z\in\mathbb C\),
\[
f'(z)=g(z),\qquad g'(z)=-f(z),\qquad f(2z)=2f(z)g(z).
\]
Find all possibilities for \(f\).
:::

::: {.solution}

::: pf

::: {.pf-step #f-g-general-solution}
Every solution of the first two identities has the form
$$
f(z)=ae^{iz}+be^{-iz},
\qquad
g(z)=aie^{iz}-bie^{-iz}
$$
for some $a,b\in\CC$.

::: pf-proof
Differentiating $f'=g$ and using $g'=-f$ gives
$$
f''=-f.
$$
The entire solutions of this constant-coefficient differential
equation are
$$
f(z)=ae^{iz}+be^{-iz}.
$$
Since $g=f'$, the displayed formula for $g$ follows.
:::

:::

::: {.pf-step #double-angle-equivalent}
The identity
$$
f(2z)=2f(z)g(z)
$$
is equivalent to
$$
(a-2ia^2)e^{2iz}+(b+2ib^2)e^{-2iz}=0
$$
for every $z\in\CC$.

::: pf-proof
Using step [](#f-g-general-solution){.pf-ref},
$$
f(2z)=ae^{2iz}+be^{-2iz},
$$
while
$$
\begin{aligned}
2f(z)g(z)
&=
2(ae^{iz}+be^{-iz})(aie^{iz}-bie^{-iz})
\\
&=
2ia^2e^{2iz}-2ib^2e^{-2iz},
\end{aligned}
$$
because the two mixed terms cancel. Moving the right-hand side to
the left gives the claim.
:::

:::

::: {.pf-step #coefficient-conditions}
The identity in step [](#double-angle-equivalent){.pf-ref} holds for all $z$ if and only if
$$
a-2ia^2=0
\qquad\text{and}\qquad
b+2ib^2=0.
$$

::: pf-proof
Multiplying the identity in step [](#double-angle-equivalent){.pf-ref} by $e^{2iz}$ gives
$$
(a-2ia^2)e^{4iz}+(b+2ib^2)=0
$$
for every $z$. Since $e^{4iz}$ is nonconstant, an identity of the
form $Ce^{4iz}+D=0$ for all $z$ forces $C=D=0$. The converse is
immediate.
:::

:::

::: {.pf-step #possible-coefficients}
The possible coefficients are
$$
a\in\left\{0,-\frac{i}{2}\right\},
\qquad
b\in\left\{0,\frac{i}{2}\right\}.
$$

::: pf-proof
The equations from step [](#coefficient-conditions){.pf-ref} factor as
$$
a(1-2ia)=0,
\qquad
b(1+2ib)=0.
$$
Solving them gives exactly the displayed possibilities.
:::

:::

::: {.pf-step #f-list}
Hence the complete list of possibilities for $f$ is
$$
\boxed{
0,\qquad
-\frac{i}{2}e^{iz},\qquad
\frac{i}{2}e^{-iz},\qquad
\sin z
}.
$$

::: pf-proof
Substituting the four pairs $(a,b)$ from step [](#possible-coefficients){.pf-ref} into the formula
for $f$ in step [](#f-g-general-solution){.pf-ref} gives the first three functions and
$$
-\frac{i}{2}e^{iz}+\frac{i}{2}e^{-iz}
=
\frac{e^{iz}-e^{-iz}}{2i}
=
\sin z.
$$
Conversely, step [](#coefficient-conditions){.pf-ref} shows that every such pair satisfies the
double-angle identity, while step [](#f-g-general-solution){.pf-ref} already gives the first two
differential identities.
:::

:::

::: pf-qed
Step [](#f-list){.pf-ref} gives all and only the possibilities.
:::

:::

:::
