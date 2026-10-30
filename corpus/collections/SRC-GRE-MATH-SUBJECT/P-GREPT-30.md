---
schema: qual/card@1
id: P-GREPT-30
kind: problem
title: "Whether $m\\bullet n=m+n+mn$ makes $\\ZZ$ a group"
classification:
  areas: [algebra]
  topics:
  - Groups
  - Group Axioms
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 30 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR). The extraction prints the operation as a centered dot in its definition and as a bullet in (Z, bullet); the bullet is used throughout."
---

::: {.problem}
Define a binary operation on $\ZZ$, the set of integers, by the equation $m \bullet n = m + n + mn$. Which of the following statements is/are true about the binary structure $(\ZZ, \bullet)$?

I. This structure is not a group since the operation is not associative.

II. This structure is not a group since there is no identity element.

III. This structure is not a group since not all elements have an inverse.

IV. This structure is a group.

(A) I and II only
(B) I and III only
(C) II and III only
(D) III only
(E) IV only
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The operation $\bullet$ is associative.


::: pf-proof

For every integer $m$, set $\phi(m)=m+1$. Then
$$
\phi(m\bullet n)
=m+n+mn+1
=(m+1)(n+1)
=\phi(m)\phi(n).
$$
Hence
$$
\begin{aligned}
\phi((m\bullet n)\bullet q)
&=\phi(m\bullet n)\phi(q)\\
&=\phi(m)\phi(n)\phi(q)\\
&=\phi(m)\phi(n\bullet q)\\
&=\phi(m\bullet(n\bullet q)).
\end{aligned}
$$
Since $\phi$ is injective, $(m\bullet n)\bullet q=m\bullet(n\bullet q)$.
Thus statement I is false.

:::

:::

::: {.pf-step #s1-2}

The integer $0$ is an identity element for $\bullet$.


::: pf-proof

For every $m\in\ZZ$,
$$
m\bullet0=m+0+m0=m
$$
and
$$
0\bullet m=0+m+0m=m.
$$
Thus statement II is false.

:::

:::

::: {.pf-step #s1-3}

The element $1$ has no inverse in $(\ZZ,\bullet)$.


::: pf-proof

If $n\in\ZZ$ were an inverse of $1$, then by step [](#s1-2){.pf-ref} it would satisfy
$$
1\bullet n=0.
$$
But
$$
1\bullet n=1+n+n=1+2n,
$$
so this would require $2n=-1$, which has no integer solution. Hence not every
element has an inverse, and statement III is true.

:::

:::

::: {.pf-step #s1-4}

Therefore exactly statement III is true, so the answer is
$$
\boxed{\text{(D) III only}}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} show that I and II are false while III is true. Since a
group requires every element to have an inverse, step [](#s1-3){.pf-ref} also shows that IV
is false.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required choice.

:::

:::

:::
