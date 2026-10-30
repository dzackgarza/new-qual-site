---
schema: qual/card@1
id: P-MAXAT-6-05
kind: problem
title: $\RP^n$ does not embed in $\RR^{2n-1}$ when $n$ is a power of $2$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 5 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that if $n$ is a power of $2$, then $\RP^{n}$ cannot be smoothly embedded in $\RR^{2n-1}$.
:::

::: {.solution}

Let
$$
n=2^r,
\qquad r\geq1,
$$
and let
$$
a\in H^1(\RP^n;\FF_2)
$$
be the standard generator. Suppose, for contradiction, that there is a smooth embedding
$$
\RP^n\hookrightarrow\RR^{2n-1}.
$$

::: pf

::: {.pf-step #s1-1}

Its normal bundle $\nu$ has rank
$$
(2n-1)-n=n-1
$$
and satisfies
$$
T\RP^n\oplus\nu\cong\varepsilon^{2n-1}.
$$


::: pf-proof

For a smooth embedding, the tangent bundle of the ambient Euclidean space restricted to the submanifold splits as the tangent bundle plus the orthogonal normal bundle. The ambient tangent bundle is trivial of rank $2n-1$, and the codimension is $n-1$.

:::

:::

::: pf-step

Since
$$
w(T\RP^n)=(1+a)^{n+1},
$$
one has
$$
w(\nu)=(1+a)^{-(n+1)}.
$$


::: pf-proof

Apply the Whitney product formula to step [](#s1-1){.pf-ref}:
$$
w(T\RP^n)w(\nu)=1.
$$
The standard tangent-bundle calculation gives the first displayed formula, so $w(\nu)$ is its multiplicative inverse in
$$
H^*(\RP^n;\FF_2)
=\FF_2[a]/(a^{n+1}).
$$

:::

:::

::: pf-step

Because $n=2^r$, in mod-$2$ cohomology
$$
(1+a)^n=1+a^n.
$$


::: pf-proof

Over a ring of characteristic $2$, Frobenius gives
$$
(x+y)^{2^r}=x^{2^r}+y^{2^r}.
$$
Set $x=1$, $y=a$.

:::

:::

::: {.pf-step #s1-4}

In the truncated ring $\FF_2[a]/(a^{n+1})$,
$$
(1+a)^{-(n+1)}
=1+a+a^2+\cdots+a^n.
$$


::: pf-proof

Since
$$
(1+a)^{n+1}=(1+a)(1+a^n)
=1+a+a^n+a^{n+1}
=1+a+a^n,
$$
it suffices to multiply by
$$
S=1+a+\cdots+a^n.
$$
Now
$$
(1+a)S=1+a^{n+1}=1
$$
in the truncated ring. Also
$$
a^nS=a^n
$$
because every higher term has degree at least $n+1$. Hence
$$
(1+a+a^n)S
=1+a^n+a^n=1.
$$
Thus $S$ is the required inverse.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
w_n(\nu)=a^n\ne0.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} identifies the degree-$n$ component of $w(\nu)$ with $a^n$. The mod-$2$ cohomology ring of real projective space is
$$
H^*(\RP^n;\FF_2)
=\FF_2[a]/(a^{n+1}),
$$
so $a^n$ is its nonzero top-dimensional class.

:::

:::

::: {.pf-step #s1-6}

But a rank-$(n-1)$ vector bundle has
$$
w_n=0.
$$


::: pf-proof

For a rank-$k$ real vector bundle, Stiefel--Whitney classes vanish in every degree greater than $k$. Here $k=n-1$, so $w_n(\nu)=0$.

:::

:::

::: {.pf-step #s1-7}

Steps [](#s1-5){.pf-ref} and [](#s1-6){.pf-ref} contradict each other.


::: pf-proof

The same normal bundle $\nu$ cannot simultaneously have $w_n(\nu)=a^n\ne0$ and $w_n(\nu)=0$.

:::

:::

::: {.pf-step #s1-8}

Hence
$$
\boxed{
\RP^{2^r}\text{ cannot be smoothly embedded in }
\RR^{2^{r+1}-1}.}
$$


::: pf-proof

The contradiction in step [](#s1-7){.pf-ref} disproves the assumed embedding.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required nonembedding result.

:::

:::

:::
