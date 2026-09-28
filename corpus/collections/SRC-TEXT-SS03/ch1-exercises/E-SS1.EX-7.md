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
7. The family of mappings introduced here plays an important role in complex analysis.
   These mappings, sometimes called Blaschke factors, will reappear in various applications in later chapters.

(a) Let $z , w$ be two complex numbers such that $\overline { { z } } w \ne 1$ . Prove that

$$
\left| \frac {w - z}{1 - \overline {{w}} z} \right| <   1 \quad \text { if } | z | <   1 \text { and } | w | <   1,
$$

and also that

$$
\left| \frac {w - z}{1 - \overline {{w}} z} \right| = 1 \quad \text { if } | z | = 1 \text { or } | w | = 1.
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

(i) F maps the unit disc to itself (that is, $F : \mathbb { D } \to \mathbb { D } )$ , and is holomorphic.

(ii) F interchanges 0 and $w ,$ namely $F ( 0 ) = w$ and $F ( w ) = 0$

(iii) $| F ( z ) | = 1 { \mathrm { ~ i f ~ } } | z | = 1 .$

(iv) $F : \mathbb { D }  \mathbb { D }$ is bijective.
[Hint: Calculate $F \circ F . ]$
:::

::: {.solution}
<1>1. (a) If $\abs z<1$ and $\abs w<1$, then $\abs{\frac{w - z}{1 - \bar w z}} < 1$; if $\abs z=1$ or $\abs w=1$, then $\abs{\frac{w - z}{1 - \bar w z}} = 1$.

<2>1. It suffices to treat $z = r\ge0$ real.

::: {.proof}
Replacing $(z,w)$ by $(e^{i\theta}z,e^{i\theta}w)$ multiplies $w-z$ by $e^{i\theta}$ and leaves $\bar wz$ unchanged, so it preserves $\abs{\frac{w - z}{1 - \bar w z}}$ and the hypotheses. Choose $\theta$ with $e^{i\theta}z=\abs z$.
:::

<2>2. For $r\ge0$, $\abs{1-\bar w r}^2-\abs{w-r}^2=(1 - r^2)(1 - |w|^2)$.

::: {.proof}
Expanding, $\abs{w-r}^2=(r - w)(r - \bar w)=r^2 - r(w + \bar w) + |w|^2$ and $\abs{1-\bar wr}^2=(1 - rw)(1 - r\bar w)=1 - r(w + \bar w) + r^2|w|^2$; subtract.
:::

<2>3. Q.E.D.

::: {.proof}
By step <2>1 take $z=r=\abs z$. If $r<1$ and $\abs w<1$, the right side of step <2>2 is positive, so $\abs{w-r}<\abs{1-\bar wr}$. If $r=1$ or $\abs w=1$, it is zero, so $\abs{w-r}=\abs{1-\bar wr}$, and this common value is nonzero because $\bar wz\ne1$.
:::

<1>2. (b) For fixed $w\in\mathbb D$, the map $F(z) = \frac{w - z}{1 - \bar w z}$ satisfies (i)--(iv).

<2>1. (i) $F$ is holomorphic on $\mathbb D$ and $F(\mathbb D)\subseteq\mathbb D$.

::: {.proof}
For $\abs z<1$, $\abs{\bar wz}<1$, so the denominator does not vanish and $F$ is a rational function without poles in $\mathbb D$. Step <1>1 gives $\abs{F(z)}<1$.
:::

<2>2. (ii) $F(0) = w$ and $F(w) = 0$; (iii) $\abs{F(z)} = 1$ if $\abs z = 1$.

::: {.proof}
Substitution gives (ii), and step <1>1 gives (iii).
:::

<2>3. (iv) $F\circ F = \operatorname{id}_{\mathbb D}$, so $F\colon\mathbb D\to\mathbb D$ is bijective.

::: {.proof}
For $z\in\mathbb D$,
$$F(F(z)) = \frac{w - \frac{w - z}{1 - \bar w z}}{1 - \bar w \frac{w - z}{1 - \bar w z}} = \frac{w(1 - \bar w z) - (w - z)}{(1 - \bar w z) - \bar w(w - z)} = \frac{z(1 - |w|^2)}{1 - |w|^2} = z.$$
By step <2>1, $F$ maps $\mathbb D$ into itself, so $F$ is its own inverse on $\mathbb D$.
:::
:::
