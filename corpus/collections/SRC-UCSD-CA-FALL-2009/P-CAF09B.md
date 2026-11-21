---
schema: qual/card@1
id: P-CAF09B
kind: problem
title: "Removable singularity for bounded analytic functions on punctured neighborhoods"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: the bound |z f(z)| -> 0 used for differentiability of g at 0, hence g
    holomorphic on the whole disk; the definition of h at 0 as g''(0)/2 together with the
    reason dividing a power series by z^2 keeps it a power series (so no removable-singularity
    argument is being assumed); and the identification of the extension with h on all of DD.
    Not claimed: a retained solution set; the provenance names the examination paper.
---

::: {.problem}
Suppose that $f(z)$ is defined and analytic in the punctured neighborhood of zero, $N = \{z \mid 0 < \abs{z} < 1\}$, and that for all $z$ in $N$, $\abs{f(z)} < 1$.
Provide a proof of the standard result that $f(z)$ has a removable singularity at $z = 0$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Fall 2009 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose; it is a proof of Riemann's removability theorem in the bounded case, as the problem asks.

Throughout $N=\theset{z\mid 0<\abs z<1}$ and $f$ is analytic on $N$ with $\abs{f(z)}<1$ there.

::: pf

::: {.pf-step #auxiliary}
The function $g$ defined by $g(z)=z^2f(z)$ for $z\in N$ and $g(0)=0$ is holomorphic at $0$, with $g'(0)=0$.

::: pf-proof
On $N$ the function $g$ is a product of holomorphic functions, hence holomorphic. At $0$,
$$
\frac{g(z)-g(0)}{z-0}=\frac{z^2f(z)}{z}=zf(z),
$$
and $\abs{zf(z)}\le\abs z\to0$ as $z\to0$ because $\abs{f}<1$. So the difference quotient has limit $0$, which means $g$ is complex differentiable at $0$ with $g'(0)=0$; being holomorphic on $N$ and differentiable at $0$, $g$ is holomorphic on $\DD$.

:::

:::

::: {.pf-step #taylor}
There is $h$ holomorphic on $\DD$ with $g(z)=z^2h(z)$ and $h=f$ on $N$.

::: pf-proof
$g$ is holomorphic on $\DD$ with $g(0)=0$ and $g'(0)=0$, so its Taylor series at $0$ has no constant or linear term: defining $h(z)=g(z)/z^2$ for $z\ne0$ and $h(0)=g''(0)/2$ gives a holomorphic function on $\DD$ with $g=z^2h$, because the power series of $g$ divided by $z^2$ is again a power series. For $z\in N$, $h(z)=g(z)/z^2=f(z)$.

:::

:::

::: {.pf-step #extension}
Setting $\widetilde f(0)=h(0)$ and $\widetilde f(z)=f(z)$ for $z\in N$ gives a holomorphic function on $\DD$ extending $f$.

::: pf-proof
$\widetilde f$ agrees with the holomorphic function $h$ at $0$ and with $f$ on $N$; on $N$ itself $h=f$ by step [](#taylor){.pf-ref}, so $\widetilde f$ equals the holomorphic $h$ on all of $\DD$. It therefore extends $f$ holomorphically across $0$.

:::

:::

::: {.pf-step #conclusion}
$f$ has a removable singularity at $0$.

::: pf-proof
By step [](#extension){.pf-ref} $f$ extends to a function holomorphic on the whole disk $\DD$, which is exactly the assertion that $0$ is a removable singularity of $f$.

:::

:::

:::
:::
