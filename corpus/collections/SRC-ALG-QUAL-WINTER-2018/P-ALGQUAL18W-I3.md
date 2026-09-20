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
The statement is **false**. Regard
$$
M=\QQ/\ZZ
$$
as a $\ZZ$-module.

<1>1. Multiplication by $2$ defines an injective homomorphism
$$
\mu_2:\ZZ\longrightarrow\ZZ,
\qquad
n\longmapsto2n.
$$

::: {.proof}
If
$$
2n=0
$$
in $\ZZ$, then $n=0$. Hence the kernel is zero.
:::

<1>2. After tensoring step <1>1 with $M$, the induced map is multiplication
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

::: {.proof}
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

<1>3. Multiplication by $2$ on $\QQ/\ZZ$ is not injective.

::: {.proof}
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

<1>4. The $\ZZ$-module $\QQ/\ZZ$ is not flat.

::: {.proof}
If $M$ were flat, then the functor
$$
-\tensor_\ZZ M
$$
would preserve injections. Applying it to the injection in step <1>1 would
produce an injective map
$$
\ZZ\tensor_\ZZ M
\longrightarrow
\ZZ\tensor_\ZZ M.
$$
By step <1>2 this is multiplication by $2$ on $M$, but step <1>3 proves that
this map is not injective. Contradiction.

Therefore
$$
\boxed{\QQ/\ZZ\text{ is not flat over }\ZZ.}
$$
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves that the statement in the problem is false.
:::
:::
