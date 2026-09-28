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

<1>1. Counting $S$ first by the coordinate $x$ gives
$$
\abs{S}
=
\sum_{x\in X}\abs{\operatorname{Stab}_G(x)}.
$$

::: {.proof}
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

<1>2. Since the action is transitive, for every $x\in X$,
$$
\abs{\operatorname{Stab}_G(x)}
=
\frac{\abs{G}}{\abs{X}}.
$$

::: {.proof}
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

<1>3. Therefore
$$
\abs{S}
=
\abs{G}.
$$

::: {.proof}
Combine steps <1>1 and <1>2:
$$
\abs{S}
=
\abs{X}
\frac{\abs{G}}{\abs{X}}
=
\abs{G}.
$$
:::

<1>4. Counting $S$ first by the coordinate $g$ gives
$$
\abs{S}
=
\sum_{g\in G}
\abs{\operatorname{Fix}_g(X)}.
$$

::: {.proof}
For a fixed $g\in G$, the elements $x\in X$ for which
$$
(x,g)\in S
$$
are exactly the fixed points of $g$. Summing these fiber sizes over $g$
gives the formula.
:::

<1>5. One has
$$
\boxed{
\abs{G}
=
\sum_{g\in G}
\abs{\operatorname{Fix}_g(X)}
}.
$$

::: {.proof}
Both sides equal $\abs{S}$ by steps <1>3 and <1>4. This proves part (a).
:::

<1>6. Suppose
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

::: {.proof}
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

<1>7. If $\abs{X}>1$, there exists
$$
\boxed{g\in G}
$$
such that
$$
\operatorname{Fix}_g(X)=\varnothing.
$$

::: {.proof}
If no such element existed, step <1>6 would contradict the equality in
step <1>5. This proves part (b).
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>5 proves part (a), and step <1>7 proves part (b).
:::
:::
