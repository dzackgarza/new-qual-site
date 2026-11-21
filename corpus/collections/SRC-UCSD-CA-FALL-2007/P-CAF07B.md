---
schema: qual/card@1
id: P-CAF07B
kind: problem
title: "Schwarz lemma applications: modulus bound and lower bound near a zero"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Zeros of Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: the chain-rule computation h'(0) = phi_alpha'(alpha) f'(0) = 0 with
    phi_alpha'(alpha) = (1-|alpha|^2)^{-1}, and the reason the zero of h has order at least two;
    the explicit inverse phi_{-alpha} showing phi_alpha is an automorphism of the disk; and the
    boundary case |alpha| = 1, where the maximum modulus principle forces f constant, with the
    resulting inequality checked. Not claimed: a retained solution set; the provenance names
    the examination paper.
---

::: {.problem}
Let $f(z)$ be analytic in $\DD$ and assume $\abs{f(z)} \leq 1$ for all $z \in \DD$.

(a) Suppose that $f(z)$ has a zero of order $m$ at $z = 0$.
Show that $\abs{f(z)} \leq \abs{z}^m$.

(b) Suppose that $f(0) = \alpha$ and $f'(0) = 0$.
Show that, for $\abs{z} \leq \sqrt{\abs{\alpha}}$, $$\abs{f(z)} \geq \frac{\abs{\alpha} - \abs{z}^2}{1 + \abs{\alpha}\abs{z}^2}.$$
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Fall 2007 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose: part (a) is the Schwarz lemma in the form needed here, and part (b) is the Schwarz–Pick estimate applied to $\phi_\alpha\circ f$.

Throughout $f$ is analytic on $\DD$ with $\abs{f(z)}\le1$ there.

::: pf

::: {.pf-step #part-a}
If $f$ has a zero of order $m$ at $0$, then $\abs{f(z)}\le\abs z^m$ on $\DD$.

::: pf-proof
Write $f(z)=z^mg(z)$ with $g$ analytic on $\DD$ — possible because the zero has order exactly $m$. For $0<r<1$ and $\abs z=r$ one has $\abs{g(z)}=\abs{f(z)}/r^m\le r^{-m}$; by the maximum modulus principle the same bound holds on $\abs z\le r$. Fixing $z\in\DD$ and letting $r\uparrow1$ gives $\abs{g(z)}\le1$, whence $\abs{f(z)}=\abs z^m\abs{g(z)}\le\abs z^m$.

:::

:::

::: {.pf-step #boundary-case}
If $\abs\alpha=1$ the inequality of (b) holds.

::: pf-proof
$f$ attains the maximum of $\abs f$, namely $1$, at the interior point $0$, so the maximum modulus principle makes $f$ constant equal to $\alpha$. Then $\abs{f(z)}=1\ge(\abs\alpha-\abs z^2)/(1+\abs\alpha\abs z^2)$ because the numerator is at most $1$ and the denominator is at least $1$.

:::

:::

::: {.pf-step #compose}
For $\abs\alpha<1$ the function $h=\phi_\alpha\circ f$ maps $\DD$ into $\DD$ with $h(0)=h'(0)=0$, where $\phi_\alpha(w)=(w-\alpha)/(1-\overline\alpha w)$.

::: pf-proof
$\phi_\alpha$ is a holomorphic automorphism of $\DD$ with inverse $\phi_{-\alpha}$ (for $\abs\alpha<1$), so $h$ maps $\DD$ into $\DD$. $h(0)=\phi_\alpha(\alpha)=0$, and by the chain rule $h'(0)=\phi_\alpha'(\alpha)f'(0)=0$ since $\phi_\alpha'(\alpha)=(1-\abs\alpha^2)^{-1}\ne0$ and $f'(0)=0$.

:::

:::

::: {.pf-step #apply-a}
$\abs{\dfrac{f(z)-\alpha}{1-\overline\alpha f(z)}}\le\abs z^2$.

::: pf-proof
$h$ is analytic with $h(0)=h'(0)=0$, so its zero at $0$ has order at least $2$; step [](#part-a){.pf-ref} with $m=2$ gives $\abs{h(z)}\le\abs z^2$, which is the displayed inequality because $h(z)=\phi_\alpha(f(z))$.

:::

:::

::: {.pf-step #part-b}
For $\abs z\le\sqrt{\abs\alpha}$, $\abs{f(z)}\ge\dfrac{\abs\alpha-\abs z^2}{1+\abs\alpha\abs z^2}$.

::: pf-proof
Put $\rho=\abs z^2$. By step [](#apply-a){.pf-ref}, $\abs{f(z)-\alpha}\le\rho\abs{1-\overline\alpha f(z)}\le\rho(1+\abs\alpha\abs{f(z)})$. The reverse triangle inequality gives $\abs\alpha-\abs{f(z)}\le\abs{f(z)-\alpha}$. Combining, $\abs\alpha-\abs{f(z)}\le\rho+\rho\abs\alpha\abs{f(z)}$, that is $\abs{f(z)}(1+\abs\alpha\rho)\ge\abs\alpha-\rho$. If $\abs z\le\sqrt{\abs\alpha}$ then $\rho\le\abs\alpha$, the right side is nonnegative, and dividing by the positive $1+\abs\alpha\rho$ gives the claim.

:::

:::

::: {.pf-step #conclusion}
Part (a) holds under the stated hypothesis, and part (b) holds for every such $f$ with $f(0)=\alpha$, $f'(0)=0$.

::: pf-proof
Step [](#part-a){.pf-ref} is (a); steps [](#boundary-case){.pf-ref} and [](#part-b){.pf-ref} cover (b) in the cases $\abs\alpha=1$ and $\abs\alpha<1$, which exhaust $\abs\alpha\le1$.

:::

:::

:::
:::
