---
schema: qual/card@1
id: P-BKS19-6A
kind: problem
title: Invertible matrices with $YX=aXY$ exist iff $a^n=1$
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
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 determinant argument and cyclic-shift construction. Both directions are correct; the solution below verifies the wraparound basis vector and invertibility explicitly.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified determinant necessity, invertibility of the shift and diagonal matrices, and the relation $YX=aXY$ on every basis vector including the wraparound case.
---

::: {.problem}
Let $n$ be a positive integer and let $a$ be a complex number.
Prove that $a^n=1$ if and only if there are invertible $n\times n$ complex matrices $X,Y$ such that
$$
YX=aXY.
$$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If invertible $n\times n$ matrices $X,Y$ satisfy $YX=aXY$, then $a^n=1$.


::: pf-proof

Taking determinants gives
$$
\det(Y)\det(X)
=
\det(YX)
=
\det(aXY)
=
a^n\det(X)\det(Y).
$$
Since $X$ and $Y$ are invertible, $\det(X)\det(Y)\neq0$. Cancelling this product yields $a^n=1$.

:::

:::

::: {.pf-step #s1-2}

Suppose $a^n=1$. On the standard basis $e_0,\ldots,e_{n-1}$ of $\CC^n$, with the convention $e_n=e_0$, define
$$
Xe_m=e_{m+1},
\qquad
Ye_m=a^m e_m
\qquad(0\leq m\leq n-1).
$$
Then $X$ and $Y$ are invertible.


::: pf-proof

The matrix $X$ cyclically permutes the basis, hence is invertible. Since $a^n=1$, one has $a\neq0$, so every diagonal entry
$$
1,a,a^2,\ldots,a^{n-1}
$$
of $Y$ is nonzero. Thus $Y$ is invertible.

:::

:::

::: {.pf-step #s1-3}

The matrices from step [](#s1-2){.pf-ref} satisfy $YX=aXY$.


::: pf-proof

For $0\leq m\leq n-2$,
$$
YXe_m
=
Ye_{m+1}
=
a^{m+1}e_{m+1}
=
aXYe_m.
$$
For the remaining basis vector,
$$
YXe_{n-1}=Ye_0=e_0,
$$
whereas
$$
aXYe_{n-1}
=
aX(a^{n-1}e_{n-1})
=
a^n e_0
=e_0.
$$
Thus $YX$ and $aXY$ agree on a basis and hence are equal.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
a^n=1
\quad\Longleftrightarrow\quad
\exists\,X,Y\in\operatorname{GL}_n(\CC)\text{ with }YX=aXY
}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} proves the reverse implication, and steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} prove the forward implication.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is exactly the asserted equivalence.

:::

:::

:::
