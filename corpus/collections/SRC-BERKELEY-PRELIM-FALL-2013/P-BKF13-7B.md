---
schema: qual/card@1
id: P-BKF13-7B
kind: problem
title: Invertibility of $I_m-AB$ implies invertibility of $I_n-BA$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2013 solution packet. Its written
    argument proves the converse singularity implication; the authored proof
    below uses the required direction.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the kernel argument, including that a BA-fixed vector with zero
    A-image must itself be zero.
---

::: {.problem}
Suppose that A is an m by n complex matrix and B is an n by m complex matrix, and write $I _ { m }$ for the m by m identity matrix.
Show that if $I _ { m } - A B$ is invertible then so is $I _ { n } - B A$ (Hint: what does the condition that $I _ { m } - X$ is not invertible say about eigenvalues and eigenvectors of X?)
:::

::: {.solution}
Assume that $I_m-AB$ is invertible.

<1>1. The kernel of $I_n-BA$ is trivial.

::: {.proof}
Let $v\in\CC^n$ satisfy
$$
(I_n-BA)v=0.
$$
Then $BAv=v$. Set $w\coloneqq Av\in\CC^m$. We have
$$
ABw
=
ABAv
=
A(BAv)
=
Av
=
w,
$$
so $(I_m-AB)w=0$. Since $I_m-AB$ is invertible, $w=0$. Therefore
$$
v=BAv=Bw=0.
$$
Thus $\ker(I_n-BA)=\{0\}$.
:::

<1>2. The matrix $I_n-BA$ is invertible.

::: {.proof}
By step <1>1, the linear map $I_n-BA:\CC^n\to\CC^n$ is injective. An
injective endomorphism of the finite-dimensional vector space $\CC^n$ is
surjective, hence invertible.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 is the required conclusion.
:::
:::
