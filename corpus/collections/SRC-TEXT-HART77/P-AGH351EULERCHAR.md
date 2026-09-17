---
schema: qual/card@1
id: P-AGH351EULERCHAR
kind: problem
title: Additivity of the Euler characteristic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Euler Characteristic
  - Coherent Sheaves
  - Projective Schemes
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the Euler-characteristic definition and additivity assertion with the retained Hartshorne Chapter III section 5 transcription. The proof first verifies finiteness of the terms and of the sum, then telescopes the dimensions in the actual long exact cohomology sequence.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a projective scheme over a field $k$, and let $\mcf$ be a coherent sheaf on $X$.
We define the Euler characteristic of $\mcf$ by
$$
\chi(\mcf)=\sum_{i\ge0}(-1)^i\dim_k H^i(X,\mcf).
$$
If
$$
0 \to \mcf' \to \mcf \to \mcf'' \to 0
$$
is a short exact sequence of coherent sheaves on $X$, show that $\chi(\mcf)=\chi(\mcf')+\chi(\mcf'')$.
:::

::: {.solution}
All dimensions below are dimensions of vector spaces over $k$.
If $X$ is empty, every term is zero and the assertion holds, so assume $X\ne\varnothing$.

<1>1. The Euler characteristics are finite sums of finite integers, and the cohomology long exact sequence has only finitely many nonzero terms.

::: {.proof}
A projective scheme over a field is noetherian and has finite dimension.
The cohomology of each coherent sheaf on it is finite-dimensional over $k$ [@Har10a, Theorem III.5.2].
Its cohomology is zero in degrees greater than $\dim X$ by Grothendieck vanishing [@Har10a, Theorem III.2.7].
These statements apply to all three coherent sheaves in the given sequence.
Thus their Euler characteristics are defined by finite sums, and the long exact sequence terminates in zeros.
:::

<1>2. The alternating sum of the dimensions in any finite exact sequence of finite-dimensional vector spaces is zero.

::: {.proof}
Let $0\to V^0\to V^1\to\cdots\to V^N\to0$ be such a sequence, and put $B^i=\im(V^{i-1}\to V^i)$, with $B^0=B^{N+1}=0$.
Exactness gives $\dim V^i=\dim B^i+\dim B^{i+1}$.
In the sum $\sum_{i=0}^N(-1)^i\dim V^i$, every dimension $\dim B^i$ therefore occurs twice with opposite signs.
The sum is zero.
:::

<1>3. The Euler characteristic is additive on the given short exact sequence.

::: {.proof}
Its long exact sequence is
$$
0\to H^0(X,\mcf')\to H^0(X,\mcf)\to H^0(X,\mcf'')
\to H^1(X,\mcf')\to H^1(X,\mcf)\to\cdots.
$$
By step <1>1, step <1>2 applies to this finite nonzero portion.
The signs in each consecutive triple are $(-1)^i,-(-1)^i,(-1)^i$, because the $i$th triple starts at position $3i$.
Consequently
$$
0=\sum_{i\ge0}(-1)^i\bigl(\dim H^i(X,\mcf')-\dim H^i(X,\mcf)+\dim H^i(X,\mcf'')\bigr).
$$
This is $\chi(\mcf')-\chi(\mcf)+\chi(\mcf'')=0$, giving the claimed identity.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>1 verifies that all the quantities and sums are finite, and steps <1>2--<1>3 prove the required additivity.
:::
:::
