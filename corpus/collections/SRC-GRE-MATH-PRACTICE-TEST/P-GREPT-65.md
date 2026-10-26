---
schema: qual/card@1
id: P-GREPT-65
kind: problem
title: "Unital ring homomorphisms between $\\ZZ_m$ and $\\ZZ_n$"
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 65 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $\ZZ_n$ denotes the ring of integers modulo $n$, for which of the pairs of rings $(\ZZ_m, \ZZ_n)$ given below does there exist a ring homomorphism $\phi\colon \ZZ_m \to \ZZ_n$ such that $\phi(1) = 1$?

(A) $(\ZZ_4, \ZZ_6)$
(B) $(\ZZ_6, \ZZ_4)$
(C) $(\ZZ_3, \ZZ_6)$
(D) $(\ZZ_6, \ZZ_3)$
(E) $(\ZZ_3, \ZZ_4)$
:::

Write $[k]_r$ for the residue class of an integer $k$ in $\ZZ_r$.

::: pf

::: pf-step

If there is a ring homomorphism
$\phi\colon\ZZ_m\to\ZZ_n$ with $\phi([1]_m)=[1]_n$, then $n\mid m$.


::: pf-proof

In $\ZZ_m$ one has $m[1]_m=[0]_m$. Therefore
\[
[0]_n
=\phi([0]_m)
=\phi(m[1]_m)
=m\phi([1]_m)
=m[1]_n
=[m]_n.
\]
Thus $m\equiv0\pmod n$, which is exactly $n\mid m$.

:::

:::

::: pf-step

If $n\mid m$, then such a homomorphism exists.


::: pf-proof

Define
\[
\phi([k]_m)=[k]_n.
\]
If $[k]_m=[\ell]_m$, then $m\mid(k-\ell)$. Since $n\mid m$, it follows
that $n\mid(k-\ell)$, so $[k]_n=[\ell]_n$. Hence $\phi$ is
well-defined. Reduction modulo $n$ preserves addition and multiplication,
and $\phi([1]_m)=[1]_n$, so $\phi$ is a ring homomorphism with the
required property.

:::

:::

::: pf-step

Among the listed pairs, the condition in steps <1>1 and <1>2 holds only for
$(m,n)=(6,3)$.


::: pf-proof

The required divisibility is $n\mid m$. Of the five choices, only
$3\mid6$ holds: $6\nmid4$, $4\nmid6$, $6\nmid3$, and $4\nmid3$.

:::

:::

::: pf-step

The correct answer is $\boxed{\text{(D) }(\ZZ_6,\ZZ_3)}$.


::: pf-proof

By step <1>3, choice (D) is the unique listed pair satisfying the
necessary and sufficient condition established in steps <1>1 and <1>2.

:::

:::

::: pf-qed

Step <1>4 gives the required pair.

:::

:::
