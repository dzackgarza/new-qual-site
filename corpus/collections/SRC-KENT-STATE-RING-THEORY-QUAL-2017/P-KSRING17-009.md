---
schema: qual/card@1
id: P-KSRING17-009
kind: problem
title: Euler's criterion for the Legendre symbol
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 9 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
If $\left(\frac{\cdot}{\cdot}\right)$ denotes the Legendre symbol, prove Euler's Criterion: if $p$ is a prime and $a$ is any integer relatively prime to $p$, then $a^{(p-1)/2} \equiv \left(\frac{a}{p}\right) \pmod{p}$.
:::

::: {.remark}
The Legendre symbol
$$
\left(\frac ap\right)
$$
is defined here for an odd prime $p$. Thus the intended hypothesis is that $p$ is odd.
:::

::: {.solution}

Assume $p$ is an odd prime and
$$
\gcd(a,p)=1.
$$

::: pf

::: {.pf-step #s1-1}

One has
$$
a^{(p-1)/2}
\equiv
\pm1
\pmod p.
$$


::: pf-proof

Fermat's little theorem gives
$$
a^{p-1}\equiv1\pmod p.
$$
Hence, in the field $\FF_p$,
$$
\left(
a^{(p-1)/2}
\right)^2
=
1.
$$
Therefore
$$
\left(
a^{(p-1)/2}-1
\right)
\left(
a^{(p-1)/2}+1
\right)
=0.
$$
Since $\FF_p$ is a field, one of the two factors is zero.

:::

:::

::: {.pf-step #s1-2}

If $a$ is a quadratic residue modulo $p$, then
$$
a^{(p-1)/2}
\equiv
1
\pmod p.
$$


::: pf-proof

If $a$ is a nonzero square modulo $p$, write
$$
a\equiv b^2\pmod p
$$
with $b\not\equiv0\pmod p$. Then
$$
a^{(p-1)/2}
\equiv
b^{p-1}
\equiv
1
\pmod p
$$
by Fermat's little theorem.

:::

:::

::: {.pf-step #s1-3}

The polynomial
$$
X^{(p-1)/2}-1
$$
has exactly the nonzero quadratic residues as its roots in $\FF_p$.


::: pf-proof

The map
$$
\FF_p^\times\longrightarrow\FF_p^\times,
\qquad
x\longmapsto x^2
$$
has fibers
$$
\{x,-x\},
$$
because $p$ is odd. Hence there are exactly
$$
\frac{p-1}{2}
$$
nonzero quadratic residues.

By step [](#s1-2){.pf-ref}, all of them are roots of
$$
X^{(p-1)/2}-1.
$$
This polynomial has degree $(p-1)/2$, so over the field $\FF_p$ it has at most $(p-1)/2$ roots. Therefore these quadratic residues are all its roots.

:::

:::

::: {.pf-step #s1-4}

If $a$ is a quadratic nonresidue modulo $p$, then
$$
a^{(p-1)/2}
\equiv
-1
\pmod p.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, a nonresidue is not a root of
$$
X^{(p-1)/2}-1.
$$
Thus
$$
a^{(p-1)/2}
\not\equiv
1
\pmod p.
$$
Step [](#s1-1){.pf-ref} shows that the only remaining possibility is
$$
a^{(p-1)/2}
\equiv
-1
\pmod p.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
a^{(p-1)/2}
\equiv
\left(\frac ap\right)
\pmod p.
}
$$


::: pf-proof

By definition,
$$
\left(\frac ap\right)
=
\begin{cases}
1,&\text{if $a$ is a quadratic residue modulo $p$},\\
-1,&\text{if $a$ is a quadratic nonresidue modulo $p$}.
\end{cases}
$$
Steps [](#s1-2){.pf-ref} and [](#s1-4){.pf-ref} give exactly these two congruences.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is Euler's criterion.

:::

:::

:::
