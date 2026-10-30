---
schema: qual/card@1
id: P-NORI-GT-3-08
kind: problem
title: $\Phi_{n'p^k}=\Phi_{n'}^{\varphi(p^k)}$ in $\FF_p[X]$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.8 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Stated the setup and claim of Problem 3.7, on which this problem depends, from p. 2 of the Nori Galois Theory Problems PDF.
---

::: {.problem}
The cylotomic polynomials $\Phi_n(X) \in \ZZ[X]$ defined for all natural numbers $n$ have the property
$$
X^n - 1 = \prod_{d \mid n} \Phi_d(X).
$$
Let $n = n'p^k$ with $p$ not dividing $n'$, and let $\varphi$ be Euler's phi function.
Problem 3.7 reads: let $F$ be a field of characteristic $p$ such that $\mu_{n'}(F)$ has order $n'$. Show that the roots of $\Phi_n(X)$ in $F$ are the primitive $n'$-th roots of unity, each of them occuring with multiplicity $\varphi(p^k)$.

Deduce the equality $\Phi_n(X) = \Phi_{n'}(X)^{\varphi(p^k)}$ in $\FF_p[X]$ from the previous problem.
:::

::: {.remark}
Here $\mu_{n'}(F) = \{x \in F : x^{n'} = 1\}$, as in the notation paragraph of the source.
:::

::: {.solution}

Let
$$
\overline{\FF}_p
$$
be an algebraic closure of $\FF_p$.

::: pf

::: {.pf-step #s1-1}

The group
$$
\mu_{n'}(\overline{\FF}_p)
$$
has exactly $n'$ elements.


::: pf-proof

Since $p\nmid n'$, the derivative of
$$
X^{n'}-1
$$
is
$$
n'X^{n'-1},
$$
which has no common root with $X^{n'}-1$ in characteristic $p$. Thus $X^{n'}-1$ is separable. It splits in the algebraic closure and has degree $n'$, so it has exactly $n'$ distinct roots there.

:::

:::

::: {.pf-step #s1-2}

By Problem 3.7, the roots of the reduction of $\Phi_n(X)$ in $\overline{\FF}_p$ are precisely the primitive $n'$-th roots of unity, and each occurs with multiplicity
$$
\varphi(p^k).
$$


::: pf-proof

The field $\overline{\FF}_p$ has characteristic $p$, and step [](#s1-1){.pf-ref} verifies the hypothesis
$$
\cardinality{\mu_{n'}(\overline{\FF}_p)}=n'.
$$
Problem 3.7 therefore applies directly to
$$
n=n'p^k.
$$

:::

:::

::: {.pf-step #s1-3}

The roots of the reduction of $\Phi_{n'}(X)$ in $\overline{\FF}_p$ are precisely the primitive $n'$-th roots of unity, each with multiplicity $1$.


::: pf-proof

Apply Problem 3.7 to
$$
n=n'p^0=n'.
$$
Since
$$
\varphi(p^0)=\varphi(1)=1,
$$
the stated roots occur with multiplicity one.

:::

:::

::: {.pf-step #s1-4}

Hence the two polynomials
$$
\Phi_n(X)
$$
and
$$
\Phi_{n'}(X)^{\varphi(p^k)}
$$
viewed in $\FF_p[X]$ have the same roots with the same multiplicities in $\overline{\FF}_p$.


::: pf-proof

By step [](#s1-2){.pf-ref}, every primitive $n'$-th root occurs in $\Phi_n$ with multiplicity $\varphi(p^k)$. By step [](#s1-3){.pf-ref}, every such root occurs once in $\Phi_{n'}$, hence with multiplicity $\varphi(p^k)$ in its indicated power. Neither polynomial has any other root.

:::

:::

::: {.pf-step #s1-5}

Both polynomials in step [](#s1-4){.pf-ref} are monic.


::: pf-proof

Every cyclotomic polynomial is monic over $\ZZ$, so its reduction modulo $p$ is monic. A positive integral power of a monic polynomial is monic.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\Phi_{n'p^k}(X)
=
\Phi_{n'}(X)^{\varphi(p^k)}
\quad\text{in }\FF_p[X].
}
$$


::: pf-proof

Over the algebraically closed field $\overline{\FF}_p$, a monic polynomial is uniquely determined by its roots counted with multiplicity. Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} therefore give equality after extending scalars to $\overline{\FF}_p$. The natural map
$$
\FF_p[X]\hookrightarrow\overline{\FF}_p[X]
$$
is injective, so the equality already holds in $\FF_p[X]$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is exactly the required deduction from Problem 3.7.

:::

:::

:::
