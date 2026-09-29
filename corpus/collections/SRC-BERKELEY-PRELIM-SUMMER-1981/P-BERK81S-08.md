---
schema: qual/card@1
id: P-BERK81S-08
kind: problem
title: Irreducibility of two geometric-sum polynomials over $\QQ$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    For 1+x+...+x^10, shifted x↦x+1 and used
    ((x+1)^11-1)/x. Every nonleading binomial coefficient is divisible by
    11, while the constant term is 11 and not divisible by 11^2, so
    Eisenstein applies. The degree-11 geometric sum is reducible because it
    vanishes at x=-1, so x+1 is a factor.
---

::: {.problem}
Show that
\[
x^{10}+x^9+x^8+\cdots+x+1
\]
is irreducible over $\mathbb Q$.
Is
\[
x^{11}+x^{10}+\cdots+x+1
\]
irreducible over $\mathbb Q$?
:::

::: {.solution}
Define
$$
P(x)=1+x+\cdots+x^{10}.
$$

::: pf

::: {.pf-step #s1}

One has
$$
P(x)
=
\frac{x^{11}-1}{x-1}.
$$

::: pf-proof

This is the finite geometric-series identity:
$$
(x-1)(1+x+\cdots+x^{10})=x^{11}-1.
$$
Since both sides are polynomial identities, the quotient formula holds in
$\QQ[x]$.

:::

:::

::: {.pf-step #s2}

The shifted polynomial satisfies
$$
P(x+1)
=
\frac{(x+1)^{11}-1}{x}
=
\sum_{j=1}^{11}
\binom{11}{j}x^{j-1}.
$$

::: pf-proof

Substitute $x+1$ into step [](#s1){.pf-ref}:
$$
P(x+1)
=
\frac{(x+1)^{11}-1}{(x+1)-1}
=
\frac{(x+1)^{11}-1}{x}.
$$
The binomial theorem gives
$$
(x+1)^{11}-1
=
\sum_{j=1}^{11}\binom{11}{j}x^j.
$$
Dividing by $x$ gives the displayed sum.

:::

:::

::: {.pf-step #s3}

Every nonleading coefficient of $P(x+1)$ is divisible by $11$.

::: pf-proof

For
$$
1\leq j\leq10,
$$
the binomial coefficient is
$$
\binom{11}{j}
=
\frac{11!}{j!(11-j)!}.
$$
Because $11$ is prime and neither $j!$ nor $(11-j)!$ is divisible by
$11$, the factor $11$ in the numerator does not cancel. Hence
$$
11\mid\binom{11}{j}.
$$
The leading coefficient corresponds to $j=11$ and equals $1$.

:::

:::

::: {.pf-step #s4}

The constant term of $P(x+1)$ is $11$, so it is not divisible by
$11^2$.

::: pf-proof

In step [](#s2){.pf-ref}, the constant term is the term with $j=1$:
$$
\binom{11}{1}=11,
$$
and $121\nmid11$.

:::

:::

::: {.pf-step #s5}

The polynomial $P(x+1)$ is irreducible over $\QQ$.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that Eisenstein's criterion applies to
$P(x+1)$ with the prime $11$: every nonleading coefficient is divisible
by $11$, the leading coefficient is not, and the constant term is not
divisible by $11^2$. Therefore $P(x+1)$ is irreducible over $\QQ$.

:::

:::

::: {.pf-step #s6}

The polynomial
$$
\boxed{
1+x+\cdots+x^{10}
}
$$
is irreducible over $\QQ$.

::: pf-proof

The substitution
$$
\tau:\QQ[x]\longrightarrow\QQ[x],
\qquad
\tau(f)(x)=f(x+1),
$$
is a ring automorphism, with inverse $f(x)\mapsto f(x-1)$. Ring
automorphisms preserve reducibility and irreducibility. Since $P(x+1)$ is
irreducible by step [](#s5){.pf-ref}, so is $P(x)$.

:::

:::

::: {.pf-step #s7}

Define
$$
Q(x)=1+x+\cdots+x^{11}.
$$
Then
$$
Q(-1)=0.
$$

::: pf-proof

There are twelve alternating terms:
$$
Q(-1)
=
1-1+1-1+\cdots+1-1
=
0.
$$

:::

:::

::: {.pf-step #s8}

The polynomial $Q$ is reducible over $\QQ$.

::: pf-proof

By step [](#s7){.pf-ref}, the factor theorem gives
$$
x+1\mid Q(x).
$$
Since $Q$ has degree $11$, the quotient has degree $10$, so this is a
nontrivial factorization in $\QQ[x]$.

:::

:::

::: {.pf-step #s9}

Thus the answer to the second question is
$$
\boxed{\text{No.}}
$$

::: pf-proof

Step [](#s8){.pf-ref} shows that the second polynomial is reducible.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} proves irreducibility of the first polynomial, and step [](#s9){.pf-ref}
answers the second question.

:::

:::

:::
