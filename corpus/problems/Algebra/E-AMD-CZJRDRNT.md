---
schema: qual/card@1
id: E-AMD-CZJRDRNT
kind: problem
title: $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$ are isomorphic but not equal
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Splitting Fields
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
    Rewritten as a Lamport structured proof. What was checked: the statement (two
    claims — isomorphic, not identical — both proved, no repair needed; "not
    identical" is only meaningful inside a fixed field, which the lead-in now
    states by working in C), and the existing prose solution against a fresh
    re-derivation: x^3 - 2 is Eisenstein at 2, so irreducible; alpha and beta =
    zeta_3 alpha are both roots, and evaluation at a root of an irreducible
    polynomial gives Q(x)/(x^3 - 2) = Q(root), so the two fields are each
    isomorphic to that quotient and hence to one another; Q(alpha) consists of real
    numbers while beta has imaginary part alpha*sqrt(3)/2, so beta is not in
    Q(alpha) although it lies in Q(beta). Correct. The prose's isomorphism step
    cited the quotient without justification; the proof now gives the evaluation
    map's well-definedness, injectivity and surjectivity. No source solution is
    retained for this card, so no source comparison was made. What was not checked:
    any printed source.
---

::: {.exercise}
Show that $\QQ(2^{1/3})$ and $\QQ(\zeta_3 2^{1/3})$ are isomorphic fields, but not identical.
:::

::: {.solution}
Work inside $\CC$: let $\alpha=\sqrt[3]{2}\in\RR$ be the real cube root of $2$ and let $\beta=\zeta_3\alpha$, where $\zeta_3$ is a primitive cube root of unity.

::: pf

::: {.pf-step #irreducible}
$x^3-2$ is irreducible over $\QQ$, and both $\alpha$ and $\beta$ are roots of it.

::: pf-proof
$x^3-2$ is Eisenstein at the prime $2$: the leading coefficient $1$ is not divisible by $2$, the other coefficients $0,0,-2$ are divisible by $2$, and the constant term $-2$ is not divisible by $4$. Hence it is irreducible. And $\alpha^3=2$, while $\beta^3=\zeta_3^3\alpha^3=2$ since $\zeta_3^3=1$; so both are roots.
:::

:::

::: {.pf-step #isomorphic}
$\QQ(\alpha)\cong\QQ[x]/(x^3-2)\cong\QQ(\beta)$, by isomorphisms carrying $\alpha$ and $\beta$ to the class of $x$.

::: pf-proof
For an irreducible polynomial $f$ over a field $F$ and a root $\gamma$ of $f$ in an extension, evaluation at $\gamma$ induces an isomorphism $F[x]/(f)\to F(\gamma)$; it is well defined because $(f)\subseteq\ker$, injective because $(f)$ is maximal and the kernel is proper (as $1\mapsto1\neq0$), and surjective because its image is a subfield of $F(\gamma)$ containing $F$ and $\gamma$, hence all of $F(\gamma)$. Applying this to $F=\QQ$, $f=x^3-2$, and $\gamma=\alpha$ or $\gamma=\beta$ — both roots, by step [](#irreducible){.pf-ref} — gives the two isomorphisms, and composing one with the inverse of the other gives a $\QQ$-isomorphism $\QQ(\alpha)\to\QQ(\beta)$ sending $\alpha$ to $\beta$.
:::

:::

::: {.pf-step #real}
$\QQ(\alpha)\subseteq\RR$, while $\beta\notin\RR$.

::: pf-proof
$\alpha\in\RR$ and $\QQ\subseteq\RR$, and $\RR$ is a field, so every element of $\QQ(\alpha)$ — a quotient of polynomials in $\alpha$ with rational coefficients, with nonzero denominator — is real. For $\beta$, write $\zeta_3=-\frac12+\frac{\sqrt3}{2}i$; then $\beta=\alpha\zeta_3$ has imaginary part $\alpha\frac{\sqrt3}{2}$, which is nonzero because $\alpha>0$. So $\beta$ is not real.
:::

:::

::: {.pf-step}
$\QQ(\sqrt[3]{2})$ and $\QQ(\zeta_3\sqrt[3]{2})$ are isomorphic but not identical subfields of $\CC$.

::: pf-proof
They are isomorphic by step [](#isomorphic){.pf-ref}. They are not equal: $\beta\in\QQ(\beta)$, but $\beta\notin\QQ(\alpha)$ by step [](#real){.pf-ref}, since $\QQ(\alpha)$ consists of real numbers and $\beta$ is not real. Two fields, one containing an element the other does not, are different, so $\QQ(\alpha)\neq\QQ(\beta)$ inside $\CC$.
:::

:::

:::
:::
