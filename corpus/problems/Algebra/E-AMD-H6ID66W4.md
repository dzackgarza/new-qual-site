---
schema: qual/card@1
id: E-AMD-H6ID66W4
kind: problem
title: $\Frac(R[t])=\Frac(R)(t)$
classification:
  areas:
  - algebra
  topics:
  - Localization
  - Polynomials
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Rewritten as a Lamport structured proof. What was checked: the statement (an
    equality of fraction fields, no repair needed), and the existing prose against a
    fresh re-derivation: R[t] embeds in K[t], so Frac(R[t]) embeds in K(t); and for
    P/Q in K(t) the product d of the denominators of all coefficients of P and Q is a
    nonzero element of the domain R clearing both, giving dP,dQ in R[t] with dQ
    nonzero, so P/Q = dP/dQ lies in Frac(R[t]). Correct. The prose's "choose d clearing
    all denominators" is now justified — d is the product of the (finitely many,
    nonzero) coefficient denominators, nonzero because R is a domain, and it clears Q
    without killing it. No source solution is retained for this card, so no source
    comparison was made. What was not checked: any printed source.
---

::: {.exercise}
Show that $\Frac(R[t]) \cong \Frac(R)(t)$ for any integral domain $R$.
:::

::: {.solution}
Let $R$ be an integral domain, $K=\Frac(R)$ its fraction field, and $F=\Frac(R[t])$ the fraction field of the polynomial ring; $\Frac(R)(t)$ means $K(t)=\Frac(K[t])$.

::: pf

::: {.pf-step #inclusion}
$R[t]\subseteq K[t]$, hence $F\subseteq K(t)$.

::: pf-proof
$R\subseteq K$, so a polynomial with coefficients in $R$ is a polynomial with coefficients in $K$; this inclusion of domains induces an inclusion of their fraction fields, by mapping a fraction $p/q$ of elements of $R[t]$ to the same fraction viewed in $K(t)$. The two expressions agree because the identification of $R[t]$ with its image in $K[t]$ is an injective ring homomorphism extending $R\hookrightarrow K$.
:::

:::

::: {.pf-step #clear}
Every element of $K(t)$ is a quotient $dP/dQ$ with $P,Q\in K[t]$, $Q\neq0$, and $d\in R$ nonzero such that $dP,dQ\in R[t]$ and $dQ\neq0$.

::: pf-proof
Let $x=P/Q$ with $P,Q\in K[t]$, $Q\neq0$. Write the coefficients as fractions, $P=\sum_i(a_i/b_i)t^i$ and $Q=\sum_j(c_j/e_j)t^j$ with $a_i,b_i,c_j,e_j\in R$ and all denominators nonzero, which is possible because each coefficient of $P$ or $Q$ is a fraction of elements of $R$. The product $d$ of all the $b_i$ and all the $e_j$ is a nonzero element of $R$, since $R$ is an integral domain and each factor is nonzero. Multiplying every coefficient of $P$ and of $Q$ by $d$ produces polynomials $dP$ and $dQ$ with coefficients in $R$, so $dP,dQ\in R[t]$; and $dQ\neq0$ because $Q\neq0$, $d\neq0$ and $R[t]$ is a domain.
:::

:::

::: {.pf-step #reverse}
$K(t)\subseteq F$.

::: pf-proof
Let $x\in K(t)$. By step [](#clear){.pf-ref} write $x=dP/dQ$ with $dP,dQ\in R[t]$ and $dQ\neq0$. Then $dP$ and $dQ$ are elements of the domain $R[t]$ with nonzero denominator, so their quotient lies in $F=\Frac(R[t])$. Since $dP/dQ=P/Q=x$, we get $x\in F$.
:::

:::

::: {.pf-step}
$\Frac(R[t])=\Frac(R)(t)$ for every integral domain $R$.

::: pf-proof
Steps [](#inclusion){.pf-ref} and [](#reverse){.pf-ref} give the two inclusions of subfields of $K(t)$, hence equality.
:::

:::

:::
:::
