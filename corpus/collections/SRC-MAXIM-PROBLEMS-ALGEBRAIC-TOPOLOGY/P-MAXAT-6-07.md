---
schema: qual/card@1
id: P-MAXAT-6-07
kind: problem
title: $\CP^4$ does not embed smoothly in $\RR^{11}$
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 6, problem 7 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that $\CP^{4}$ cannot be smoothly embedded in $\RR^{n}$ with $n \leq 11$. (Hint: use Pontrjagin classes)
:::

::: {.solution}

The real dimension of $\CP^4$ is $8$. Suppose, for contradiction, that there is a smooth embedding
$$
\CP^4\hookrightarrow\RR^N
\qquad(N\leq11),
$$
and let $\nu$ be its normal bundle.

::: pf

::: {.pf-step #s1-1}

The normal bundle has rank
$$
r=N-8\leq3
$$
and satisfies
$$
T\CP^4\oplus\nu\cong\varepsilon^N.
$$


::: pf-proof

For a smooth embedding, the restricted tangent bundle of Euclidean space splits as the tangent bundle of the submanifold plus its orthogonal normal bundle. Since $\dim_{\RR}\CP^4=8$, the normal rank is $N-8$.

:::

:::

::: pf-step

Let
$$
x\in H^2(\CP^4;\ZZ)
$$
be the positive generator. Then
$$
p(T\CP^4)=(1+x^2)^5.
$$


::: pf-proof

The complex Euler sequence gives the stable complex-bundle identity
$$
T\CP^4\oplus\varepsilon^1_{\CC}
\cong5\gamma^*,
$$
where $c_1(\gamma^*)=x$. The underlying real bundle of a complex line with first Chern class $x$ has total Pontryagin class $1+x^2$. Pontryagin classes are stable and multiplicative, giving the formula.

:::

:::

::: pf-step

Since
$$
H^*(\CP^4;\ZZ)
=\ZZ[x]/(x^5),
$$
the tangent Pontryagin class is
$$
p(T\CP^4)
=1+5x^2+10x^4.
$$


::: pf-proof

Expand
$$
(1+x^2)^5
=1+5x^2+10x^4+10x^6+5x^8+x^{10}.
$$
Since $x^5=0$, all terms involving $x^6$ or higher vanish.

:::

:::

::: pf-step

From the stable trivialization in step [](#s1-1){.pf-ref},
$$
p(\nu)=p(T\CP^4)^{-1}.
$$


::: pf-proof

Whitney multiplicativity gives
$$
p(T\CP^4)p(\nu)=p(\varepsilon^N)=1.
$$
Thus the normal total Pontryagin class is the multiplicative inverse.

:::

:::

::: {.pf-step #s1-5}

Through degree $8$,
$$
p(\nu)=1-5x^2+15x^4.
$$


::: pf-proof

Write
$$
(1+5x^2+10x^4)^{-1}=1+Ax^2+Bx^4.
$$
Multiplication gives
$$
1+(A+5)x^2+(B+5A+10)x^4.
$$
Setting the positive-degree coefficients equal to zero yields
$$
A=-5,
\qquad
B=25-10=15.
$$

:::

:::

::: {.pf-step #s1-6}

The decisive obstruction is $p_2(\nu)$: because $\operatorname{rank}\nu\leq3$,
$$
p_2(\nu)=0,
$$
but step [](#s1-5){.pf-ref} gives
$$
p_2(\nu)=15x^4\ne0.
$$


::: pf-proof

For a real rank-$r$ bundle, $p_i$ vanishes for $2i>r$ because after applying the splitting principle there are only $\lfloor r/2\rfloor$ Pontryagin roots; equivalently $p_i=(-1)^ic_{2i}(E\otimes\CC)$ and the special real structure forces $p_i=0$ for $i>\lfloor r/2\rfloor$. In particular a rank-$3$ bundle has no $p_2$. On the other hand, step [](#s1-5){.pf-ref} identifies $p_2(\nu)$ with $15x^4$, and
$$
x^4\ne0\in H^8(\CP^4;\ZZ).
$$
This is the required contradiction.

:::

:::

::: {.pf-step #s1-7}

Therefore
$$
\boxed{
\CP^4\text{ cannot be smoothly embedded in }
\RR^N\text{ for }N\leq11.}
$$


::: pf-proof

Any such embedding would produce the rank-$\leq3$ normal bundle of step [](#s1-1){.pf-ref}, contradicting step [](#s1-6){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} is the desired nonembedding statement.

:::

:::

:::
