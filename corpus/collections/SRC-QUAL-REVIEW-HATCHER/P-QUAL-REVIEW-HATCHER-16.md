---
schema: qual/card@1
id: P-QUAL-REVIEW-HATCHER-16
kind: problem
title: Degree of a normalized polynomial counts roots in the unit disk
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against practice problem 16 in assets/attachments/Qual_Review_Selection_of_Hatcher_Problems_-_Unknown_extracted.md.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The deterministic extraction writes the initial inclusion as “S^1 ∈ C”; it is normalized here to the evident inclusion arrow.
---

::: {.problem}
Let $f\in\mathbb C[z]$ and assume that $f$ has no roots on the unit circle.
Consider
\[
S^1\hookrightarrow\mathbb C\xrightarrow{f}\mathbb C\setminus\{0\}\xrightarrow{\pi}S^1,
\]
where $\pi$ is the norm map.
Prove that the degree of this composition equals the number of roots of $f$ inside the unit circle.
:::

::: {.solution}
Write the polynomial as
\[
\boxed{
f(z)=c\prod_{j=1}^{d}(z-a_j)},
\]
where the roots \(a_j\) are listed with multiplicity and
\[
c\in\mathbb C^\times.
\]

Because \(f\) has no roots on \(S^1\),
\[
|a_j|\ne1
\]
for every \(j\).

Let
\[
F:S^1\to S^1
\]
be the normalized map
\[
F(z)=\frac{f(z)}{|f(z)|}.
\]

<1>1. For \(z\in S^1\),
\[
\boxed{
F(z)
=
\frac{c}{|c|}
\prod_{j=1}^{d}
\frac{z-a_j}{|z-a_j|}}.
\]

::: {.proof}
Using multiplicativity of the complex modulus,
\[
|f(z)|
=
|c|\prod_{j=1}^{d}|z-a_j|.
\]
Divide the factorization of \(f\) by this expression.
:::

For each root \(a\) with \(|a|\ne1\), define
\[
g_a:S^1\to S^1,
\qquad
g_a(z)=\frac{z-a}{|z-a|}.
\]

## Roots inside the unit disk

Assume
\[
|a|<1.
\]

<1>2. The homotopy
\[
H:S^1\times[0,1]\to\mathbb C^\times,
\qquad
H(z,t)=z-ta
\]
never takes the value \(0\).

::: {.proof}
If
\[
z-ta=0,
\]
then
\[
|z|=t|a|\le|a|<1,
\]
contradicting
\[
|z|=1.
\]
:::

<1>3. After normalization,
\[
\widetilde H(z,t)
=
\frac{z-ta}{|z-ta|}
\]
is a homotopy in \(S^1\) from \(g_a\) to the identity map \(z\mapsto z\).

::: {.proof}
At \(t=1\),
\[
\widetilde H(z,1)=g_a(z).
\]
At \(t=0\),
\[
\widetilde H(z,0)=\frac z{|z|}=z
\]
because \(z\in S^1\). Step <1>2 guarantees the normalization is defined throughout.
:::

<1>4. Therefore
\[
\boxed{\deg g_a=1}
\]
when
\[
|a|<1.
\]

::: {.proof}
Degree is invariant under homotopy, and the identity map of \(S^1\) has degree \(1\).
:::

## Roots outside the unit disk

Assume
\[
|a|>1.
\]

<1>5. The homotopy
\[
K:S^1\times[0,1]\to\mathbb C^\times,
\qquad
K(z,t)=tz-a
\]
never takes the value \(0\).

::: {.proof}
If
\[
tz-a=0,
\]
then
\[
|a|=t|z|\le1,
\]
contradicting
\[
|a|>1.
\]
:::

<1>6. After normalization,
\[
\widetilde K(z,t)
=
\frac{tz-a}{|tz-a|}
\]
is a homotopy from \(g_a\) to the constant map
\[
z\longmapsto -\frac a{|a|}.
\]

::: {.proof}
At \(t=1\),
\[
\widetilde K(z,1)=g_a(z).
\]
At \(t=0\),
\[
\widetilde K(z,0)
=
\frac{-a}{|a|},
\]
independent of \(z\). Step <1>5 guarantees the denominator is never zero.
:::

<1>7. Therefore
\[
\boxed{\deg g_a=0}
\]
when
\[
|a|>1.
\]

::: {.proof}
A constant map \(S^1\to S^1\) has degree \(0\), and degree is homotopy invariant.
:::

## Additivity of degree

<1>8. If
\[
u,v:S^1\to S^1,
\]
then for the pointwise product
\[
(uv)(z)=u(z)v(z),
\]
one has
\[
\boxed{
\deg(uv)=\deg u+\deg v}.
\]

::: {.proof}
On
\[
H_1(S^1;\mathbb Z)\cong\mathbb Z,
\]
the multiplication map
\[
m:S^1\times S^1\to S^1,
\qquad
m(\zeta,\eta)=\zeta\eta,
\]
induces
\[
m_*(r,s)=r+s.
\]
The pointwise product is
\[
uv=m\circ(u,v),
\]
so its induced map on \(H_1\) multiplies by
\[
\deg u+\deg v.
\]
:::

<1>9. The constant factor
\[
z\longmapsto\frac c{|c|}
\]
has degree \(0\).

::: {.proof}
Every constant map has degree \(0\).
:::

<1>10. Hence
\[
\deg F
=
\sum_{j=1}^{d}\deg g_{a_j}.
\]

::: {.proof}
Apply step <1>8 repeatedly to the product decomposition in step <1>1, and use step <1>9 for the leading constant.
:::

<1>11. Each root with
\[
|a_j|<1
\]
contributes \(1\), and each root with
\[
|a_j|>1
\]
contributes \(0\).

::: {.proof}
Use steps <1>4 and <1>7.
:::

<1>12. Therefore
\[
\boxed{
\deg F
=
\#\{j:|a_j|<1\}},
\]
where roots are counted with multiplicity.

::: {.proof}
The roots \(a_j\) were listed with multiplicity in the factorization of \(f\), and step <1>10 sums exactly the contributions from step <1>11.
:::

<1>13. Thus the degree of
\[
S^1\hookrightarrow\mathbb C
\xrightarrow{f}
\mathbb C\setminus\{0\}
\xrightarrow{\pi}
S^1
\]
equals the number of roots of \(f\) inside the unit circle, counted with multiplicity.

::: {.proof}
The displayed composite is exactly
\[
z\longmapsto\frac{f(z)}{|f(z)|}=F(z),
\]
whose degree was computed in step <1>12.
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>13 is the required conclusion.
:::
:::
