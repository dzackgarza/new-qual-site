---
schema: qual/card@1
id: P-UCLAB11F-12
kind: problem
title: Least-squares minimizers differ by a kernel vector
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Let $A$ be an $m\times n$ real matrix and let $b\in\RR^m$.
Suppose $Ax$ and $Ay$ both have minimal distance to $b$ among all vectors in $\operatorname{image}(A)$.
Prove that
$$
x-y\in\ker A.
$$
:::

::: {.solution}

Let
$$
M=\operatorname{image}(A)\subseteq\RR^m.
$$

::: pf

::: {.pf-step #s1-1}

The nearest point in the subspace $M$ to $b$ is unique.


::: pf-proof

Suppose
$$
u,v\in M
$$
both minimize the Euclidean distance to $b$, and let
$$
d=\norm{b-u}=\norm{b-v}.
$$
Since $M$ is a subspace,
$$
\frac{u+v}{2}\in M.
$$
Using the parallelogram identity with
$$
p=b-u,
\qquad
q=b-v,
$$
one obtains
$$
\norm{b-\frac{u+v}{2}}^2
=
\frac12\norm{b-u}^2
+
\frac12\norm{b-v}^2
-
\frac14\norm{u-v}^2.
$$
Thus
$$
\norm{b-\frac{u+v}{2}}^2
=
d^2-\frac14\norm{u-v}^2.
$$
If $u\ne v$, the right side is strictly smaller than $d^2$, contradicting minimality of $d$. Hence
$$
u=v.
$$

:::

:::

::: {.pf-step #s1-2}

Under the hypotheses of the problem,
$$
Ax=Ay.
$$


::: pf-proof

The vectors $Ax$ and $Ay$ both belong to
$$
M=\operatorname{image}(A)
$$
and both have minimal distance to $b$. By uniqueness from step [](#s1-1){.pf-ref}, they are equal.

:::

:::

::: {.pf-step #s1-3}

One has
$$
A(x-y)=0.
$$


::: pf-proof

By linearity of $A$ and step [](#s1-2){.pf-ref},
$$
A(x-y)
=
Ax-Ay
=0.
$$

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{x-y\in\ker A}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} is exactly the defining condition for membership in the kernel of $A$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
