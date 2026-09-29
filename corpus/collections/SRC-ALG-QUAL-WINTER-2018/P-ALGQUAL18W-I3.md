---
schema: qual/card@1
id: P-ALGQUAL18W-I3
kind: problem
title: Flatness of $\mathbb Q/\mathbb Z$
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, Problem 3 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Independently used the injection Z --2--> Z and observed that tensoring
    with Q/Z produces multiplication by 2, which kills the nonzero class of
    1/2. This agrees with the recorded source solution.
---

::: {.problem}
True or false?
Justify your answer with a proof or counterexample: the abelian group $\mathbb Q/\mathbb Z$ is flat.
:::

::: {.solution}
The statement is false. Regard
$$
M=\QQ/\ZZ
$$
as a $\ZZ$-module.

::: pf

::: {.pf-step #s1}

Multiplication by $2$ defines an injective homomorphism
$$
\mu_2:\ZZ\longrightarrow\ZZ,
\qquad
n\longmapsto2n.
$$

::: pf-proof

If
$$
2n=0
$$
in $\ZZ$, then $n=0$. Hence the kernel is zero.

:::

:::

::: {.pf-step #s2}

After tensoring step [](#s1){.pf-ref} with $M$, the induced map is multiplication
by $2$ on $M$:
$$
\mu_2\tensor_\ZZ\id_M
:
\ZZ\tensor_\ZZ M
\longrightarrow
\ZZ\tensor_\ZZ M
\cong
M
$$
corresponds to
$$
[q]\longmapsto2[q].
$$

::: pf-proof

Use the canonical isomorphism
$$
\ZZ\tensor_\ZZ M
\xrightarrow{\sim}
M,
\qquad
n\tensor m
\longmapsto
nm.
$$
For a pure tensor,
$$
(\mu_2\tensor\id_M)(n\tensor m)
=
2n\tensor m,
$$
which maps to
$$
2nm.
$$
Thus the induced endomorphism of $M$ is multiplication by $2$.

:::

:::

::: {.pf-step #s3}

Multiplication by $2$ on $\QQ/\ZZ$ is not injective.

::: pf-proof

The class
$$
\frac12+\ZZ
$$
is nonzero in $\QQ/\ZZ$, because $1/2\notin\ZZ$. But
$$
2\left(\frac12+\ZZ\right)
=
1+\ZZ
=
0.
$$
Thus the multiplication-by-$2$ map has nonzero kernel.

:::

:::

::: {.pf-step #s4}

The $\ZZ$-module $\QQ/\ZZ$ is not flat.

::: pf-proof

If $M$ were flat, then the functor
$$
-\tensor_\ZZ M
$$
would preserve injections. Applying it to the injection in step [](#s1){.pf-ref} would
produce an injective map
$$
\ZZ\tensor_\ZZ M
\longrightarrow
\ZZ\tensor_\ZZ M.
$$
By step [](#s2){.pf-ref} this is multiplication by $2$ on $M$, but step [](#s3){.pf-ref} proves that
this map is not injective. Contradiction.

Therefore
$$
\boxed{\QQ/\ZZ\text{ is not flat over }\ZZ.}
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} proves that the statement in the problem is false.

:::

:::

:::
