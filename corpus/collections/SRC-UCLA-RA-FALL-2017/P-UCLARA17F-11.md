---
schema: qual/card@1
id: P-UCLARA17F-11
kind: problem
title: Normalized univalent maps of the disk omit a point of modulus at most 1
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f:\DD\to\CC$ be an injective holomorphic function with $f(0)=0$ and $f'(0)=1$. Show that
$$
\inf\{\abs{w}:w\notin f(\DD)\}\le1,
$$
with equality if and only if $f(z)=z$ for all $z\in\DD$.
:::

::: {.solution}

Set
$$
R\coloneqq\inf\{\abs{w}:w\notin f(\DD)\}.
$$

::: pf

::: {.pf-step #s1-1}

The omitted set $\CC\setminus f(\DD)$ is nonempty; moreover, if $R\ge1$, then $\DD\subset f(\DD)$.


::: pf-proof

If $f(\DD)=\CC$, then the inverse map $f^{-1}:\CC\to\DD$ is an entire bounded function. Liouville's theorem would make $f^{-1}$ constant, contradicting injectivity of $f$. Thus the omitted set is nonempty and $R$ is a finite real number.

If some $w\in\DD$ were omitted by $f$, then $\abs{w}<1$, so the definition of $R$ would give
$$
R\le \abs{w}<1,
$$
contrary to $R\ge1$.

:::

:::

::: {.pf-step #s1-2}

If $R\ge1$, then $f(z)=z$ for every $z\in\DD$.


::: pf-proof

By step [](#s1-1){.pf-ref}, the inverse of the injective holomorphic map $f$ is defined on $\DD$. Let
$$
g\coloneqq f^{-1}\restrict_{\DD}:\DD\to\DD.
$$
Since an injective holomorphic function has nonvanishing derivative, its inverse is holomorphic. Moreover,
$$
g(0)=0,
\qquad
g'(0)=\frac1{f'(0)}=1.
$$
Schwarz's lemma, including its equality case, therefore gives $g(z)=z$ for every $z\in\DD$. Thus for every $w\in\DD$,
$$
f^{-1}(w)=w,
$$
and applying $f$ gives $f(w)=w$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
R\le1.
$$


::: pf-proof

If $R>1$, then step [](#s1-2){.pf-ref} gives $f(z)=z$ on $\DD$. But then $f(\DD)=\DD$, so
$$
R
=
\inf\{\abs{w}:w\notin\DD\}
=1,
$$
a contradiction. Hence $R\le1$.

:::

:::

::: {.pf-step #s1-4}

The equality $R=1$ holds if and only if $f(z)=z$ for every $z\in\DD$.


::: pf-proof

If $R=1$, then $R\ge1$, so step [](#s1-2){.pf-ref} gives $f(z)=z$. Conversely, if $f(z)=z$, then $f(\DD)=\DD$, and therefore
$$
R
=
\inf\{\abs{w}:\abs{w}\ge1\}
=1.
$$

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} proves the required inequality, and step [](#s1-4){.pf-ref} proves the equality characterization.

:::

:::

:::
