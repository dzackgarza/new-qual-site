---
schema: qual/card@1
id: P-GREPT-48
kind: problem
title: "Five consecutive rings $\\ZZ_n$ containing exactly one field"
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 48 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
If $m$ is an integer greater than $1$, let $\ZZ_m$ denote the ring of integers modulo $m$. Determine the smallest value of $n$ such that the set $A = \{\ZZ_n, \ZZ_{n+1}, \ZZ_{n+2}, \ZZ_{n+3}, \ZZ_{n+4}\}$ contains precisely one field.

(A) $2$
(B) $4$
(C) $6$
(D) $8$
(E) None of the above
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every integer $m>1$, the ring $\ZZ_m$ is a field exactly when
$m$ is prime.


::: pf-proof

If $m$ is composite, write $m=ab$ with $1<a,b<m$. Then the nonzero residue
classes of $a$ and $b$ multiply to $0$, so $\ZZ_m$ is not a field. If $m$ is
prime, every nonzero residue class $[a]$ has $\gcd(a,m)=1$, so Bezout's
identity gives integers $u,v$ with $au+mv=1$; hence $[u]$ is an inverse of
$[a]$.

:::

:::

::: {.pf-step #s1-2}

For $n=2,3,4,5$, the five integers $n,n+1,\ldots,n+4$ contain at
least two primes.


::: pf-proof

The corresponding prime entries are
$$
\begin{array}{c|c}
n&\text{primes among }n,\ldots,n+4\\ \hline
2&2,3,5\\
3&3,5,7\\
4&5,7\\
5&5,7.
\end{array}
$$
By step [](#s1-1){.pf-ref}, each of these intervals therefore gives at least two fields.

:::

:::

::: {.pf-step #s1-3}

For $n=6$, exactly one of $6,7,8,9,10$ is prime, namely $7$.


::: pf-proof

The integers $6,8,9,10$ are composite, while $7$ is prime. By step [](#s1-1){.pf-ref},
among
$$
\ZZ_6,\ZZ_7,\ZZ_8,\ZZ_9,\ZZ_{10}
$$
only $\ZZ_7$ is a field.

:::

:::

::: {.pf-step #s1-4}

Therefore the smallest possible value is
$$
\boxed{6},
$$
so the answer is (C).


::: pf-proof

Step [](#s1-2){.pf-ref} excludes every admissible integer below $6$, and step [](#s1-3){.pf-ref} shows
that $6$ has the required property.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the required smallest value.

:::

:::

:::
