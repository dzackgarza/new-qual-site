---
schema: qual/card@1
id: P-CAS24G
kind: problem
title: Polynomial of an isolated singularity preserves singularity type
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Holomorphic Functions
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each part re-read: the removable case is the composite of
      holomorphic extensions; the pole case uses |P(w)| -> infinity; and the essential case needs
      that the sublevel sets of a nonconstant polynomial are bounded, which is now a step of its
      own, applied in both directions (bounded g would give bounded f; f unbounded gives
      |P(f)| -> infinity). The card records where nonconstancy of P is used. Not claimed: the
      converse implications, which are false for constant P.
---

::: {.problem}
Let $U \subset \CC$ be an open set.
Let $f : U \setminus \{a\} \to \CC$ be a holomorphic function with an isolated singularity at $a \in U$.

Let $P$ be a non-constant polynomial.
Let $g : U \setminus \{a\} \to \CC$ be given by
$$
g(z) = P(f(z)).
$$

Show that:

(i) If $f$ has a removable singularity at $a$, then $g$ has a removable singularity at $a$.

(ii) If $f$ has a pole at $a$, then $g$ has a pole at $a$.

(iii) If $f$ has an essential singularity at $a$, then $g$ has an essential singularity at $a$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #setup}
Write $P(w)=c_{d}w^{d}+\cdots+c_{0}$ with $c_{d}\ne0$ and $d\ge1$, and let $g=P\circ f$ on $U\setminus\{a\}$.

::: pf-proof
This is the data of the problem; $g$ is holomorphic on $U\setminus\{a\}$ as a composite of holomorphic maps, so $a$ is an isolated singularity of $g$ and the trichotomy removable / pole / essential applies to it.
:::

:::

::: {.pf-step #removable}
If $f$ has a removable singularity at $a$ then so does $g$.

::: pf-proof
$f$ then extends holomorphically to $a$, and $P\circ f$ extends to the composite, which is holomorphic at $a$; so $g$ is bounded near $a$ and extends.
:::

:::

::: {.pf-step #pole}
If $f$ has a pole at $a$ then so does $g$.

::: pf-proof
A pole means $\abs{f(z)}\to\infty$ as $z\to a$. For $c_{d}\ne0$ and $d\ge1$ one has $\abs{P(w)}\to\infty$ as $\abs{w}\to\infty$, so $\abs{g(z)}=\abs{P(f(z))}\to\infty$; a function tending to infinity in modulus at an isolated singularity has a pole there.
:::

:::

::: {.pf-step #boundedlevel}
For every $M>0$ the set $\{w:\abs{P(w)}\le M\}$ is bounded.

::: pf-proof
If it were unbounded there would be $w_{n}$ with $\abs{w_{n}}\to\infty$ and $\abs{P(w_{n})}\le M$; but $\abs{P(w)}\ge\tfrac{\abs{c_{d}}}{2}\abs{w}^{d}$ for large $\abs{w}$, which is unbounded, a contradiction.
:::

:::

::: {.pf-step #essential}
If $f$ has an essential singularity at $a$ then so does $g$.

::: pf-proof
Suppose $g$ were removable. Then $g$ would be bounded near $a$, say $\abs{g(z)}\le M$; by step [](#boundedlevel){.pf-ref} the set of $w$ with $\abs{P(w)}\le M$ is bounded, so $f$ would be bounded near $a$ and $a$ would be a removable singularity of $f$, contrary to the hypothesis. Suppose instead that $g$ had a pole; then $\abs{P(f(z))}\to\infty$, so for $\abs{P(f(z))}>M$ the value $f(z)$ lies outside the bounded set $\{w:\abs{P(w)}\le M\}$, whence $\abs{f(z)}\to\infty$ and $f$ would have a pole, again contrary to the hypothesis. So $g$ is neither removable nor a pole, hence essential.
:::

:::

::: {.pf-step}
Parts (i), (ii) and (iii) hold.

::: pf-proof
Steps [](#removable){.pf-ref}, [](#pole){.pf-ref} and [](#essential){.pf-ref} are the three assertions:
$$
\boxed{f\text{ removable, pole or essential at }a\implies P\circ f\text{ is of the same type}.}
$$
The hypothesis that $P$ is nonconstant is used twice: in step [](#pole){.pf-ref} for $\abs{P(w)}\to\infty$, and in step [](#boundedlevel){.pf-ref} for the boundedness of the sublevel sets; a constant $P$ would destroy both conclusions.
:::

:::

:::
:::
