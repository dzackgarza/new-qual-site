---
schema: qual/card@1
id: P-UCLARA17F-11
kind: problem
title: Normalized univalent maps of the disk omit a point of modulus at most 1
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
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Fall 2017, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 11. Let $f:\mathbb D\to\mathbb C$ be an injective holomorphic function with $f(0)=0$ and $f'(0)=1$. Show that
\[
\inf\{|w|:w\notin f(\mathbb D)\}\le1,
\]
with equality if and only if $f(z)=z$ for all $z\in\mathbb D$.
:::

::: {.solution}
Set
\[
R\coloneqq\inf\{|w|:w\notin f(\mathbb D)\}.
\]

<1>1. The omitted set $\mathbb C\setminus f(\mathbb D)$ is nonempty; moreover, if $R\ge1$, then $\mathbb D\subset f(\mathbb D)$.

::: {.proof}
If $f(\mathbb D)=\mathbb C$, then the inverse map $f^{-1}:\mathbb C\to\mathbb D$ is an entire bounded function. Liouville's theorem would make $f^{-1}$ constant, contradicting injectivity of $f$. Thus the omitted set is nonempty and $R$ is a finite real number.

If some $w\in\mathbb D$ were omitted by $f$, then $|w|<1$, so the definition of $R$ would give
\[
R\le |w|<1,
\]
contrary to $R\ge1$.
:::

<1>2. If $R\ge1$, then $f(z)=z$ for every $z\in\mathbb D$.

::: {.proof}
By step <1>1, the inverse of the injective holomorphic map $f$ is defined on $\mathbb D$. Let
\[
g\coloneqq f^{-1}|_{\mathbb D}:\mathbb D\to\mathbb D.
\]
Since an injective holomorphic function has nonvanishing derivative, its inverse is holomorphic. Moreover,
\[
g(0)=0,
\qquad
g'(0)=\frac1{f'(0)}=1.
\]
Schwarz's lemma, including its equality case, therefore gives $g(z)=z$ for every $z\in\mathbb D$. Thus for every $w\in\mathbb D$,
\[
f^{-1}(w)=w,
\]
and applying $f$ gives $f(w)=w$.
:::

<1>3. One has
\[
R\le1.
\]

::: {.proof}
If $R>1$, then step <1>2 gives $f(z)=z$ on $\mathbb D$. But then $f(\mathbb D)=\mathbb D$, so
\[
R
=
\inf\{|w|:w\notin\mathbb D\}
=1,
\]
a contradiction. Hence $R\le1$.
:::

<1>4. The equality $R=1$ holds if and only if $f(z)=z$ for every $z\in\mathbb D$.

::: {.proof}
If $R=1$, then $R\ge1$, so step <1>2 gives $f(z)=z$. Conversely, if $f(z)=z$, then $f(\mathbb D)=\mathbb D$, and therefore
\[
R
=
\inf\{|w|:|w|\ge1\}
=1.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>3 proves the required inequality, and step <1>4 proves the equality characterization.
:::
:::
