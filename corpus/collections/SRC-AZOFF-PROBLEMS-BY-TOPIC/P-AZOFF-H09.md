---
schema: qual/card@1
id: P-AZOFF-H09
kind: problem
title: Monic polynomials have modulus at least $1$ somewhere on the unit circle
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Rouché’s theorem, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Cleaned the OCR LaTeX and the broken accent in Rouché against Rouché’s theorem, Problem 9, of Azoff Problems by Topic.pdf; the source itself omits the first part it mentions.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Argued by contradiction. If the monic polynomial had modulus strictly
    below one on the unit circle, Rouché would force z^n-p(z), a nonzero
    polynomial of degree at most n-1, to have the same n zeros in the disk
    as z^n, which is impossible.
---

::: {.problem}
Prove that
$$
\max_{\abs{z}=1} \abs{a_0 + a_1 z + \cdots + a_{n-1}z^{n-1} + z^n} \ge 1.
$$

Hint: The first part of the problem asks for a statement of Rouché’s Theorem.
:::

::: {.solution}
Set
$$
p(z)
=
a_0+a_1z+\cdots+a_{n-1}z^{n-1}+z^n.
$$

::: pf

::: {.pf-step #s1}

Suppose, for contradiction, that
$$
\max_{\abs{z}=1}\abs{p(z)}<1.
$$
Then on the unit circle,
$$
\abs{p(z)}<\abs{z^n}.
$$

::: pf-proof

If $\abs{z}=1$, then
$$
\abs{z^n}=1.
$$
The assumed strict upper bound on $\abs{p(z)}$ therefore gives the
displayed inequality.

:::

:::

::: {.pf-step #s2}

Under the assumption of step [](#s1){.pf-ref}, the polynomial
$$
q(z)
=
z^n-p(z)
=
-a_0-a_1z-\cdots-a_{n-1}z^{n-1}
$$
has exactly $n$ zeros in the open unit disk, counting multiplicity.

::: pf-proof

On $\abs{z}=1$,
$$
\abs{q(z)-z^n}
=
\abs{-p(z)}
=
\abs{p(z)}
<
\abs{z^n}
$$
by step [](#s1){.pf-ref}. Rouché's theorem implies that $q$ and $z^n$ have the same
number of zeros in the unit disk. The polynomial $z^n$ has exactly $n$,
counting multiplicity.

:::

:::

::: {.pf-step #s3}

The conclusion of step [](#s2){.pf-ref} is impossible.

::: pf-proof

The polynomial $q$ has degree at most $n-1$. It is not identically zero:
if $q\equiv0$, then $p(z)=z^n$, which has
$$
\abs{p(z)}=1
$$
on the unit circle, contradicting step [](#s1){.pf-ref}.

A nonzero polynomial of degree at most $n-1$ has at most $n-1$ zeros in
$\CC$, counting multiplicity. It therefore cannot have the $n$ zeros in
the unit disk asserted by step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
\max_{\abs{z}=1}
\abs{
a_0+a_1z+\cdots+a_{n-1}z^{n-1}+z^n
}
\geq1.
}
$$

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} show that the strict inequality
$$
\max_{\abs{z}=1}\abs{p(z)}<1
$$
leads to a contradiction. Hence the maximum is at least $1$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required inequality.

:::

:::

:::
