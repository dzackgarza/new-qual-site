---
schema: qual/card@1
id: E-SS1.EX-7
kind: problem
title: Blaschke factors map the unit disc bijectively onto itself
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
The family of mappings introduced here plays an important role in complex analysis.
   These mappings, sometimes called Blaschke factors, will reappear in various applications in later chapters.

(a) Let $z , w$ be two complex numbers such that $\overline { { z } } w \ne 1$ . Prove that

$$
\abs{ \frac {w - z}{1 - \overline {{w}} z} } <   1 \quad \text { if } \abs{ z } <   1 \text { and } \abs{ w } <   1,
$$

and also that

$$
\abs{ \frac {w - z}{1 - \overline {{w}} z} } = 1 \quad \text { if } \abs{ z } = 1 \text { or } \abs{ w } = 1.
$$

[Hint: Why can one assume that z is real?
It then sufices to prove that

$$
(r - w) (r - \overline {{w}}) \leq (1 - r w) (1 - r \overline {{w}})
$$

with equality for appropriate r and $\abs w$.]

(b) Prove that for a fixed w in the unit disc D, the mapping

$$
F: z \mapsto \frac {w - z}{1 - \overline {{w}} z}
$$

satisfies the following conditions:

(i) F maps the unit disc to itself (that is, $F : \DD \to \DD )$ , and is holomorphic.

(ii) F interchanges 0 and $w ,$ namely $F ( 0 ) = w$ and $F ( w ) = 0$

(iii) $\abs{ F ( z ) } = 1 { \mathrm { ~ i f ~ } } \abs{ z } = 1 .$

(iv) $F : \DD \to \DD$ is bijective.
[Hint: Calculate $F \circ F . ]$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

(a) If $\abs z<1$ and $\abs w<1$, then $\abs{\frac{w - z}{1 - \bar w z}} < 1$; if $\abs z=1$ or $\abs w=1$, then $\abs{\frac{w - z}{1 - \bar w z}} = 1$.

::: pf-proof

::: {.pf-step #s1-1}

It suffices to treat $z = r\ge0$ real.

::: pf-proof

Replacing $(z,w)$ by $(e^{i\theta}z,e^{i\theta}w)$ multiplies $w-z$ by $e^{i\theta}$ and leaves $\bar wz$ unchanged, so it preserves $\abs{\frac{w - z}{1 - \bar w z}}$ and the hypotheses. Choose $\theta$ with $e^{i\theta}z=\abs z$.

:::

:::

::: {.pf-step #s1-2}

For $r\ge0$, $\abs{1-\bar w r}^2-\abs{w-r}^2=(1 - r^2)(1 - \abs{w}^2)$.

::: pf-proof

Expanding, $\abs{w-r}^2=(r - w)(r - \bar w)=r^2 - r(w + \bar w) + \abs{w}^2$ and $\abs{1-\bar wr}^2=(1 - rw)(1 - r\bar w)=1 - r(w + \bar w) + r^2\abs{w}^2$; subtract.

:::

:::

::: pf-qed

By step [](#s1-1){.pf-ref} take $z=r=\abs z$. If $r<1$ and $\abs w<1$, the right side of step [](#s1-2){.pf-ref} is positive, so $\abs{w-r}<\abs{1-\bar wr}$. If $r=1$ or $\abs w=1$, it is zero, so $\abs{w-r}=\abs{1-\bar wr}$, and this common value is nonzero because $\bar wz\ne1$.

:::

:::

:::

::: pf-step

(b) For fixed $w\in\DD$, the map $F(z) = \frac{w - z}{1 - \bar w z}$ satisfies (i)--(iv).

::: pf-proof

::: {.pf-step #s2-1}

(i) $F$ is holomorphic on $\DD$ and $F(\DD)\subseteq\DD$.

::: pf-proof

For $\abs z<1$, $\abs{\bar wz}<1$, so the denominator does not vanish and $F$ is a rational function without poles in $\DD$. Step [](#s1){.pf-ref} gives $\abs{F(z)}<1$.

:::

:::

::: pf-step

(ii) $F(0) = w$ and $F(w) = 0$; (iii) $\abs{F(z)} = 1$ if $\abs z = 1$.

::: pf-proof

Substitution gives (ii), and step [](#s1){.pf-ref} gives (iii).

:::

:::

::: pf-step

(iv) $F\circ F = \operatorname{id}_{\DD}$, so $F\colon\DD\to\DD$ is bijective.

::: pf-proof

For $z\in\DD$,
$$F(F(z)) = \frac{w - \frac{w - z}{1 - \bar w z}}{1 - \bar w \frac{w - z}{1 - \bar w z}} = \frac{w(1 - \bar w z) - (w - z)}{(1 - \bar w z) - \bar w(w - z)} = \frac{z(1 - \abs{w}^2)}{1 - \abs{w}^2} = z.$$
By step [](#s2-1){.pf-ref}, $F$ maps $\DD$ into itself, so $F$ is its own inverse on $\DD$.

:::

:::

:::

:::

:::

:::
