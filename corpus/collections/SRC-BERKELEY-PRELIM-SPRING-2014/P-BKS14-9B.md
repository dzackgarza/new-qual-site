---
schema: qual/card@1
id: P-BKS14-9B
kind: problem
title: Burnside counting for a transitive action
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked both incidence-set counts, the orbit-stabilizer simplification, and the fixed-point-free element contradiction.
---

::: {.problem}
Let a finite group $G$ act transitively on a finite set $X$. For $g\in G$, let
$$
\operatorname{Fix}_g(X)=\{x\in X:g(x)=x\}.
$$

(a) Show that
$$
|G|=\sum_{g\in G}|\operatorname{Fix}_g(X)|.
$$
Hint: count $\{(x,g)\in X\times G:gx=x\}$ in two ways.

(b) Show that if $|X|>1$, then some $g\in G$ fixes no point of $X$.
:::

::: {.solution}
Define
$$
S
\coloneqq
\{(x,g)\in X\times G:g x=x\}.
$$

::: pf

::: {.pf-step #s1}

Counting $S$ first by the coordinate $x$ gives
$$
\abs{S}
=
\sum_{x\in X}\abs{\operatorname{Stab}_G(x)}.
$$

::: pf-proof

For a fixed $x\in X$, the elements $g\in G$ for which
$$
(x,g)\in S
$$
are exactly the stabilizer
$$
\operatorname{Stab}_G(x)
=
\{g\in G:gx=x\}.
$$
Summing these fiber cardinalities over $x$ gives the formula.

:::

:::

::: {.pf-step #s2}

Since the action is transitive, for every $x\in X$,
$$
\abs{\operatorname{Stab}_G(x)}
=
\frac{\abs{G}}{\abs{X}}.
$$

::: pf-proof

The orbit of $x$ is all of $X$ by transitivity. The orbit-stabilizer
theorem gives
$$
\abs{G}
=
\abs{\operatorname{Orb}(x)}
\abs{\operatorname{Stab}_G(x)}
=
\abs{X}
\abs{\operatorname{Stab}_G(x)}.
$$
Rearrange.

:::

:::

::: {.pf-step #s3}

Therefore
$$
\abs{S}
=
\abs{G}.
$$

::: pf-proof

Combine steps [](#s1){.pf-ref} and [](#s2){.pf-ref}:
$$
\abs{S}
=
\abs{X}
\frac{\abs{G}}{\abs{X}}
=
\abs{G}.
$$

:::

:::

::: {.pf-step #s4}

Counting $S$ first by the coordinate $g$ gives
$$
\abs{S}
=
\sum_{g\in G}
\abs{\operatorname{Fix}_g(X)}.
$$

::: pf-proof

For a fixed $g\in G$, the elements $x\in X$ for which
$$
(x,g)\in S
$$
are exactly the fixed points of $g$. Summing these fiber sizes over $g$
gives the formula.

:::

:::

::: {.pf-step #s5}

One has
$$
\boxed{
\abs{G}
=
\sum_{g\in G}
\abs{\operatorname{Fix}_g(X)}
}.
$$

::: pf-proof

Both sides equal $\abs{S}$ by steps [](#s3){.pf-ref} and [](#s4){.pf-ref}. This proves part (a).

:::

:::

::: {.pf-step #s6}

Suppose
$$
\abs{X}>1.
$$
If every $g\in G$ fixed at least one point, then
$$
\sum_{g\in G}
\abs{\operatorname{Fix}_g(X)}
>
\abs{G}.
$$

::: pf-proof

The identity element $e$ fixes every point of $X$, so
$$
\abs{\operatorname{Fix}_e(X)}
=
\abs{X}.
$$
Under the supposition, each of the other $\abs{G}-1$ elements contributes
at least one fixed point. Therefore
$$
\begin{aligned}
\sum_{g\in G}
\abs{\operatorname{Fix}_g(X)}
&\geq
\abs{X}+(\abs{G}-1)\\
&>
1+(\abs{G}-1)\\
&=
\abs{G}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s7}

If $\abs{X}>1$, there exists
$$
\boxed{g\in G}
$$
such that
$$
\operatorname{Fix}_g(X)=\varnothing.
$$

::: pf-proof

If no such element existed, step [](#s6){.pf-ref} would contradict the equality in
step [](#s5){.pf-ref}. This proves part (b).

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves part (a), and step [](#s7){.pf-ref} proves part (b).

:::

:::

:::
