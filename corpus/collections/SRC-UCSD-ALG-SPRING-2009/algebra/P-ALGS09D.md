---
schema: qual/card@1
id: P-ALGS09D
kind: problem
title: "Galois group of the splitting field of sqrt(2 + sqrt(2)) over Q"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared with Problem 4 of the official UCSD Spring 2009 algebra qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Corrected the splitting-field identification and exhibited an automorphism cycling the four roots, proving the Galois group is cyclic of order 4.
---

::: problem
Let $\alpha = \sqrt{2 + \sqrt{2}}$ in $\mathbb{C}$ and let $f$ be the minimal polynomial of $\alpha$ over $\mathbb{Q}$.
Let $E$ be the splitting field for $f$ over $\mathbb{Q}$.
Determine the Galois group $\operatorname{Gal}(E/\mathbb{Q})$.
:::

::: {.solution}
Let
\[
\alpha=\sqrt{2+\sqrt2},
\qquad
\beta=\sqrt{2-\sqrt2}.
\]

<1>1. The minimal polynomial of $\alpha$ over $\mathbb Q$ is
\[
f(x)=x^4-4x^2+2.
\]
::: {.proof}
Since
\[
\alpha^2=2+\sqrt2,
\]
we have
\[
(\alpha^2-2)^2=2,
\]
so $f(\alpha)=0$.
The polynomial $f$ is Eisenstein at $2$: every nonleading coefficient is divisible by $2$, and the constant term $2$ is not divisible by $4$.
Hence $f$ is irreducible over $\mathbb Q$.
Therefore $f$ is the minimal polynomial of $\alpha$ and
\[
[\mathbb Q(\alpha):\mathbb Q]=4.
\]
:::

<1>2. The roots of $f$ are
\[
\pm\alpha,
\qquad
\pm\beta.
\]
::: {.proof}
The equation $f(x)=0$ is equivalent to
\[
(x^2-2)^2=2,
\]
so
\[
x^2=2\pm\sqrt2.
\]
Taking square roots gives precisely the four displayed roots.
:::

<1>3. The field $\mathbb Q(\alpha)$ already contains $\beta$.
::: {.proof}
We have
\[
\sqrt2=\alpha^2-2\in\mathbb Q(\alpha).
\]
Also
\[
\alpha\beta
=\sqrt{(2+\sqrt2)(2-\sqrt2)}
=\sqrt2,
\]
where the positive square root is taken because $\alpha,\beta>0$.
Thus
\[
\beta=\frac{\sqrt2}{\alpha}\in\mathbb Q(\alpha).
\]
:::

<1>4. The splitting field is
\[
E=\mathbb Q(\alpha).
\]
::: {.proof}
By <1>2 and <1>3, $\mathbb Q(\alpha)$ contains all four roots $\pm\alpha,\pm\beta$ of $f$.
Hence it is the splitting field of $f$.
Since $f$ is separable over the characteristic-zero field $\mathbb Q$, the extension $E/\mathbb Q$ is Galois.
By <1>1,
\[
|\operatorname{Gal}(E/\mathbb Q)|=[E:\mathbb Q]=4.
\]
:::

<1>5. There is an automorphism $\sigma\in\operatorname{Gal}(E/\mathbb Q)$ satisfying
\[
\sigma(\alpha)=\beta,
\]
and it has order $4$.
::: {.proof}
Because $\beta$ is another root of the irreducible polynomial $f$, the assignment $\alpha\mapsto\beta$ defines a $\mathbb Q$-embedding
\[
\mathbb Q(\alpha)\longrightarrow E.
\]
Since $E=\mathbb Q(\alpha)$ is finite over $\mathbb Q$, this embedding is an automorphism; call it $\sigma$.

Now
\[
\sqrt2=\alpha^2-2,
\]
so
\[
\sigma(\sqrt2)=\beta^2-2=(2-\sqrt2)-2=-\sqrt2.
\]
Using $\beta=\sqrt2/\alpha$,
\[
\sigma(\beta)
=\frac{\sigma(\sqrt2)}{\sigma(\alpha)}
=\frac{-\sqrt2}{\beta}
=-\alpha.
\]
Therefore
\[
\alpha\xmapsto{\sigma}\beta
\xmapsto{\sigma}-\alpha
\xmapsto{\sigma}-\beta
\xmapsto{\sigma}\alpha.
\]
Thus $\sigma$ has order $4$.
:::

<1>6. Consequently
\[
\operatorname{Gal}(E/\mathbb Q)\cong C_4.
\]
::: {.proof}
By <1>4 the Galois group has order $4$, and by <1>5 it contains an element of order $4$.
Hence the group is cyclic of order $4$.
:::
:::
