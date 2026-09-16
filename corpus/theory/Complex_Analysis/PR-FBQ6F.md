---
schema: qual/card@1
id: PR-FBQ6F
kind: proposition
title: Functional equation for $\Gamma$
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
relations: []
review: draft
---

::: {.proposition}
For $s\in\CC$ with $\Re(s)>0$, the [[D-Q3MYK|Gamma function]] satisfies
$$
\Gamma(s+1) = s\,\Gamma(s).
$$
Consequently $\Gamma(n+1)=n!$ for every integer $n\ge0$.
:::

::: {.proof}
For $0<\varepsilon<1$, integration by parts on $[\varepsilon,1/\varepsilon]$ gives
$$
\int_\varepsilon^{1/\varepsilon}\frac{d}{dt}\qty{e^{-t}t^s}\dt=-\int_\varepsilon^{1/\varepsilon}e^{-t}t^s\dt+s\int_\varepsilon^{1/\varepsilon}e^{-t}t^{s-1}\dt.
$$
The left side equals $e^{-1/\varepsilon}\varepsilon^{-s}-e^{-\varepsilon}\varepsilon^s$, which tends to $0$ as $\varepsilon\to0$ because $\abs{\varepsilon^s}=\varepsilon^{\Re s}\to0$ and $e^{-1/\varepsilon}$ decays faster than any power of $\varepsilon$.
The right side tends to $-\Gamma(s+1)+s\Gamma(s)$, so $\Gamma(s+1)=s\Gamma(s)$.
Since $\Gamma(1)=\int_0^\infty e^{-t}\dt=1$, induction on $n$ gives $\Gamma(n+1)=n\Gamma(n)=n!$.
:::
