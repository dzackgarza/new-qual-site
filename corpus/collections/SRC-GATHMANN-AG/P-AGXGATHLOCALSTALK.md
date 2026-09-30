---
schema: qual/card@1
id: P-AGXGATHLOCALSTALK
kind: problem
title: Which of the continuous and locally polynomial function sheaves has local stalks
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Stalks
  - Local Rings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-20
  note: >-
    Read Gathmann 3.21 in the retained native Problem Set 4 source at revision
    7eafedfc0 and compared it with the current card. The retained source states
    this problem but gives no worked solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Re-read the proof. Checked that a continuous germ is a unit exactly when
    its value at a is nonzero, and that the locally polynomial stalk is
    canonically R[t], with distinct maximal ideals corresponding to a and
    a+1.
---

::: {.problem}
Let $a\in \RR$, and consider sheaves $\mcf$ on $\RR$ with the standard topology:

1. $\mcf \definedas$ the sheaf of continuous functions;

2. $\mcf \definedas$ the sheaf of locally polynomial functions.

For which is the stalk $\mcf_a$ a local ring?

> Recall that a local ring has precisely one maximal ideal.
:::

::: {.solution}
For the first sheaf, write $C_a$ for the stalk at $a$. For the second,
write $P_a$ for the stalk at $a$.

::: pf

::: {.pf-step #continuous-stalk-is-local}
The ring $C_a$ has the unique maximal ideal
$$
\mfm_a
\coloneqq
\{[f]_a\in C_a:f(a)=0\}.
$$

::: pf-proof
Evaluation at $a$ gives a surjective ring homomorphism
$$
\operatorname{ev}_a:C_a\longrightarrow \RR,
\qquad
[f]_a\longmapsto f(a).
$$
It is well defined because two representatives of the same germ agree on a
neighborhood of $a$, and its kernel is $\mfm_a$. Hence
$$
C_a/\mfm_a\cong\RR,
$$
so $\mfm_a$ is maximal.

If $[f]_a\notin\mfm_a$, then $f(a)\ne0$. By continuity, after shrinking
the domain of $f$ there is a neighborhood $U$ of $a$ on which $f$
never vanishes. The continuous function $1/f$ on $U$ then represents an
inverse germ for $[f]_a$. Thus every element outside $\mfm_a$ is a unit.

A proper ideal cannot contain a unit, so every proper ideal of $C_a$ is
contained in $\mfm_a$. Therefore every maximal ideal equals $\mfm_a$, and
$C_a$ is local.
:::

:::

::: {.pf-step #polynomial-stalk-isomorphism}
There is a canonical ring isomorphism
$$
\Phi:\RR[t]\xrightarrow{\sim}P_a,
\qquad
p\longmapsto[p]_a.
$$

::: pf-proof
Every germ in $P_a$ has a representative that is polynomial on some
neighborhood of $a$, by the definition of a locally polynomial function.
Hence $\Phi$ is surjective.

If $\Phi(p)=0$, then $p$ vanishes on some neighborhood of $a$. A real
polynomial that vanishes on a nonempty open interval is the zero polynomial.
Thus $p=0$, so $\Phi$ is injective.
:::

:::

::: {.pf-step #polynomial-stalk-not-local}
The ring $P_a$ is not local.

::: pf-proof
In $\RR[t]$, the ideals
$$
(t-a)
\qquad\text{and}\qquad
(t-(a+1))
$$
are distinct maximal ideals, since the corresponding quotient rings are both
isomorphic to $\RR$. By the isomorphism in step [](#polynomial-stalk-isomorphism){.pf-ref}, their images are two
distinct maximal ideals of $P_a$. Hence $P_a$ is not local.
:::

:::

::: {.pf-step #classification-answer}
The requested classification is
$$
\boxed{\text{the stalk is local exactly for the sheaf of continuous functions.}}
$$

::: pf-proof
Step [](#continuous-stalk-is-local){.pf-ref} proves that the stalk of the sheaf of continuous functions is
local. Step [](#polynomial-stalk-not-local){.pf-ref} proves that the stalk of the sheaf of locally polynomial
functions is not local.
:::

:::

::: pf-qed
Step [](#classification-answer){.pf-ref} gives the complete answer to the two cases in the problem.
:::

:::
:::
