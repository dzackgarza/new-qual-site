---
schema: qual/card@1
id: P-ALGQUAL18W-I5
kind: problem
title: Irreducibility modulo $2$ of $\Phi_{255}$
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part I, Problem 5 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-20
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-20
  note: >-
    Independently placed every root in F_256 using alpha^255=1, bounded its
    minimal-polynomial degree by 8, and compared with phi(255)=128. This agrees
    with the recorded source solution.
---

::: {.problem}
True or false?
Justify your answer with a proof or counterexample: the cyclotomic polynomial $\Phi_{255}(x)$, reduced modulo $2$, is irreducible in $\mathbb F_2[x]$.
:::

::: {.solution}
The statement is false. Let
$$
\overline{\Phi}_{255}(x)
\in
\FF_2[x]
$$
denote the reduction of $\Phi_{255}(x)$ modulo $2$.

::: pf

::: {.pf-step #s1}

The polynomial $\overline{\Phi}_{255}(x)$ divides
$$
x^{255}-1
$$
in $\FF_2[x]$.

::: pf-proof

Over $\ZZ[x]$, the cyclotomic factorization gives
$$
x^{255}-1
=
\prod_{d\mid255}\Phi_d(x).
$$
Reducing coefficients modulo $2$ preserves multiplication and therefore
preserves divisibility. Hence
$$
\overline{\Phi}_{255}(x)
\mid
x^{255}-1
$$
in $\FF_2[x]$.

:::

:::

::: {.pf-step #s2}

If
$$
\alpha
$$
is any root of $\overline{\Phi}_{255}$ in an algebraic closure of $\FF_2$,
then
$$
\alpha^{256}=\alpha.
$$

::: pf-proof

By step [](#s1){.pf-ref},
$$
\alpha^{255}=1.
$$
Multiplying by $\alpha$ gives
$$
\alpha^{256}=\alpha.
$$

:::

:::

::: {.pf-step #s3}

Every root $\alpha$ of $\overline{\Phi}_{255}$ lies in
$$
\FF_{256}.
$$

::: pf-proof

The roots in an algebraic closure of
$$
x^{256}-x
$$
are exactly the elements of the finite field
$$
\FF_{256}.
$$
Step [](#s2){.pf-ref} says that $\alpha$ is such a root. Therefore
$$
\alpha\in\FF_{256}.
$$

:::

:::

::: {.pf-step #s4}

The minimal polynomial of any such root $\alpha$ over $\FF_2$ has
degree at most $8$.

::: pf-proof

Since
$$
256=2^8,
$$
one has
$$
[\FF_{256}:\FF_2]=8.
$$
Step [](#s3){.pf-ref} gives
$$
\FF_2(\alpha)\subseteq\FF_{256}.
$$
Thus
$$
[\FF_2(\alpha):\FF_2]
\leq
8.
$$
This degree is exactly the degree of the minimal polynomial of $\alpha$ over
$\FF_2$.

:::

:::

::: {.pf-step #s5}

The degree of $\overline{\Phi}_{255}$ is
$$
\boxed{128}.
$$

::: pf-proof

Reduction modulo $2$ does not change the leading coefficient of the monic
cyclotomic polynomial, so
$$
\deg\overline{\Phi}_{255}
=
\deg\Phi_{255}
=
\varphi(255).
$$
Since
$$
255=3\cdot5\cdot17,
$$
Euler's totient formula gives
$$
\begin{aligned}
\varphi(255)
&=
255
\left(1-\frac13\right)
\left(1-\frac15\right)
\left(1-\frac1{17}\right)\\
&=
2\cdot4\cdot16\\
&=
128.
\end{aligned}
$$

:::

:::

::: {.pf-step #s6}

The polynomial $\overline{\Phi}_{255}(x)$ is reducible in
$\FF_2[x]$.

::: pf-proof

Suppose it were irreducible. Let $\alpha$ be one of its roots. Then
$\overline{\Phi}_{255}$ would be the minimal polynomial of $\alpha$ over
$\FF_2$, so step [](#s5){.pf-ref} would give
$$
[\FF_2(\alpha):\FF_2]
=
128.
$$
But step [](#s4){.pf-ref} gives the upper bound
$$
[\FF_2(\alpha):\FF_2]
\leq
8.
$$
This is impossible. Therefore $\overline{\Phi}_{255}$ is reducible.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} proves that the statement in the problem is false.

:::

:::

:::
