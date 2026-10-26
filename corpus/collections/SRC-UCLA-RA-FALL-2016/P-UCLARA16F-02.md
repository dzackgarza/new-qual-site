---
schema: qual/card@1
id: P-UCLARA16F-02
kind: problem
title: Singular measures have infinite density almost everywhere
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2016, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $\mu$ be a finite positive Borel measure on $\mathbb R$ that is singular to Lebesgue measure.
Show that
\[
\lim_{r\to0^+}\frac{\mu([x-r,x+r])}{2r}=+\infty
\]
for $\mu$-almost every $x\in\mathbb R$.
:::

Let \(m\) denote Lebesgue measure on \(\mathbb R\), and define the locally finite positive Borel measure
\[
\boxed{
\nu=\mu+m}.
\]

Since \(m\ll\nu\), the Radon--Nikodym theorem gives a measurable function
\[
f=\frac{dm}{d\nu}
\]
with
\[
0\le f\le1
\]
\(\nu\)-almost everywhere and
\[
m(E)=\int_E f\,d\nu
\]
for every Borel set \(E\).

::: pf

::: pf-step

Since \(\mu\perp m\), there exists a Borel set
\[
S\subseteq\mathbb R
\]
such that
\[
\boxed{
m(S)=0,
\qquad
\mu(\mathbb R\setminus S)=0}.
\]


::: pf-proof

This is the definition of mutual singularity of the positive measures \(\mu\) and \(m\).

:::

:::

::: pf-step

One has
\[
\boxed{
f=0}
\]
for \(\nu\)-almost every point of \(S\).


::: pf-proof

Since
\[
m(S)=0,
\]
the Radon--Nikodym representation gives
\[
0
=
m(S)
=
\int_S f\,d\nu.
\]
Because \(f\ge0\), the integral of \(f\) over \(S\) can vanish only if
\[
f=0
\]
\(\nu\)-almost everywhere on \(S\).

:::

:::

::: pf-step

Therefore
\[
\boxed{
f(x)=0}
\]
for \(\mu\)-almost every \(x\in\mathbb R\).


::: pf-proof

By step <1>1, \(\mu\) is concentrated on \(S\). The exceptional subset of \(S\) in step <1>2 is \(\nu\)-null, hence also \(\mu\)-null because
\[
\mu\le\nu.
\]

:::

:::

::: pf-step

By the differentiation theorem for locally finite Borel measures on \(\mathbb R\),
\[
\boxed{
f(x)
=
\lim_{r\to0^+}
\frac{
\int_{[x-r,x+r]} f\,d\nu
}{
\nu([x-r,x+r])
}}
\]
for \(\nu\)-almost every \(x\).


::: pf-proof

This is the Lebesgue differentiation theorem in the measure \(\nu\), applied locally to the function \(f\in L^1_{\mathrm{loc}}(\nu)\).

:::

:::

::: pf-step

The numerator in step <1>4 is
\[
\boxed{
\int_{[x-r,x+r]}f\,d\nu
=
2r}.
\]


::: pf-proof

By the defining Radon--Nikodym identity,
\[
\int_{[x-r,x+r]}f\,d\nu
=
m([x-r,x+r])
=
2r.
\]

:::

:::

::: pf-step

The denominator is
\[
\boxed{
\nu([x-r,x+r])
=
2r+\mu([x-r,x+r])}.
\]


::: pf-proof

Since
\[
\nu=\mu+m,
\]
\[
\nu([x-r,x+r])
=
\mu([x-r,x+r])
+
m([x-r,x+r])
=
\mu([x-r,x+r])+2r.
\]

:::

:::

::: pf-step

Hence, for \(\nu\)-almost every \(x\),
\[
\boxed{
f(x)
=
\lim_{r\to0^+}
\frac{
2r
}{
2r+\mu([x-r,x+r])
}}.
\]


::: pf-proof

Substitute steps <1>5--<1>6 into step <1>4.

:::

:::

::: pf-step

For \(\mu\)-almost every \(x\),
\[
\boxed{
\lim_{r\to0^+}
\frac{
2r
}{
2r+\mu([x-r,x+r])
}
=
0}.
\]


::: pf-proof

The differentiation identity in step <1>7 holds \(\nu\)-almost everywhere, hence \(\mu\)-almost everywhere because \(\mu\le\nu\). At \(\mu\)-almost every such point, step <1>3 gives
\[
f(x)=0.
\]

:::

:::

::: pf-step

The ratio in step <1>8 can be rewritten as
\[
\boxed{
\frac1{1+q_r(x)}}.
\]


::: pf-proof

Divide numerator and denominator by \(2r>0\):
\[
\frac{2r}{2r+\mu([x-r,x+r])}
=
\frac1{
1+\mu([x-r,x+r])/(2r)
}.
\]

:::

:::

::: pf-step

Since
\[
q_r(x)\ge0,
\]
the convergence
\[
\frac1{1+q_r(x)}\to0
\]
is equivalent to
\[
\boxed{
q_r(x)\to+\infty}.
\]


::: pf-proof

For nonnegative numbers \(q\),
\[
\frac1{1+q}\to0
\]
if and only if \(1+q\to+\infty\), equivalently \(q\to+\infty\).

:::

:::

::: pf-step

Therefore, for \(\mu\)-almost every \(x\),
\[
\boxed{
\lim_{r\to0^+}
\frac{
\mu([x-r,x+r])
}{
2r
}
=
+\infty}.
\]


::: pf-proof

Combine steps <1>8--<1>10.

:::

:::

::: pf-qed

Step <1>11 is the required density statement.

:::

:::
