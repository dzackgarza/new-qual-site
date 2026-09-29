---
schema: qual/card@1
id: P-BKS16-9A
kind: problem
title: Galois group of the normal closure of $\QQ(\sqrt3+\sqrt5)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Checked against Sp16_Exam.pdf Problem 9A and corrected the prior nested-radical transcription; the source has two separate radicals, sqrt(3)+sqrt(5).
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked recovery of sqrt(3) and sqrt(5) from the primitive element, degree four of the biquadratic field, normality, and the independent sign-change automorphisms.
---

::: {.problem}
Compute the Galois group of the normal closure of the field
$$
K=\QQ\!\left(\sqrt3+\sqrt5\right)
$$
over $\QQ$.
:::

::: {.solution}
Set
$$
\alpha=\sqrt3+\sqrt5,
\qquad
K=\QQ(\alpha).
$$

::: pf

::: {.pf-step #s1}

One has
$$
\sqrt{15}\in K.
$$

::: pf-proof

Squaring $\alpha$ gives
$$
\alpha^2
=
3+5+2\sqrt{15}
=
8+2\sqrt{15}.
$$
Hence
$$
\sqrt{15}
=
\frac{\alpha^2-8}{2}
\in
K.
$$

:::

:::

::: {.pf-step #s2}

Both $\sqrt3$ and $\sqrt5$ lie in $K$.

::: pf-proof

By step [](#s1){.pf-ref},
$$
\beta
\coloneqq
\alpha\sqrt{15}
\in
K.
$$
Expanding gives
$$
\beta
=
(\sqrt3+\sqrt5)\sqrt{15}
=
5\sqrt3+3\sqrt5.
$$
Together with
$$
\alpha=\sqrt3+\sqrt5,
$$
this yields
$$
\sqrt3
=
\frac{\beta-3\alpha}{2}
\in K
$$
and
$$
\sqrt5
=
\frac{5\alpha-\beta}{2}
\in K.
$$

:::

:::

::: {.pf-step #s3}

Therefore
$$
K=\QQ(\sqrt3,\sqrt5).
$$

::: pf-proof

Step [](#s2){.pf-ref} gives
$$
\QQ(\sqrt3,\sqrt5)\subseteq K.
$$
The reverse inclusion holds because
$$
\alpha=\sqrt3+\sqrt5
\in
\QQ(\sqrt3,\sqrt5).
$$

:::

:::

::: {.pf-step #s4}

The extension
$$
\QQ(\sqrt3,\sqrt5)/\QQ
$$
has degree $4$.

::: pf-proof

Certainly
$$
[\QQ(\sqrt3):\QQ]=2.
$$
It remains to show
$$
\sqrt5\notin\QQ(\sqrt3).
$$
Suppose otherwise. Then for some $a,b\in\QQ$,
$$
\sqrt5=a+b\sqrt3.
$$
Squaring gives
$$
5=a^2+3b^2+2ab\sqrt3.
$$
Since $\sqrt3\notin\QQ$, one must have $ab=0$. If $b=0$, then $a^2=5$, impossible for $a\in\QQ$. If $a=0$, then $b^2=5/3$, also impossible for $b\in\QQ$. Indeed, a square in $\QQ^\times$ has even exponent at every prime in its reduced numerator and denominator, whereas both $5$ and $5/3$ have odd exponent at the prime $5$. Hence adjoining $\sqrt5$ to $\QQ(\sqrt3)$ has degree $2$, so the total degree is $4$.

:::

:::

::: {.pf-step #s5}

The field $K$ is already normal over $\QQ$.

::: pf-proof

By step [](#s3){.pf-ref},
$$
K=\QQ(\sqrt3,\sqrt5),
$$
which is the splitting field over $\QQ$ of
$$
(x^2-3)(x^2-5).
$$
In characteristic $0$ this polynomial is separable. Thus $K/\QQ$ is Galois, in particular normal, so the normal closure of the original field is $K$ itself.

:::

:::

::: {.pf-step #s6}

There are four $\QQ$-automorphisms of $K$, obtained by independently choosing the signs of $\sqrt3$ and $\sqrt5$.

::: pf-proof

Every $\QQ$-automorphism must send
$$
\sqrt3\longmapsto\pm\sqrt3
$$
and
$$
\sqrt5\longmapsto\pm\sqrt5.
$$
Conversely, each independent choice of these two signs preserves all algebraic relations and defines an automorphism of $\QQ(\sqrt3,\sqrt5)$. Thus there are four automorphisms, consistent with the degree computation in step [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s7}

Hence the Galois group of the normal closure is
$$
\boxed{
\Gal(K/\QQ)
\cong
\ZZ_2\times\ZZ_2
}.
$$

::: pf-proof

The two sign changes
$$
\sqrt3\mapsto-\sqrt3,
\qquad
\sqrt5\mapsto\sqrt5
$$
and
$$
\sqrt3\mapsto\sqrt3,
\qquad
\sqrt5\mapsto-\sqrt5
$$
are commuting involutions and generate all four automorphisms from step [](#s6){.pf-ref}. Therefore the group is the Klein four group.

:::

:::

::: pf-qed

Steps [](#s5){.pf-ref} and [](#s7){.pf-ref} identify the normal closure and its Galois group.

:::

:::

:::
