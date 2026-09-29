---
schema: qual/card@1
id: P-BKF06-6A
kind: problem
title: Irreducibility of $x^p-x+1$ over $\mathbb F_p$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6A of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the translated-root factor argument. The retained
    solution contains a circular sentence asserting irreducibility in order
    to exclude a root in F_p; the proof below instead uses f(a)=1 for every
    a in F_p.
---

::: {.problem}
Let $p$ be prime.
Prove that
\[
f(x)=x^p-x+1
\]
is irreducible over the field $\mathbb F_p$.
:::

::: {.solution}

Let $\alpha$ be a root of $f$ in a splitting field over $\FF_p$.

::: pf

::: {.pf-step #roots-are-alpha-plus-a}
The roots of $f$ are precisely
$$
\alpha+a,
\qquad
a\in\FF_p,
$$
and they are pairwise distinct.

::: pf-proof
For every $a\in\FF_p$, characteristic $p$ gives
$$
(x+a)^p=x^p+a^p=x^p+a.
$$
Hence
$$
f(x+a)
=(x+a)^p-(x+a)+1
=
x^p-x+1
=
f(x).
$$
Therefore
$$
f(\alpha+a)=f(\alpha)=0
$$
for every $a\in\FF_p$. The elements $\alpha+a$ are pairwise
distinct because the elements $a$ are. Since $f$ has degree $p$,
these $p$ distinct roots are all of its roots.
:::

:::

::: {.pf-step #alpha-not-in-Fp}
One has
$$
\alpha\notin\FF_p.
$$

::: pf-proof
For every $a\in\FF_p$, Fermat's identity $a^p=a$ gives
$$
f(a)=a^p-a+1=1.
$$
Thus $f$ has no root in $\FF_p$, while $f(\alpha)=0$.
:::

:::

::: {.pf-step #factor-degree-0-or-p}
Every monic factor $g\in\FF_p[x]$ of $f$ has degree either
$0$ or $p$.

::: pf-proof
By step [](#roots-are-alpha-plus-a){.pf-ref}, in the splitting field every monic factor of $f$ has
the form
$$
g(x)=\prod_{a\in I}(x-(\alpha+a))
$$
for some subset $I\subseteq\FF_p$. Since $g$ has coefficients in
$\FF_p$, the negative of its $x^{\deg g-1}$ coefficient, namely the
sum of its roots, belongs to $\FF_p$. Thus
$$
\abs I\,\alpha+\sum_{a\in I}a\in\FF_p.
$$
The second term is already in $\FF_p$, so
$$
\abs I\,\alpha\in\FF_p.
$$
If $0<\abs I<p$, then the class of $\abs I$ is nonzero in
$\FF_p$ and therefore invertible. It would follow that
$\alpha\in\FF_p$, contradicting step [](#alpha-not-in-Fp){.pf-ref}. Hence
$$
\abs I=0
\qquad\text{or}\qquad
\abs I=p.
$$
Since $\deg g=\abs I$, the claim follows.
:::

:::

::: {.pf-step #f-irreducible}
The polynomial
$$
\boxed{x^p-x+1}
$$
is irreducible over $\FF_p$.

::: pf-proof
If $f$ had a nontrivial factorization over $\FF_p$, it would have a
monic factor of degree strictly between $0$ and $p$. Step [](#factor-degree-0-or-p){.pf-ref} shows
that no such factor exists. Hence $f$ is irreducible.
:::

:::

::: pf-qed
Step [](#f-irreducible){.pf-ref} proves the required conclusion.
:::

:::

:::
